# 3.4. Submitting a support case

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
