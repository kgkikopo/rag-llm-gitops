# 8.5. Updates for the hosted cluster

The `spec.release.image` value dictates the version of the control plane. The `HostedCluster` object transmits the intended `spec.release.image` value to the `HostedControlPlane.spec.releaseImage` value and runs the appropriate Control Plane Operator version. 

The hosted control plane manages the rollout of the new version of the control plane components along with any OpenShift Container Platform components through the new version of the Cluster Version Operator (CVO). 

Important

In hosted control planes, the `NodeHealthCheck` resource cannot detect the status of the CVO. A cluster administrator must manually pause the remediation triggered by `NodeHealthCheck`, before performing critical operations, such as updating the cluster, to prevent new remediation actions from interfering with cluster updates. 

To pause the remediation, enter the array of strings, for example, `pause-test-cluster`, as a value of the `pauseRequests` field in the `NodeHealthCheck` resource. For more information, see "About the Node Health Check Operator". 

After the cluster update is complete, you can edit or delete the remediation. Go to the **Compute** **NodeHealthCheck** page, click your node health check, and then click **Actions** , which shows a drop-down list. 

**Additional resources**

  * [About the Node Health Check Operator](https://docs.redhat.com/en/documentation/workload_availability_for_red_hat_openshift/24.4/html/remediation_fencing_and_maintenance/node-health-check-operator#about-node-health-check-operator_node-health-check-operator)
