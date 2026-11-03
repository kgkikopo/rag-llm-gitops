# 8.7. Manually updating the boot image on an RHOSP cluster

For a Red Hat OpenStack Platform (RHOSP) cluster, you can manually update the boot image for your cluster by configuring your machine sets to use the latest OpenShift Container Platform image as the boot image to help ensure any new nodes can scale up properly. 

Note

The standard boot image management feature is not supported for RHOSP clusters. 

The following procedure, which includes steps to create environment variables that facilitate running the required commands, shows how to obtain RHOSP authentication credentials, download a boot image, upload that image to the RHOSP image service (Glance), and modify your worker machine sets to use the new boot image. 

This procedure requires the `clouds.yaml` file, which is needed by the OpenStackClient CLI to connect to your RHOSP cloud. If you need to re-create this file, you can get the RHOSP credentials from an OpenShift Container Platform secret, the name of which you can find in the default compute machine set. You can decrypt this secret and export the credentials to create the `clouds.yaml` file, as described in the following procedure. 

Note

Updating control plane machine sets is not supported in RHOSP. 

**Prerequisites**

  * You have completed the general boot image prerequisites as described in the Prerequisites section of [OpenShift Container Platform Boot Image Updates](https://access.redhat.com/articles/7053165#prerequisites-2). 
  * You have downloaded the latest version of the OpenShift Container Platform installation program, openshift-install, from the [OpenShift Cluster Manager](https://console.redhat.com/openshift). For more information, see "Obtaining the installation program." 
  * You have installed the OpenShift CLI (`oc`) installed. 
  * You have installed the [OpenStackClient (RHCOS documentation)](https://docs.openstack.org/python-openstackclient/latest/). 
  * You have installed the [`jq`](https://stedolan.github.io/jq/) program. 



**Procedure**

  1. If you need to re-create the `clouds.yaml` file, perform the following steps: 

     1. Obtain the name of the secret that contains your credentials by running the following command: 

```shell-session
$ oc get machineset -n openshift-machine-api -o yaml | grep cloudsSecret -A 1
```


**Example output**

```shell-session
cloudsSecret:
  name: openstack-cloud-credentials
```


     2. Decrypt the secret and add the contents to the `clouds.yaml` file by running the following command: 

```shell-session
$ oc get secret <secret_name> -n openshift-machine-api -o jsonpath='{.data.clouds\.yaml}' | base64 -d > <file_path>/clouds.yaml
```


Replace `<secret_name>` with the name of the secret, which you obtained in the previous step, and `<file_path>` with the path to the `clouds.yaml` file. 

     3. Optional: Verify the contents of the `clouds.yaml` file by running the following command: 

```shell-session
$ cat <file_path>/clouds.yaml
```


Replace `<file_path>` with the path to the `clouds.yaml` file. 

**Example output**

```shell-session
clouds:
  openstack:
    auth:
      auth_url: https://your-openstack-url:13000
      username: "your-username"
      password: "your-password"
      project_name: "your-project"
      user_domain_name: "Default"
      project_domain_name: "Default"
```


  2. Set an environment variable for the location of the `clouds.yaml` file by running the following command: 

```shell-session
$ export OS_CLIENT_CONFIG_FILE=<file_path>/clouds.yaml
```


Replace `<file_path>` with the path to the `clouds.yaml` file. 

The OpenStackClient CLI uses this environment variable to locate the `clouds.yaml` file. 

  3. Obtain the name of your RHOSP cloud from the default compute machine set and set the name in an environment variable by running the following command: 

```shell-session
$ export CLOUD_NAME=$(oc get machineset -n openshift-machine-api -o jsonpath='{.items[0].spec.template.spec.providerSpec.value.cloudName}')
```


  4. Obtain the URL of the RHCOS image you want to use as the boot image and set the location in an environment variable by running one of the following commands, based on cluster architecture: 

     * Linux (x86_64, amd64): 

```shell-session
$ export RHCOS_URL=$(openshift-install coreos print-stream-json | jq -r \
  '.architectures.x86_64.artifacts.openstack.formats."qcow2.gz".disk.location')
```


     * Linux on IBM Z® and IBM® LinuxONE (s390x): 

```shell-session
$ export RHCOS_URL=$(openshift-install coreos print-stream-json | jq -r \
  '.architectures.s390x.artifacts.openstack.formats."qcow2.gz".disk.location')
```


     * Linux on ARM (aarch64, arm64) 

```shell-session
$ export RHCOS_URL=$(openshift-install coreos print-stream-json | jq -r \
  '.architectures.aarch64.artifacts.openstack.formats."qcow2.gz".disk.location')
```


  5. Obtain the boot image and upload the image to the RHOSP image service (Glance): 

     1. Download the image by using the following command: 

```shell-session
$ curl -L -o /tmp/rhcos-new.qcow2.gz "${RHCOS_URL}"
```


`RHCOS_URL` is the URL environment variables you created in a previous step. 

     2. Decompress the downloaded image by using the following command: 

```shell-session
$ gunzip <file_path>/rhcos-new.qcow2.gz
```


Replace `<file_path>` with the path to the location for the image. 

     3. Set an environment variable to create a descriptive name for your boot image in Glance by running the following command: 

```shell-session
$ export IMAGE_NAME="<descriptive_image_name>"
```


Setting a descriptive name for your boot image, such as using the Red Hat Enterprise Linux CoreOS (RHCOS) version number in the image name, makes it easier to track which version is currently deployed if you update the cluster in the future. 

**Example command**

```shell-session
$ export IMAGE_NAME="rhcos 9.6 boot image"
```


     4. Upload the image to Glance by using the following command: 

```shell-session
$ openstack --os-cloud "${CLOUD_NAME}" image create "${IMAGE_NAME}" \
  --disk-format qcow2 \
  --container-format bare \
  --file <file_path>/rhcos-new.qcow2 \
  --property os_type=linux \
  --property os_distro=rhcos
```


Replace `<file_path>` with the path to the location for the image. 

`CLOUD_NAME` and `IMAGE_NAME` are environment variables you created in previous steps. 

It might take several minutes for the image to upload. When the upload is complete, details on the image displays, similar to the following example: 

**Example output**

```shell-session
+------------------+----------------------------------------+
| Field            | Value
+------------------+----------------------------------------+
| checksum         | 469fa549f706617ff15b41bd2a919679       |
# ...                                                       |
| disk_format      | qcow2                                  |
# ...
| name             | rhcos 9.6 boot image
```


     5. Optional: Verify that the image has uploaded and is in active state by running the following command: 

```shell-session
$ openstack --os-cloud "${CLOUD_NAME}" image show "${IMAGE_NAME}" -f json | jq '{name: .name, status: .status}'
```


**Example output**

```shell-session
{
  "name": "rhcos 9.6 boot image",
  "status": "active"
}
```


  6. Update each of your compute machine sets to include the new boot image: 

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
$ oc patch machineset <machineset_name> -n openshift-machine-api --type merge -p \
  '{"spec":{"template":{"spec":{"providerSpec":{"value":{"image":"'${IMAGE_NAME}'"}}}}}}'
```


Replace `<machineset_name>` with the name of your machine set. 

`IMAGE_NAME` is the environment variable you created in a previous step. 

  7. If boot image skew enforcement in your cluster is set to the manual mode, update the version of the new boot image in the `MachineConfiguration` object as described in "Updating the boot image skew enforcement version". 



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

After you migrate all machine sets to the new boot image, you can remove the old boot image from Glance.
