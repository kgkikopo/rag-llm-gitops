# 1.2. Uninstalling the Kubernetes NMState Operator

Remove the Kubernetes NMState Operator and related resources when they are no longer needed. 

You can use the Operator Lifecycle Manager (OLM) to uninstall the Kubernetes NMState Operator, but by design OLM does not delete any associated custom resource definitions (CRDs), custom resources (CRs), or API Services. 

Before you uninstall the Kubernetes NMState Operator from the `Subcription` resource used by OLM, identify what Kubernetes NMState Operator resources to delete. This identification ensures that you can delete resources without impacting your running cluster. 

If you need to reinstall the Kubernetes NMState Operator, see "Installing the Kubernetes NMState Operator by using the CLI" or "Installing the Kubernetes NMState Operator by using the web console". 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 
  * You have installed the `jq` CLI tool. 
  * You are logged in as a user with `cluster-admin` privileges. 



**Procedure**

  1. Unsubscribe the Kubernetes NMState Operator from the `Subcription` resource by running the following command: 

```shell-session
$ oc delete --namespace openshift-nmstate subscription kubernetes-nmstate-operator
```


  2. Find the `ClusterServiceVersion` (CSV) resource that associates with the Kubernetes NMState Operator: 

```shell-session
$ oc get --namespace openshift-nmstate clusterserviceversion
```


**Example output that lists a CSV resource**

```shell-session
NAME                              	  DISPLAY                   	VERSION   REPLACES     PHASE
kubernetes-nmstate-operator.v4.22.0   Kubernetes NMState Operator   4.22.0           	   Succeeded
```


  3. Delete the CSV resource. After you delete the file, OLM deletes certain resources, such as `RBAC`, that it created for the Operator. 

```shell-session
$ oc delete --namespace openshift-nmstate clusterserviceversion kubernetes-nmstate-operator.v4.22.0
```


  4. Delete the `nmstate` CR and any associated `Deployment` resources by running the following commands: 

```shell-session
$ oc -n openshift-nmstate delete nmstate nmstate
```


```shell-session
$ oc delete --all deployments --namespace=openshift-nmstate
```


  5. After you deleted the `nmstate` CR, remove the `nmstate-console-plugin` console plugin name from the `console.operator.openshift.io/cluster` CR. 

     1. Store the position of the `nmstate-console-plugin` entry that exists among the list of enable plugins by running the following command. The following command uses the `jq` CLI tool to store the index of the entry in an environment variable named `INDEX`: 

```shell-session
INDEX=$(oc get console.operator.openshift.io cluster -o json | jq -r '.spec.plugins | to_entries[] | select(.value == "nmstate-console-plugin") | .key')
```


     2. Remove the `nmstate-console-plugin` entry from the `console.operator.openshift.io/cluster` CR by running the following patch command: 

```shell-session
$ oc patch console.operator.openshift.io cluster --type=json -p "[{\"op\": \"remove\", \"path\": \"/spec/plugins/$INDEX\"}]"
```


        * `INDEX` is an auxiliary variable. You can specify a different name for this variable. 

  6. Optional: To preserve CR instances so that you can restore them after you delete CRDs, enter the following command: 

```shell-session
$ oc get -A nncp -o yaml > cluster-nncp.yaml
```


Important

To reuse preserved CRs, such as NNCPs, you must uninstall the Kubernetes NMState Operator, reinstall the Kubernetes NMState Operator, and then run the following command to restore the CRs: 

```shell-session
$ oc apply -f cluster-nncp.yaml
```


  7. Delete all the CRDs, such as `nmstates.nmstate.io`, by running the following commands: 

```shell-session
$ oc delete crd nmstates.nmstate.io
```


```shell-session
$ oc delete crd nodenetworkconfigurationenactments.nmstate.io
```


```shell-session
$ oc delete crd nodenetworkstates.nmstate.io
```


```shell-session
$ oc delete crd nodenetworkconfigurationpolicies.nmstate.io
```


  8. Delete the namespace: 

```shell-session
$ oc delete namespace openshift-nmstate
```
