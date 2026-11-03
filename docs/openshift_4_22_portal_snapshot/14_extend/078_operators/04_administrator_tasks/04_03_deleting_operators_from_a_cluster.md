# 4.3. Deleting Operators from a cluster

You can delete Operators that were previously installed with Operator Lifecycle Manager (OLM) on your OpenShift Container Platform cluster. 

Important

You must successfully and completely uninstall an Operator prior to attempting to reinstall the same Operator. Failure to fully uninstall the Operator properly can leave resources, such as a project or namespace, stuck in a "Terminating" state and cause "error resolving resource" messages to be observed when trying to reinstall the Operator. 

For more information, see "Reinstalling Operators after failed uninstallation". 

## 4.3.1. Deleting Operators from a cluster using the web console

Cluster administrators can delete installed Operators from a selected namespace by using the web console. 

Warning

Failed Operator installations do not automatically remove created permissions. Audit and remove remaining permissions to secure the namespace. 

For more information, see [Audit and secure delegated Operator installations (Red Hat Knowledgebase)](https://access.redhat.com/articles/7149230). 

**Prerequisites**

  * You have access to the OpenShift Container Platform cluster web console using an account with `cluster-admin` permissions. 



**Procedure**

  1. Navigate to the **Ecosystem** **Installed Operators** page. 
  2. Scroll or enter a keyword into the **Filter by name** field to find the Operator that you want to remove. Then, click on it. 
  3. On the right side of the **Operator Details** page, select **Uninstall Operator** from the **Actions** list. 

An **Uninstall Operator?** dialog box is displayed. 

  4. Select **Uninstall** to remove the Operator, Operator deployments, and pods. Following this action, the Operator stops running and no longer receives updates. 

Note

This action does not remove resources managed by the Operator, including custom resource definitions (CRDs) and custom resources (CRs). Dashboards and navigation items enabled by the web console and off-cluster resources that continue to run might need manual clean up. To remove these after uninstalling the Operator, you might need to manually delete the Operator CRDs. 




## 4.3.2. Deleting Operators from a cluster using the CLI

To remove an installed Operator from a namespace, cluster administrators can delete its subscription and cluster service version (CSV) by using the CLI. 

Warning

Failed Operator installations do not automatically remove created permissions. Audit and remove remaining permissions to secure the namespace. 

For more information, see [Audit and secure delegated Operator installations (Red Hat Knowledgebase)](https://access.redhat.com/articles/7149230). 

**Prerequisites**

  * You have access to the OpenShift Container Platform cluster using an account with `cluster-admin` permissions. 
  * The OpenShift CLI (`oc`) is installed on your workstation. 



**Procedure**

  1. Ensure the latest version of the subscribed operator (for example, `serverless-operator`) is identified in the `currentCSV` field. 

```shell-session
$ oc get subscription.operators.coreos.com serverless-operator -n openshift-serverless -o yaml | grep currentCSV
```


**Example output**

```shell-session
  currentCSV: serverless-operator.v1.28.0
```


  2. Delete the subscription (for example, `serverless-operator`): 

```shell-session
$ oc delete subscription.operators.coreos.com serverless-operator -n openshift-serverless
```


**Example output**

```shell-session
subscription.operators.coreos.com "serverless-operator" deleted
```


  3. Delete the CSV for the Operator in the target namespace using the `currentCSV` value from the previous step: 

```shell-session
$ oc delete clusterserviceversion serverless-operator.v1.28.0 -n openshift-serverless
```


**Example output**

```shell-session
clusterserviceversion.operators.coreos.com "serverless-operator.v1.28.0" deleted
```


## 4.3.3. Refreshing failing subscriptions

In Operator Lifecycle Manager (OLM), if you subscribe to an Operator that references images that are not accessible on your network, you can find jobs in the `openshift-marketplace` namespace that are failing with the following errors: 

```shell-session
ImagePullBackOff for
Back-off pulling image "example.com/openshift4/ose-elasticsearch-operator-bundle@sha256:6d2587129c846ec28d384540322b40b05833e7e00b25cca584e004af9a1d292e"
```


```shell-session
rpc error: code = Unknown desc = error pinging docker registry example.com: Get "https://example.com/v2/": dial tcp: lookup example.com on 10.0.0.1:53: no such host
```


As a result, the subscription is stuck in this failing state and the Operator is unable to install or upgrade. 

You can refresh a failing subscription by deleting the subscription, cluster service version (CSV), and other related objects. After recreating the subscription, OLM then reinstalls the correct version of the Operator. 

**Prerequisites**

  * You have a failing subscription that is unable to pull an inaccessible bundle image. 
  * You have confirmed that the correct bundle image is accessible. 



**Procedure**

  1. Get the names of the `Subscription` and `ClusterServiceVersion` objects from the namespace where the Operator is installed: 

```shell-session
$ oc get sub,csv -n <namespace>
```


**Example output**

```shell-session
NAME                                                       PACKAGE                  SOURCE             CHANNEL
subscription.operators.coreos.com/elasticsearch-operator   elasticsearch-operator   redhat-operators   5.0

NAME                                                                         DISPLAY                            VERSION    REPLACES   PHASE
clusterserviceversion.operators.coreos.com/elasticsearch-operator.5.0.0-65   OpenShift Elasticsearch Operator   5.0.0-65              Succeeded
```


  2. Delete the subscription: 

```shell-session
$ oc delete subscription <subscription_name> -n <namespace>
```


  3. Delete the cluster service version: 

```shell-session
$ oc delete csv <csv_name> -n <namespace>
```


  4. Get the names of any failing jobs and related config maps in the `openshift-marketplace` namespace: 

```shell-session
$ oc get job,configmap -n openshift-marketplace
```


**Example output**

```shell-session
NAME                                                                        COMPLETIONS   DURATION   AGE
job.batch/1de9443b6324e629ddf31fed0a853a121275806170e34c926d69e53a7fcbccb   1/1           26s        9m30s

NAME                                                                        DATA   AGE
configmap/1de9443b6324e629ddf31fed0a853a121275806170e34c926d69e53a7fcbccb   3      9m30s
```


  5. Delete the job: 

```shell-session
$ oc delete job <job_name> -n openshift-marketplace
```


This ensures pods that try to pull the inaccessible image are not recreated. 

  6. Delete the config map: 

```shell-session
$ oc delete configmap <configmap_name> -n openshift-marketplace
```


  7. Reinstall the Operator using the software catalog in the web console. 



**Verification**

  * Check that the Operator has been reinstalled successfully: 

```shell-session
$ oc get sub,csv,installplan -n <namespace>
```


**Additional resources**

  * [Reinstalling Operators after failed uninstallation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/administrator-tasks#olm-reinstall_olm-troubleshooting-operator-issues "4.12.8. Reinstalling Operators after failed uninstallation")
