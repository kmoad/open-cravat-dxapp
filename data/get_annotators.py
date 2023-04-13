from cravat import admin_util as au
import re
import json

# Exclude annotators with too many sub-annotators
exclude_length = [
    r'segway_.*',
    r'chasmplus_.*',
]

# Exclude annotators with commercial use restrictions
exclude_commercial = [
    'abraom',
    'brca1_func_assay',
    'cadd',
    'cadd_exome',
    'cancer_genome_interpreter',
    'cgc',
    'cosmic',
    'cosmic_gene',
    'dann_coding',
    'dida',
    'genehancer',
    'grasp',
    'hgdp',
    'linsight',
    'mupit',
    r'ndex.*',
    'oncokb',
    'revel',
    'sift',
    'spliceai',
    'vest',
    'vista_enhancer',    
]

exclude = exclude_length + exclude_commercial

include_minfos = []

all_annots = au.get_remote_module_infos_of_type('annotator')
for mname, mdict in all_annots.items():
	exclude_matches = [re.match(_, mname) for _ in exclude]
	if not(any(exclude_matches)):
		include_minfos.append(au.RemoteModuleInfo(mname, **mdict))

print(json.dumps([minfo.name for minfo in include_minfos]))
print('\n')


table = '''
| Name | Title | Description |
| - | - | - |
'''[1:-1]

for minfo in include_minfos:
	table_row = ' | '+' | '.join((minfo.name, minfo.title, minfo.description))+' |'
	table += '\n'+table_row

print(table)