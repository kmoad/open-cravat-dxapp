# OpenCRAVAT

OpenCRAVAT performs genomic variant interpretation including variant impact, annotation, and scoring.

OpenCRAVAT has a modular architecture with a wide variety of analysis modules that can be selected and run based on the needs of a given study. The modules are made available via the CRAVAT Store and are developed both by the CRAVAT team and the broader variant analysis community. This DNAnexus app uses packages of related modules to streamline the selection of modules.

OpenCRAVAT is a product of the [Karchin Lab](https://karchinlab.org) at [Johns Hopkins University](https://jhu.edu) with funding provided by the National Cancer Institute’s [ITCR](https://itcr.cancer.gov/) program.

## What does this app do?

This app applies annotations to a variant file from a wide variety of analysis modules.

## What are typical use cases for this app?

Variant and gene level annotations can be applied to a VCF. The provided packages compile several popular annotators and filters for specific areas of research such as clinical relavance or drug interactions.

## What data are required for this app to run?

The primary input for OpenCRAVAT on DNAnexus is a VCF file containing variants.

## What does this app output?

OpenCRAVAT on DNAnexus will produce a VCF file with the same variants as the input along with annotations based on the selected annotator package.

## How does this app work?

For more information, check the OpenCRAVAT documentation at:

https://open-cravat.readthedocs.io/en/latest/index.html

## Packages

| Package Name | Description | Included Annotators |
| ------------ | ------------------- | ------- |
| default | The default package includes a wide range of popular annotation modules to provide a strong overview of a variant. | `gnomAD3`, `clinvar`, `cosmic`, `GO`, `polyphen2`, `sift`, `vest`, `chasmplus`, `revel`, `cadd_exome`, `dann_coding` |
| drug_interaction | Identify variants with potential impact on drug reponse. | `clinvar`, `pharmgkb`, `clingen`, `dgi` |
| hereditary | Reports on variants in a list of genes implicated in nine hereditary cancer types by the [Cancer Gene Census](https://cancer.sanger.ac.uk/census) | `clinvar`, `cosmic`, `dbsnp`, `gnomad3`, `oncokb`, `cgc` |
| pathogenic | Identifies variants that have been annotated as being associated with disease. |  `clinvar`, `clinvar_acmg`, `denovo`, `gwas_catalog`, `clingen` |
| rare_coding | The gnomAD3 annotator is used to determine variant allele frequency.  Only variants occuring in the general population less than 1% of the time are included. **Note**: A review of population specific allele frequency may be appropriate as a variant could occur at higher rates in specific sub-populations. |  `dbsnp`, `gnomad3`, `go`, `ncbigene` |
| splicing | This package combines multiple methods and applies filters to select variants that are likely to disrupt mRNA transcript splicing (cryptic splicing). | `dbscsnv`, `spliceai`, `ncbigene` |

## Additional Annotators

The OpenCRAVAT module store features over one hundred annotators which can be included in a run. To add additional annotators to a package, supply a comma-separated list of annotators such as:

```clinvar, cosmic, dbsnp```

For a complete list of annotators, please see the module store of the OpenCRAVAT public web interface at:

https://run.opencravat.org/submit/nocache/index.html
