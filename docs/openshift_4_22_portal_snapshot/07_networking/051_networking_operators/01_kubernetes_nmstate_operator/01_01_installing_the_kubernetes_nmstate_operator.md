# 1.1. Installing the Kubernetes NMState Operator

You can install the Kubernetes NMState Operator by using the web console or the CLI. 

## 1.1.1. Install the Kubernetes NMState Operator by using the web console

You can install the Kubernetes NMState Operator by using the web console. After you install the Kubernetes NMState Operator, the Operator has deployed the NMState State Controller as a daemon set across all of the cluster nodes. 

**Prerequisites**

  * You are logged in as a user with `cluster-admin` privileges. 



**Procedure**

  1. Select **Ecosystem** **Software Catalog**. 
  2. In the search field below **All Items** , enter `nmstate` and click **Enter** to search for the Kubernetes NMState Operator. 
  3. Click on the Kubernetes NMState Operator search result. 
  4. Click on **Install** to open the **Install Operator** window. 
  5. Click **Install** to install the Operator. 
  6. After the Operator finishes installing, click **View Operator**. 
  7. Under **Provided APIs** , click **Create Instance** to open the dialog box for creating an instance of `kubernetes-nmstate`. 
  8. In the **Name** field of the dialog box, ensure the name of the instance is `nmstate.`

Note

The name restriction is a known issue. The instance is a singleton for the entire cluster. 

  9. Accept the default settings and click **Create** to create the instance. 



## 1.1.2. Install the Kubernetes NMState Operator by using the CLI

You can install the Kubernetes NMState Operator by using the OpenShift CLI (`oc)`. After it is installed, the Operator deploys the NMState State Controller as a daemon set across all of the cluster nodes to manage the node network state and configuration. 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 
  * You are logged in as a user with `cluster-admin` privileges. 



**Procedure**

  1. Create the `nmstate` Operator namespace: 

```shell-session
$ cat << EOF | oc apply -f -
apiVersion: v1
kind: Namespace
metadata:
  name: openshift-nmstate
spec:
  finalizers:
  - kubernetes
EOF
```


  2. Create the `OperatorGroup`: 

```shell-session
$ cat << EOF | oc apply -f -
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: openshift-nmstate
  namespace: openshift-nmstate
spec:
  targetNamespaces:
  - openshift-nmstate
EOF
```


  3. Subscribe to the `nmstate` Operator: 

```shell-session
$ cat << EOF| oc apply -f -
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: kubernetes-nmstate-operator
  namespace: openshift-nmstate
spec:
  channel: stable
  installPlanApproval: Automatic
  name: kubernetes-nmstate-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace
EOF
```


  4. Confirm the `ClusterServiceVersion` (CSV) status for the `nmstate` Operator deployment equals `Succeeded`: 

```shell-session
$ oc get clusterserviceversion -n openshift-nmstate \
 -o custom-columns=Name:.metadata.name,Phase:.status.phase
```


  5. Create an instance of the `nmstate` Operator: 

```shell-session
$ cat << EOF | oc apply -f -
apiVersion: nmstate.io/v1
kind: NMState
metadata:
  name: nmstate
EOF
```


  6. If your cluster has problems with the DNS health check probe because of DNS connectivity issues, you can add the following DNS host name configuration to the `NMState` CRD to build in health checks that can resolve these issues: 

```shell-session
apiVersion: nmstate.io/v1
kind: NMState
metadata:
  name: nmstate
spec:
  probeConfiguration:
    dns:
      host: redhat.com
# ...
```


     1. Apply the DNS host name configuration to your cluster network by running the following command. Ensure that you replace `<filename>` with the name of your CRD file. 

```yaml
$ oc apply -f <filename>.yaml
```


     2. Monitor the `nmstate` CRD until the resource reaches the `Available` condition by running the following command. Ensure that you set a value for the `--timeout` option so that if the `Available` condition is not met within this set maximum waiting time, the command times out and generates an error message. 

```yaml
$ oc wait --for=condition=Available nmstate/nmstate --timeout=600s
```


**Verification**

  1. Verify that all pods for the NMState Operator have the `Running` status by entering the following command: 

```shell-session
$ oc get pod -n openshift-nmstate
```


## 1.1.3. View metrics collected by the Kubernetes NMState Operator

The Kubernetes NMState Operator, `kubernetes-nmstate-operator`, can collect metrics from the Kubernetes components and expose them as ready-to-use metrics. 

The Kubernetes NMState Operator can collect metrics from the following Kubernetes components: 

  * `kubernetes_nmstate_features_applied`, which tracks what NMState features are enabled and successfully applied to the cluster. 
  * `kubernetes_nmstate_policies_status`, which tracks the active status of `NodeNetworkConfigurationPolicy` (NNCP) resources across the cluster. 
  * `kubernetes_nmstate_enactments_status`, which tracks the active status of `NodeNetworkConfigurationEnactment` (NNCE) resources on a per-node basis. 



As a use case for viewing metrics, consider a situation where you created a `NodeNetworkConfigurationPolicy` custom resource (CR) and you want to confirm that the policy is active. 

Note

The `kubernetes_nmstate_features_applied` metrics are not an API and might change between OpenShift Container Platform versions. 

In the web console, the Metrics UI includes some predefined CPU, memory, bandwidth, and network packet queries for the selected project. You can run custom Prometheus Query Language (PromQL) queries for CPU, memory, bandwidth, network packet and application metrics for the project. 

The following example demonstrates a `NodeNetworkConfigurationPolicy` manifest example that is applied to an OpenShift Container Platform cluster: 

```yaml
# ...
interfaces:
  - name: br1
    type: linux-bridge
    state: up
    ipv4:
      enabled: true
      dhcp: true
      dhcp-custom-hostname: foo
    bridge:
      options:
        stp:
          enabled: false
      port: []
# ...
```


The `NodeNetworkConfigurationPolicy` manifest exposes metrics and makes them available to the Cluster Monitoring Operator (CMO). The following example shows some exposed metrics: 

```shell-session
controller_runtime_reconcile_time_seconds_bucket{controller="nodenetworkconfigurationenactment",le="0.005"} 16
controller_runtime_reconcile_time_seconds_bucket{controller="nodenetworkconfigurationenactment",le="0.01"} 16
controller_runtime_reconcile_time_seconds_bucket{controller="nodenetworkconfigurationenactment",le="0.025"} 16
...
# HELP kubernetes_nmstate_features_applied Number of nmstate features applied labeled by its name
# TYPE kubernetes_nmstate_features_applied gauge
kubernetes_nmstate_features_applied{name="dhcpv4-custom-hostname"} 1
```


**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 
  * You have logged in to the web console as the administrator and installed the Kubernetes NMState Operator. 
  * You have access to the cluster as a developer or as a user with view permissions for the project that you are viewing metrics for. 
  * You have enabled monitoring for user-defined projects. 
  * You have deployed a service in a user-defined project. 
  * You have created a `NodeNetworkConfigurationPolicy` manifest and applied it to your cluster. 



Important

Starting with OpenShift Container Platform 4.19, the perspectives in the web console have unified. The **Developer** perspective is no longer enabled by default. 

All users can interact with all OpenShift Container Platform web console features. However, if you are not the cluster owner, you might need to request permission to access certain features from the cluster owner. 

You can still enable the **Developer** perspective. On the **Getting Started** pane in the web console, you can take a tour of the console, find information on setting up your cluster, view a quick start for enabling the **Developer** perspective, and follow links to explore new features and capabilities. 

See also, "Enabling the **Developer** perspective in the web console". 

**Procedure**

  1. If you want to view the metrics from the **Developer** perspective in the OpenShift Container Platform web console, complete the following tasks: 

     1. Click **Observe**. 
     2. To view the metrics of a specific project, select the project in the **Project:** list. For example, `openshift-nmstate`. 
     3. Click the **Metrics** tab. 
     4. To visualize the metrics on the plot, select a query from the **Select query** list or create a custom PromQL query based on the selected query by selecting **Show PromQL**. 

Note

You can only run one query at a time with the developer role. 

  2. If you want to view the metrics in the OpenShift Container Platform web console as an administrator, complete the following tasks: 

     1. Click **Observe** **Metrics**. 
     2. Enter `kubernetes_nmstate_features_applied` in the **Expression** field. 
     3. Click **Add query** and then **Run queries**. 

  3. To explore the visualized metrics, do any of the following tasks: 

     1. To zoom into the plot and change the time range, do any of the following tasks: 

        * To visually select the time range, click and drag on the plot horizontally. 
        * To select the time range, use the menu which is in the upper left of the console. 

     2. To reset the time range, select **Reset zoom**. 
     3. To display the output for all the queries at a specific point in time, hold the mouse cursor on the plot at that point. The query output displays in a pop-up box.
