# 8.1. Installing the opm CLI

## 8.1.1. About the opm CLI

The `opm` CLI is an Operator Framework tool for creating and maintaining Operator catalogs from bundle images in OpenShift Container Platform. You can use it to build catalog container images that Operator Lifecycle Manager (OLM) references through catalog sources. 

A catalog contains a database of pointers to Operator manifest content that can be queried through an included API that is served when the container image is run. On OpenShift Container Platform, Operator Lifecycle Manager (OLM) can reference the image in a catalog source, defined by a `CatalogSource` object, which polls the image at regular intervals to enable frequent updates to installed Operators on the cluster. 

**Additional resources**

  * See [Operator Framework packaging format](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operators/#olm-bundle-format_olm-packaging-format) for more information about the bundle format. 



## 8.1.2. Installing the opm CLI

You can install the `opm` CLI tool on your Linux, macOS, or Windows workstation. 

**Prerequisites**

  * For Red Hat Enterprise Linux (RHEL) 9.0 and later, you must provide the following packages: 

    * `podman` version 1.9.3+ (version 2.0+ recommended) 
    * `glibc` version 2.28+ 




**Procedure**

  1. Navigate to the [OpenShift mirror site](https://mirror.openshift.com/pub/openshift-v4/x86_64/clients/ocp/latest-4.22/) and download the latest version of the tarball that matches your operating system. 
  2. Unpack the archive. 

     * For Linux or macOS: 

```shell-session
$ tar xvf <file>
```


     * For Windows, unzip the archive with a ZIP program. 

  3. Place the file anywhere in your `PATH`. 

     * For Linux or macOS: 

       1. Check your `PATH`: 

```shell-session
$ echo $PATH
```


       2. Move the file. For example: 

```shell-session
$ sudo mv ./opm /usr/local/bin/
```


     * For Windows: 

       1. Check your `PATH`: 

```shell-session
C:\> path
```


       2. Move the file: 

```shell-session
C:\> move opm.exe <directory>
```


**Verification**

  * After you install the `opm` CLI, verify that it is available: 

```shell-session
$ opm version
```


## 8.1.3. Additional resources

  * See [Managing custom catalogs](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operators/#olm-managing-custom-catalogs) for `opm` procedures including creating, updating, and pruning catalogs.
