# OpenCRAVAT

OpenCRAVAT is a meta-annotator for variant and gene prioritization.

OpenCRAVAT has a modular architecture with a wide variety of annotators that can be selected and run based on the needs of a given study. The modules are made available via the CRAVAT Store and are developed both by the CRAVAT team and the broader variant analysis community. 

OpenCRAVAT is a product of the [Karchin Lab](https://karchinlab.org) at [Johns Hopkins University](https://jhu.edu) with funding provided by the National Cancer Institute’s [ITCR](https://itcr.cancer.gov/) program through grant U24CA258393.

For more information about OpenCRAVAT, visit

https://opencravat.org

and/or see detailed documenatation at:

https://open-cravat.readthedocs.io/en/latest/index.html

## What does this app do?

OpenCRAVAT on DNAnexus will annotate a VCF file with by mapping variants onto transcripts, cDNA and protein sequences, plus variant and gene annotations from a wide range of databases and tools.

## Screenshot of parameters

See below the screenshot for a detailed description of the parameters.

![](./screenshot-run-arguments.png)

## Annotators

The OpenCRAVAT store features over one hundred annotators, which provide information about:

<ul>
<li> Allele frequency</li> 
<li> Clinical relevance</li>
<li> Evolution</li>
<li> In silico predictions</li>
<li> Functional studies</li>
<li> Literature</li>
<li> Non-coding variants</li>
<li> Cancer relevance</li>
</ul>

To start, you can try a package of commonly used annotators, which includes:

- gnomad3
- clinvar
- phylop
- revel
- dbsnp
- encode_tfbs
- ncer
- go
- cscape
- dann

Or jump right in and put together your own list of up to six annotators using our drop-down menus. To use more than six annotators, you can supply a comma-seperated list of annotators in the `Annotators` text field.

Such as:

```
clinvar,dbsnp,loftool
```

Short descriptions of available annotators are below. For more detailed and colorful descriptions of each annotator visit [run.opencravat.org](https://run.opencravat.org), select **Try as Guest** and click on the **Store** tab.

| Annotator Name | Title | Description |
| - | - | - |
 | alfa | ALFA: Allele Frequency Aggregator | The goal of the ALFA project is to make frequency data from over 1M dbGaP subjects open-access in future releases to facilitate discoveries and interpretations of common and rare variants with biological impacts or causing diseases.
 | alfa_african | ALFA: Allele Frequency Aggregator African | The goal of the ALFA project is to make frequency data from over 1M dbGaP subjects open-access in future releases to facilitate discoveries and interpretations of common and rare variants with biological impacts or causing diseases.
 | alfa_asian | ALFA: Allele Frequency Aggregator Asian | The goal of the ALFA project is to make frequency data from over 1M dbGaP subjects open-access in future releases to facilitate discoveries and interpretations of common and rare variants with biological impacts or causing diseases.
 | alfa_european | ALFA: Allele Frequency Aggregator European | The goal of the ALFA project is to make frequency data from over 1M dbGaP subjects open-access in future releases to facilitate discoveries and interpretations of common and rare variants with biological impacts or causing diseases.
 | alfa_latin_american | ALFA: Allele Frequency Aggregator Latin American | The goal of the ALFA project is to make frequency data from over 1M dbGaP subjects open-access in future releases to facilitate discoveries and interpretations of common and rare variants with biological impacts or causing diseases.
 | alfa_other | ALFA: Allele Frequency Aggregator Others | The goal of the ALFA project is to make frequency data from over 1M dbGaP subjects open-access in future releases to facilitate discoveries and interpretations of common and rare variants with biological impacts or causing diseases.
 | aloft | ALoFT | ALoFT provides extensive annotations to putative loss-of-function variants (LoF) in protein-coding genes including functional, evolutionary and network features.
 | arrvars | Arrhythmia Channelopathy Variants | Examines variants associated with arrhythmia diseases such as Brugada Syndrome and Long QT Syndrome.
 | biogrid | BioGRID | Comprehensive interaction repository
 | cancer_hotspots | Cancer Hotspots | A resource for statistically significant mutations in cancer.
 | cardioboost | CardioBoost | Predicts pathogenicity of missense variants for inherited cardiac conditions
 | ccr | CCR: Constrained Coding Regions | The constrained coding regions model (CCR) uses the Genome Aggregation Database to reveal regions of protein coding genes that are likely to be under potentially purifiying selection.
 | ccre_screen | Candidate cis-Regulatory Elements by ENCODE (SCREEN) | SCREEN allows the user to explore Candidate cis-Regulatory Elements (cCREs) and investigate how these elements relate to other Encyclopedia annotations and raw ENCODE data.
 | cgd | CGD: Clinical Genomic Database | A manually curated database of conditions with known genetic causes, focusing on medically significant genetic data with available interventions.
 | cgl | Cancer Gene Landscape | Oncogenes and tumor supressor genes from Vogelstein et al. 2013
 | chasmplus | CHASMplus | CHASMplus is a machine learning algorithm that discriminates somatic missense mutations as either cancer drivers or passengers. Predictions can be done in either a cancer type-specific manner or by a model considering multiple cancer types together (a useful default). Along with scoring each mutation, CHASMplus has a rigorous statistical model to evaluate the statistical significance of predictions. This OpenCRAVAT module represents the v1.0 precompute of CHASMplus (source code v1.0).
 | civic | CIViC | Provides descriptions and linkouts to CIViC
 | civic_gene | CIViC Gene | Provides descriptions and linkouts to CIViC
 | clingen | ClinGen Gene | ClinGen is a National Institutes of Health (NIH)-funded resource dedicated to building a central resource that defines the clinical relevance of genes and variants for use in precision medicine and research.
 | clinpred | ClinPred | Prediction tool to identify disease-relevant nonsynonymous single nucleotide variants.
 | clinvar | ClinVar | ClinVar is an archive of reports of the relationships among human variations and phenotypes, with supporting evidence.
 | clinvar_acmg | ClinVar ACMG | ACMG PS1 and PM5 pathogenicity prediction based on ClinVar
 | cscape | CScape | CScape predicts the oncogenic status (disease-driver or neutral) of somatic point mutations in coding and non coding region of the cancer genome.
 | cscape_coding | CScape Coding | CScape predicts the oncogenic status (disease-driver or neutral) of somatic point mutations in the coding region of the cancer genome.
 | cvdkp | Cardiovascular Disease Knowledge Portal | Produces an effect weight for the variant in which disease it is found. Weights are assigned according to the strength of their association with disease risk.
 | dann | DANN | A deep learning approach for annotating the pathogenicity of genetic variants.
 | dbcid | dbCID: Database of Cancer Driver InDels | The database of Cancer driver InDels (dbCID) is a highly curated database of driver indels (insertions and deletions) that are likely to engage in cancer development, progression, or therapy.
 | dbscsnv | dbscSNV | A comprehensive database of all potential human SNVs within splicing consensus regions and their functional annotations.
 | dbsnp | dbSNP | Comprehensive database of both single base nucleotide subsitutions and short deletion and insertion polymorphisms
 | dbsnp_common | dbSNP Common | Selection of SNPs with a minor allele frequency of 1% or greater is an attempt to identify variants that appear to be reasonably common in the general population.
 | denovo | Denovo-DB | Denovo annotation. Denovo is a collection of germline variants in the human genome which are present in children but not their parents.
 | dgi | DGIdb: The Drug Interaction Database | The goal of DGIdb is to help you annotate your genes of interest with respect to known drug-gene interactions and potential druggability.
 | encode_tfbs | ENCODE TFBS | Human transcription factor binding sites based on ChIP-seq experiments generated by production groups in the ENCODE Consortium.
 | ensembl_regulatory_build | Ensembl Regulatory Build | An up-to-date and comprehensive summary of regulatory features across the genome, as well as popular curated external resources.
 | esp6500 | ESP6500 | Exome Sequencing Project 6500
 | ess_gene | Essential Genes | Essential Genes provides a database of genetic variation & mutational burden in 2472 human orthologs
 | exac_gene | ExAC Gene and CNV | ExAC Functional Gene Constraint & CNV Scores provides probability of LoF tolerance/intolerance
 | fathmm | FATHMM | Functional analysis through hidden markov models.
 | fathmm_mkl | FATHMM MKL | A database capable of predicting the effects of coding variants using nucleotide-based HMMs.
 | fathmm_xf | FATHMM XF | Enhanced Accuracy in Predicting the Functional Consequences of Coding Single Nucleotide Variants (SNVs).
 | fathmm_xf_coding | FATHMM XF Coding | Enhanced Accuracy in Predicting the Functional Consequences of Coding Single Nucleotide Variants (SNVs).
 | fitcons | fitCons | fitCons predicts the fraction of genomic positions belonging to a specific function class that are under selective pressure.
 | flank_seq | Flanking Sequence | Reference and alternate bases with flanking sequence
 | funseq2 | FunSeq2 | A flexible framework to prioritize regulatory mutations from cancer genome sequencing
 | genocanyon | GenoCanyon | GenoCanyon is a whole-genome functional annotation approach based on unsupervised statistical learning. It integrates genomic conservation measures and biochemical annotation data to predict the functional potential at each nucleotid.
 | gerp | GERP++ | Genomic Evolutionary Rate Profiling
 | geuvadis | Geuvadis eQTLs | Significant snp-gene associations reported by the Geuvadis project
 | ghis | GHIS | Gene haploinsufficiency scoring
 | gnomad | gnomAD | Genome Aggregation Database (gnomAD) is a resource developed by an international coalition of investigators, with the goal of aggregating and harmonizing both exome and genome sequencing data from a wide variety of large-scale sequencing projects
 | gnomad3 | gnomAD3 | Genome Aggregation Database (gnomAD) is a resource developed by an international coalition of investigators, with the goal of aggregating and harmonizing both exome and genome sequencing data from a wide variety of large-scale sequencing projects
 | gnomad3_counts | gnomAD3 Counts | Genome Aggregation Database (gnomAD) is a resource developed by an international coalition of investigators, with the goal of aggregating and harmonizing both exome and genome sequencing data from a wide variety of large-scale sequencing projects
 | gnomad_gene | gnomAD Gene | Gene level population statistics from gnomAD
 | go | Gene Ontology | Gene Ontology (GO) project provides a comprehensive computable knowledge regarding the functions of genes and gene products.
 | gtex | GTEx eQTLs | Genotype-tissue expression
 | gwas_catalog | GWAS Catalog | GWAS Catalog Annotator
 | haploreg_afr | HaploReg African | SNPs in LD with the variant in African populations
 | haploreg_amr | HaploReg American | SNPs in LD with the variant in American populations
 | haploreg_asn | HaploReg Asian | SNPs in LD with the variant in Asian populations
 | haploreg_eur | HaploReg European | SNPs in LD with the variant in European populations
 | hg19 | hg19 coordinates | Input coordinates are mapped to hg19 through liftOver.
 | hpo | Human Phenotype Ontology | The Human Phenotype Ontology (HPO) provides a standardized vocabulary of phenotypic abnormalities encountered in human disease. Each term in the HPO describes a phenotypic abnormality.
 | intact | IntAct | Molecular interaction data
 | interpro | InterPro | Protein sequence analysis & classification
 | javierre_promoters | Promoter IR | Javierre et al promoter-interacting regions | Promoter capture Hi-C was used to identify interacting regions of 31,253 promoters that are significantly associated across 17 human primary hematopoietic cell types.
 | litvar | LitVar | LitVar allows the search and retrieval of variant relevant information from biomedical literature.
 | loftool | LoFtool | Gene intolerance score based on loss-of-function variants
 | lrt | Likelihood Ratio Test | The likelihood ratio test (LRT) can accurately identify a subset of deleterious mutations that disrupt highly conserved amino acids within protein-coding sequences.
 | mavedb | MaveDB | MaveDB is a public repository for datasets from Multiplexed Assays of Variant Effect (MAVEs).
 | metalr | MetaLR | MetaLR creates an ensemble-based prediction score by using machine learning and logistic regression.
 | metasvm | MetaSVM | MetaSVM creates an ensemble-based prediction score by using a support vector machine model.
 | mirbase | miRBase | A microRNA database is a searchable database of published miRNA sequences and annotation.
 | mitomap | MITOMAP | The MITOMAP database of human mitochondrial DNA (mtDNA) information has been an important compilation of mtDNA variation for researchers, clinicians and genetic counselors.
 | mutation_assessor | Mutation Assessor | Mutation Assessor is a database providing prediction of the functional impact of amino-acid substitutions in proteins
 | mutationtaster | MutationTaster | Evaluates disease-causing potential of sequence alterations
 | mutpanning | Mutpanning | Discovers new tumor genes in aggregated sequencing data.
 | mutpred1 | MutPred | MutPred is a random forest model for the prediction of pathogenic missense variants and automated inference of molecular mechanisms of disease.
 | mutpred_indel | MutPred-Indel | A web application developed to classify human non-frameshifting indels as pathogenic or benign. In addition, it predicts their impact on over 50 different protein properties and, thus, enables the inference of molecular mechanisms of pathogenicity.
 | ncbigene | NCBI Gene | Gene description from NIH's NCBI Gene Info
 | ncer | ncER: non-coding essential regulation | ncER has a good performance for the identification of deleterious variants in the non-coding genome. ncER can also identify non-coding regions associated with cell viability, an in vitro surrogate of essentiality9, and with regulation of an essential gene.
 | ncrna | ncRNA | Non-coding RNA from RepeatMasker library
 | omim | OMIM | Online Mendelian Inheritance in Man. Catalog of human genes and genetic disorders and traits.
 | pangalodb | PangaloDB | PanglaoDB is a single cell gene expression resource for the scientific community. The goal of this database is to provide exploration of single cell RNA sequencing experiments.
 | pharmgkb | PharmGKB | Clinically actionable gene-drug associations and genotype-phenotype relationships
 | phastcons | Phast Cons | A database of compressed phastCons conservation scores.
 | phdsnpg | PhD-SNPg | A binary classifier for predicting pathogenic variants in coding and non-coding regions.
 | phi | p(HI) | Providing probabilities for gene-based haploinsufficiency
 | phylop | PhyloP | A database providing conservation scoring by phylogenetic p-values
 | polyphen2 | PolyPhen-2 | PolyPhen-2 (Polymorphism Phenotyping v2) is a tool which predicts possible impact of an amino acid substitution on the structure and function of a human protein using straightforward physical and comparative considerations
 | prec | P(rec) | Providing probabilities for LoF alleles
 | provean | PROVEAN: Protein Variant Effect Analyzer | A tool to predict the functional effect of amino acid substitutions and indels.
 | pseudogene | Pseudogene | Pseudogenes from UCSC hg38 wgEncodeGencodePseudoGeneV27
 | pubmed | PubMed | PubMed articles related to a particular gene
 | regulomedb | RegulomeDB | Identifies DNA features and regulatory elements in non-coding regions of the human genome.
 | repeat | Repeat Sequences | Repeating elements from RepeatMasker and Simple Repeat tracks of UCSC hg38 database. UCSC Genome Browser Tracks rmsk and simpleRepeat were used to obtain Low complexity, SINE, LINE, LTR, Simple Repeat, and Satellite data and they were combined.
 | rvis | RVIS | Residual variation intolerance scoring
 | siphy | SiPhy | A database of conservation scores based on 29 mammal genomes
 | swissprot_binding | Swiss-Prot Binding | Provides any useful information about the protein, mostly binding sites.
 | swissprot_domains | Swiss-Prot Domains | Provides information on location,topology, and domain(s) of a protein.
 | swissprot_ptm | Swiss-Prot PTM | A high quality manually annotated protein sequence database, specifying in post-translational modifications (PTMs).
 | target | TARGET | Tumor Alterations Relevant for GEnomics-driven Therapy
 | thousandgenomes | 1000 Genomes | Population allele frequencies from 1000 Genomes Project
 | thousandgenomes_ad_mixed_american | 1000 Genomes-Ad Mixed American | Population allele frequencies from 1000 Genomes Project
 | thousandgenomes_african | 1000 Genomes-African | Population allele frequencies from 1000 Genomes Project
 | thousandgenomes_east_asian | 1000 Genomes-East Asian | Population allele frequencies from 1000 Genomes Project
 | thousandgenomes_european | 1000 Genomes-European | Population allele frequencies from 1000 Genomes Project
 | thousandgenomes_south_asian | 1000 Genomes-South Asian | Population allele frequencies from 1000 Genomes Project
 | trinity | Trinity CTAT | Trinity assembles transcript sequences from Illumina RNA-Seq data.
 | uk10k_cohort | UK10k Cohorts | UK10K cohort provides genetic information from DTR & ALSPAC
 | uniprot | UniProt | Comprehensive resource for protein sequence and functional information.