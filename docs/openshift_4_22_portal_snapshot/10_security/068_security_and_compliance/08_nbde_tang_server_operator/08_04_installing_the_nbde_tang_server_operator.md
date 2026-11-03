# 8.4. Installing the NBDE Tang Server Operator

You can install the NBDE Tang Operator either by using the web console or through the `oc` command from CLI. 

## 8.4.1. Install the NBDE Tang Server Operator using the web console

You can install the NBDE Tang Server Operator from the software catalog using the web console. 

**Prerequisites**

  * You must have `cluster-admin` privileges on an OpenShift Container Platform cluster. 



**Procedure**

  1. In the OpenShift Container Platform web console, navigate to **Ecosystem** **Software Catalog**. 
  2. Search for the NBDE Tang Server Operator: 

![NBDE Tang Server Operator in the software catalog](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Security_and_compliance-en-US/images/83c00746ec22ba3d557d58787e60f06d/nbde-tang-server-operator-01-operatorhub.png) ![NBDE Tang Server Operator in the software catalog](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Security_and_compliance-en-US/images/83c00746ec22ba3d557d58787e60f06d/nbde-tang-server-operator-01-operatorhub.png)

  3. Click **Install**. 
  4. On the **Operator Installation** screen, keep the **Update channel** , **Version** , **Installation mode** , **Installed Namespace** , and **Update approval** fields on the default values. 
  5. After you confirm the installation options by clicking **Install** , the console displays the installation confirmation. 

![Confirmation of a NBDE Tang Server Operator installation](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Security_and_compliance-en-US/images/99b80a9d09455aeb0362604c65210ff6/nbde-tang-server-operator-03-confirmation.png) ![Confirmation of a NBDE Tang Server Operator installation](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Security_and_compliance-en-US/images/99b80a9d09455aeb0362604c65210ff6/nbde-tang-server-operator-03-confirmation.png)




**Verification**

  1. Navigate to the **Ecosystem** **Installed Operators** page. 
  2. Check that the NBDE Tang Server Operator is installed and its status is `Succeeded`. 

![NBDE Tang Server Operator status](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Security_and_compliance-en-US/images/89689feb45b48b9e83f858f6198bddd0/nbde-tang-server-operator-05-succeeded.png) ![NBDE Tang Server Operator status](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Security_and_compliance-en-US/images/89689feb45b48b9e83f858f6198bddd0/nbde-tang-server-operator-05-succeeded.png)




## 8.4.2. Install the NBDE Tang Server Operator using CLI

You can install the NBDE Tang Server Operator from the software catalog using the CLI. 

**Prerequisites**

  * You must have `cluster-admin` privileges on an OpenShift Container Platform cluster. 
  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  1. Use the following command to list available Operators in the software catalog, and limit the output to Tang-related results: 

```shell-session
$ oc get packagemanifests -n openshift-marketplace | grep tang
```


**Example output**

```shell-session
tang-operator           Red Hat
```


In this case, the corresponding packagemanifest name is `tang-operator`. 

  2. Create a `Subscription` object YAML file to subscribe a namespace to the NBDE Tang Server Operator, for example, `tang-operator.yaml`: 

**Example subscription YAML for tang-operator**

```yaml
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: tang-operator
  namespace: openshift-operators
spec:
  channel: stable
  installPlanApproval: Automatic
  name: tang-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace
```


where: 

`spec.channel`
     Specifies the channel name from where you want to subscribe the Operator. 
`spec.name`
     Specifies the name of the Operator to subscribe to. 
`spec.source`
     Specifies the name of the CatalogSource that provides the Operator. 
`spec.sourceNamespace`
     Specifies the namespace of the CatalogSource. Use `openshift-marketplace` for the default software catalog sources. 

  3. Apply the `Subscription` to the cluster: 

```shell-session
$ oc apply -f tang-operator.yaml
```


**Verification**

  * Check that the NBDE Tang Server Operator controller runs in the `openshift-operators` namespace: 

```shell-session
$ oc -n openshift-operators get pods
```


**Example output**

```shell-session
NAME                                                READY   STATUS    RESTARTS   AGE
tang-operator-controller-manager-694b754bd6-4zk7x   2/2     Running   0          12s
```
