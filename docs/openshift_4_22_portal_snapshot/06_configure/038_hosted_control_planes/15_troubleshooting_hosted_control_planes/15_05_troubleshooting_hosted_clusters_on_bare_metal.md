# 15.5. Troubleshooting hosted clusters on bare metal

If you encounter issues with hosted control planes on bare metal, review the troubleshooting procedures to diagnose and resolve them. 

## 15.5.1. Determining why nodes are not added to a hosted cluster on bare metal

When you scale up a hosted cluster with nodes that were provisioned by using Assisted Installer, the host fails to pull the ignition with a URL that contains port `22642`. That URL is invalid for hosted control planes and indicates that an issue exists with the cluster. 

**Procedure**

  1. To determine the issue, review the assisted-service logs by entering the following command: 

```shell-session
$ oc logs -n multicluster-engine <assisted_service_pod_name>
```


Replace `<assisted_service_pod_name>` with the Assisted Service pod name. 

  2. In the logs, find errors that resemble these examples: 

```shell-session
error="failed to get pull secret for update: invalid pull secret data in secret pull-secret"
```


```shell-session
pull secret must contain auth for \"registry.redhat.io\"
```


  3. To fix this issue, see "Add the pull secret to the namespace" in the multicluster engine for Kubernetes Operator documentation. 

Note

To use hosted control planes, you must have multicluster engine Operator installed, either as a standalone Operator or as part of Red Hat Advanced Cluster Management. Because the Operator has a close association with Red Hat Advanced Cluster Management, the documentation for the Operator is published within that product’s documentation. Even if you do not use Red Hat Advanced Cluster Management, the parts of its documentation that cover multicluster engine Operator are relevant to hosted control planes. 




**Additional resources**

  * [Add the pull secret to the namespace](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.16/html-single/clusters/index#on-prem-creating-your-cluster-with-the-cli-pull-secret)
