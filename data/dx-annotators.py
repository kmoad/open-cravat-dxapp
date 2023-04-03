import re
import json

# Exclude annotators with too many sub-annotators
exclude_length = [
    r'segway.*',
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

with open('all-annotators.txt') as f:
    annots = []
    for l in f:
        annot_name = l.strip()
        exclude_matches = [re.match(_, annot_name) for _ in exclude]
        if not(any(exclude_matches)):
            annots.append(annot_name)
            
print(json.dumps(annots))