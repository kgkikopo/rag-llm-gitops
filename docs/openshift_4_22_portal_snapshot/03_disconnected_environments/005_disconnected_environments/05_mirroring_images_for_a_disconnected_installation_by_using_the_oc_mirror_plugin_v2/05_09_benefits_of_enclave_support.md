# 5.9. Benefits of enclave support

Enclave support restricts internal access to a specific part of a network. Unlike a demilitarized zone (DMZ) network, which allows inbound and outbound traffic access through firewall boundaries, enclaves do not cross firewall boundaries. 

The new enclave support functionality is for scenarios where mirroring is needed for multiple enclaves that are secured behind at least one intermediate disconnected network. 

Enclave support has the following benefits: 

  * You can mirror content for multiple enclaves and centralize it in a single internal registry. Because some customers want to run security checks on the mirrored content, with this setup they can run these checks all at once. The content is then vetted before being mirrored to downstream enclaves. 
  * You can mirror content directly from the centralized internal registry to enclaves without restarting the mirroring process from the internet for each enclave. 
  * You can minimize data transfer between network stages, so to ensure that a blob or image is transferred only once from one stage to another. 



## 5.9.1. Enclave mirroring workflow

![Enclave Support](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Disconnected_environments-en-US/images/8cc1807490d35edf67c1f15ef8f62d1e/445_OpenShift_Enclave_support_0724.png) ![Enclave Support](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Disconnected_environments-en-US/images/8cc1807490d35edf67c1f15ef8f62d1e/445_OpenShift_Enclave_support_0724.png)

The previous image outlines the flow for using the oc-mirror plugin in different environments, including environments with and without an internet connection. 

**Environment with Internet Connection** : 

  1. The user executes oc-mirror plugin v2 to mirror content from an online registry to a local disk directory. 
  2. The mirrored content is saved to the disk for transfer to offline environments. 



**Disconnected Enterprise Environment (No Internet)** : 

  * Flow 1: 

    * The user runs oc-mirror plugin v2 to load the mirrored content from the disk directory, which was transferred from the online environment, into the `enterprise-registry.in` registry. 

  * Flow 2: 

    1. After updating the `registries.conf` file, the user executes the oc-mirror plugin v2 to mirror content from the `enterprise-registry.in` registry to an enclave environment. 
    2. The content is saved to a disk directory for transfer to the enclave. 




**Enclave Environment (No Internet)** : 

  * The user runs oc-mirror plugin v2 to load content from the disk directory into the `enclave-registry.in` registry. 



The image visually represents the data flow across these environments and emphasizes the use of oc-mirror to handle disconnected and enclave environments without an internet connection. 

## 5.9.2. Mirroring to an enclave

When you mirror to an enclave, you must first transfer the necessary images from one or more enclaves into the enterprise central registry. 

The central registry is situated within a secure network, specifically a disconnected environment, and is not directly linked to the public internet. But the user must execute `oc mirror` in an environment with access to the public internet. 

**Procedure**

  1. Before running oc-mirror plugin v2 in the disconnected environment, create a `registries.conf` file. The TOML format of the file is described in this specification: 

Note

It is recommended to store the file under `$HOME/.config/containers/registries.conf` or `/etc/containers/registries.conf`. 

**Example`registries.conf`**

```plaintext
[[registry]]
location="registry.redhat.io"
[[registry.mirror]]
location="<enterprise-registry.in>"

[[registry]]
location="quay.io"
[[registry.mirror]]
location="<enterprise-registry.in>"
```


  2. Generate a mirror archive. 

     1. To collect all the OpenShift Container Platform content into an archive on the disk under `<file_path>/enterprise-content`, run the following command: 

```shell-session
$ oc mirror --v2 -c isc.yaml file://<file_path>/enterprise-content
```


**Example of isc.yaml**

```yaml
apiVersion: mirror.openshift.io/v2alpha1
kind: ImageSetConfiguration
mirror:
  platform:
    architectures:
      - "amd64"
    channels:
      - name: stable-4.15
        minVersion: 4.15.0
        maxVersion: 4.15.3
```


After the archive is generated, it is transferred to the disconnected environment. The transport mechanism is not part of oc-mirror plugin v2. The enterprise network administrators determine the transfer strategy. 

In some cases, the transfer is done manually, in that the disk is physically unplugged from one location, and plugged to another computer in the disconnected environment. In other cases, the Secure File Transfer Protocol (SFTP) or other protocols are used. 

  3. After the transfer of the archive is done, you can execute oc-mirror plugin v2 again in order to mirror the relevant archive contents to the registry (`entrerpise_registry.in` in the example) as demonstrated in the following example: 

```shell-session
$ oc mirror --v2 -c isc.yaml --from file://<disconnected_environment_file_path>/enterprise-content docker://<enterprise_registry.in>/
```


Where: 

     * `--from` points to the folder containing the archive. It starts with the `file://`. 
     * `docker://` is the destination of the mirroring is the final argument. Because it is a docker registry. 
     * `-c` (`--config`) is a mandatory argument. It enables oc-mirror plugin v2 to eventually mirror only sub-parts of the archive to the registry. One archive might contain several OpenShift Container Platform releases, but the disconnected environment or an enclave might mirror only a few. 

  4. Prepare the `imageSetConfig` YAML file, which describes the content to mirror to the enclave: 

**Example isc-enclave.yaml**

```yaml
apiVersion: mirror.openshift.io/v2alpha1
kind: ImageSetConfiguration
mirror:
  platform:
    architectures:
      - "amd64"
    channels:
      - name: stable-4.15
        minVersion: 4.15.2
        maxVersion: 4.15.2
```


You must run oc-mirror plugin v2 on a machine with access to the disconnected registry. In the previous example, the disconnected environment, `enterprise-registry.in`, is accessible. 

  5. Update the graph URL 

If you are using `graph:true`, oc-mirror plugin v2 attempts to reach the `cincinnati` API endpoint. Because this environment is disconnected, be sure to export the environment variable `UPDATE_URL_OVERRIDE` to refer to the URL for the OpenShift Update Service (OSUS): 

```shell-session
$ export UPDATE_URL_OVERRIDE=https://<osus.enterprise.in>/graph
```


For more information on setting up OSUS on an OpenShift cluster, see "Updating a cluster in a disconnected environment using the OpenShift Update Service". 

Note

When updating between OpenShift Container Platform Extended Update Support (EUS) versions, you must also include images for an intermediate minor version between the current and target versions. The oc-mirror plugin v2 might not always detect this requirement automatically, so check the [Red Hat OpenShift Container Platform Update Graph page](https://access.redhat.com/labs/ocpupgradegraph/update_path) to confirm any required intermediate versions. 

Use the Update Graph page to find the intermediate minor versions suggested by the application, and include any of these versions in the `ImageSetConfiguration` file when using the oc-mirror plugin v2. 

  6. Generate a mirror archive from the enterprise registry for the enclave. 

To prepare an archive for the `enclave1`, the user executes oc-mirror plugin v2 in the enterprise disconnected environment by using the `imageSetConfiguration` specific for that enclave. This ensures that only images needed by that enclave are mirrored: 

```shell-session
$ oc mirror --v2 -c isc-enclave.yaml
file:///disk-enc1/
```


This action collects all the OpenShift Container Platform content into an archive and generates an archive on disk. 

  7. After the archive is generated, it will be transferred to the `enclave1` network. The transport mechanism is not the responsibility of oc-mirror plugin v2. 
  8. Mirror contents to the enclave registry 

After the transfer of the archive is done, the user can execute oc-mirror plugin v2 again in order to mirror the relevant archive contents to the registry. 

```shell-session
$ oc mirror --v2 -c isc-enclave.yaml --from file://local-disk docker://registry.enc1.in
```


The administrators of the OpenShift Container Platform cluster in `enclave1` are now ready to install or upgrade that cluster.
