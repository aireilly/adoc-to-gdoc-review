# gdoc-review

`gdoc-review` is a simple script utility that utilizes `pandoc` and `gdrive` tools to generate a google doc directly from a local asciidoc file.

## Prerequisites

* Install the latest version of Pandoc: https://pandoc.org/installing.html. On Fedora, install pandoc with `sudo dnf install pandoc`.
* Install `gdrive`: https://github.com/prasmussen/gdrive. If you have `go` installed, run `go get github.com/prasmussen/gdrive` to install. 
* Give permission to `gdrive` to write to your Google Drive cloud folder.

## Installing

* Copy the `gdoc-review` script to `/usr/local/bin`, and run `chmod a+x gdoc-review` to allow the script to be executed from anywhere in the file system.

That's it! The script should now be ready to use. 

## Getting started

To generate a google doc review of any assembly or module, open a command prompt, and navigate to the folder that contains the asciidoc file. Run the following command, passing in the relative name of the asciidoc file, for example:

```
$ gdoc-review modules/ztp-cluster-provisioning.adoc
```  
Follow the link to navigate to the generated google doc.

**Note:** Every run of `gdoc-review` generates a new output file, previous output files are not overwritten. 
