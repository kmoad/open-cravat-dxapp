#!/usr/bin/env python3

import sqlite3
from argparse import ArgumentParser
import gzip
import sys
from pathlib import Path
import json
import yaml
from Bio import bgzf

# Replacement of % must come first
perc_encode = [
    [r'%', r'%25'],
    [r':', r'%3A'],
    [r';', r'%3B'],
    [r'=', r'%3D'],
    [r',', r'%2C'],
    [r'\n', r'%0A'],
    [r'\t', r'%09'],
    [r'\r', r'%0D'],
]

def vcf_encode(orig):
    new = orig
    for k,v in perc_encode:
        new = new.replace(k,v)
    return new

def vcf_decode(orig):
    new = orig
    for k,v in perc_encode[::-1]:
        new = new.replace(v,k)
    return new

class ReportSubber(object):
    def __init__(self):
        hg38_conf = yaml.safe_load((Path(__file__).resolve().parent/'hg38.yml').open())
        self.subs = {'base__'+k:v for k,v in hg38_conf['report_substitution'].items()}
    
    def sub(self, col_name, value):
        if col_name == 'base__all_mappings':
            subd = self.subs['base__all_mappings']
            mappings = json.loads(value)
            for gene in mappings:
                for i in range(len(mappings[gene])):
                    sos = mappings[gene][i][2].split(',')
                    sos = [subd.get(so,so) for so in sos]
                    mappings[gene][i][2] = ','.join(sos)
            value = json.dumps(mappings)
        elif col_name in self.subs:
            for old, new in self.subs[col_name].items():
                if value:
                    value = value.replace(old, new)
        return value

def include_column(col_name):
    hardcoded = {'base__chrom', 'base__pos', 'base__ref_base', 'base__alt_base'}
    if col_name in hardcoded:
        return False
    elif col_name.startswith('tagsampler__'):
        return False
    elif col_name.startswith('vcfinfo__'):
        return False
    elif col_name.startswith('extra_vcf_info__'):
        return False
    else:
        return True

def lockstep(f, c):

    def getln(r):
        if r is None:
            return None
        else:
            return r[0]

    def step(c):
        try:
            return next(c)
        except StopIteration:
            return None

    r = step(c)
    for i,l in enumerate(f):
        ln = i+1
        linedata = []
        # Catch c up if needed
        while getln(r) is not None and ln > getln(r):
            r = step(c)
        while getln(r) == ln:
            linedata.append(r)
            r = step(c)
        yield ln, l, linedata

parser = ArgumentParser()
parser.add_argument('db',type=Path)
parser.add_argument('vcf',type=Path)
parser.add_argument('-z','--gzip',
    action='store_true',
    help='Compress output with gzip',
)
parser.add_argument('-b','--bgzip',
    action='store_true',
    help='Compress output with bgzip',
)
parser.add_argument('-s','--skip',
    action='store_true',
    help='Skip lines without annotation'
)
parser.add_argument('-c','--stdout',
    action='store_true',
    help='Write to stdout. Ignores --gzip and --bgzip',
)
parser.add_argument('--head',
    type=int,
    help='Stop after n data lines',
)
parser.add_argument('-o','--output',
    type=Path,
    help='Output file'
)
args = parser.parse_args()


db = sqlite3.connect(str(args.db))
c = db.cursor()

if args.vcf.suffix == '.gz':
    finput = gzip.open(str(args.vcf),'rt')
else:
    finput = args.vcf.open('rt')

if args.stdout:
    wf = sys.stdout
else:
    if args.output:
        writepath = args.output
    else:
        suffixes = args.vcf.suffixes
        basepath = str(args.vcf.name).split('.')[0]
        if suffixes and suffixes[-1] == '.gz':
            suffixes = suffixes[:-1]
        if suffixes and suffixes[-1] == '.vcf':
            suffixes = suffixes[:-1]
        suffixes += ['vcf']
        if args.gzip or args.bgzip:
            suffixes += ['gz']
        writepath = Path(basepath+'_opencravat').with_suffix('.'+'.'.join(suffixes))
    if args.gzip:
        wf = gzip.open(writepath,'wt')
    elif args.bgzip:
        wf = bgzf.open(writepath,'wt')
    else:
        wf = writepath.open('wt')

def oc2vcf_key(column):
    return f'OC_{col_name}'

def make_info_header(col_name, colinfo, annot_title):
    oc2vcf_type = {'int':'Integer','float':'Float','string':'String'}
    vcf_type = oc2vcf_type[colinfo['type']]
    vcf_key = oc2vcf_key(col_name)
    desc = colinfo.get('desc')
    desc_toks = ['OpenCRAVAT',annot_title, colinfo['title']]
    if desc is not None:
        desc_toks.append(desc)
    long_desc = '; '.join(desc_toks)
    return f'##INFO=<ID={vcf_key},Number=A,Type={vcf_type},Description="{long_desc}">'

def include_column(col_name):
    if col_name.startswith('extra_vcf_info__'):
        return False
    if col_name.startswith('vcfinfo__'):
        return False
    if col_name.startswith('tagsampler__'):
        return False
    if col_name.endswith('__original_line'):
        return False
    return True

q = 'select col_name, col_def from variant_header;'
c.execute(q)
colinfo = [json.loads(r[1]) for r in c]
q = 'select name, displayname from variant_annotator'
c.execute(q)
annot_titles = {k:v for k,v in c}

for l in finput:
    if l.startswith('#CHROM'):
        for column in colinfo:
            col_name = column['name']
            if not include_column(col_name):
                continue
            annot_name = col_name.split('__')[0]
            annot_title = annot_titles.get(annot_name, annot_name)
            info_header = make_info_header(col_name, column, annot_title)
            wf.write(info_header+'\n')
        wf.write(l)
        #TODO add a couple meta lines. Date, process to get here, etc
        break
    wf.write(l)
finput.seek(0)

subber = ReportSubber()
q = 'select m.base__original_line, v.* from variant as v join mapping as m on v.base__uid=m.base__uid order by m.base__original_line'
c.execute(q)
dbcol_names = [x[0] for x in c.description]
data_line_n = 0
for ln, l, data in lockstep(finput, c):
    if l.startswith('##') or l.startswith('#CHROM'):
        continue
    elif l.startswith('#'):
        wf.write(l)
        continue
    if args.skip and not data:
        continue
    data_line_n += 1
    if args.head and args.head<data_line_n:
        break
    if data:
        row = data[0]
        rowd = dict(zip(dbcol_names, row))
        infod = {}
        for col_name in rowd.keys():
            if not include_column(col_name):
                continue
            cell = rowd[col_name]
            cell = subber.sub(col_name, cell)
            if cell is None:
                continue
            info_key = oc2vcf_key(col_name)
            if type(cell) is str:
                try:
                    o = json.loads(cell)
                    if type(o) in (dict, list):
                        if len(o) == 0:
                            continue
                        jsoncell = json.dumps(o, separators=(',',':'))
                        infocell = vcf_encode(jsoncell)
                    else:
                        infocell = vcf_encode(cell)
                except json.JSONDecodeError:
                    infocell = vcf_encode(cell)
            elif type(cell) in (dict, list):
                infocell = vcf_encode(json.dumps(infocell, separators=(',',':')))
            else:
                infocell = cell
            infod[info_key] = infocell
        oc_info = ''
        oc_info = ';'.join([f'{k}={v}' for k,v in infod.items()])
        toks = l.split('\t')
        if toks[7] == '.' or toks[7] == '':
            toks[7] = oc_info
        else:
            toks[7] = toks[7].rstrip()+';'+oc_info
            if len(toks) == 8:
                toks[7]+='\n'
        l = '\t'.join(toks)
    wf.write(l)
wf.close()
c.close()
db.close()
finput.close()
