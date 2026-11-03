# 8.1. Manually updating the boot image on an Azure cluster

You can manually update the boot image for your Microsoft Azure cluster by configuring your machine sets to use the latest OpenShift Container Platform image as the boot image to ensure that new nodes can scale up properly. 

Note

Boot image updates are not supported for Azure confidential virtual machines and Azure Stack Hub clusters. Contact Red Hat Support for these cases. 

Use the following procedure to create environment variables that facilitate running the required commands, identify the correct boot image to use as the new boot image, and modify your compute machine sets to use that image. 

The process requires you to determine the product variant and Hyper-V generation of your Azure boot image. The following procedure helps determine both values, which you need in order to look up the target image. 

Note

For clusters that use a default Red Hat Enterprise Linux CoreOS (RHCOS), Azure Red Hat OpenShift (ARO), or Azure Marketplace image, you can configure the cluster to automatically update the boot image each time the cluster is updated. If you are using the following procedure, ensure that automatic boot image updates are disabled and skew enforcement is in manual mode. For more information, see "Boot image management" and "Boot image skew enforcement". 

**Prerequisites**

  * You have completed the general boot image prerequisites as described in the "Prerequisites" section of the [OpenShift Container Platform Boot Image Updates knowledgebase article](https://access.redhat.com/articles/7053165#prerequisites-2). 
  * You have installed the OpenShift CLI (`oc`). 
  * You have set boot image skew enforcement to the manual or none mode. For more information, see "Configuring boot image skew enforcement". 
  * You have disabled boot image management for the cluster. For more information, see "Disabling boot image management". 
  * You have downloaded the latest version of the OpenShift Container Platform installation program from the [OpenShift Cluster Manager](https://console.redhat.com/openshift). For more information, see "Obtaining the installation program." 
  * You have installed the [`jq`](https://stedolan.github.io/jq/) program. 



**Procedure**

  1. Set an environment variable with your cluster architecture by running the following command: 

```shell-session
$ export ARCH=<architecture_type>
```


Replace `<architecture_type>` with one of the following values: 

     * Use `aarch64` for the AArch64 or ARM64 architecture. 
     * Use `x86_64` for the x86_64 or AMD64 architecture. 

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


  2. Determine your Azure image variant and Hyper-V generation: 

     1. Obtain the required values from your machine set by running the following command: 

```shell-session
$ oc get machineset <machineset-name> -n openshift-machine-api \
  -o jsonpath='{.spec.template.spec.providerSpec.value.image}'
```


**Example output**

```shell-session
{"offer":"rh-ocp-worker","publisher":"redhat","resourceID":"","sku":"rh-ocp-worker","type":"MarketplaceWithPlan","version":"4.16.20231023"}
```


     2. Determine your image variant by comparing the output to the entries in the following table: 

Output parmeters| Variant  
---|---  
`resourceID` is non-empty  |  `no-purchase-plan`  
`publisher` is `azureopenshift` |  `no-purchase-plan`  
`publisher` is `redhat` and `offer` is `rh-ocp-worker` |  `ocp`  
`publisher` is `redhat` and `offer` is `rh-opp-worker` |  `opp`  
`publisher` is `redhat` and `offer` is `rh-oke-worker` |  `oke`  
`publisher` is `redhat-limited` and `offer` is `rh-ocp-worker` |  `ocp-emea`  
`publisher` is `redhat-limited` and `offer` is `rh-ocp-worker` |  `opp-emea`  
`publisher` is `redhat-limited` and `offer` is `rh-ocp-worker` |  `oke-emea`  
Show more

Make note of the variant for later use. 

     3. Determine your image Hyper-V generation by comparing the output to the entries in the following table: 

Output| Image type| Hyper-V generation  
---|---|---  
`resourceID` is non-empty  |  Legacy uploaded  | 
        * `hyperVGen2` if the `resourceID` value contains `gen2`
        * `hyperVGen1` if the `resourceID` value does not contain `gen2`  
`publisher` is `azureopenshift` |  Unpaid marketplace  | 
        * `hyperVGen2` if `sku` contains `v2` or the cluster architecture is AArch64 or ARM64 
        * `hyperVGen1` for all other images   
`publisher` is `redhat` or `redhat-limited`.  |  Paid marketplace  | 
        * `hyperVGen1` if `sku` contains `-gen1`
        * `hyperVGen2` for all other images   
Show more

Make note of the generation for later use. 

     4. Optional: You can compare the output of the `version` parameter against the output of the following command to determine if your boot image needs updating. 

```shell-session
$ openshift-install coreos print-stream-json | jq '.architectures."'"${ARCH}"'"."rhel-coreos-extensions"."marketplace"."azure"'
```


`ARCH` is the environment variable you created in a previous step. 

In the output of the command, locate your variant and generation as shown in the following example: 

**Example output**

```shell-session
  "ocp": {
# ...
    "hyperVGen2": {
      "publisher": "redhat",
      "offer": "rh-ocp-worker",
      "sku": "rh-ocp-worker",
      "version": "4.18.2025031114"
```


If the boot image referenced in the `version` parameter of your machine set matches or is later than the version in this output, no further action on your part is required to update the boot image. If not, continue with this procedure. 

  3. Obtain the values needed to identify the new boot image and set the values as environment variables: 

     1. Obtain the values required for the new boot image by running the following command: 

```shell-session
$ openshift-install coreos print-stream-json | jq '.architectures."'"${ARCH}"'"."rhel-coreos-extensions"."marketplace"."azure"'
```


`ARCH` is the environment variable you created in a previous step. 

     2. In the output of the command, locate your variant and generation as shown in the following example: 

**Example output**

```shell-session
  "ocp": {
  # ...
    "hyperVGen2": {
      "publisher": "redhat",
      "offer": "rh-ocp-worker",
      "sku": "rh-ocp-worker",
      "version": "9.6.20251015"
```


     3. Set an environment variable with your image variant by running the following command: 

```shell-session
$ export VARIANT=<variant>
```


Replace `<variant>` with the variant of your image, one of the following vales: `no-purchase-plan`, `ocp`, `opp`, `oke`, `ocp-emea`, `opp-emea`, or `oke-emea`. 

     4. Set an environment variable with your image generation by running the following command: 

```shell-session
$ export GEN=<generation>
```


Replace `<generation>` with the generation of your image, one of the following vales: `hyperVGen1` or `hyperVGen2`. 

     5. Set environment variables for the `publisher`, `offer`, `sku`, and `version` fields based on the `openshift-install` output for your variant and generation by running the following commands: 

```shell-session
$ export PUBLISHER=$(openshift-install coreos print-stream-json | jq -r '.architectures."'"${ARCH}"'"."rhel-coreos-extensions"."marketplace"."azure"."'"${VARIANT}"'"."'"${GEN}"'".publisher')
```


`ARCH`, `VARIANT`, and `GEN` are environment variables you created in a previous step. 

```shell-session
$ export OFFER=$(openshift-install coreos print-stream-json | jq -r '.architectures."'"${ARCH}"'"."rhel-coreos-extensions"."marketplace"."azure"."'"${VARIANT}"'"."'"${GEN}"'".offer')
```


```shell-session
$ export SKU=$(openshift-install coreos print-stream-json | jq -r '.architectures."'"${ARCH}"'"."rhel-coreos-extensions"."marketplace"."azure"."'"${VARIANT}"'"."'"${GEN}"'".sku')
```


```shell-session
$ export VERSION=$(openshift-install coreos print-stream-json | jq -r '.architectures."'"${ARCH}"'"."rhel-coreos-extensions"."marketplace"."azure"."'"${VARIANT}"'"."'"${GEN}"'".version')
```


     6. Obtain the RHCOS version by running the following command: 

```shell-session
$ echo $VERSION
```


**Example output**

```shell-session
9.6.20251015
```


Make note of the RHCOS version for later use. 

     7. Set an environment variable with the type of your image by running the following command: 

```shell-session
$ export IMAGE_TYPE=<image_type>
```


Replace `<image_type>` with one of the following values based on the variant of your image: 

        * For the `no-purchase-plan` variant, use `MarketplaceNoPlan`. 
        * For all other variants, use `MarketplaceWithPlan`. 

  4. Update each of your compute machine sets to include the new boot image: 

     1. Obtain the name of your machine sets for use in the following step by running the following command: 

```shell-session
$ oc get machineset -n openshift-machine-api
```


**Example output**

```shell-session
NAME                                        DESIRED   CURRENT   READY   AVAILABLE   AGE
ci-ln-lbf9h9k-1d09d-fwh4l-worker-eastus21   1         1         1       1           135m
ci-ln-lbf9h9k-1d09d-fwh4l-worker-eastus22   1         1         1       1           135m
ci-ln-lbf9h9k-1d09d-fwh4l-worker-eastus23   1         1         1       1           135m
```


     2. Edit a machine set to update the `image` field in the `providerSpec` stanza to add your boot image by running the following command: 

```shell-session
$ oc patch machineset <machineset-name> -n openshift-machine-api --type merge \
  -p '{"spec":{"template":{"spec":{"providerSpec":{"value":{"image":{"publisher":"'${PUBLISHER}'","offer":"'${OFFER}'","sku":"'${SKU}'","version":"'${VERSION}'","resourceID":"","type":"'${IMAGE_TYPE}'"}}}}}}}'
```


`PUBLISHER`, `OFFER`, `SKU`, `VERSION`, and `IMAGE_TYPE` are environment variables you created in previous steps. 

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
    "ref": "docker://ostree-image-signed:oci-archive:/rhcos-9.6.20251015-ostree.x86_64.ociarchive",
    "version": "9.6.20251015"
}
```


where: 

`version`
     Specifies the boot image version. 

  3. Verify that the boot image is the same the RHCOS version as the image you noted in a previous step by running the following command: 

```shell-session
$ echo $VERSION
```


**Example output**

```shell-session
9.6.20251015
```
