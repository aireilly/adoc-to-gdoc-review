# gdoc-review

`gdoc-review` is a simple script utility that utilizes `asciidoctor` and `pandoc` to generate a Google Doc from a local AsciiDoc file for easy review.

## New in this version

* Removed dependency on the `gdrive` tool which cannot be used without setting up GCP IAM access to your GDrive account 😧

## Prerequisites

* Install Asciidoctor: https://docs.asciidoctor.org/asciidoctor/latest/install/linux-packaging/. On Fedora, run `sudo dnf install -y asciidoctor`.

* Install Pandoc: https://pandoc.org/installing.html. On Fedora, run `sudo dnf install pandoc`.

* Install `gio` CLI tool. on Fedora, run `sudo dnf install glib2-devel`

* Connect your Red Hat Google account to your online account in the Settings app in Fedora or RHEL. This mounts the Google Drive user account folder locally. 

![image](https://github.com/aireilly/adoc-to-gdoc-review/assets/74046732/2722198c-edb0-43be-a0f1-8c5646fd8e98)

## Installing

* Copy the `gdoc-review` script to `~/bin`, and run `chmod a+x ~/bin/gdoc-review` to allow the script to be executed from anywhere in your file system.

* Create a `~/.gdoc-review` file populated with frequently used Asciidoctor variables. This ensures that variables are always resolved in the output. For example:

```ini
[asciidoctor-attributes]
product-title=OpenShift Container Platform
product-version=4.14
sno=single-node OpenShift
sno-caps=Single-node OpenShift
cgu-operator-first=Topology Aware Lifecycle Manager (TALM)
cgu-operator-full=Topology Aware Lifecycle Manager
cgu-operator=TALM
redfish-operator=Bare Metal Event Relay
rh-rhacm-first=Red Hat Advanced Cluster Management (RHACM)
rh-rhacm=RHACM
ztp=GitOps ZTP
ztp-first=GitOps zero touch provisioning (ZTP) 
op-system-first=Red Hat Enterprise Linux CoreOS (RHCOS)
op-system=RHCOS
icons=image
iconsdir=/home/aireilly/icons
```

That's it! The script should now be ready to use. 

## Getting started

To generate a review doc of any assembly or module, open a shell prompt, and change to the folder that contains the AsciiDoc file. Run the following command, passing in the AsciiDoc file as input, for example:

```
$ gdoc-review modules/ztp-cluster-provisioning.adoc
```  

Follow the link to open the generated Google doc.

**Note:** Every run of `gdoc-review` overwrites the previous output. 
