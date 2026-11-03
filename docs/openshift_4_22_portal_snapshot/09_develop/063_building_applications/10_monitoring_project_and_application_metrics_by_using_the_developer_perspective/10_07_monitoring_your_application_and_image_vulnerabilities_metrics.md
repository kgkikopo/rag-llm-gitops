# 10.7. Monitoring your application and image vulnerabilities metrics

Analyze application dependency vulnerabilities across your cluster to identify and remediate security issues in container images. 

After you create applications in your project and deploy them, use the **Developer** perspective in the web console to see the metrics for your application dependency vulnerabilities across your cluster. The metrics help you to analyze the following image vulnerabilities in detail: 

  * Total count of vulnerable images in a selected project 
  * Severity-based counts of all vulnerable images in a selected project 
  * Drill down into severity to obtain the details, such as count of vulnerabilities, count of fixable vulnerabilities, and number of affected pods for each vulnerable image 



**Prerequisites**

  * You have installed the Red Hat Quay Container Security Operator. 

Note

The Red Hat Quay Container Security Operator detects vulnerabilities by scanning the images that are in the Red Hat Quay registry. 




**Procedure**

  1. In the **Developer** perspective, click **Project** to open the project dashboard. 
  2. For a detailed vulnerabilities overview, click the **Vulnerabilities** tab. 

     1. To get more detail about an image, click its name. 
     2. View the default graph with all types of vulnerabilities in the **Details** tab. 
     3. Optional: Click the toggle button to view a specific type of vulnerability. For example, click **App dependency** to see vulnerabilities specific to application dependency. 
     4. Optional: You can filter the list of vulnerabilities based on their **Severity** and **Type** or sort them by **Severity** , **Package** , **Type** , **Source** , **Current Version** , and **Fixed in Version**. 
     5. Click a **Vulnerability** to get its associated details: 

        * **Base image** vulnerabilities display information from a Red Hat Security Advisory (RHSA). 
        * **App dependency** vulnerabilities display information from the Snyk security application.
