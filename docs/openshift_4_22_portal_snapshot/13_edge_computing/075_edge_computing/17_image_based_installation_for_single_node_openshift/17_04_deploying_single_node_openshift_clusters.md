# 17.4. Deploying single-node OpenShift clusters

## 17.4.1. About image-based deployments for managed single-node OpenShift

When a host preinstalled with single-node OpenShift using an image-based installation arrives at a remote site, a technician can easily reconfigure and deploy the host in a matter of minutes. 

For clusters with a hub-and-spoke architecture, to complete the deployment of a preinstalled host, you must first define site-specific configuration resources on the hub cluster for each host. These resources contain configuration information such as the properties of the bare-metal host, authentication details, and other deployment and networking information. 

The Image Based Install (IBI) Operator creates a configuration ISO from these resources, and then boots the host with the configuration ISO attached. The host mounts the configuration ISO and runs the reconfiguration process. When the reconfiguration completes, the single-node OpenShift cluster is ready. 

Note

You must create distinct configuration resources for each bare-metal host. 

See the following high-level steps to deploy a preinstalled host in a cluster with a hub-and-spoke architecture: 

  1. Install the IBI Operator on the hub cluster. 
  2. Create site-specific configuration resources in the hub cluster for each host. 
  3. The IBI Operator creates a configuration ISO from these resources and boots the target host with the configuration ISO attached. 
  4. The host mounts the configuration ISO and runs the reconfiguration process. When the reconfiguration completes, the single-node OpenShift cluster is ready. 



Note

Alternatively, you can manually deploy a preinstalled host for a cluster without using a hub cluster. You must define an `ImageBasedConfig` resource and an installation manifest, and provide these as inputs to the `openshift-install` installation program. For more information, see "Deploying a single-node OpenShift cluster using the `openshift-install` program". 

**Additional resources**

  * [Deploying a single-node OpenShift cluster using the `openshift-install` program](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/image-based-installation-for-single-node-openshift#create-standalone-config-iso_ibi-edge-image-based-install "17.4.2.1. Deploying a single-node OpenShift cluster using the openshift-install program")



### 17.4.1.1. Installing the Image Based Install Operator

The Image Based Install (IBI) Operator is part of the image-based deployment workflow for preinstalled single-node OpenShift on bare-metal hosts. 

Note

The IBI Operator is part of the multicluster engine for Kubernetes Operator from MCE version 2.7. 

**Prerequisites**

  * You logged in as a user with `cluster-admin` privileges. 
  * You deployed a Red Hat Advanced Cluster Management (RHACM) hub cluster or you deployed the multicluster engine for Kubernetes Operator. 
  * You reviewed the required versions of software components in the section "Software prerequisites for an image-based installation". 



**Procedure**

  * Set the `enabled` specification to `true` for the `image-based-install-operator` component in the `MultiClusterEngine` resource by running the following command: 

```shell-session
$ oc patch multiclusterengines.multicluster.openshift.io multiclusterengine --type json \
--patch '[{"op": "add", "path":"/spec/overrides/components/-", "value": {"name":"image-based-install-operator","enabled": true}}]'
```


**Verification**

  * Check that the Image Based Install Operator pod is running by running the following command: 

```shell-session
$ oc get pods -A | grep image-based
```


Example output: 

```shell-session
multicluster-engine             image-based-install-operator-57fb8sc423-bxdj8             2/2     Running     0               5m
```


### 17.4.1.2. Deploying a managed single-node OpenShift cluster using the IBI Operator

Create the site-specific configuration resources in the hub cluster to initiate the image-based deployment of a preinstalled host. 

When you create these configuration resources in the hub cluster, the Image Based Install (IBI) Operator generates a configuration ISO and attaches it to the target host to begin the site-specific configuration process. When the configuration process completes, the single-node OpenShift cluster is ready. 

Note

For more information about the configuration resources that you must configure in the hub cluster, see "Cluster configuration resources for deploying a preinstalled host". 

**Prerequisites**

  * You preinstalled a host with single-node OpenShift using an image-based installation. 
  * You logged in as a user with `cluster-admin` privileges. 
  * You deployed a Red Hat Advanced Cluster Management (RHACM) hub cluster or you deployed the multicluster engine for Kubernetes operator (MCE). 
  * You installed the IBI Operator on the hub cluster. 
  * You created a pull secret to authenticate pull requests. For more information, see "Using image pull secrets". 



**Procedure**

  1. Create the `ibi-ns` namespace by running the following command: 

```shell-session
$ oc create namespace ibi-ns
```


  2. Create the `Secret` resource for your image registry: 

     1. Create a YAML file that defines the `Secret` resource for your image registry: 

Example `secret-image-registry.yaml` file: 

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: ibi-image-pull-secret
  namespace: ibi-ns
stringData:
  .dockerconfigjson: <base64_docker_auth_code>
type: kubernetes.io/dockerconfigjson
```


where: 

`<base64_docker_auth_code>`
     Specifies base64-encoded credential details. See the "Additional resources" section for more information about using image pull secrets. 

     2. Create the `Secret` resource for your image registry by running the following command: 

```shell-session
$ oc create -f secret-image-registry.yaml
```


  3. Optional: Configure static networking for the host: 

     1. Create a `Secret` resource containing the static network configuration in `nmstate` format: 

Example `host-network-config-secret.yaml` file: 

```yaml
apiVersion: v1
kind: Secret
metadata:
 name: <network_secret_name>
 namespace: ibi-ns
type: Opaque
stringData:
 nmstate: |
  interfaces:
    - name: <interface_name>
      type: ethernet
      state: up
      ipv4:
        enabled: true
        address:
          - ip: 192.168.200.25
            prefix-length: 24
        dhcp: false
      ipv6:
        enabled: false
  dns-resolver:
    config:
      server:
        - <dns_server_1>
        - 192.168.15.48
  routes:
    config:
      - destination: 0.0.0.0/0
        metric: 150
        next-hop-address: 192.168.200.254
        next-hop-interface: <interface_name>
        table-id: 254
```


where: 

`<network_secret_name>`
     Specifies the name for the `Secret` resource, for example `host-network-config-secret`. 
`nmstate`
     Specifies the static network configuration in `nmstate` format. 
`<interface_name>`
     Specifies the name of the interface on the host, for example `ens1f0`. The name of the interface must match the actual NIC name as shown in the operating system. To use your MAC address for NIC matching, set the `identifier` field to `mac-address`. 
`dhcp: false`
     Specifies that DHCP is disabled to ensure `nmstate` assigns the static IP address to the interface. 
`<dns_server_1>`
     Specifies one or more DNS servers that the system will use to resolve domain names, for example `192.168.15.47`. 
`config`
     Specifies the default route through the `ens1f0` interface to the next hop IP address `192.168.200.254`. 

  4. Create the `BareMetalHost` and `Secret` resources: 

     1. Create a YAML file that defines the `BareMetalHost` and `Secret` resources: 

Example `ibi-bmh.yaml` file: 

```yaml
apiVersion: metal3.io/v1alpha1
kind: BareMetalHost
metadata:
  name: <baremetalhost_name>
  namespace: ibi-ns
spec:
  online: <online_status>
  bootMACAddress: <boot_mac_address>
  bmc:
    address: <bmc_address>
    credentialsName: <bmh_secret_name>
  preprovisioningNetworkDataName: <network_secret_name>
  automatedCleaningMode: disabled
  externallyProvisioned: true
---
apiVersion: v1
kind: Secret
metadata:
  name: <bmh_secret_name>
  namespace: ibi-ns
type: Opaque
data:
  username: <username>
  password: <password>
```


where: 

`<baremetalhost_name>`
     Specifies the name for the `BareMetalHost` resource, for example `ibi-bmh`. 
`<online_status>`
     Specifies if the host should be online, for example `false`. 
`<boot_mac_address>`
     Specifies the host boot MAC address, for example `00:a5:12:55:62:64`. 
`<bmc_address>`
     Specifies the BMC address, for example `redfish-virtualmedia+http://192.168.111.1:8000/redfish/v1/Systems/8a5babac-94d0-4c20-b282-50dc3a0a32b5`. You can only use bare-metal host drivers that support virtual media networking booting, for example redfish-virtualmedia and idrac-virtualmedia. 
`<bmh_secret_name>`
     Specifies the name of the bare-metal host `Secret` resource, for example `ibi-bmh-bmc-secret`. 
`<network_secret_name>`
     (Optional) Specifies the name of the `Secret` resource containing the static network configuration for the host, for example `host-network-config-secret`. 
`automatedCleaningMode: disabled`
     Specifies that automated cleaning is disabled to prevent the provisioning service from deleting all preinstallation artifacts, such as the seed image, during disk inspection. 
`externallyProvisioned: true`
     Specifies that the host is externally provisioned to enable it to boot from the preinstalled disk, instead of the configuration ISO. 
`<username>`
     Specifies the username for BMC authentication. 
`<password>`
     Specifies the password for BMC authentication. 

     2. Create the `BareMetalHost` and `Secret` resources by running the following command: 

```shell-session
$ oc create -f ibi-bmh.yaml
```


  5. Create the `ClusterImageSet` resource: 

     1. Create a YAML file that defines the `ClusterImageSet` resource: 

Example `ibi-cluster-image-set.yaml` file: 

```yaml
apiVersion: hive.openshift.io/v1
kind: ClusterImageSet
metadata:
  name: <clusterimageset_name>
spec:
  releaseImage: <release_image>
```


where: 

`<clusterimageset_name>`
     Specifies the name for the `ClusterImageSet` resource, for example `ibi-img-version-arch`. 
`<release_image>`
     Specifies the address for the release image to use for the deployment, for example `ibi.example.com:path/to/release/images:version-arch`. If you use a different image registry compared to the image registry used during seed image generation, ensure that the OpenShift Container Platform version for the release image remains the same. 

     2. Create the `ClusterImageSet` resource by running the following command: 

```shell-session
$ oc apply -f ibi-cluster-image-set.yaml
```


  6. Create the `ImageClusterInstall` resource: 

     1. Create a YAML file that defines the `ImageClusterInstall` resource: 

Example `ibi-image-cluster-install.yaml` file: 

```yaml
apiVersion: extensions.hive.openshift.io/v1alpha1
kind: ImageClusterInstall
metadata:
  name: <imageclusterinstall_name>
  namespace: ibi-ns
spec:
  bareMetalHostRef:
    name: <baremetalhost_name>
    namespace: ibi-ns
  clusterDeploymentRef:
    name: <clusterdeployment_name>
  hostname: <cluster_hostname>
  imageSetRef:
    name: <clusterimageset_name>
  machineNetworks:
  - cidr: 10.0.0.0/24
  #- cidr: fd01::/64
  proxy:
    httpProxy: "http://proxy.example.com:8080"
    #httpsProxy: "http://proxy.example.com:8080"
    #noProxy: "no_proxy.example.com"
```


where: 

`<imageclusterinstall_name>`
     Specifies the name for the `ImageClusterInstall` resource, for example `ibi-image-install`. 
`<baremetalhost_name>`
     Specifies the `BareMetalHost` resource that you want to target for the image-based installation, for example `ibi-bmh`. 
`<clusterdeployment_name>`
     Specifies the name of the `ClusterDeployment` resource that you want to use for the image-based installation of the target host, for example `ibi-cluster-deployment`. 
`<cluster_hostname>`
     Specifies the hostname for the cluster, for example `ibi-host`. 
`<clusterimageset_name>`
     Specifies the name of the `ClusterImageSet` resource you used to define the container release images to use for deployment, for example `ibi-img-version-arch`. 
`machineNetworks`
     Specifies the public Classless Inter-Domain Routing (CIDR) of the external network. For dual-stack networking, you can specify both IPv4 and IPv6 CIDRs using a list format. The first CIDR in the list is the primary address family and must match the primary address family of the seed cluster. 
`proxy`
    

(Optional) Specifies a proxy to use for the cluster deployment. 

Important

If your cluster deployment requires a proxy configuration, you must do the following: 

        * Create a seed image from a seed cluster featuring a proxy configuration. The proxy configurations do not have to match. 
        * Configure the `machineNetwork` field in your installation manifest. 

     2. Create the `ImageClusterInstall` resource by running the following command: 

```shell-session
$ oc create -f ibi-image-cluster-install.yaml
```


  7. Create the `ClusterDeployment` resource: 

     1. Create a YAML file that defines the `ClusterDeployment` resource: 

Example `ibi-cluster-deployment.yaml` file: 

```yaml
apiVersion: hive.openshift.io/v1
kind: ClusterDeployment
metadata:
  name: <clusterdeployment_name>
  namespace: <namespace>
spec:
  baseDomain: <base_domain>
  clusterInstallRef:
    group: extensions.hive.openshift.io
    kind: ImageClusterInstall
    name: <imageclusterinstall_name>
    version: v1alpha1
  clusterName: <cluster_name>
  platform:
    none: {}
  pullSecretRef:
    name: <pull_secret_name>
```


where: 

`<clusterdeployment_name>`
     Specifies the name for the `ClusterDeployment` resource, for example `ibi-cluster-deployment`. 
`<namespace>`
     Specifies the namespace for the `ClusterDeployment` resource, for example `ibi-ns`. 
`<base_domain>`
     Specifies the base domain that the cluster should belong to, for example `example.com`. 
`<imageclusterinstall_name>`
     Specifies the name of the `ImageClusterInstall` in which you defined the container images to use for the image-based installation of the target host, for example `ibi-image-install`. 
`<cluster_name>`
     Specifies a name for the cluster, for example `ibi-cluster`. 
`<pull_secret_name>`
     Specifies the secret to use for pulling images from your image registry, for example `ibi-image-pull-secret`. 

     2. Create the `ClusterDeployment` resource by running the following command: 

```shell-session
$ oc apply -f ibi-cluster-deployment.yaml
```


  8. Create the `ManagedCluster` resource: 

     1. Create a YAML file that defines the `ManagedCluster` resource: 

Example `ibi-managed.yaml` file: 

```yaml
apiVersion: cluster.open-cluster-management.io/v1
kind: ManagedCluster
metadata:
  name: <managedcluster_name>
spec:
  hubAcceptsClient: <hub_accepts_client>
```


where: 

`<managedcluster_name>`
     Specifies the name for the `ManagedCluster` resource, for example `sno-ibi`. 
`<hub_accepts_client>`
     Specifies whether RHACM manages the cluster. Set to `true` to enable management. 

     2. Create the `ManagedCluster` resource by running the following command: 

```shell-session
$ oc apply -f ibi-managed.yaml
```


**Verification**

  1. Check the status of the `ImageClusterInstall` in the hub cluster to monitor the progress of the target host installation by running the following command: 

```shell-session
$ oc get imageclusterinstall
```


Example output: 

```shell-session
NAME       REQUIREMENTSMET           COMPLETED                     BAREMETALHOSTREF
target-0   HostValidationSucceeded   ClusterInstallationSucceeded  ibi-bmh
```


Warning

If the `ImageClusterInstall` resource is deleted, the IBI Operator reattaches the `BareMetalHost` resource and reboots the machine. 

  2. When the installation completes, you can retrieve the `kubeconfig` secret to log in to the managed cluster by running the following command: 

```shell-session
$ oc extract secret/<cluster_name>-admin-kubeconfig -n <cluster_namespace>  --to - > <directory>/<cluster_name>-kubeconfig
```


where: 

`<cluster_name>`
     Specifies the name of the cluster. 
`<cluster_namespace>`
     Specifies the namespace of the cluster. 
`<directory>`
     Specifies the directory in which to create the file. 




**Additional resources**

  * [Using image pull secrets](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/images/#using-image-pull-secrets-1)
  * [Cluster configuration resources for deploying a preinstalled host](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/image-based-installation-for-single-node-openshift#ibi-managed-cluster-config-resources_ibi-edge-image-based-install "17.4.1.2.1. Cluster configuration resources for deploying a preinstalled host")



#### 17.4.1.2.1. Cluster configuration resources for deploying a preinstalled host

To complete a deployment for a preinstalled host at a remote site, you must configure the following site-specifc cluster configuration resources in the hub cluster for each bare-metal host. 

Table 17.6. Cluster configuration resources referenceResource| Description  
---|---  
`Namespace` |  Namespace for the managed single-node OpenShift cluster.   
`BareMetalHost` |  Describes the physical host and its properties, such as the provisioning and hardware configuration.   
`Secret` for the bare-metal host  |  Credentials for the host BMC.   
`Secret` for the bare-metal host static network configuration  |  Optional: Describes static network configuration for the target host.   
`Secret` for the image registry  |  Credentials for the image registry. The secret for the image registry must be of type `kubernetes.io/dockerconfigjson`.   
`ImageClusterInstall` |  References the bare-metal host, deployment, and image set resources.   
`ClusterImageSet` |  Describes the release images to use for the cluster.   
`ClusterDeployment` |  Describes networking, authentication, and platform-specific settings.   
`ManagedCluster` |  Describes cluster details to enable Red Hat Advanced Cluster Management (RHACM) to register and manage.   
`ConfigMap` |  Optional: Describes additional configurations for the cluster deployment, such as adding a bundle of trusted certificates for the host to ensure trusted communications for cluster services.   
Show more

#### 17.4.1.2.2. ImageClusterInstall resource API specifications

The following content describes the API specifications for the `ImageClusterInstall` resource. This resource is the endpoint for the Image Based Install Operator. 

Table 17.7. Required specificationsSpecification| Type| Description  
---|---|---  
`imageSetRef` |  `string` |  Specify the name of the `ClusterImageSet` resource that defines the release images for the deployment.   
`hostname` |  `string` |  Specify the hostname for the cluster.   
`sshKey` |  `string` |  Specify your SSH key to provide SSH access to the target host.   
Show more

Table 17.8. Optional specificationsSpecification| Type| Description  
---|---|---  
`clusterDeploymentRef` |  `string` |  Specify the name of the `ClusterDeployment` resource that you want to use for the image-based installation of the target host.   
`clusterMetadata` |  `string` |  After the deployment completes, this specification is automatically populated with metadata information about the cluster, including the `cluster-admin` kubeconfig credentials for logging in to the cluster.   
`imageDigestSources` |  `string` |  Specifies the sources or repositories for the release-image content, for example:  `imageDigestSources: - mirrors: - "registry.example.com:5000/ocp4/openshift4" source: "quay.io/openshift-release-dev/ocp-release"`  
`extraManifestsRefs` |  `string` |  Specify a `ConfigMap` resource containing additional manifests to be applied to the target cluster.   
`bareMetalHostRef` |  `string` |  Specify the `bareMetalHost` resource to use for the cluster deployment   
`machineNetworks` |  `string` |  Specify the public Classless Inter-Domain Routing (CIDR) of the external network. For dual-stack networking, you can specify both IPv4 and IPv6 CIDRs using a list format. The first CIDR in the list is the primary address family and must match the primary address family of the seed cluster.   
`proxy` |  `string` |  Specifies proxy settings for the cluster, for example:  `proxy: httpProxy: "http://proxy.example.com:8080" httpsProxy: "http://proxy.example.com:8080" noProxy: "no_proxy.example.com"`  
`caBundleRef` |  `string` |  Specify a `ConfigMap` resource containing the new bundle of trusted certificates for the host.   
Show more

### 17.4.1.3. ConfigMap resources for extra manifests

You can optionally create a `ConfigMap` resource to define additional manifests in an image-based deployment for managed single-node OpenShift clusters. 

After you create the `ConfigMap` resource, reference it in the `ImageClusterInstall` resource. During deployment, the IBI Operator includes the extra manifests in the deployment. 

#### 17.4.1.3.1. Creating a ConfigMap resource to add extra manifests in an image-based deployment

You can use a `ConfigMap` resource to add extra manifests to the image-based deployment for single-node OpenShift clusters. 

The following example adds an single-root I/O virtualization (SR-IOV) network to the deployment. 

Note

Filenames for extra manifests must not exceed 30 characters. Longer filenames might cause deployment failures. 

Before you begin, ensure that: 

  * You preinstalled a host with single-node OpenShift using an image-based installation. 
  * You logged in as a user with `cluster-admin` privileges. 



To create the `ConfigMap` resource, complete the following steps: 

  1. Create the `SriovNetworkNodePolicy` and `SriovNetwork` resources: 

     1. Create a YAML file that defines the resources, as in the following example: 

```yaml
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetworkNodePolicy
metadata:
  name: "example-sriov-node-policy"
  namespace: openshift-sriov-network-operator
spec:
  deviceType: vfio-pci
  isRdma: false
  nicSelector:
    pfNames: [ens1f0]
  nodeSelector:
    node-role.kubernetes.io/master: ""
  mtu: 1500
  numVfs: 8
  priority: 99
  resourceName: example-sriov-node-policy
---
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetwork
metadata:
  name: "example-sriov-network"
  namespace: openshift-sriov-network-operator
spec:
  ipam: |-
    {
    }
  linkState: auto
  networkNamespace: sriov-namespace
  resourceName: example-sriov-node-policy
  spoofChk: "on"
  trust: "off"
```


     2. Create the `ConfigMap` resource by running the following command: 

```shell-session
$ oc create configmap sr-iov-extra-manifest --from-file=sriov-extra-manifest.yaml -n <namespace>
```


where: 

`<namespace>`
    

Specifies the namespace that has the `ImageClusterInstall` resource, for example `ibi-ns`. 

Example output: 

```shell-session
configmap/sr-iov-extra-manifest created
```


Note

If you add more than one extra manifest, and the manifests must be applied in a specific order, you must prefix the filenames of the manifests with numbers that represent the required order. For example, `00-namespace.yaml`, `01-sriov-extra-manifest.yaml`, and so on. 

  2. Reference the `ConfigMap` resource in the `spec.extraManifestsRefs` field of the `ImageClusterInstall` resource: 

```yaml
#...
  spec:
    extraManifestsRefs:
    - name: sr-iov-extra-manifest
#...
```


#### 17.4.1.3.2. Creating a ConfigMap resource to add a CA bundle in an image-based deployment

You can use a `ConfigMap` resource to add a certificate authority (CA) bundle to the host to ensure trusted communications for cluster services. 

After you create the `ConfigMap` resource, reference it in the `spec.caBundleRef` field of the `ImageClusterInstall` resource. 

Before you begin, ensure that: 

  * You preinstalled a host with single-node OpenShift using an image-based installation. 
  * You logged in as a user with `cluster-admin` privileges. 



To create the CA bundle `ConfigMap` resource, complete the following steps: 

  1. Create a CA bundle file called `tls-ca-bundle.pem`, as in the following example: 

```plaintext
-----BEGIN CERTIFICATE-----
MIIDXTCCAkWgAwIBAgIJAKmjYKJbIyz3MA0GCSqGSIb3DQEBCwUAMEUxCzAJBgNV
...Custom CA certificate bundle...
4WPl0Qb27Sb1xZyAsy1ww6MYb98EovazUSfjYr2EVF6ThcAPu4/sMxUV7He2J6Jd
cA8SMRwpUbz3LXY=
-----END CERTIFICATE-----
```


  2. Create the `ConfigMap` object by running the following command: 

```shell-session
$ oc create configmap custom-ca --from-file=tls-ca-bundle.pem -n ibi-ns
```


where: 

`custom-ca`
     Specifies the name for the `ConfigMap` resource. 
`tls-ca-bundle.pem`
     Specifies the key for the `data` entry in the `ConfigMap` resource. You must include a `data` entry with the `tls-ca-bundle.pem` key. 
`ibi-ns`
    

Specifies the namespace that has the `ImageClusterInstall` resource. 

Example output: 

```shell-session
configmap/custom-ca created
```


  3. Reference the `ConfigMap` resource in the `spec.caBundleRef` field of the `ImageClusterInstall` resource: 

```yaml
#...
  spec:
    caBundleRef:
      name: custom-ca
#...
```


**Additional resources**

  * [About the BareMetalHost resource](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_bare_metal/#bmo-about-the-baremetalhost-resource_bare-metal-postinstallation-configuration)
  * [Using image pull secrets](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/images/#using-image-pull-secrets-1)
  * [Reference specifications for the image-based-config.yaml manifest](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/image-based-installation-for-single-node-openshift#ibi-installer-installation-config_ibi-factory-image-based-install "17.3.3. Reference specifications for the image-based-installation-config.yaml manifest")



## 17.4.2. About image-based deployments for single-node OpenShift

You can manually generate a configuration ISO by using the `openshift-install` program. Attach the configuration ISO to your preinstalled target host to complete the deployment. 

### 17.4.2.1. Deploying a single-node OpenShift cluster using the openshift-install program

You can use the `openshift-install` program to configure and deploy a host that you preinstalled with an image-based installation. To configure the target host with site-specific details, you must create the following resources: 

  * The `install-config.yaml` installation manifest 
  * The `image-based-config.yaml` manifest 



The `openshift-install` program uses these resources to generate a configuration ISO that you attach to the preinstalled target host to complete the deployment. 

Note

For more information about the specifications for the `image-based-config.yaml` manifest, see "Reference specifications for the image-based-config.yaml manifest". 

**Prerequisites**

  * You preinstalled a host with single-node OpenShift using an image-based installation. 
  * You downloaded the latest version of the `openshift-install` program. 
  * You created a pull secret to authenticate pull requests. For more information, see "Using image pull secrets". 



**Procedure**

  1. Create a working directory by running the following: 

```shell-session
$ mkdir <working_directory>
```


where `<working_directory>` is the name of your working directory, for example `ibi-config-iso-workdir`. 

  2. Create the installation manifest: 

     1. Create a YAML file that defines the `install-config` manifest, as in the following example: 

```yaml
apiVersion: v1
metadata:
  name: sno-cluster-name
baseDomain: host.example.com
compute:
  - architecture: amd64
    hyperthreading: Enabled
    name: worker
    replicas: 0
controlPlane:
  architecture: amd64
  hyperthreading: Enabled
  name: master
  replicas: 1
networking:
  machineNetwork:
  - cidr: 192.168.200.0/24
  #- cidr: fd01::/64
platform:
  none: {}
fips: false
cpuPartitioningMode: "AllNodes"
pullSecret: '{"auths":{"<your_pull_secret>"}}}'
sshKey: 'ssh-rsa <your_ssh_pub_key>'
```


\+ For dual-stack networking, you can specify both IPv4 and IPv6 CIDRs using a list format in the `machineNetwork` field. The first CIDR in the list is the primary address family and must match the primary address family of the seed cluster. 

Important

If your cluster deployment requires a proxy configuration, you must do the following: 

        * Create a seed image from a seed cluster featuring a proxy configuration. The proxy configurations do not have to match. 
        * Configure the `machineNetwork` field in your installation manifest. 

     2. Save the file in your working directory. 

  3. Optional. Create a configuration template in your working directory by running the following command: 

```shell-session
$ openshift-install image-based create config-template --dir ibi-config-iso-workdir/
```


Example output: 

```shell-session
INFO Config-Template created in: ibi-config-iso-workdir
```


The command creates the `image-based-config.yaml` configuration template in your working directory: 

```yaml
#
# Note: This is a sample ImageBasedConfig file showing
# which fields are available to aid you in creating your
# own image-based-config.yaml file.
#
apiVersion: v1beta1
kind: ImageBasedConfig
metadata:
  name: example-image-based-config
additionalNTPSources:
  - 0.rhel.pool.ntp.org
  - 1.rhel.pool.ntp.org
hostname: change-to-hostname
releaseRegistry: quay.io
# networkConfig contains the network configuration for the host in NMState format.
# See https://nmstate.io/examples.html for examples.
networkConfig:
  interfaces:
    - name: eth0
      type: ethernet
      state: up
      mac-address: 00:00:00:00:00:00
      ipv4:
        enabled: true
        address:
          - ip: 192.168.122.2
            prefix-length: 23
        dhcp: false
```


  4. Edit your configuration file: 

Example `image-based-config.yaml` file: 

```yaml
#
# Note: This is a sample ImageBasedConfig file showing
# which fields are available to aid you in creating your
# own image-based-config.yaml file.
#
apiVersion: v1beta1
kind: ImageBasedConfig
metadata:
  name: sno-cluster-name
additionalNTPSources:
  - 0.rhel.pool.ntp.org
  - 1.rhel.pool.ntp.org
hostname: host.example.com
releaseRegistry: quay.io
# networkConfig contains the network configuration for the host in NMState format.
# See https://nmstate.io/examples.html for examples.
networkConfig:
    interfaces:
      - name: ens1f0
        type: ethernet
        state: up
        ipv4:
          enabled: true
          dhcp: false
          auto-dns: false
          address:
            - ip: 192.168.200.25
              prefix-length: 24
        ipv6:
          enabled: false
    dns-resolver:
      config:
        server:
          - 192.168.15.47
          - 192.168.15.48
    routes:
      config:
      - destination: 0.0.0.0/0
        metric: 150
        next-hop-address: 192.168.200.254
        next-hop-interface: ens1f0
```


  5. Create the configuration ISO in your working directory by running the following command: 

```shell-session
$ openshift-install image-based create config-image --dir ibi-config-iso-workdir/
```


Example output: 

```shell-session
INFO Adding NMConnection file <ens1f0.nmconnection>
INFO Consuming Install Config from target directory
INFO Consuming Image-based Config ISO configuration from target directory
INFO Config-Image created in: ibi-config-iso-workdir/auth
```


View the output in the working directory: 

Example output: 

```shell-session
ibi-config-iso-workdir/
├── auth
│   ├── kubeadmin-password
│   └── kubeconfig
└── imagebasedconfig.iso
```


  6. Attach the `imagebasedconfig.iso` to the preinstalled host using your preferred method and restart the host to complete the configuration process and deploy the cluster. 



**Verification**

When the configuration process completes on the host, access the cluster to verify its status. 

  1. Export the `kubeconfig` environment variable to your kubeconfig file by running the following command: 

```shell-session
$ export KUBECONFIG=ibi-config-iso-workdir/auth/kubeconfig
```


  2. Verify that the cluster is responding by running the following command: 

```shell-session
$ oc get nodes
```


Example output: 

```shell-session
NAME                                         STATUS   ROLES                  AGE     VERSION
node/sno-cluster-name.host.example.com       Ready    control-plane,master   5h15m   v1.35.4
```


**Additional resources**

  * [Using image pull secrets](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/images/#using-image-pull-secrets-1)
  * [Reference specifications for the `image-based-installation-config.yaml` manifest](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/image-based-installation-for-single-node-openshift#ibi-installer-configuration-config_ibi-edge-image-based-install "17.4.2.1.1. Reference specifications for the image-based-config.yaml manifest")



#### 17.4.2.1.1. Reference specifications for the image-based-config.yaml manifest

The following content describes the specifications for the `image-based-config.yaml` manifest. 

The `openshift-install` program uses the `image-based-config.yaml` manifest to create a site-specific configuration ISO for image-based deployments of single-node OpenShift. 

Table 17.9. Required specificationsSpecification| Type| Description  
---|---|---  
`hostname` |  `string` |  Define the name of the node for the single-node OpenShift cluster.   
Show more

Table 17.10. Optional specificationsSpecification| Type| Description  
---|---|---  
`networkConfig` |  `string` |  Specifies networking configurations for the host, for example:  `networkConfig: interfaces: - name: ens1f0 type: ethernet state: up ...` If you require static networking, you must install the `nmstatectl` library on the host that creates the live installation ISO. For further information about defining network configurations by using `nmstate`, see [nmstate.io](https://nmstate.io/).  Important The name of the interface must match the actual NIC name as shown in the operating system.   
`additionalNTPSources` |  `string` |  Specifies a list of NTP sources for all cluster hosts. These NTP sources are added to any existing NTP sources in the cluster. You can use the hostname or IP address for the NTP source.   
`releaseRegistry` |  `string` |  Specifies the container image registry that you used for the release image of the seed cluster.   
`nodeLabels` |  `map[string]string` |  Specifies custom node labels for the single-node OpenShift node, for example:  `nodeLabels: node-role.kubernetes.io/edge: true environment: production`  
Show more

### 17.4.2.2. Configuring resources for extra manifests

You can optionally define additional resources in an image-based deployment for single-node OpenShift clusters. 

Create the additional resources in an `extra-manifests` folder in the same working directory that has the `install-config.yaml` and `image-based-config.yaml` manifests. 

Note

Filenames for additional resources in the `extra-manifests` directory must not exceed 30 characters. Longer filenames might cause deployment failures. 

The following example shows how to create a resource in the `extra-manifests` folder of your working directory to add an single-root I/O virtualization (SR-IOV) network to the deployment. 

Note

If you add more than one extra manifest, and the manifests must be applied in a specific order, you must prefix the filenames of the manifests with numbers that represent the required order. For example, `00-namespace.yaml`, `01-sriov-extra-manifest.yaml`, and so on. 

**Prerequisites**

  * You created a working directory with the `install-config.yaml` and `image-based-config.yaml` manifests 



**Procedure**

  1. Go to your working directory and create the `extra-manifests` folder by running the following command: 

```shell-session
$ mkdir extra-manifests
```


  2. Create the `SriovNetworkNodePolicy` and `SriovNetwork` resources in the `extra-manifests` folder: 

     1. Create a YAML file that defines the resources, as shown in the following example: 

Note

If the cluster nodes include Intel vRAN Boost (VRB1 or VRB2) hardware, you can include a `SriovVrbClusterConfig` resource in the extra manifests to configure the hardware. 

```yaml
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetworkNodePolicy
metadata:
  name: "example-sriov-node-policy"
  namespace: openshift-sriov-network-operator
spec:
  deviceType: vfio-pci
  isRdma: false
  nicSelector:
    pfNames: [ens1f0]
  nodeSelector:
    node-role.kubernetes.io/master: ""
  mtu: 1500
  numVfs: 8
  priority: 99
  resourceName: example-sriov-node-policy
---
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetwork
metadata:
  name: "example-sriov-network"
  namespace: openshift-sriov-network-operator
spec:
  ipam: |-
    {
    }
  linkState: auto
  networkNamespace: sriov-namespace
  resourceName: example-sriov-node-policy
  spoofChk: "on"
  trust: "off"
---
apiVersion: sriovvrb.intel.com/v1
kind: SriovVrbClusterConfig
metadata:
  name: config
  namespace: vran-acceleration-operators
spec:
  priority: 1
  nodeSelector:
    kubernetes.io/hostname: worker-node
  acceleratorSelector:
    pciAddress: 0000:07:00.0
  drainSkip: true
  physicalFunction:
    pfDriver: vfio-pci
    vfDriver: vfio-pci
    vfAmount: 2
    bbDevConfig:
      vrb2:
        pfMode: false
        numVfBundles: 2
        maxQueueSize: 1024
        downlink4G:
          aqDepthLog2: 4
          numAqsPerGroups: 16
          numQueueGroups: 0
        uplink4G:
          aqDepthLog2: 4
          numAqsPerGroups: 16
          numQueueGroups: 0
        downlink5G:
          aqDepthLog2: 4
          numAqsPerGroups: 16
          numQueueGroups: 4
        uplink5G:
          aqDepthLog2: 4
          numAqsPerGroups: 16
          numQueueGroups: 4
        qfft:
          aqDepthLog2: 4
          numAqsPerGroups: 16
          numQueueGroups: 4
        qmld:
          aqDepthLog2: 4
          numAqsPerGroups: 64
          numQueueGroups: 4
```


**Verification**

  * When you create the configuration ISO, you can view the reference to the extra manifests in the `.openshift_install_state.json` file in your working directory: 

```plaintext
 "*configimage.ExtraManifests": {
        "FileList": [
            {
                "Filename": "extra-manifests/sriov-extra-manifest.yaml",
                "Data": "YXBFDFFD..."
            }
        ]
    }
```
