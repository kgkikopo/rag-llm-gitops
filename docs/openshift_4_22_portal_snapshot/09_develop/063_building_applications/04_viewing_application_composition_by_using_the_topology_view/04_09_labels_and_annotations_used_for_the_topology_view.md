# 4.9. Labels and annotations used for the Topology view

The **Topology** view uses labels and annotations to display icons, source links, node connectors, and application groupings on the topology graph. 

The **Topology** view uses the following labels and annotations: 

Icon displayed in the node
     Icons in the node are defined by looking for matching icons using the `app.openshift.io/runtime` label, followed by the `app.kubernetes.io/name` label. This matching is done using a predefined set of icons. 
Link to the source code editor or the source
     The `app.openshift.io/vcs-uri` annotation is used to create links to the source code editor. 
Node Connector
     The `app.openshift.io/connects-to` annotation is used to connect the nodes. 
App grouping
     The `app.kubernetes.io/part-of=<appname>` label is used to group the applications, services, and components. 

**Additional resources**

  * [Guidelines for labels and annotations for OpenShift applications](https://github.com/redhat-developer/app-labels/blob/master/labels-annotation-for-openshift.adoc)
