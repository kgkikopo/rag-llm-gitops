# 9.3. Configuring cluster network MTU at installation time

You can explicitly set the cluster network maximum transmission unit (MTU) during installation by including a `Network` custom resource (CR) as an extra manifest in the GitOps Zero Touch Provisioning (ZTP) pipeline. 

Setting the cluster network MTU with additional headroom during deployment prevents the need for a Day 2 MTU update that requires at least two rolling reboots of all cluster nodes. 

During installation, the Cluster Network Operator (CNO) automatically calculates the cluster network MTU based on the primary network interface MTU. When you enable IPsec at installation time, the calculation includes both the OVN-Kubernetes overhead of 100 bytes and the IPsec overhead. If you plan to enable IPsec or another encapsulation technology as a Day 2 operation, the calculated MTU includes only the OVN-Kubernetes overhead and might be insufficient. 

By explicitly setting the cluster network MTU at installation time, you can include additional headroom for those future needs and avoid a disruptive MTU migration. 

Important

The cluster network MTU value must be lower than the machine network MTU by at least 100 bytes to account for OVN-Kubernetes overlay overhead. If you plan to enable IPsec as a Day 2 operation, allow an additional 46 bytes for IPsec headroom. For example, with a machine network MTU of `9100` bytes, set the cluster network MTU to `8900` bytes, which accounts for the following offset: 

  * OVN-Kubernetes overhead: 100 bytes 
  * IPsec headroom: 46 bytes 
  * Extra headroom: 54 bytes 
  * Total offset: 200 bytes 



To avoid selecting an MTU value that a node cannot support, verify the maximum MTU (`maxmtu`) that the network interface accepts by running the `ip -d link` command. 

**Prerequisites**

  * You have configured the hub cluster to provision managed clusters by using the GitOps ZTP pipeline. 
  * You have a Git repository where you manage your custom site configuration data. The repository must be accessible from the hub cluster and be defined as a source repository for the Argo CD application. 



**Procedure**

  1. In your `ClusterInstance` CR, set the machine network MTU on the network interface for all nodes. 

The following example configures a VLAN interface with MTU `9100`: 

```yaml
apiVersion: siteconfig.open-cluster-management.io/v1alpha1
kind: ClusterInstance
metadata:
  name: "site1-sno-du"
  namespace: "site1-sno-du"
spec:
  nodes:
    - hostName: "node1.example.com"
      nodeNetwork:
        interfaces:
          - name: "bond0.120"
            macAddress: "00:00:00:00:00:00"
        config:
          interfaces:
            - name: bond0.120
              type: vlan
              state: up
              mtu: 9100
              ipv4:
                enabled: true
                dhcp: false
                address:
                  - ip: "192.168.120.15"
                    prefix-length: 25
              vlan:
                base-iface: bond0
                id: 120
  # ...
```


  2. Create a `Network` CR manifest file named `set-cluster-mtu.yaml` that sets the cluster network MTU: 

```yaml
apiVersion: operator.openshift.io/v1
kind: Network
metadata:
  name: cluster
spec:
  defaultNetwork:
    ovnKubernetesConfig:
      mtu: 8900
```


where: 

`mtu`
     Specifies the cluster network MTU value. This value must be at least 100 bytes less than the machine network MTU. In this example, the value is 200 bytes less than the machine network MTU of 9100 to allow headroom for IPsec and other future requirements. 

  3. In your `clusterinstance` directory, place the manifest file in an extra manifests subdirectory: 

```plaintext
clusterinstance/
├── site1-sno-du.yaml
├── extra-manifest/
│   └── set-cluster-mtu.yaml
└── kustomization.yaml
```


  4. Create or update the `kustomization.yaml` file to package the extra manifest into a `ConfigMap`: 

```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
  - site1-sno-du.yaml
configMapGenerator:
  - name: cluster-mtu-extra-manifests
    namespace: site1-sno-du
    files:
      - extra-manifest/set-cluster-mtu.yaml
generatorOptions:
  disableNameSuffixHash: true
```


  5. In your `ClusterInstance` CR, reference the `ConfigMap` in the `extraManifestsRefs` field: 

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
    - name: cluster-mtu-extra-manifests
  # ...
```


  6. Commit the `ClusterInstance` CR, the `set-cluster-mtu.yaml` manifest, and the `kustomization.yaml` to your Git repository and push the changes. 

During cluster provisioning, the SiteConfig Operator applies the `Network` CR as an extra manifest, and the CNO uses the specified MTU value instead of auto-calculating it. 




**Verification**

  * After the cluster installation is complete, verify the cluster network MTU by running the following command: 

```shell-session
$ oc get networks.operator.openshift.io cluster -o yaml
```


**Example output**

```yaml
apiVersion: operator.openshift.io/v1
kind: Network
metadata:
  name: cluster
# ...
spec:
  # ...
  defaultNetwork:
    ovnKubernetesConfig:
      # ...
      mtu: 8900
```


**Additional resources**

  * [Customizing extra installation manifests in the GitOps ZTP pipeline](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/ztp-advanced-install-ztp#ztp-customizing-the-install-extra-manifests_ztp-advanced-install-ztp "9.1. Customizing extra installation manifests in the GitOps ZTP pipeline")
  * [Creating a manifest object that includes a customized br-ex bridge](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_bare_metal/#creating-manifest-file-customized-br-ex-bridge_ipi-install-installation-workflow)
