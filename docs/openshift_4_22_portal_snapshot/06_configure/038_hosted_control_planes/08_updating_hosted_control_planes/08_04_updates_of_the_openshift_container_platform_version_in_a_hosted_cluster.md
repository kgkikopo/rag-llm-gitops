# 8.4. Updates of the OpenShift Container Platform version in a hosted cluster

Hosted control planes enables the decoupling of updates between the control plane and the data plane. 

As a cluster service provider or cluster administrator, you can manage the control plane and the data separately. 

You can update a control plane by modifying the `HostedCluster` custom resource (CR) and a node by modifying its `NodePool` CR. Both the `HostedCluster` and `NodePool` CRs specify an OpenShift Container Platform release image in a `.release` field. 

To keep your hosted cluster fully operational during an update process, the control plane and the node versions must be compatible. For more information, see "Hosted cluster and node pool version skew policy". 

## 8.4.1. The multicluster engine Operator hub management cluster

The multicluster engine for Kubernetes Operator requires a specific OpenShift Container Platform version for the management cluster to remain in a supported state. You can install the multicluster engine Operator from the software catalog in the OpenShift Container Platform web console. 

For more information, see the support matrixes for the multicluster engine Operator versions. 

The multicluster engine Operator supports the following OpenShift Container Platform versions: 

  * The latest unreleased version 
  * The latest released version 
  * Two versions before the latest released version 



You can also get the multicluster engine Operator version as a part of Red Hat Advanced Cluster Management (RHACM). 

## 8.4.2. Supported OpenShift Container Platform versions in a hosted cluster

When deploying a hosted cluster, the OpenShift Container Platform version of the management cluster does not affect the OpenShift Container Platform version of a hosted cluster. 

The HyperShift Operator creates the `supported-versions` ConfigMap in the `hypershift` namespace. The `supported-versions` ConfigMap describes the range of supported OpenShift Container Platform versions that you can deploy. 

See the following example of the `supported-versions` ConfigMap: 

```yaml
apiVersion: v1
data:
    server-version: 2f6cfe21a0861dea3130f3bed0d3ae5553b8c28b
    supported-versions: '{"versions":["4.17","4.16","4.15","4.14"]}'
kind: ConfigMap
metadata:
    creationTimestamp: "2024-06-20T07:12:31Z"
    labels:
        hypershift.openshift.io/supported-versions: "true"
    name: supported-versions
    namespace: hypershift
    resourceVersion: "927029"
    uid: f6336f91-33d3-472d-b747-94abae725f70
```


Important

To create a hosted cluster, you must use the OpenShift Container Platform version from the support version range. However, the multicluster engine Operator can manage only between `n+1` and `n-2` OpenShift Container Platform versions, where `n` defines the current minor version. You can check the multicluster engine Operator support matrix to ensure the hosted clusters managed by the multicluster engine Operator are within the supported OpenShift Container Platform range. 

To deploy a higher version of a hosted cluster on OpenShift Container Platform, you must update the multicluster engine Operator to a new minor version release to deploy a new version of the Hypershift Operator. Upgrading the multicluster engine Operator to a new patch, or z-stream, release does not update the HyperShift Operator to the next version. 

See the following example output of the `hcp version` command that shows the supported OpenShift Container Platform versions for OpenShift Container Platform 4.16 in the management cluster: 

```shell-session
Client Version: openshift/hypershift: fe67b47fb60e483fe60e4755a02b3be393256343. Latest supported OCP: 4.17.0
Server Version: 05864f61f24a8517731664f8091cedcfc5f9b60d
Server Supports OCP Versions: 4.17, 4.16, 4.15, 4.14
```


**Additional resources**

  * [Hosted cluster and node pool version skew policy](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hosted_control_planes/hcp-updating#hcp-np-version-skew_hcp-updating "8.2. Hosted cluster and node pool version skew policy")
  * [multicluster engine Operator 2.17](https://access.redhat.com/articles/7142379)
  * [multicluster engine Operator 2.11](https://access.redhat.com/articles/7136929)
  * [multicluster engine Operator 2.10](https://access.redhat.com/articles/7133096)
  * [multicluster engine Operator 2.9](https://access.redhat.com/articles/7120837)
  * [multicluster engine Operator 2.8](https://access.redhat.com/articles/7099674)
  * [multicluster engine Operator 2.7](https://access.redhat.com/articles/7086906)
  * [multicluster engine Operator 2.6](https://access.redhat.com/articles/7073030)
  * [multicluster engine Operator 2.5](https://access.redhat.com/articles/7056007)
  * [multicluster engine Operator 2.4](https://access.redhat.com/articles/7027079)
