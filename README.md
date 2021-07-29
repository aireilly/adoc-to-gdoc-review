# gdoc-review
`gdoc-review` is a simple script utility that utilizes pandoc and gdrive tools to generate a google doc direct from a local asciidoc file.

## Prerequisites

* Install the latest version of Pandoc: https://pandoc.org/installing.html. On Fedora, install pandoc with `sudo dnf install pandoc`.
* Install `gdrive`: https://github.com/prasmussen/gdrive. If you have `go` installed, run `go get github.com/prasmussen/gdrive` to install. 
* Give permission to `gdrive` to write to your Google Drive cloud folder.

## Installing

* Copy the `gdoc-review` script to `/usr/local/bin`, and run `chmod a+x gdoc-review` to allow the script to be executed.

That's it! The script should now be ready to use. 

## Python rewrite

May need to visit and revoke access before starting again: https://myaccount.google.com/permissions?pli=1

## Getting started

To generate a google doc review of any assembly or module, open a command prompt, and navigate to the folder that contains the asciidoc. Run the following command, passing in the relative name of the file to be generated, for example,

```
$ gdoc-review modules/ztp-cluster-provisioning.adoc
```  
Follow the link to navigate to the google doc that has just been generated.

**Note:** Every run of `gdoc-review` generates a new output file, previous output files are not overwritten. 
