# 8.6. Manually updating the boot image on a Nutanix cluster

You can manually update the boot image for your Nutanix cluster by configuring your machine sets to use the latest OpenShift Container Platform image as the boot image to ensure that new nodes can scale up properly. 

Note

The standard boot image management feature is not supported for Nutanix clusters. 

The following procedure, which includes steps to create environment variables that facilitate running the required commands, shows how to obtain Nutanix authentication credentials, download a boot image, upload that image to the Nutanix Prism Central, and modify your compute machine sets to use the new boot image. 

This procedure requires Nutanix authentication credentials, which you need to access Prism Central. If you need to recover your credentials, you can get them from an OpenShift Container Platform secret, the name of which you can find in the default compute machine set. You can decrypt this secret and export the credentials to create the `clouds.yaml` file, as described in the following procedure. 

**Prerequisites**

  * You have completed the general boot image prerequisites as described in the "Prerequisites" section of the [OpenShift Container Platform Boot Image Updates knowledgebase article](https://access.redhat.com/articles/7053165#prerequisites-2). 
  * You have downloaded the latest version of the OpenShift Container Platform installation program, openshift-install, from the [OpenShift Cluster Manager](https://console.redhat.com/openshift). For more information, see "Obtaining the installation program." 
  * You have installed the OpenShift CLI (`oc`). 
  * You have installed the [`jq`](https://stedolan.github.io/jq/) program. 



**Procedure**

  1. If you need to recover your Nutanix authentication credentials, perform the following steps: 

     1. Obtain the name of the secret that contains your credentials by running the following command: 

```shell-session
$ oc get machineset -n openshift-machine-api -o yaml | grep credentialsSecret -A 1
```


**Example output**

```shell-session
    credentialsSecret:
      name: nutanix-credentials
```


     2. Decrypt the secret by running the following command: 

```shell-session
$ oc get secret <secret_name> -n openshift-machine-api -o jsonpath='{.data.credentials}' | base64 -d
```


Replace `<secret_name>` with the name of the secret, which you obtained in the previous step. 

**Example output**

```shell-session
[{"type":"basic_auth","data":{"prismCentral":{"username":"","password":""},"prismElements":null}}]
```


  2. Set an environment variable for the Nutanix username by running the following command: 

```shell-session
$ export USER="<username>"
```


  3. Set an environment variable for the Nutanix password by running the following command: 

```shell-session
$ export PASS="<password>"
```


  4. If you need to recover your IP address for Prism Central, run the following command: 

```shell-session
$ oc get configmap cloud-provider-config -n openshift-config -o jsonpath='{.data.config}' | grep prismCentral -A 8
```


**Example output**

```shell-session
    "prismCentral": {
        "address": "",
        "port": 9440,
        "credentialRef": {
            "kind": "Secret",
            "name": "nutanix-credentials",
            "namespace": "openshift-cloud-controller-manager"
        }
    },
```


where: 

`prismCentral.address`
     Specifies the Prism Central IP address. 

  5. Set an environment variables for the Prism Central IP address by running the following command: 

```shell-session
$ export PC_IP="<prism_central_ip_address>"
```


  6. Obtain the boot image and upload the image to Prism Central: 

     1. Obtain the URL of the RHCOS image you want to use as the boot image and set the location in an environment variable by running the following command: 

```shell-session
$ export RHCOS_URL=$(openshift-install coreos print-stream-json | jq -r '.architectures.x86_64.artifacts.nutanix.formats.qcow2.disk.location')
```


     2. Set an environment variable to create a descriptive name for your boot image in Prism Central by running the following command: 

```shell-session
$ export IMAGE_NAME="<descriptive_image_name>"
```


Setting a descriptive name for your boot image in Prism Central, such as using the Red Hat Enterprise Linux CoreOS (RHCOS) version number in the image name, makes it easier to track which version is currently deployed if you update the cluster in the future. 

**Example command**

```shell-session
$ export IMAGE_NAME="rhcos-9.6-boot-image"
```


     3. Upload the image to Prism Central by running the following command: 

```shell-session
$ curl -k -u "$USER:$PASS" \
  -X POST "https://$PC_IP:9440/api/nutanix/v3/images" \
  -H "Content-Type: application/json" \
  -d '{
    "spec": {
      "name": "'"$IMAGE_NAME"'",
      "resources": {
        "image_type": "DISK_IMAGE",
        "source_uri": "'"$RHCOS_URL"'"
      }
    },
    "metadata": {
      "kind": "image"
    }
  }'
```


`USER`,`PASS`, `IMAGE_NAME`, and `RHCOS_URL` are environment variables you created in previous steps. 

     4. Optional: Verify that the image is uploaded by running the following command: 

```shell-session
$ curl -k -u "$USER:$PASS" \
  -X POST "https://$PC_IP:9440/api/nutanix/v3/images/list" \
  -H "Content-Type: application/json" \
  -d '{
    "kind": "image",
    "filter": "name=='"$IMAGE_NAME"'"
  }'
```


**Example output**

```shell-session
{
  "name": "<image-name>",
  "state": "COMPLETE"
}
```


  7. Update each of your compute machine sets to include the new boot image: 

     1. Obtain the name of your machine sets for use in the following step by running the following command: 

```shell-session
$ oc get machineset -n openshift-machine-api
```


**Example output**

```shell-session
NAME                                 DESIRED   CURRENT   READY   AVAILABLE   AGE
rhhdrbk-b5564-4pcm9-worker-0         3         3         3       3           123m
ci-ln-xj96skb-72292-48nm5-worker-d   1         1         1       1           27m
```


     2. Edit a machine set to update the `image` field in the `providerSpec` stanza to add your boot image by running the following command: 

```shell-session
$ oc patch machineset <machineset_name> -n openshift-machine-api --type merge -p '{"spec":{"template":{"spec":{"providerSpec":{"value":{"image":{"type":"name","name":"'${IMAGE_NAME}'"}}}}}}}'
```


Replace `<machineset_name>` with the name of your machine set. 

  8. If boot image skew enforcement in your cluster is set to the manual mode, update the version of the new boot image in the `MachineConfiguration` object as described in "Updating the boot image skew enforcement version". 



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

  3. Verify that the boot image is the same version as the image you uploaded in a previous step by running the following command: 

```shell-session
$ echo ${RHCOS_URL}
```


**Example output**

```shell-session
https://rhcos.mirror.openshift.com/art/storage/prod/streams/rhel-9.6/builds/9.6.20251212-1/x86_64/rhcos-9.6.20251212-1-nutanix.x86_64.qcow2
```


After you migrate all machine sets to the new boot image, you can remove the old boot image from Prism Central.
