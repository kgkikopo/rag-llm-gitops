# 4.2. View the topology of your application

You can navigate to the **Topology** view in the **Developer** perspective to see the status of application pods, access the application on a public URL, access the source code, and see the status of your last build. 

After you deploy an application, the **Graph view** opens automatically. You can zoom in and out to see more details for a particular application. 

The **Topology** view provides you the option to monitor your applications using the **List** view. Use the **List view** icon ( ![odc list view icon](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Building_applications-en-US/images/032596348862094372b7b78bde8be659/odc_list_view_icon.png) ) to see a list of all your applications and use the **Graph view** icon ( ![odc topology view icon](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Building_applications-en-US/images/512a1cd17c0c727218bc5ec50a992423/odc_topology_view_icon.png) ) to switch back to the graph view. 

You can customize the views as required using the following: 

  * Use the **Find by name** field to find the required components. Search results may appear outside of the visible area; click **Fit to Screen** from the lower-left toolbar to resize the **Topology** view to show all components. 
  * Use the **Display Options** drop-down list to configure the **Topology** view of the various application groupings. The options are available depending on the types of components deployed in the project: 

    * **Expand** group 

      * Virtual Machines: Toggle to show or hide the virtual machines. 
      * Application Groupings: Clear to condense the application groups into cards with an overview of an application group and alerts associated with it. 
      * Helm Releases: Clear to condense the components deployed as Helm Release into cards with an overview of a given release. 
      * Knative Services: Clear to condense the Knative Service components into cards with an overview of a given component. 
      * Operator Groupings: Clear to condense the components deployed with an Operator into cards with an overview of the given group. 

    * **Show** elements based on **Pod Count** or **Labels**

      * Pod Count: Select to show the number of pods of a component in the component icon. 
      * Labels: Toggle to show or hide the component labels. 




The **Topology** view also provides you the **Export application** option to download your application in the ZIP file format. You can then import the downloaded application to another project or cluster. For more details, see _Exporting an application to another project or cluster_ in the _Additional resources_ section.
