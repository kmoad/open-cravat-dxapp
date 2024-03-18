#!/bin/bash
# open-cravat 0.0.1
# Generated by dx-app-wizard.
#
# Basic execution pattern: Your app will run on a single machine from
# beginning to end.
#
# Your job's input variables (if any) will be loaded as environment
# variables before this script runs.  Any array inputs will be loaded
# as bash arrays.
#
# Any code outside of main() (or any entry point you may add) is
# ALWAYS executed, followed by running the entry point itself.
#
# See https://documentation.dnanexus.com/developer for tutorials on how
# to modify this file.

main() {
    
    set -x

    echo "Value of input_file: '$input_file'"
    echo "Value of default_annotators: '$default_annotators'"
    echo "Value of genome: '$genome'"
    echo "Value of store_url: '$store_url'"
    echo "Value of annotator01: '$annotator01'"
    echo "Value of annotator02: '$annotator02'"
    echo "Value of annotator03: '$annotator03'"
    echo "Value of annotator04: '$annotator04'"
    echo "Value of annotator05: '$annotator05'"
    echo "Value of annotator06: '$annotator06'"
    echo "Value of annotators: '${annotators[@]}'"

    if [ $default_annotators = true ]
    then
        echo "include default annotators"
        annotators+=( \
                      'clinvar' \
                      'gnomad3' \
                      'phylop' \
                      'revel' \
                      'dbsnp' \
                      'encode_tfbs' \
                      'ncer' \
                      'go' \
                      'cscape' \
                      'dann' \
                    )
    else
        echo "no default annotators"
    fi

    if [ ! -z "$annotator01" ]; then annotators+=("$annotator01"); fi;
    if [ ! -z "$annotator02" ]; then annotators+=("$annotator02"); fi;
    if [ ! -z "$annotator03" ]; then annotators+=("$annotator03"); fi;
    if [ ! -z "$annotator04" ]; then annotators+=("$annotator04"); fi;
    if [ ! -z "$annotator05" ]; then annotators+=("$annotator05"); fi;
    if [ ! -z "$annotator06" ]; then annotators+=("$annotator06"); fi;

    echo "Full value of annotators: '${annotators[@]}'"

    if (( ${#annotators[@]} ));
    then
        addtlAnnotators=true
    else
        addtlAnnotators=false
    fi

    containerRef='karchinlab/opencravat:vcfanno'
    docker pull $containerRef

    # The following line(s) use the dx command-line tool to download your file
    # inputs to the local file system using variable names for the filenames. To
    # recover the original filenames, you can use the output of "dx describe
    # "$variable" --name".
    input_fn=`dx describe "$input_file" --name`
    dx download "$input_file" -o "$input_fn"

    #debug
    pwd
    ls -la .
    ls -la /opencravat

    # Fill in your application code here.
    #
    # To report any recognized errors in the correct format in
    # $HOME/job_error.json and exit this script, you can use the
    # dx-jobutil-report-error utility as follows:
    #
    #   dx-jobutil-report-error "My error message"
    #
    # Note however that this entire bash script is executed with -e
    # when running in the cloud, so any line which returns a nonzero
    # exit code will prematurely exit the script; if no error was
    # reported in the job_error.json file, then the failure reason
    # will be AppInternalError with a generic error message.

    # The following line(s) use the dx command-line tool to upload your file
    # outputs after you have created them on the local file system.  It assumes
    # that you have used the output field name for the filename for each output,
    # but you can change that behavior to suit your needs.  Run "dx upload -h"
    # to see more options to set metadata.
    
    # Set store to S3 mirror
    mkdir conf
    docker run \
        -v $PWD/conf:/mnt/newconf \
        $containerRef cp /mnt/conf/cravat-system.yml /mnt/newconf
    docker run \
        -v $PWD/conf:/mnt/newconf \
        $containerRef cp /mnt/conf/cravat.yml /mnt/newconf
    sed -i conf/cravat-system.yml -e '/store_url/d'
    echo "store_url: $store_url" >> conf/cravat-system.yml

    # Install base modules
    mkdir md
    docker run \
        -v $PWD/md:/mnt/modules \
	    -v $PWD/conf:/mnt/conf \
        $containerRef oc module install-base
    
    # Install annotators
    if [ $addtlAnnotators = true ]
    then
        docker run \
            -v $PWD/md:/mnt/modules \
            -v $PWD/conf:/mnt/conf \
            $containerRef oc module install -y ${annotators[@]}
    fi
    
    # Run job
    mkdir job
    mv $input_fn job
    runArgs=(oc vcfanno "$input_fn")
    if [ $addtlAnnotators = true ]
    then
        runArgs+=("-a" ${annotators[@]})
    fi
    runArgs+=("--debug")
    docker run \
        -v $PWD/md:/mnt/modules \
	    -v $PWD/conf:/mnt/conf \
        -v $PWD/job:/tmp/job \
        -w /tmp/job \
        $containerRef ${runArgs[@]}

    # Build output vcf
    # annoVcfGz=`basename "$input_fn" '.gz'`
    # annoVcfGz=`basename "$annoVcfGz" '.bgz'`
    # annoVcfGz=`basename "$annoVcfGz" '.bz'`
    # annoVcfGz=`basename "$annoVcfGz" '.vcf'`
    # annoVcfGz="$annoVcfGz".opencravat.vcf.gz
    annoVcfGz="$input_fn".oc.vcf.bgz
    annoVcfGzTbi="$annoVcfGz".tbi
    # docker run \
    #     -v $PWD/md:/mnt/modules \
    #     -v $PWD/conf:/mnt/conf \
    #     -v $PWD/job:/tmp/job \
    #     -v /opencravat:/opencravat \
    #     -w /tmp/job \
    #     $containerRef python /opencravat/oc-vcf-anno.py "$input_fn".sqlite "$input_fn" -b -o "$annoVcfGz"
    docker run \
        -v $PWD/job:/tmp/job \
        -w /tmp/job \
        $containerRef tabix "$annoVcfGz"

    # The following line(s) use the utility dx-jobutil-add-output to format and
    # add output variables to your job's output as appropriate for the output
    # class.  Run "dx-jobutil-add-output -h" for more information on what it
    # does.

    ls job

    # sqlite=$(dx upload "job/$input_fn.sqlite" --brief)
    # log=$(dx upload "job/$input_fn.log" --brief)
    # err=$(dx upload "job/$input_fn.err" --brief)
    vcf=$(dx upload "job/$annoVcfGz" --brief)
    tbi=$(dx upload "job/$annoVcfGzTbi" --brief)


    # dx-jobutil-add-output sqlite "$sqlite" --class=file
    # dx-jobutil-add-output log "$log" --class=file
    # dx-jobutil-add-output err "$err" --class=file
    dx-jobutil-add-output vcf "$vcf" --class=file
    dx-jobutil-add-output tbi "$tbi" --class=file
}
