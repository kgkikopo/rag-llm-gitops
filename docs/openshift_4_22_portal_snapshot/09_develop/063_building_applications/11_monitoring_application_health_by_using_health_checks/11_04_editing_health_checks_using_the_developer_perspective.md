# 11.4. Editing health checks using the Developer perspective

You can edit, remove, or add readiness, liveness, and startup probes on a deployed application from the **Topology** view in the **Developer** perspective. Use the **Edit Health Checks** page to update probe parameters, remove probes, or add new probe types. 

**Prerequisites**

  * You have switched to the **Developer** perspective in the web console. 
  * You have created and deployed an application on OpenShift Container Platform using the **Developer** perspective. 
  * You have added health checks to your application. 



**Procedure**

  1. In the **Topology** view, right-click your application and select **Edit Health Checks**. Alternatively, in the side panel, click the **Actions** drop-down list and select **Edit Health Checks**. 
  2. To remove a previously added health probe, click the **Remove** icon adjoining it. 
  3. To edit the parameters of an existing probe: 

     1. Click the **Edit Probe** link next to a previously added probe to see the parameters for the probe. 
     2. Modify the parameters as required, and click the check mark to save your changes. 

  4. To add a new health probe, click the add probe links. For example, to add a liveness probe that checks if your container is running: 

     1. Click **Add Liveness Probe** to see a form containing the parameters for the probe. 
     2. Edit the probe parameters as required. 

Note

The `Timeout` value must be lower than the `Period` value. The `Timeout` default value is `1`. The `Period` default value is `10`. 

     3. Click the check mark at the bottom of the form. The **Liveness Probe Added** message is displayed. 

  5. Click **Save** to save your modifications and add the additional probes to your container. You are redirected to the **Topology** view. 



**Verification**

  1. In the side panel, verify that the probes have been added by clicking on the deployed pod under the **Pods** section. 
  2. In the **Pod Details** page, click the listed container in the **Containers** section. 
  3. In the **Container Details** page, verify that the Liveness probe - `HTTP Get 10.129.4.65:8080/` has been added to the container, in addition to the earlier existing probes.
