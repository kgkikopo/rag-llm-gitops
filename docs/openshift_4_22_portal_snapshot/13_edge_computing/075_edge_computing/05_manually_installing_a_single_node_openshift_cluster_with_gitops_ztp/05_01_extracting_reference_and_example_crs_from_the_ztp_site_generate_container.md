# 5.1. Extracting reference and example CRs from the ztp-site-generate container

Use the `ztp-site-generate` container to extract reference custom resources (CRs) and example `ClusterInstance` CRs to prepare for cluster installation and Day 2 configuration. 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 
  * You have logged in to the hub cluster as a user with `cluster-admin` privileges. 
  * You installed `podman`. 



**Procedure**

  1. Create an output folder by running the following command: 

```shell-session
$ mkdir -p ./out
```


  2. Log in to the Ecosystem container registry with your credentials by running the following command: 

```shell-session
$ podman login registry.redhat.io
```


  3. Extract the reference and example CRs from the `ztp-site-generate` container image by running the following command: 

```shell-session
$ podman run --log-driver=none --rm registry.redhat.io/openshift4/ztp-site-generate-rhel8:v4.22 extract /home/ztp --tar | tar x -C ./out
```


The `./out` directory contains the reference `PolicyGenerator` and `ClusterInstance` CRs in the `out/argocd/example/` folder. 

**Example output**

```shell-session
out
 └── argocd
      └── example
           ├── acmpolicygenerator
           │     ├── {policy-prefix}common-ranGen.yaml
           │     ├── {policy-prefix}example-sno-site.yaml
           │     ├── {policy-prefix}group-du-sno-ranGen.yaml
           │     ├── ...
           │     ├── kustomization.yaml
           │     └── ns.yaml
           └── clusterinstance
                 ├── example-sno.yaml
                 ├── example-3node.yaml
                 ├── example-standard.yaml
                 └── ...
```


  4. Create a `ClusterInstance` CR for your cluster. 

Use the example `ClusterInstance` CRs in the `out/argocd/example/clusterinstance/` folder that you previously extracted from the `ztp-site-generate` container as a reference. The folder includes example files for single node, three-node, and standard clusters: 

     * `example-sno.yaml`
     * `example-3node.yaml`
     * `example-standard.yaml`

Change the cluster and host details in the example file to match the type of cluster you want to install. For example: 

**Example single-node OpenShift ClusterInstance CR**

```yaml
# example-node1-bmh-secret & assisted-deployment-pull-secret need to be created under same namespace example-ai-sno
---
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

Optional: To provision additional install-time manifests on the provisioned cluster, create the extra manifest CRs and apply them to the hub cluster. Then reference them in the `extraManifestsRefs` field of the `ClusterInstance` CR. For more information, see "Customizing extra installation manifests in the GitOps ZTP pipeline". 

  5. Optional: Generate Day 2 configuration CRs from the reference `PolicyGenerator` CRs: 

     1. Create an output folder for the configuration CRs by running the following command: 

```shell-session
$ mkdir -p ./ref
```


     2. Generate the configuration CRs by running the following command: 

```shell-session
$ podman run -it --rm -v `pwd`/out/argocd/example/policygentemplates:/resources:Z -v `pwd`/ref:/output:Z,U registry.redhat.io/openshift4/ztp-site-generate-rhel8:v4.22 generator config -N . /output
```


The command generates example group and cluster-specific configuration CRs in the `./ref` folder. You can apply these CRs to the cluster after installation is complete.
