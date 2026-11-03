# 2.4. Versioning for hosted control planes

The hosted control planes feature includes several components that might require independent versioning and support levels. 

Those components are as follows: 

  * Management cluster 
  * HyperShift Operator 
  * Hosted control planes (`hcp`) command-line interface (CLI) 
  * `hypershift.openshift.io` API 
  * Control Plane Operator 



## 2.4.1. Management cluster

In management clusters for production use, you need multicluster engine for Kubernetes Operator, which is available through the software catalog. The multicluster engine Operator bundles a supported build of the HyperShift Operator. For your management clusters to remain supported, you must use the version of OpenShift Container Platform that multicluster engine Operator runs on. In general, a new release of multicluster engine Operator runs on the following versions of OpenShift Container Platform: 

  * The latest General Availability version of OpenShift Container Platform 
  * Two versions before the latest General Availability version of OpenShift Container Platform 



The full list of OpenShift Container Platform versions that you can install through the HyperShift Operator on a management cluster depends on the version of your HyperShift Operator. However, the list always includes at least the same OpenShift Container Platform version as the management cluster and two previous minor versions relative to the management cluster. For example, if the management cluster is running 4.17 and a supported version of multicluster engine Operator, the HyperShift Operator can install 4.17, 4.16, 4.15, and 4.14 hosted clusters. 

With each major, minor, or patch version release of OpenShift Container Platform, two components of hosted control planes are released: 

  * The HyperShift Operator 
  * The `hcp` command-line interface (CLI) 



## 2.4.2. HyperShift Operator

The HyperShift Operator manages the lifecycle of hosted clusters that are represented by the `HostedCluster` API resources. The HyperShift Operator is released with each OpenShift Container Platform release. The HyperShift Operator creates the `supported-versions` config map in the `hypershift` namespace. The config map contains the supported hosted cluster versions. 

You can host different versions of control planes on the same management cluster. 

**Example`supported-versions` config map object**

```yaml
    apiVersion: v1
    data:
      supported-versions: '{"versions":["4.22"]}'
    kind: ConfigMap
    metadata:
      labels:
        hypershift.openshift.io/supported-versions: "true"
      name: supported-versions
      namespace: hypershift
```


## 2.4.3. hosted control planes CLI

You can use the `hcp` CLI to create hosted clusters. You can download the CLI from multicluster engine Operator. When you run the `hcp version` command, the output shows the latest OpenShift Container Platform that the CLI supports against your `kubeconfig` file. 

## 2.4.4. hypershift.openshift.io API

You can use the `hypershift.openshift.io` API resources, such as, `HostedCluster` and `NodePool`, to create and manage OpenShift Container Platform clusters at scale. A `HostedCluster` resource contains the control plane and common data plane configuration. When you create a `HostedCluster` resource, you have a fully functional control plane with no attached nodes. A `NodePool` resource is a scalable set of worker nodes that is attached to a `HostedCluster` resource. 

The API version policy generally aligns with the policy for Kubernetes API versioning. 

Updates for hosted control planes involve updating the hosted cluster and the node pools. For more information, see "Updates for hosted control planes". 

## 2.4.5. Control Plane Operator

The Control Plane Operator is released as part of each OpenShift Container Platform payload release image for the following architectures: 

  * amd64 
  * arm64 
  * multi-arch 



**Additional resources**

  * [Kubernetes API versioning](https://kubernetes.io/docs/reference/using-api/#api-versioning)
  * [AMD64 release images](https://amd64.ocp.releases.ci.openshift.org/)
  * [ARM64 release images](https://arm64.ocp.releases.ci.openshift.org/)
  * [Multi-arch release images](https://multi.ocp.releases.ci.openshift.org/)
