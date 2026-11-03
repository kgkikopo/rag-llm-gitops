# 8.6. Downloading the RHCOS cluster image

The installation program requires the Red Hat Enterprise Linux CoreOS (RHCOS) image to install the cluster. While optional, downloading the Red Hat Enterprise Linux CoreOS (RHCOS) image before deploying removes the need for internet access when creating the cluster. 

**Prerequisites**

  * The host running the installation program has internet access. 



**Procedure**

  1. Change to the directory that contains the installation program and run the following command: 

```shell-session
$ ./openshift-install coreos print-stream-json
```


  2. Use the output of the command to find the location of the IBM Cloud® image. 

```shell-session
.Example output
----
  "release": "415.92.202311241643-0",
  "formats": {
    "qcow2.gz": {
      "disk": {
        "location": "https://rhcos.mirror.openshift.com/art/storage/prod/streams/4.15-9.2/builds/415.92.202311241643-0/x86_64/rhcos-415.92.202311241643-0-ibmcloud.x86_64.qcow2.gz",
        "sha256": "6b562dee8431bec3b93adeac1cfefcd5e812d41e3b7d78d3e28319870ffc9eae",
        "uncompressed-sha256": "5a0f9479505e525a30367b6a6a6547c86a8f03136f453c1da035f3aa5daa8bc9"
----
```


  3. Download and extract the image archive. Make the image available on the host that the installation program uses to create the cluster.
