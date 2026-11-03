# 11.4. Filter the network traffic

The **Network Traffic** view provides query options and filtering parameters that let you optimize data searches, analyze specific log types, and manage directional traffic visibility. 

By default, the **Network Traffic** page displays the traffic flow data in the cluster based on the default filters configured in the `FlowCollector` instance. You can use the filter options to observe the required data by changing the preset filter. 

Alternatively, you can access the traffic flow data in the **Network Traffic** tab of the **Namespaces** , **Services** , **Routes** , **Nodes** , and **Workloads** pages which provide the filtered data of the corresponding aggregations. 

Query Options
    

You can use **Query Options** to optimize the search results, as listed below: 

  * **Log Type** : The available options **Conversation** and **Flows** provide the ability to query flows by log type, such as flow log, new conversation, completed conversation, and a heartbeat, which is a periodic record with updates for long conversations. A conversation is an aggregation of flows between the same peers. 
  * **Match filters** : You can determine the relation between different filter parameters selected in the advanced filter. The available options are **Match all** and **Match any**. **Match all** provides results that match all the values, and **Match any** provides results that match any of the values entered. The default value is **Match all**. 
  * **Datasource** : You can choose the datasource to use for queries: **Loki** , **Prometheus** , or **Auto**. Notable performance improvements can be realized when using Prometheus as a datasource rather than Loki, but Prometheus supports a limited set of filters and aggregations. The default datasource is **Auto** , which uses Prometheus on supported queries or uses Loki if the query does not support Prometheus. 
  * **Drops filter** : You can view different levels of dropped packets with the following query options: 

    * **Fully dropped** shows flow records with fully dropped packets. 
    * **Containing drops** shows flow records that contain drops but can be sent. 
    * **Without drops** shows records that contain sent packets. 
    * **All** shows all the aforementioned records. 

  * **Limit** : The data limit for internal backend queries. Depending upon the matching and the filter settings, the number of traffic flow data is displayed within the specified limit. 



Quick filters
     The default values in **Quick filters** drop-down menu are defined in the `FlowCollector` configuration. You can modify the options from console. 
Advanced filters
     You can set the advanced filters, **Common** , **Source** , or **Destination** , by selecting the parameter to be filtered from the dropdown list. The flow data is filtered based on the selection. To enable or disable the applied filter, you can click on the applied filter listed below the filter options. 

You can toggle between ![arrow up long solid](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Network_Observability-en-US/images/9dbbc83270dd7de4d8fb267e9172f7f3/arrow-up-long-solid.png) **One way** and ![arrow up long solid](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Network_Observability-en-US/images/9dbbc83270dd7de4d8fb267e9172f7f3/arrow-up-long-solid.png) ![arrow down long solid](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Network_Observability-en-US/images/4f8892ede40f2626cc2be02feb6a5954/arrow-down-long-solid.png) **Back and forth** filtering. The ![arrow up long solid](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Network_Observability-en-US/images/9dbbc83270dd7de4d8fb267e9172f7f3/arrow-up-long-solid.png) **One way** filter shows only **Source** and **Destination** traffic according to your filter selections. You can use **Swap** to change the directional view of the **Source** and **Destination** traffic. The ![arrow up long solid](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Network_Observability-en-US/images/9dbbc83270dd7de4d8fb267e9172f7f3/arrow-up-long-solid.png) ![arrow down long solid](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Network_Observability-en-US/images/4f8892ede40f2626cc2be02feb6a5954/arrow-down-long-solid.png) **Back and forth** filter includes return traffic with the **Source** and **Destination** filters. The directional flow of network traffic is shown in the **Direction** column in the Traffic flows table as `Ingress`or `Egress` for inter-node traffic and `Inner`for traffic inside a single node. 

You can click **Reset defaults** to remove the existing filters, and apply the filter defined in `FlowCollector` configuration. 

Note

To understand the rules of specifying the text value, click **Learn More**. 

**Additional resources**

  * [Configuring Quick Filters](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_observability/configuring-network-observability-operators#network-observability-config-quick-filters_network_observability "6.8. Configure quick filters")
  * [Flow Collector sample resource](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_observability/configuring-network-observability-operators#network-observability-flowcollector-view_network_observability "6.1. View the FlowCollector resource")
