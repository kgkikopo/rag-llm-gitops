# 2.26. Troubleshooting Envoy proxy

The Envoy proxy intercepts all inbound and outbound traffic for all services in the service mesh. Envoy also collects and reports telemetry on the service mesh. Envoy is deployed as a sidecar to the relevant service in the same pod. 

## 2.26.1. Enabling Envoy access logs

Envoy access logs are useful in diagnosing traffic failures and flows, and help with end-to-end traffic flow analysis. 

To enable access logging for all istio-proxy containers, edit the `ServiceMeshControlPlane` (SMCP) object to add a file name for the logging output. 

**Procedure**

  1. Log in to the OpenShift Container Platform CLI as a user with the cluster-admin role. Enter the following command. Then, enter your username and password when prompted. 

```shell-session
$ oc login --username=<NAMEOFUSER> https://<HOSTNAME>:6443
```


  2. Change to the project where you installed the Service Mesh control plane, for example `istio-system`. 

```shell-session
$ oc project istio-system
```


  3. Edit the `ServiceMeshControlPlane` file. 

```shell-session
$ oc edit smcp <smcp_name>
```


  4. As show in the following example, use `name` to specify the file name for the proxy log. If you do not specify a value for `name`, no log entries will be written. 

```yaml
apiVersion: maistra.io/v2
kind: ServiceMeshControlPlane
metadata:
  name: basic
  namespace: istio-system
spec:
  proxy:
    accessLogging:
      file:
        name: /dev/stdout     #file name
```


For more information about troubleshooting pod issues, see [Investigating pod issues](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/support/#investigating-pod-issues-1)

## 2.26.2. Get support

Red Hat offers several support channels to help you troubleshoot issues and get the most from OpenShift Container Platform. 

From the Red Hat Customer Portal, you can: 

  * Search or browse through the Red Hat Knowledgebase of articles and solutions about Red Hat products. 
  * Submit a support case to Red Hat Support. 
  * Access other product documentation. 



To identify issues with your cluster, you can use Red Hat Lightspeed in [OpenShift Cluster Manager](https://console.redhat.com/openshift). Red Hat Lightspeed provides details about issues and, if available, information about how to solve a problem. 

To suggest improvements or report errors, give specific details such as the section name and OpenShift Container Platform version. 

### 2.26.2.1. About the Red Hat Knowledgebase

The Red Hat Knowledgebase helps you get the most from Red Hat products and technologies. 

It includes articles, product documentation, and videos that outline best practices for installing, configuring, and using Red Hat products. You can also search for solutions to known issues. Each solution has a root cause description and steps to fix the problem. 

**Additional resources**

  * [Red Hat Knowledgebase](https://access.redhat.com/knowledgebase)



### 2.26.2.2. Search the Red Hat Knowledgebase

Search the Red Hat Knowledgebase to find solutions to known issues and resolve problems quickly without opening a support case. 

**Prerequisites**

  * You have a Red Hat Customer Portal account. 



**Procedure**

  1. Log in to the [Red Hat Customer Portal](http://access.redhat.com). 
  2. Click **Search**. 
  3. In the search field, input keywords and strings relating to the problem, including: 

     * OpenShift Container Platform components (such as **etcd**) 
     * Related procedure (such as **installation**) 
     * Warnings, error messages, and other outputs related to explicit failures 

  4. Click the **Enter** key. 
  5. Optional: Select the **OpenShift Container Platform** product filter. 
  6. Optional: Select the **Documentation** content type filter. 



### 2.26.2.3. About collecting service mesh data

You can use the `oc adm must-gather` CLI command to collect information about your cluster, including features and objects associated with Red Hat OpenShift Service Mesh. 

**Prerequisites**

  * Access to the cluster as a user with the `cluster-admin` role. 
  * The OpenShift Container Platform CLI (`oc`) installed. 



**Procedure**

  1. To collect Red Hat OpenShift Service Mesh data with `must-gather`, you must specify the Red Hat OpenShift Service Mesh image. 

```shell-session
$ oc adm must-gather --image=registry.redhat.io/openshift-service-mesh/istio-must-gather-rhel8:2.6
```


  2. To collect Red Hat OpenShift Service Mesh data for a specific Service Mesh control plane namespace with `must-gather`, you must specify the Red Hat OpenShift Service Mesh image and namespace. In this example, after `gather,` replace `<namespace>` with your Service Mesh control plane namespace, such as `istio-system`. 

```shell-session
$ oc adm must-gather --image=registry.redhat.io/openshift-service-mesh/istio-must-gather-rhel8:2.6 gather <namespace>
```


This creates a local directory that contains the following items: 

     * The Istio Operator namespace and its child objects 
     * All control plane namespaces and their children objects 
     * All namespaces and their children objects that belong to any service mesh 
     * All Istio custom resource definitions (CRD) 
     * All Istio CRD objects, such as VirtualServices, in a given namespace 
     * All Istio webhooks 




For prompt support, supply diagnostic information for both OpenShift Container Platform and Red Hat OpenShift Service Mesh. 

### 2.26.2.4. Submitting a support case

If you cannot resolve an OpenShift Container Platform issue by using the Red Hat Knowledgebase, submit a support case to get direct help from Red Hat Support. 

**Prerequisites**

  * You have access to the cluster as a user with the `cluster-admin` role. 
  * You have installed the OpenShift CLI (`oc`). 
  * You have a Red Hat Customer Portal account. 
  * You have a Red Hat Standard or Premium subscription. 



**Procedure**

  1. Log in to [the **Customer Support** page](https://access.redhat.com/support/cases/#/case/list) of the Red Hat Customer Portal. 
  2. Click **Get support**. 
  3. On the **Cases** tab of the **Customer Support** page: 

     1. Optional: Change the pre-filled account and owner details if needed. 
     2. Select the appropriate category for your issue, such as **Bug or Defect** , and click **Continue**. 

  4. Enter the following information: 

     1. In the **Summary** field, enter a concise but descriptive problem summary and further details about the symptoms that you experience and your expectations. 
     2. Select **OpenShift Container Platform** from the **Product** drop-down menu. 
     3. Select **4.22** from the **Version** drop-down. 

  5. Review the list of suggested Red Hat Knowledgebase solutions for a potential match against the problem that you are reporting. If the suggested articles do not address the issue, click **Continue**. 
  6. Review the updated list of suggested Red Hat Knowledgebase solutions for a potential match against the problem that you are reporting. The list updates as you give more information during the case creation process. If the suggested articles do not address the issue, click **Continue**. 
  7. Ensure that the account information presented is as expected, and if not, change it as needed. 
  8. Check that the autofilled OpenShift Container Platform Cluster ID is correct. If it is not, manually obtain your cluster ID. 

     * To manually obtain your cluster ID using the OpenShift Container Platform web console: 

       1. Navigate to **Home** **Overview**. 
       2. Find the value in the **Cluster ID** field of the **Details** section. 

     * Or, open a new support case from the OpenShift Container Platform web console, which automatically fills in your cluster ID. 

       1. From the toolbar, navigate to **(?) Help** **Open Support Case**. 
       2. The **Cluster ID** value automatically fills in. 

     * To obtain your cluster ID using the OpenShift CLI (`oc`), run the following command: 

```shell-session
$ oc get clusterversion -o jsonpath='{.items[].spec.clusterID}{"\n"}'
```


  9. Complete the following questions where prompted and then click **Continue** : 

     * What are you experiencing? What are you expecting to happen? 
     * Define the value or impact to you or the business. 
     * Where are you experiencing this behavior? What environment? 
     * When does this behavior occur? Frequency? Repeatedly? At certain times? 

  10. Upload relevant diagnostic data files and click **Continue**. Red Hat recommends including data gathered by using the `oc adm must-gather` command as a starting point, plus any issue-specific data that the command does not collect. 
  11. Input relevant case management details and click **Continue**. 
  12. Preview the case details and click **Submit**.
