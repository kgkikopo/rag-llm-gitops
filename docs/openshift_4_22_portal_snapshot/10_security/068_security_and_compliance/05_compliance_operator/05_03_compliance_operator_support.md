# 5.3. Compliance Operator support

You can find support resources for the Compliance Operator, including lifecycle information, general support procedures, and troubleshooting tools. 

## 5.3.1. Compliance Operator lifecycle

The Compliance Operator is a "Rolling Stream" Operator, meaning updates are available asynchronously of OpenShift Container Platform releases. For more information, see "OpenShift Operator Life Cycles" on the Red Hat Customer Portal. 

## 5.3.2. Get support

Red Hat offers several support channels to help you troubleshoot issues and get the most from OpenShift Container Platform. 

From the Red Hat Customer Portal, you can: 

  * Search or browse through the Red Hat Knowledgebase of articles and solutions about Red Hat products. 
  * Submit a support case to Red Hat Support. 
  * Access other product documentation. 



To identify issues with your cluster, you can use Red Hat Lightspeed in [OpenShift Cluster Manager](https://console.redhat.com/openshift). Red Hat Lightspeed provides details about issues and, if available, information about how to solve a problem. 

To suggest improvements or report errors, give specific details such as the section name and OpenShift Container Platform version. 

## 5.3.3. Using the must-gather tool for the Compliance Operator

You can collect detailed Compliance Operator configuration and logs by using the must-gather tool to aid in troubleshooting issues and support case resolution. 

Starting in Compliance Operator v1.6.0, you can collect data about the Compliance Operator resources by running the `must-gather` command with the Compliance Operator image. 

Note

Consider using the `must-gather` tool when opening support cases or filing bug reports, as it provides additional details about the Operator configuration and logs. 

**Procedure**

  * Run the following command to collect data about the Compliance Operator: 

```shell-session
$ oc adm must-gather --image=$(oc get csv compliance-operator.v1.6.0 -o=jsonpath='{.spec.relatedImages[?(@.name=="must-gather")].image}')
```


## 5.3.4. Additional resources

  * [About the must-gather tool](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/support/#about-must-gather_gathering-cluster-data)
  * [OpenShift Operator Life Cycles](https://access.redhat.com/support/policy/updates/openshift_operators)
  * [Product Compliance](https://access.redhat.com/compliance)
