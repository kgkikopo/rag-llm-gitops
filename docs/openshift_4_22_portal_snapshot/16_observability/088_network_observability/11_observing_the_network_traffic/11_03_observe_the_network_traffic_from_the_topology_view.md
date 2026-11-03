# 11.3. Observe the network traffic from the Topology view

Use the **Topology** view in the **Network Traffic** page to visualize network flows, track traffic volume, and monitor relationships across cluster components. 

The visualization represents network entities as nodes and traffic flows as edges. By selecting individual components within the graph, you can access a side panel containing specific metrics and health details for that resource. This interactive approach allows for rapid identification of traffic patterns and connectivity issues within the cluster. 

To manage complex environments, the **Topology** view includes advanced configuration options that allow you to customize the layout and data density. You can adjust the **Scope** of the view, apply **Groups** to represent resource ownership, and choose different **Layout** algorithms to optimize the graphical display. Additionally, you can enable **Edge labels** to show real-time measurements, such as the average byte rate, directly on the flow lines. 

For reporting or external analysis, the **Topology** view provides an export feature. You can download the current graphical representation as a PNG image or generate a direct link to the specific view configuration to share with other administrators. These tools ensure that network insights are both accessible and easily documented. 

## 11.3.1. Work with the Topology view

Access the **Topology** view to visually inspect cluster network relationships and select individual components to view detailed traffic metrics and metadata. 

As an administrator, you can navigate to the **Topology** view to see the details and metrics of the component. 

**Prerequisites**

  * You have administrator access. 



**Procedure**

  1. Navigate to **Observe** **Network Traffic**. 
  2. In the **Network Traffic** page, click the **Topology** tab. 
  3. Click each component in the **Topology** tab to view its details and metrics. 



## 11.3.2. Configure the advanced options for the Topology view

The **Topology** view provides advanced options that let you customize display settings, configure component grouping and layouts, and export the network graph as an image. 

You can customize and export the view by using **Show advanced options**. The advanced options view has the following features: 

  * **Find in view** : To search the required components in the view. 
  * **Display options** : To configure the following options: 

    * **Edge labels** : To show the specified measurements as edge labels. The default is to show the **Average rate** in **Bytes**. 
    * **Scope** : To select the scope of components between which the network traffic flows. The default value is **Namespace**. 
    * **Groups** : To enhance the understanding of ownership by grouping the components. The default value is **None**. 
    * **Layout** : To select the layout of the graphical representation. The default value is **ColaNoForce**. 
    * **Show** : To select the details that need to be displayed. All the options are checked by default. The options available are: **Edges** , **Edges label** , and **Badges**. 
    * **Truncate labels** : To select the required width of the label from the drop-down list. The default value is **M**. 
    * **Collapse groups** : To expand or collapse the groups. The groups are expanded by default. This option is disabled if **Groups** has the value of **None**. 




### 11.3.2.1. Exporting the topology view

To export the view, click **Export topology view**. The view is downloaded in PNG format.
