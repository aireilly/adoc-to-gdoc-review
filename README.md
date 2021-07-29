# adoc-to-gdoc-review
`gdoc-review` is a simple script utility that utilizes pandoc and gdrive tools to generate a google doc direct from assciidoc.

## Prerequisites

* Install the latest version of Pandoc: https://pandoc.org/installing.html. On Fedora, run `sudo dnf install pandoc`
* Install gdrive: https://github.com/prasmussen/gdrive. If you have `go` installed, run `go get github.com/prasmussen/gdrive`. Once installed, you will need to give permission to `gdrive` to write to your google drive cloud folder.
* Copy the `gdoc-review` script to `/usr/local/bin`, and run `chmod a+x gdoc-review` to allow the script to be executed.

That's it! The script should now be ready to use. To generate a google doc review of any assembly or module, open a command prompt, and navigate to the folder that contains the asciidoc. Run the following command, passing in the relative name of the file to be generated, for example,

```
gdoc-review modules/ztp-cluster-provisioning.adoc
```  
