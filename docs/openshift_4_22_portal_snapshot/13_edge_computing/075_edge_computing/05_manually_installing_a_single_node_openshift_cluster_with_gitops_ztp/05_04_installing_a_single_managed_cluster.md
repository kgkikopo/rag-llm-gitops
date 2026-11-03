# 5.4. Installing a single managed cluster

You can manually deploy a single managed cluster using the assisted service and Red Hat Advanced Cluster Management (RHACM). 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 
  * You have logged in to the hub cluster as a user with `cluster-admin` privileges. 
  * You have extracted the reference and example CRs from the `ztp-site-generate` container and you configured the `ClusterInstance` CR. 
  * You have created the baseboard management controller (BMC) `Secret` and the image pull-secret `Secret` custom resources (CRs). See "Creating the managed bare-metal host secrets" for details. 
  * Your target bare-metal host meets the networking and hardware requirements for managed clusters. 



**Procedure**

  1. Create a `ClusterImageSet` for each specific cluster version to be deployed, for example `clusterImageSet-4.22.yaml`. A `ClusterImageSet` has the following format: 

```yaml
apiVersion: hive.openshift.io/v1
kind: ClusterImageSet
metadata:
  name: openshift-4.22.0
spec:
   releaseImage: quay.io/openshift-release-dev/ocp-release:4.22.0-x86_64
```


where: 

`name`
     The descriptive version that you want to deploy. 
`releaseImage`
     Specifies the `releaseImage` to deploy and determines the operating system image version. The discovery ISO is based on the image version as set by `releaseImage`, or the latest version if the exact version is unavailable. 

  2. Apply the `clusterImageSet` CR: 

```shell-session
$ oc apply -f clusterImageSet-4.22.yaml
```


  3. Create the `Namespace` CR in the `cluster-namespace.yaml` file: 

```yaml
apiVersion: v1
kind: Namespace
metadata:
     name: <cluster_name>
     labels:
        name: <cluster_name>
```


where: 

`name`
     The name of the managed cluster to provision. 

  4. Apply the `Namespace` CR by running the following command: 

```shell-session
$ oc apply -f cluster-namespace.yaml
```


  5. Apply the `ClusterInstance` CR that you configured to the hub cluster by running the following command: 

```shell-session
$ oc apply -f clusterinstance.yaml
```


The SiteConfig Operator processes the `ClusterInstance` CR and automatically generates the required installation CRs, including `BareMetalHost`, `AgentClusterInstall`, `ClusterDeployment`, `InfraEnv`, and `NMStateConfig`. The assisted service then begins the cluster installation. 




**Additional resources**

  * [BMC addressing](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_bare_metal/#bmc-addressing_ipi-install-installation-workflow)
  * [About root device hints](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_an_on-premise_cluster_with_the_agent-based_installer/#root-device-hints_preparing-to-install-with-agent-based-installer)
  * [Single-node OpenShift ClusterInstance CR installation reference](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/ztp-deploying-far-edge-sites#ztp-clusterinstance-config-reference_ztp-deploying-far-edge-sites "4.6.4. ClusterInstance CR installation reference")
  * [Connectivity prerequisites for managed cluster networks](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/sno-configure-for-vdu#ztp-managed-cluster-network-prereqs_sno-configure-for-vdu "7.4. Connectivity prerequisites for managed cluster networks")
  * [Deploying LVM Storage on single-node OpenShift clusters](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage/#lvms-preface-sno-ran_logical-volume-manager-storage)
  * [Configuring LVM Storage using PolicyGenerator CRs](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/managing-cluster-policies-with-policygentemplate-resources#ztp-provisioning-lvm-storage_ztp-advanced-policy-config "11.2.7. Configuring LVM Storage using PolicyGenTemplate CRs")
  * [Configuring managed cluster policies by using PolicyGenerator resources](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/managing-cluster-policies-with-policygenerator-resources#ztp-configuring-managed-clusters-policygenerator "10.1. Configuring managed cluster policies by using PolicyGenerator resources")
