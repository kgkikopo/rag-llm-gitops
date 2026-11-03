# 8.3. Manually updating the boot image on an Google Cloud cluster

You can manually update the boot image for your Google Cloud cluster by configuring your machine sets to use the latest OpenShift Container Platform image as the boot image to ensure that new nodes can scale up properly. 

Use the following procedure to create environment variables that facilitate running the required commands, identify the correct boot image to use as the new boot image, and modify your machine sets to use that image. 

The process differs for clusters that use a default Red Hat Enterprise Linux CoreOS (RHCOS) image, clusters that use a custom Red Hat Enterprise Linux CoreOS (RHCOS) image from the Google Cloud Marketplace, and user-provisioned infrastructure clusters. The following procedure helps determine which type of cluster you have. 

For user-provisioned infrastructure Google Cloud clusters, which typically have no Machine API compute machine sets, you can provision new nodes based on the new boot image by updating the underlying Google Cloud infrastructure with the new boot image, such as instance templates, Deployment Manager templates, or Terraform configuration. For more information, see "Creating additional worker machines in Google Cloud". 

Note

For clusters that use a default Red Hat Enterprise Linux CoreOS (RHCOS) image, you can configure the cluster to automatically update the boot image each time the cluster is updated. If you are using the following procedure, ensure that automatic boot image updates are disabled and skew enforcement is in manual mode. For more information, see "Boot image management" and "Boot image skew enforcement". 

**Prerequisites**

  * You have completed the general boot image prerequisites as described in the "Prerequisites" section of the [OpenShift Container Platform Boot Image Updates knowledgebase article](https://access.redhat.com/articles/7053165#prerequisites-2). 
  * You have installed the OpenShift CLI (`oc`). 
  * You have set boot image skew enforcement to the manual or none mode. For more information, see "Configuring boot image skew enforcement". 
  * You have disabled boot image management for the cluster. For more information, see "Disabling boot image management". 
  * For a cluster that uses a default RHCOS image, ensure that your cluster meets the following additional prerequisites: 

    * You have downloaded the latest version of the OpenShift Container Platform installation program, openshift-install, from the [OpenShift Cluster Manager](https://console.redhat.com/openshift). For more information, see "Obtaining the installation program." 
    * You have installed the [`jq`](https://jqlang.github.io/jq/) program. 

  * For a user-provisioned infrastructure cluster, ensure that your cluster meets the following additional prerequisites: 

    * You have downloaded the latest version of the OpenShift Container Platform installation program from the [OpenShift Cluster Manager](https://console.redhat.com/openshift). For more information, see "Obtaining the installation program." 
    * You have installed the [Google Cloud CLI](https://cloud.google.com/sdk/docs/install). 
    * You have created a Google Cloud service account. 




**Procedure**

  1. Determine which image in the machine set is the boot image and set the value in an environment variable: 

     1. Set the boot image value in an environment variable by running the following command: 

```shell-session
$ export BOOT_DISK_INDEX=$(oc get machineset -n openshift-machine-api -o json | \
  jq '.items[0].spec.template.spec.providerSpec.value.disks | map(.boot == true) | index(true)')
```


     2. Display the contents of the `BOOT_DISK_INDEX` environment variable by running the following command: 

```shell-session
$ echo $BOOT_DISK_INDEX
```


**Example output**

```shell-session
0
```


If the output for the `BOOT_DISK_INDEX` environment variable is `null`, none of the disks in the machine set has the `boot` field explicitly set. In this case, the boot disk is typically the first disk. 

**Example null output**

```shell-session
null
```


     3. If the `BOOT_DISK_INDEX` output is `null`, set the boot image to the first image by running the following command: 

```shell-session
$ export BOOT_DISK_INDEX=0
```


  2. Determine if your cluster uses a default RHCOS image or a GCP Marketplace RHCOS image from the Google Cloud Marketplace, or is a user-provisioned infrastructure cluster: 

     1. Obtain the name of the current boot image and set the name as an environment variable by running the following command: 

```shell-session
$ export CURRENT_IMAGE=$(oc get machineset -n openshift-machine-api -o json | \
  jq -r ".items[0].spec.template.spec.providerSpec.value.disks[${BOOT_DISK_INDEX}].image")
```


`BOOT_DISK_INDEX` is the environment variable you created in a previous step. 

     2. View the name of the image by running the following command: 

```shell-session
$ echo $CURRENT_IMAGE
```


**Example output**

```shell-session
projects/rhcos-cloud/global/images/rhcos-416-94-202510081640-0-gcp-x86-64
```


     3. Compare the prefix of the image name to the entries in the following table: 

Current image prefix| Variant  
---|---  
`projects/rhcos-cloud/global/images/` |  Default   
`projects/redhat-marketplace-public/global/images/` |  GCP Marketplace RHCOS image   
No machine set present/custom prefix  |  User-provisioned infrastructure   
Show more

Default RHCOS clusters use images from the `rhcos-cloud` project in the `rhcos-<version>-<platform>-<arch>` format. 

GCP Marketplace RHCOS clusters use images from the `redhat-marketplace-public` project in the `redhat-coreos-<offering>-<version>-<arch>-<date>` format. 

Note

The following images are the latest Google Cloud Marketplace images for the OpenShift Container Platform: 

OpenShift Container Platform
     `redhat-coreos-ocp-413-x86-64-202305021736`
OpenShift Platform Plus
     `redhat-coreos-opp-413-x86-64-202305021736`
OpenShift Kubernetes Engine
     `redhat-coreos-oke-413-x86-64-202305021736`

Red Hat has not published Marketplace images for OpenShift Container Platform later than these OpenShift Container Platform 4.13 images. If the current boot image in your cluster matches one of the listed images, no further action is necessary. 

  3. Obtain the name of the new boot image by using one of the following steps, depending upon your cluster: 

     * For a cluster that uses a default RHCOS image, perform the following steps: 

       1. Set an environment variable with your cluster architecture by running the following command: 

```shell-session
$ export ARCH=<architecture_type>
```


Replace `<architecture_type>` with one of the following values: 

          * Specify `aarch64` for the AArch64 or ARM64 architecture. 
          * Specify `ppc64le` for the IBM Power® (ppc64le) architecture. 
          * Specify `s390x` for the IBM Z® and IBM® LinuxONE (s390x) architecture. 
          * Specify `x86_64` for the x86_64 or AMD64 architecture. 

You can find the architecture as a label in any `MachineSet` object. 

**Example machine set with an architecture label**

```shell-session
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  annotations:
    capacity.cluster-autoscaler.kubernetes.io/labels: kubernetes.io/arch=amd64
# ...
```


       2. Set an environment variable with the name of the new boot image by running the following command: 

```shell-session
$ export GCP_IMAGE=$(openshift-install coreos print-stream-json | jq -r ".architectures.\"${ARCH}\".images.gcp.name")
```


`ARCH` is the environment variable you created in a previous step. 

       3. Set an environment variable with the Google Cloud project of the new boot image by running the following command: 

```shell-session
$ export GCP_PROJECT=$(openshift-install coreos print-stream-json | jq -r ".architectures.\"${ARCH}\".images.gcp.project")
```


`ARCH` is the environment variable you created in a previous step. 

       4. View the Red Hat Enterprise Linux CoreOS (RHCOS) version of the new boot image by running the following command: 

```shell-session
$ openshift-install coreos print-stream-json | jq -r ".architectures.\"${ARCH}\".images.gcp.release"
```


**Example output**

```shell-session
9.6.20251212-1
```


Make note of the RHCOS version for later use. 

     * For a cluster that uses a GCP Marketplace RHCOS image that is earlier than the 4.13 images listed above, perform the following steps: 

       1. Set an environment variable with the name of the new boot image by running the following command: 

```shell-session
$ export GCP_IMAGE=<image_name>
```


Replace `<image_name>` with one of the following values: 

          * Specify `redhat-coreos-ocp-413-x86-64-202305021736` for an OpenShift Container Platform cluster. 
          * Specify `redhat-coreos-opp-413-x86-64-202305021736` for an OpenShift Platform Plus cluster. 
          * Specify `redhat-coreos-oke-413-x86-64-202305021736` for an OpenShift Kubernetes Engine cluster. 

       2. Set an environment variable with the Google Cloud project of the new boot image by running the following command: 

```shell-session
$ export GCP_PROJECT=redhat-marketplace-public
```


     * For a user-provisioned infrastructure cluster, perform the following steps: 

       1. Set an environment variable with your cluster architecture by running the following command: 

```shell-session
$ export ARCH=<architecture_type>
```


Replace `<architecture_type>` with one of the following values: 

          * Specify `aarch64` for the AArch64 or ARM64 architecture. 
          * Specify `ppc64le` for the IBM Power® (ppc64le) architecture. 
          * Specify `s390x` for the IBM Z® and IBM® LinuxONE (s390x) architecture. 
          * Specify `x86_64` for the x86_64 or AMD64 architecture. 

       2. Set an environment variable with the name of the new boot image by running the following command: 

```shell-session
$ export GCP_IMAGE=$(openshift-install coreos print-stream-json | jq -r ".architectures.\"${ARCH}\".images.gcp.name")
```


`ARCH` is the environment variable you created in a previous step. 

       3. Set an environment variable with the Google Cloud project of the new boot image in your cluster by running the following command: 

```shell-session
$ export GCP_PROJECT=$(openshift-install coreos print-stream-json | jq -r ".architectures.\"${ARCH}\".images.gcp.project")
```


`ARCH` is the environment variable you created in a previous step. 

If the default RHCOS image is not accessible in your environment, for example in a restricted or disconnected environment, you could download the new boot image tar file and upload the file as a custom image to your own Google Cloud project before updating your Google Cloud instance templates. 

Update your Google Cloud instance template(s) to reference the new image, then create new instances from the updated template. The exact steps depend on how your infrastructure was provisioned. For more information, see "Creating additional worker machines in Google Cloud". 

After creating the new instances, you can proceed to the verification steps, unless your user-provisioned infrastructure cluster has any Machine API machine sets, such as for Day-2 scaling. You can update those machine sets as described in the following steps. 

  4. Update each of your compute machine sets to include the new boot image: 

     1. Obtain the name of your machine sets for use in the following step by running the following command: 

```shell-session
$ oc get machineset -n openshift-machine-api
```


**Example output**

```shell-session
NAME                                 DESIRED   CURRENT   READY   AVAILABLE   AGE
ci-ln-xw7zmyt-72292-x7nqv-worker-a   1         1         1       1           53m
ci-ln-xw7zmyt-72292-x7nqv-worker-b   1         1         1       1           53m
ci-ln-xw7zmyt-72292-x7nqv-worker-c   1         1         1       1           53m
```


     2. Edit a machine set to update the `image` field in the `providerSpec` stanza to add your boot image by running the following command: 

```shell-session
$ oc patch machineset <machineset-name> -n openshift-machine-api --type json \
  -p '[{"op": "replace", "path": "/spec/template/spec/providerSpec/value/disks/'${BOOT_DISK_INDEX}'/image", "value": "projects/'${GCP_PROJECT}'/global/images/'${GCP_IMAGE}'"}]'
```


Replace `<machineset_name>` with the name of your machine set. 

`BOOT_DISK_INDEX`, `GCP_PROJECT`, and `GCP_IMAGE` are environment variables you created in previous steps. 

  5. If boot image skew enforcement in your cluster is set to the manual mode, update the version of the new boot image in the `MachineConfiguration` object as described in "Updating the boot image skew enforcement version". 



**Verification**

  1. Scale up a machine set to check that the new node is using the new boot image: 

     1. Increase the machine set replicas by one to trigger a new machine by running the following command: 

```shell-session
$ oc scale --replicas=<count> machineset <machineset_name> -n openshift-machine-api
```


where: 

`<count>`
     Specifies the total number of replicas, including any existing replicas, that you want for this machine set. 
`<machineset_name>`
     Specifies the name of the machine set to scale. 

     2. Optional: View the status of the machine set as it provisions by running the following command: 

```shell-session
$ oc get machines.machine.openshift.io -n openshift-machine-api -w
```


It can take several minutes for the machine set to achieve the `Running` state. 

     3. Verify that the new node has been created and is in the `Ready` state by running the following command: 

```shell-session
$ oc get nodes
```


  2. Verify that the new node is using the new boot image by running the following command: 

```shell-session
$ oc debug node/<new_node> -- chroot /host cat /sysroot/.coreos-aleph-version.json
```


Replace `<new_node>` with the name of your new node. 

**Example output**

```shell-session
{
# ...
    "ref": "docker://ostree-image-signed:oci-archive:/rhcos-9.6.20251212-1-ostree.x86_64.ociarchive",
    "version": "9.6.20251212-1"
}
```


where: 

`version`
     Specifies the boot image version. 

  3. Verify that the boot image is the same the RHCOS version as the image you noted in a previous step by running the following command: 

```shell-session
$ echo $GCP_IMAGE
```


`RHCOS_URL` is the environment variable you created in a previous step. 

**Example output**

```shell-session
https://rhcos.mirror.openshift.com/art/storage/prod/streams/rhel-9.6/builds/9.6.20251212-1/x86_64/rhcos-9.6.20251212-1-nutanix.x86_64.qcow2
```
