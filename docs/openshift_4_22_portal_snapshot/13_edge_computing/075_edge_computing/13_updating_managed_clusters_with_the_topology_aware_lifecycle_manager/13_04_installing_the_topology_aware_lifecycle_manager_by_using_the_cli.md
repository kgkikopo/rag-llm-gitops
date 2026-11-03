# 13.4. Installing the Topology Aware Lifecycle Manager by using the CLI

You can use the OpenShift CLI (`oc`) to install the Topology Aware Lifecycle Manager (TALM). 

**Prerequisites**

  * Install the OpenShift CLI (`oc`). 
  * Install the latest version of the RHACM Operator. 
  * TALM requires RHACM 2.9 or later. 
  * Set up a hub cluster with disconnected registry. 
  * Log in as a user with `cluster-admin` privileges. 



**Procedure**

  1. Create a `Subscription` CR: 

     1. Define the `Subscription` CR and save the YAML file, for example, `talm-subscription.yaml`: 

```yaml
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: openshift-topology-aware-lifecycle-manager-subscription
  namespace: openshift-operators
spec:
  channel: "stable"
  name: topology-aware-lifecycle-manager
  source: redhat-operators
  sourceNamespace: openshift-marketplace
```


     2. Create the `Subscription` CR by running the following command: 

```shell-session
$ oc create -f talm-subscription.yaml
```


**Verification**

  1. Verify that the installation succeeded by inspecting the CSV resource: 

```shell-session
$ oc get csv -n openshift-operators
```


**Example output**

```shell-session
NAME                                                   DISPLAY                            VERSION               REPLACES                           PHASE
topology-aware-lifecycle-manager.4.22.x   Topology Aware Lifecycle Manager   4.22.x                                      Succeeded
```


  2. Verify that the TALM is up and running: 

```shell-session
$ oc get deploy -n openshift-operators
```


**Example output**

```shell-session
NAMESPACE                                          NAME                                             READY   UP-TO-DATE   AVAILABLE   AGE
openshift-operators                                cluster-group-upgrades-controller-manager        1/1     1            1           14s
```
