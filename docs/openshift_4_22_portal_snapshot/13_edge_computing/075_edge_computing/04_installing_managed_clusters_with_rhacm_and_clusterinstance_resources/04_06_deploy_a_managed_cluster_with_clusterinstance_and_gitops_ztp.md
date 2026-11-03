# 4.6. Deploy a managed cluster with ClusterInstance and GitOps ZTP

Use the following procedure to create a `ClusterInstance` custom resource (CR) and related files and initiate the GitOps Zero Touch Provisioning (ZTP) cluster deployment. 

Note

You require Red Hat Advanced Cluster Management (RHACM) version 2.12 or later to install the SiteConfig Operator and use the `ClusterInstance` CR. 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 
  * You installed the SiteConfig Operator in the hub cluster. 
  * You have logged in to the hub cluster as a user with `cluster-admin` privileges. 
  * You configured the hub cluster for generating the required installation and policy CRs. 
  * You created a Git repository where you manage your custom site configuration data. The repository must be accessible from the hub cluster and you must configure it as a source repository for the ArgoCD application. See "Preparing the GitOps ZTP site configuration repository" for more information. 

Note

When you create the source repository, ensure that you patch the ArgoCD application with the `argocd/deployment/argocd-openshift-gitops-patch.json` patch-file that you extract from the `ztp-site-generate` container. See "Configuring the hub cluster with ArgoCD". 

  * To be ready for provisioning managed clusters, you require the following for each bare-metal host: 

Network connectivity
     Your network requires DNS. Managed cluster hosts should be reachable from the hub cluster. Ensure that Layer 3 connectivity exists between the hub cluster and the managed cluster host. 
Baseboard Management Controller (BMC) details
     GitOps ZTP uses BMC username and password details to connect to the BMC during cluster installation. The GitOps ZTP plugin manages the `ManagedCluster` CRs on the hub cluster based on the `ClusterInstance` CR in your site Git repo. You create individual `BMCSecret` CRs for each host manually. 




**Procedure**

  1. Create the required managed cluster secrets on the hub cluster. These resources must be in a namespace with a name matching the cluster name. For example, in `out/argocd/example/clusterinstance/example-sno.yaml`, the cluster name and namespace is `example-sno`. 

     1. Export the cluster namespace by running the following command: 

```shell-session
$ export CLUSTERNS=example-sno
```


     2. Create the namespace: 

```shell-session
$ oc create namespace $CLUSTERNS
```


  2. Create pull secret and BMC `Secret` CRs for the managed cluster. The pull secret must contain all the credentials necessary for installing OpenShift Container Platform and all required Operators. See "Creating the managed bare-metal host secrets" for more information. 

Note

The secrets are referenced from the `ClusterInstance` custom resource (CR) by name. The namespace must match the `ClusterInstance` namespace. 

  3. Create a `ClusterInstance` CR for your cluster in your local clone of the Git repository: 

     1. Choose the appropriate example for your CR from the `out/argocd/example/clusterinstance/` folder. The folder includes example files for single node, three-node, and standard clusters: 

        * `example-sno.yaml`
        * `example-3node.yaml`
        * `example-standard.yaml`

     2. Change the cluster and host details in the example file to match the type of cluster you want. For example: 

**Example single-node OpenShift ClusterInstance CR**

```yaml
apiVersion: siteconfig.open-cluster-management.io/v1alpha1
kind: ClusterInstance
metadata:
  name: "example-ai-sno"
  namespace: "example-ai-sno"
spec:
  baseDomain: "example.com"
  pullSecretRef:
    name: "assisted-deployment-pull-secret"
  clusterImageSetNameRef: "openshift-4.22"
  sshPublicKey: "ssh-rsa AAAA..."
  clusterName: "example-ai-sno"
  networkType: "OVNKubernetes"
  # installConfigOverrides is a generic way of passing install-config
  # parameters through the siteConfig.  The 'capabilities' field configures
  # the composable openshift feature.  In this 'capabilities' setting, we
  # remove all the optional set of components.
  # Notes:
  # - OperatorLifecycleManager is needed for 4.15 and later
  # - NodeTuning is needed for 4.13 and later, not for 4.12 and earlier
  # - Ingress is needed for 4.16 and later
  installConfigOverrides: |
    {
      "capabilities": {
        "baselineCapabilitySet": "None",
        "additionalEnabledCapabilities": [
          "NodeTuning",
          "OperatorLifecycleManager",
          "Ingress"
        ]
      }
    }
  # Include references to extraManifest ConfigMaps.
  extraManifestsRefs:
    - name: sno-extra-manifest-configmap
  extraLabels:
    ManagedCluster:
      # These example cluster labels correspond to the bindingRules in the PolicyGenTemplate examples
      du-profile: "latest"
      # These example cluster labels correspond to the bindingRules in the PolicyGenTemplate examples in ../policygentemplates:
      # ../policygentemplates/common-ranGen.yaml will apply to all clusters with 'common: true'
      common: "true"
      # ../policygentemplates/group-du-sno-ranGen.yaml will apply to all clusters with 'group-du-sno: ""'
      group-du-sno: ""
      # ../policygentemplates/example-sno-site.yaml will apply to all clusters with 'sites: "example-sno"'
      # Normally this should match or contain the cluster name so it only applies to a single cluster
      sites : "example-sno"
  clusterNetwork:
    - cidr: 1001:1::/48
      hostPrefix: 64
  machineNetwork:
    - cidr: 1111:2222:3333:4444::/64
  serviceNetwork:
    - cidr: 1001:2::/112
  additionalNTPSources:
    - 1111:2222:3333:4444::2
  # Initiates the cluster for workload partitioning. Setting specific reserved/isolated CPUSets is done via PolicyTemplate
  # please see Workload Partitioning Feature for a complete guide.
  cpuPartitioningMode: AllNodes
  templateRefs:
    - name: ai-cluster-templates-v1
      namespace: open-cluster-management
  nodes:
    - hostName: "example-node1.example.com"
      role: "master"
      bmcAddress: "idrac-virtualmedia+https://[1111:2222:3333:4444::bbbb:1]/redfish/v1/Systems/System.Embedded.1"
      bmcCredentialsName:
        name: "example-node1-bmh-secret"
      bootMACAddress: "AA:BB:CC:DD:EE:11"
      # Use UEFISecureBoot to enable secure boot, UEFI to disable.
      bootMode: "UEFISecureBoot"
      rootDeviceHints:
        deviceName: "/dev/disk/by-path/pci-0000:01:00.0-scsi-0:2:0:0"
      # disk partition at `/var/lib/containers` with ignitionConfigOverride. Some values must be updated. See DiskPartitionContainer.md in argocd folder for more details
      ignitionConfigOverride: |
        {
          "ignition": {
            "version": "3.2.0"
          },
          "storage": {
            "disks": [
              {
                "device": "/dev/disk/by-path/pci-0000:01:00.0-scsi-0:2:0:0",
                "partitions": [
                  {
                    "label": "var-lib-containers",
                    "sizeMiB": 0,
                    "startMiB": 250000
                  }
                ],
                "wipeTable": false
              }
            ],
            "filesystems": [
              {
                "device": "/dev/disk/by-partlabel/var-lib-containers",
                "format": "xfs",
                "mountOptions": [
                  "defaults",
                  "prjquota"
                ],
                "path": "/var/lib/containers",
                "wipeFilesystem": true
              }
            ]
          },
          "systemd": {
            "units": [
              {
                "contents": "# Generated by Butane\n[Unit]\nRequires=systemd-fsck@dev-disk-by\\x2dpartlabel-var\\x2dlib\\x2dcontainers.service\nAfter=systemd-fsck@dev-disk-by\\x2dpartlabel-var\\x2dlib\\x2dcontainers.service\n\n[Mount]\nWhere=/var/lib/containers\nWhat=/dev/disk/by-partlabel/var-lib-containers\nType=xfs\nOptions=defaults,prjquota\n\n[Install]\nRequiredBy=local-fs.target",
                "enabled": true,
                "name": "var-lib-containers.mount"
              }
            ]
          }
        }
      nodeNetwork:
        interfaces:
          - name: eno1
            macAddress: "AA:BB:CC:DD:EE:11"
        config:
          interfaces:
            - name: eno1
              type: ethernet
              state: up
              ipv4:
                enabled: false
              ipv6:
                enabled: true
                address:
                # For SNO sites with static IP addresses, the node-specific,
                # API and Ingress IPs should all be the same and configured on
                # the interface
                - ip: 1111:2222:3333:4444::aaaa:1
                  prefix-length: 64
          dns-resolver:
            config:
              search:
              - example.com
              server:
              - 1111:2222:3333:4444::2
          routes:
            config:
            - destination: ::/0
              next-hop-interface: eno1
              next-hop-address: 1111:2222:3333:4444::1
              table-id: 254
      templateRefs:
        - name: ai-node-templates-v1
          namespace: open-cluster-management
```


Note

For more information about BMC addressing, see the "Additional resources" section. The `installConfigOverrides` and `ignitionConfigOverride` fields are expanded in the example for ease of readability. 

Note

To override the default `BareMetalHost` CR for a node, create a custom node template in a `ConfigMap` and reference it in the node-level `spec.nodes.templateRefs` field in the `ClusterInstance` CR. Ensure that you set the `argocd.argoproj.io/sync-wave: "3"` annotation in your override `BareMetalHost` CR. 

     3. You can inspect the default set of extra-manifest `MachineConfig` CRs in `out/argocd/extra-manifest`. It is automatically applied to the cluster when it is installed. 
     4. Optional: To provision additional install-time manifests on the provisioned cluster, package your extra manifest CRs in a `ConfigMap` and reference it in the `extraManifestsRefs` field of the `ClusterInstance` CR. For more information, see "Customizing extra installation manifests in the GitOps ZTP pipeline". 

Important

For optimal cluster performance, enable crun for master and worker nodes in single-node OpenShift, single-node OpenShift with additional worker nodes, three-node OpenShift, and standard clusters. 

Enable crun in a `ContainerRuntimeConfig` CR as an additional Day 0 install-time manifest to avoid the cluster having to reboot. 

The `enable-crun-master.yaml` and `enable-crun-worker.yaml` CR files are in the `out/source-crs/optional-extra-manifest/` folder that you can extract from the `ztp-site-generate` container. 

  4. Add the `ClusterInstance` CR to the `kustomization.yaml` file in the `generators` section, similar to the example shown in `out/argocd/example/clusterinstance/kustomization.yaml`. 
  5. Commit the `ClusterInstance` CR and associated `kustomization.yaml` changes in your Git repository and push the changes. 

The ArgoCD pipeline detects the changes and begins the managed cluster deployment. 




**Verification**

  * Verify that the custom roles and labels are applied after the node is deployed: 

```shell-session
$ oc describe node example-node.example.com
```


The following example output shows the custom roles and labels: 

```shell-session
Name:   example-node.example.com
Roles:  control-plane,example-label,master,worker
Labels: beta.kubernetes.io/arch=amd64
        beta.kubernetes.io/os=linux
        custom-label/parameter1=true
        kubernetes.io/arch=amd64
        kubernetes.io/hostname=cnfdf03.telco5gran.eng.rdu2.redhat.com
        kubernetes.io/os=linux
        node-role.kubernetes.io/control-plane=
        node-role.kubernetes.io/example-label=
        node-role.kubernetes.io/master=
        node-role.kubernetes.io/worker=
        node.openshift.io/os_id=rhcos
```


    * `node-role.kubernetes.io/example-label=` shows the custom label applied to the node. 




**Additional resources**

  * [Single-node OpenShift ClusterInstance CR installation reference](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/ztp-deploying-far-edge-sites#ztp-clusterinstance-config-reference_ztp-deploying-far-edge-sites "4.6.4. ClusterInstance CR installation reference")



## 4.6.1. Configuring IPsec encryption for single-node OpenShift clusters using GitOps ZTP and ClusterInstance resources

You can enable IPsec encryption in managed single-node OpenShift clusters that you install using GitOps ZTP and Red Hat Advanced Cluster Management (RHACM). 

You can encrypt traffic between the managed cluster and IPsec endpoints external to the managed cluster. All network traffic between nodes on the OVN-Kubernetes cluster network is encrypted with IPsec in Transport mode. 

Important

You can also configure IPsec encryption for single-node OpenShift clusters with an additional worker node by following this procedure. It is recommended to use the `MachineConfig` custom resource (CR) to configure IPsec encryption for single-node OpenShift clusters and single-node OpenShift clusters with an additional worker node because of their low resource availability. 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 
  * You have logged in to the hub cluster as a user with `cluster-admin` privileges. 
  * You have installed the SiteConfig Operator in the hub cluster. 
  * You have configured RHACM and the hub cluster for generating the required installation and policy custom resources (CRs) for managed clusters. 
  * You have created a Git repository where you manage your custom site configuration data. The repository must be accessible from the hub cluster and be defined as a source repository for the Argo CD application. 
  * You have installed the `butane` utility version 0.20.0 or later. 
  * You have a PKCS#12 certificate for the IPsec endpoint and a CA cert in PEM format. 



**Procedure**

  1. Extract the latest version of the `ztp-site-generate` container source and merge it with your repository where you manage your custom site configuration data. 
  2. Configure `optional-extra-manifest/ipsec/ipsec-endpoint-config.yaml` with the required values that configure IPsec in the cluster. For example: 

```yaml
interfaces:
- name: hosta_conn
  type: ipsec
  libreswan:
    left: '%defaultroute'
    leftid: '%fromcert'
    leftmodecfgclient: false
    leftcert: left_server
    leftrsasigkey: '%cert'
    right: <external_host>
    rightid: '%fromcert'
    rightrsasigkey: '%cert'
    rightsubnet: <external_address>
    ikev2: insist
    type: tunnel
```


     * `leftcert` must match the name of the certificate used on the remote system. 
     * `right` is the external host IP address or DNS hostname. 
     * `rightsubnet` is the IP subnet of the external host on the other side of the IPsec tunnel. 
     * `ikev2: insist` uses the IKEv2 VPN encryption protocol only. Do not use IKEv1, which is deprecated. 

  3. Add the following certificates to the `optional-extra-manifest/ipsec` folder: 

     * `left_server.p12`: The certificate bundle for the IPsec endpoints 
     * `ca.pem`: The certificate authority that you signed your certificates with 

The certificate files are required for the Network Security Services (NSS) database on each host. These files are imported as part of the Butane configuration in later steps. 

  4. Open a shell prompt at the `optional-extra-manifest/ipsec` folder of the Git repository where you maintain your custom site configuration data. 
  5. Run the `optional-extra-manifest/ipsec/build.sh` script to generate the required Butane and `MachineConfig` CRs files. 

If the PKCS#12 certificate is protected with a password, set the `-W` argument. 

The following example shows the generated output directory structure: 

```shell-session
out
 └── argocd
      └── example
           └── optional-extra-manifest
                └── ipsec
                     ├── 99-ipsec-master-endpoint-config.bu
                     ├── 99-ipsec-master-endpoint-config.yaml
                     ├── 99-ipsec-worker-endpoint-config.bu
                     ├── 99-ipsec-worker-endpoint-config.yaml
                     ├── build.sh
                     ├── ca.pem
                     ├── left_server.p12
                     ├── enable-ipsec.yaml
                     ├── ipsec-endpoint-config.yml
                     └── README.md
```


     * The `ipsec/build.sh` script generates the Butane and endpoint configuration CRs. 
     * Add the `ca.pem` and `left_server.p12` certificate files that are relevant to your network. 

  6. Create an `ipsec-manifests/` folder in the repository where you manage your custom site configuration data. Add the `enable-ipsec.yaml` and `99-ipsec-*` YAML files to the directory. For example: 

```shell-session
site-configs/
  ├── hub-1/
  │   └── clusterinstance-site1-sno-du.yaml
  ├── ipsec-manifests/
  │   ├── enable-ipsec.yaml
  │   ├── 99-ipsec-worker-endpoint-config.yaml
  │   └── 99-ipsec-master-endpoint-config.yaml
  └── kustomization.yaml
```


  7. Create a `kustomization.yaml` file that uses `configMapGenerator` to package your IPsec manifests into a `ConfigMap`: 

```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
  - hub-1/clusterinstance-site1-sno-du.yaml
configMapGenerator:
  - name: ipsec-manifests-cm
    namespace: site1-sno-du
    files:
      - ipsec-manifests/enable-ipsec.yaml
      - ipsec-manifests/99-ipsec-master-endpoint-config.yaml
      - ipsec-manifests/99-ipsec-worker-endpoint-config.yaml
generatorOptions:
  disableNameSuffixHash: true
```


     * `namespace` must match the `ClusterInstance` namespace. 
     * `disableNameSuffixHash: true` disables the hash suffix so the `ConfigMap` name is predictable. 

  8. In your `ClusterInstance` CR, reference the `ConfigMap` in the `extraManifestsRefs` field: 

```yaml
apiVersion: siteconfig.open-cluster-management.io/v1alpha1
kind: ClusterInstance
metadata:
  name: "site1-sno-du"
  namespace: "site1-sno-du"
spec:
  clusterName: "site1-sno-du"
  networkType: "OVNKubernetes"
  extraManifestsRefs:
    - name: ipsec-manifests-cm
# ...
```


     * `extraManifestsRefs.name` references the `ConfigMap` containing the IPsec manifests. 

Note

If you have other extra manifests, you can either include them in the same `ConfigMap` or create multiple `ConfigMap` resources and reference each of those in the `extraManifestsRefs` field. 

  9. Commit the `ClusterInstance` CR, IPsec manifest files, and `kustomization.yaml` changes in your Git repository and push the changes to provision the managed cluster and configure IPsec encryption. 

The Argo CD pipeline detects the changes and begins the managed cluster deployment. 

During cluster provisioning, the SiteConfig Operator applies the CRs contained in the referenced `ConfigMap` resources as extra manifests. 




**Verification**

For information about verifying the IPsec encryption, see "Verifying the IPsec encryption". 

**Additional resources**

  * [Verifying the IPsec encryption](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/ztp-deploying-far-edge-sites#ztp-verifying-ipsec_ztp-deploying-far-edge-sites "4.6.3. Verifying the IPsec encryption")
  * [Configuring IPsec encryption](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_security/#configuring-ipsec-ovn)
  * [Encryption protocol and IPsec mode](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_security/#nw-ovn-ipsec-encryption_configuring-ipsec-ovn)
  * [Installing managed clusters with RHACM and ClusterInstance resources](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/ztp-deploying-far-edge-sites "Chapter 4. Installing managed clusters with RHACM and ClusterInstance resources")



## 4.6.2. Configuring IPsec encryption for multi-node clusters using GitOps ZTP and ClusterInstance resources

You can enable IPsec encryption in managed multi-node clusters that you install using GitOps ZTP and Red Hat Advanced Cluster Management (RHACM). 

You can encrypt traffic between the managed cluster and IPsec endpoints external to the managed cluster. All network traffic between nodes on the OVN-Kubernetes cluster network is encrypted with IPsec in Transport mode. 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 
  * You have logged in to the hub cluster as a user with `cluster-admin` privileges. 
  * You have installed the SiteConfig Operator in the hub cluster. 
  * You have configured RHACM and the hub cluster for generating the required installation and policy custom resources (CRs) for managed clusters. 
  * You have created a Git repository where you manage your custom site configuration data. The repository must be accessible from the hub cluster and be defined as a source repository for the Argo CD application. 
  * You have installed the `butane` utility version 0.20.0 or later. 
  * You have a PKCS#12 certificate for the IPsec endpoint and a CA cert in PEM format. 
  * You have installed the NMState Operator. 



**Procedure**

  1. Extract the latest version of the `ztp-site-generate` container source and merge it with your repository where you manage your custom site configuration data. 
  2. Configure the `optional-extra-manifest/ipsec/ipsec-config-policy.yaml` file with the required values that configure IPsec in the cluster. 

**`ConfigurationPolicy` object for creating an IPsec configuration**

```yaml
apiVersion: policy.open-cluster-management.io/v1
kind: ConfigurationPolicy
metadata:
  name: policy-config
spec:
  namespaceSelector:
    include: ["default"]
    exclude: []
    matchExpressions: []
    matchLabels: {}
  remediationAction: inform
  severity: low
  evaluationInterval:
    compliant:
    noncompliant:
  object-templates-raw: |
    {{- range (lookup "v1" "Node" "" "").items }}
    - complianceType: musthave
      objectDefinition:
        kind: NodeNetworkConfigurationPolicy
        apiVersion: nmstate.io/v1
        metadata:
          name: {{ .metadata.name }}-ipsec-policy
        spec:
          nodeSelector:
            kubernetes.io/hostname: {{ .metadata.name }}
          desiredState:
            interfaces:
            - name: hosta_conn
              type: ipsec
              libreswan:
                left: '%defaultroute'
                leftid: '%fromcert'
                leftmodecfgclient: false
                leftcert: left_server
                leftrsasigkey: '%cert'
                right: <external_host>
                rightid: '%fromcert'
                rightrsasigkey: '%cert'
                rightsubnet: <external_address>
                ikev2: insist
                type: tunnel
```


     * `leftcert` must match the name of the certificate used on the remote system. 
     * `right` is the external host IP address or DNS hostname. 
     * `rightsubnet` is the IP subnet of the external host on the other side of the IPsec tunnel. 
     * `ikev2: insist` uses the IKEv2 VPN encryption protocol only. Do not use IKEv1, which is deprecated. 

  3. Add the following certificates to the `optional-extra-manifest/ipsec` folder: 

     * `left_server.p12`: The certificate bundle for the IPsec endpoints 
     * `ca.pem`: The certificate authority that you signed your certificates with 

The certificate files are required for the Network Security Services (NSS) database on each host. These files are imported as part of the Butane configuration in later steps. 

  4. Open a shell prompt at the `optional-extra-manifest/ipsec` folder of the Git repository where you maintain your custom site configuration data. 
  5. Run the `optional-extra-manifest/ipsec/import-certs.sh` script to generate the required Butane and `MachineConfig` CRs to import the external certs. 

If the PKCS#12 certificate is protected with a password, set the `-W` argument. 

The following example shows the generated output directory structure: 

```shell-session
out
 └── argocd
      └── example
           └── optional-extra-manifest
                └── ipsec
                     ├── 99-ipsec-master-import-certs.bu
                     ├── 99-ipsec-master-import-certs.yaml
                     ├── 99-ipsec-worker-import-certs.bu
                     ├── 99-ipsec-worker-import-certs.yaml
                     ├── import-certs.sh
                     ├── ca.pem
                     ├── left_server.p12
                     ├── enable-ipsec.yaml
                     ├── ipsec-config-policy.yaml
                     └── README.md
```


     * The `ipsec/import-certs.sh` script generates the Butane and endpoint configuration CRs. 
     * Add the `ca.pem` and `left_server.p12` certificate files that are relevant to your network. 

  6. Create an `ipsec-manifests/` folder in the repository where you manage your custom site configuration data and add the `enable-ipsec.yaml` and `99-ipsec-*` YAML files to the directory. 

**Example site configuration directory**

```shell-session
site-configs/
  ├── hub-1/
  │   └── clusterinstance-site1-mno-du.yaml
  ├── ipsec-manifests/
  │   ├── enable-ipsec.yaml
  │   ├── 99-ipsec-master-import-certs.yaml
  │   └── 99-ipsec-worker-import-certs.yaml
  └── kustomization.yaml
```


  7. Create a `kustomization.yaml` file that uses `configMapGenerator` to package your IPsec manifests into a `ConfigMap`: 

```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
  - hub-1/clusterinstance-site1-mno-du.yaml
configMapGenerator:
  - name: ipsec-manifests-cm
    namespace: site1-mno-du
    files:
      - ipsec-manifests/enable-ipsec.yaml
      - ipsec-manifests/99-ipsec-master-import-certs.yaml
      - ipsec-manifests/99-ipsec-worker-import-certs.yaml
generatorOptions:
  disableNameSuffixHash: true
```


     * `namespace` must match the `ClusterInstance` namespace. 
     * `disableNameSuffixHash: true` disables the hash suffix so the `ConfigMap` name is predictable. 

  8. In your `ClusterInstance` CR, reference the `ConfigMap` in the `extraManifestsRefs` field: 

```yaml
apiVersion: siteconfig.open-cluster-management.io/v1alpha1
kind: ClusterInstance
metadata:
  name: "site1-mno-du"
  namespace: "site1-mno-du"
spec:
  clusterName: "site1-mno-du"
  networkType: "OVNKubernetes"
  extraManifestsRefs:
    - name: ipsec-manifests-cm
# ...
```


     * `extraManifestsRefs.name` references the `ConfigMap` containing the IPsec certificate import manifests. 

Note

If you have other extra manifests, you can either include them in the same `ConfigMap` or create multiple `ConfigMap` resources and reference them all in `extraManifestsRefs`. 

  9. Include the `ipsec-config-policy.yaml` config policy file in the `source-crs` directory in GitOps and reference the file in one of the `PolicyGenerator` CRs. 
  10. Commit the `ClusterInstance` CR, IPsec manifest files, and `kustomization.yaml` changes in your Git repository and push the changes to provision the managed cluster and configure IPsec encryption. 

The Argo CD pipeline detects the changes and begins the managed cluster deployment. 

During cluster provisioning, the SiteConfig Operator applies the CRs contained in the referenced `ConfigMap` resources as extra manifests. The IPsec configuration policy is applied as a Day 2 operation after the cluster is provisioned. 




**Verification**

For information about verifying the IPsec encryption, see "Verifying the IPsec encryption". 

**Additional resources**

  * [Verifying the IPsec encryption](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/ztp-deploying-far-edge-sites#ztp-verifying-ipsec_ztp-deploying-far-edge-sites "4.6.3. Verifying the IPsec encryption")
  * [Configuring IPsec encryption](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_security/#configuring-ipsec-ovn)
  * [Encryption protocol and IPsec mode](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_security/#nw-ovn-ipsec-encryption_configuring-ipsec-ovn)
  * [Installing managed clusters with RHACM and ClusterInstance resources](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/ztp-deploying-far-edge-sites "Chapter 4. Installing managed clusters with RHACM and ClusterInstance resources")



## 4.6.3. Verifying the IPsec encryption

You can verify that the IPsec encryption is successfully applied in a managed OpenShift Container Platform cluster. 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 
  * You have logged in to the hub cluster as a user with `cluster-admin` privileges. 
  * You have configured the IPsec encryption. 



**Procedure**

  1. Start a debug pod for the managed cluster by running the following command: 

```shell-session
$ oc debug node/<node_name>
```


  2. Check that the IPsec policy is applied in the cluster node by running the following command: 

```shell-session
sh-5.1# ip xfrm policy
```


The following example output shows the IPsec policy applied to the cluster node: 

```shell-session
src 172.16.123.0/24 dst 10.1.232.10/32
  dir out priority 1757377 ptype main
  tmpl src 10.1.28.190 dst 10.1.232.10
    proto esp reqid 16393 mode tunnel
src 10.1.232.10/32 dst 172.16.123.0/24
  dir fwd priority 1757377 ptype main
  tmpl src 10.1.232.10 dst 10.1.28.190
    proto esp reqid 16393 mode tunnel
src 10.1.232.10/32 dst 172.16.123.0/24
  dir in priority 1757377 ptype main
  tmpl src 10.1.232.10 dst 10.1.28.190
    proto esp reqid 16393 mode tunnel
```


  3. Check that the IPsec tunnel is up and connected by running the following command: 

```shell-session
sh-5.1# ip xfrm state
```


The following example output shows the IPsec tunnel is up and connected: 

```shell-session
src 10.1.232.10 dst 10.1.28.190
  proto esp spi 0xa62a05aa reqid 16393 mode tunnel
  replay-window 0 flag af-unspec esn
  auth-trunc hmac(sha1) 0x8c59f680c8ea1e667b665d8424e2ab749cec12dc 96
  enc cbc(aes) 0x2818a489fe84929c8ab72907e9ce2f0eac6f16f2258bd22240f4087e0326badb
  anti-replay esn context:
   seq-hi 0x0, seq 0x0, oseq-hi 0x0, oseq 0x0
   replay_window 128, bitmap-length 4
   00000000 00000000 00000000 00000000
src 10.1.28.190 dst 10.1.232.10
  proto esp spi 0x8e96e9f9 reqid 16393 mode tunnel
  replay-window 0 flag af-unspec esn
  auth-trunc hmac(sha1) 0xd960ddc0a6baaccb343396a51295e08cfd8aaddd 96
  enc cbc(aes) 0x0273c02e05b4216d5e652de3fc9b3528fea94648bc2b88fa01139fdf0beb27ab
  anti-replay esn context:
   seq-hi 0x0, seq 0x0, oseq-hi 0x0, oseq 0x0
   replay_window 128, bitmap-length 4
   00000000 00000000 00000000 00000000
```


  4. Ping a known IP in the external host subnet by running the following command: For example, ping an IP address in the `rightsubnet` range that you set in the `ipsec/ipsec-endpoint-config.yaml` file: 

```shell-session
sh-5.1# ping 172.16.110.8
```


The following example output shows a successful ping response: 

```shell-session
PING 172.16.110.8 (172.16.110.8) 56(84) bytes of data.
64 bytes from 172.16.110.8: icmp_seq=1 ttl=64 time=153 ms
64 bytes from 172.16.110.8: icmp_seq=2 ttl=64 time=155 ms
```


## 4.6.4. ClusterInstance CR installation reference

For a detailed API reference for the `ClusterInstance` custom resource, see [ClusterInstance API](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.17/html-single/apis/index#clusterinstance-api) in the Red Hat Advanced Cluster Management (RHACM) documentation. 

**Additional resources**

  * [Customizing extra installation manifests in the GitOps ZTP pipeline](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/ztp-advanced-install-ztp#ztp-customizing-the-install-extra-manifests_ztp-advanced-install-ztp "9.1. Customizing extra installation manifests in the GitOps ZTP pipeline")
  * [Preparing the GitOps ZTP site configuration repository](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/ztp-preparing-the-hub-cluster#ztp-preparing-the-ztp-git-repository_ztp-preparing-the-hub-cluster "2.9. Prepare the GitOps ZTP site configuration repository")
  * [Configuring the hub cluster with ArgoCD](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/ztp-preparing-the-hub-cluster#ztp-configuring-hub-cluster-with-argocd_ztp-preparing-the-hub-cluster "2.8. Configure the hub cluster with ArgoCD")
  * [Signalling GitOps ZTP cluster deployment completion with validator inform policies](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/managing-cluster-policies-with-policygentemplate-resources#ztp-creating-a-validator-inform-policy_ztp-advanced-policy-config "11.2.5. Signalling GitOps ZTP cluster deployment completion with validator inform policies")
  * [Creating the managed bare-metal host secrets](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/ztp-manual-install#ztp-creating-the-site-secrets_ztp-manual-install "5.2. Create the managed bare-metal host secrets")
  * [BMC addressing](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_bare_metal/#bmc-addressing_ipi-install-installation-workflow)
  * [About root device hints](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_an_on-premise_cluster_with_the_agent-based_installer/#root-device-hints_preparing-to-install-with-agent-based-installer)
