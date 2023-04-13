# OpenCRAVAT (DNAnexus Platform App)

This is the source code for an app that runs on the DNAnexus Platform.

## Installing

To start, [install the `dx` command line tool](https://documentation.dnanexus.com/downloads#installing-the-python-sdk-and-command-line-tools).

Log in with the [`dx login`](https://documentation.dnanexus.com/getting-started/cli-quickstart#step-1-log-in) command. Then switch to your project 
```
dx select <ProjectName>
```

Next, clone this repository and navigate to it.
```
git clone https://github.com/KarchinLab/open-cravat-dxapp.git
cd open-cravat-dxapp
```

Use [dx build](https://documentation.dnanexus.com/user/helpstrings-of-sdk-command-line-utilities#build) to build the applet.

```
dx build open-cravat
```

On the DNAnexus platform GUI, the applet will appear at the top level of your project's files. 

To update the applet, add the `--overwrite` or `-f` flag to `dx build`.

```
dx build --overwrite open-cravat
```

## Running

To run the applet in the GUI, simply find the applet in your project's files and click it.

The applet can also be run from a terminal using [`dx run`](https://documentation.dnanexus.com/user/helpstrings-of-sdk-command-line-utilities#run)

For documentation of the app, and a detailed explanation of parameters, see the main app readme at [`open-cravat/Readme.md`](./open-cravat/Readme.md)