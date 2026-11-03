# 11.1. Observe the network traffic from the Overview view

Use the Network Traffic **Overview** view to monitor aggregated flow metrics, troubleshoot cluster connectivity, and detect unusual traffic patterns. 

The **Overview** view shows aggregate network traffic in your OpenShift Container Platform cluster, allowing you to see which applications are communicating and the volume of data being transferred. It provides detailed insights by source, destination, and flow type, along with the top traffic flows and average byte rates. 

As an administrator, you can troubleshoot connectivity issues, detect unusual traffic patterns, and optimize application performance. It provides a quick overview of network behavior, making it easier to prioritize actions and ensure efficient resource usage. 

## 11.1.1. Advanced options for the Overview view

Customize the network traffic **Overview** view by configuring advanced options, such as graph scope, label truncation, and panel management, to refine the display of flow rate statistics and traffic data. 

To access the advanced options, click **Show advanced options**. You can configure the details in the graph by using the **Display options** drop-down menu. The options available are as follows: 

  * **Scope** : Select to view the components that network traffic flows between. You can set the scope to **Node** , **Namespace** , **Owner** , **Zones** , **Cluster** , or **Resource**. **Owner** is an aggregation of resources. **Resource** can be a pod, service, node, in case of host-network traffic, or an unknown IP address. The default value is **Namespace**. 
  * **Truncate labels** : Select the required width of the label from the drop-down list. The default value is **M**. 



### 11.1.1.1. Accessing feature-specific data with preconfigured views

When specific network observability features are enabled, you can select preconfigured feature views that automatically display relevant panels and columns for that feature. 

Feature views reduce the number of clicks required to access feature-specific data. 

The following feature views are available when their corresponding features are enabled: 

  * **Packet Drops** :: Displays packet drop panels and columns for analyzing network packet loss when packet drop tracking is enabled. 
  * **DNS** :: Displays DNS tracking panels such as DNS response codes, DNS latencies, and DNS-specific columns when DNS tracking is enabled. 
  * **Flow RTT** :: Displays round-trip time (RTT) metrics and related panels when RTT tracking is enabled. 
  * **TLS Tracking** :: Displays TLS monitoring panels and TLS-specific columns when TLS tracking is enabled. 
  * **UDN** :: Displays user-defined network mapping panels and columns when UDN is enabled. 
  * **Network Events** :: Displays network events panels and columns when network events are enabled. 
  * **Packet Translation** :: Displays packet translation analysis panels and columns when packet translation is enabled. 



When you change columns or panels in a feature view, the view name changes to **Custom** to indicate customization. To restore the default feature view configuration, click **Restore defaults** in the **Manage columns** or **Manage panels** dialog. 

Note

Preconfigured feature views are only available when the corresponding feature is enabled in the `FlowCollector` custom resource. 

### 11.1.1.2. Panels and display management

You can select the required panels to be displayed, reorder them, and focus on a specific panel. To add or remove panels, click **Manage panels**. 

When using a preconfigured feature view, the panels displayed by default are specific to that feature. Changing the panel configuration changes the view to **Custom**. 

The following panels are shown by default: 

  * **Top X average bytes rates**
  * **Top X bytes rates stacked with total**



Other panels can be added in **Manage panels** : 

  * **Top X average packets rates**
  * **Top X packets rates stacked with total**



**Query options** allows you to choose whether to show the **Top 5** , **Top 10** , or **Top 15** rates. 

## 11.1.2. Work with the Overview view

Navigate to the network traffic **Overview** view in the OpenShift Container Platform console to visualize flow rate statistics and customize the display scope for monitoring cluster network activity. 

**Prerequisite**

  * Access to the cluster with administrator rights. 



**Procedure**

  1. Navigate to **Observe** **Network Traffic**. 
  2. In the **Network Traffic** page, click the **Overview** tab. 
  3. Optional: When analyzing specific network features, select a preconfigured feature view from the view selector to instantly display feature-specific panels and columns. 
  4. Click the menu icon to configure the scope of each flow rate data. 



## 11.1.3. Packet drop tracking

Monitor and analyze network packet loss by using eBPF-based packet drop tracking, which identifies drop locations, detects host or OVS-specific drop reasons, and provides dedicated graphical panels in the **Overview** view. 

You can configure graphical representation of network flow records with packet loss in the **Overview** view. By employing eBPF tracepoint hooks, you can gain valuable insights into packet drops for TCP, UDP, SCTP, ICMPv4, and ICMPv6 protocols, which can result in the following actions: 

  * Identification: Pinpoint the exact locations and network paths where packet drops are occurring. Determine whether specific devices, interfaces, or routes are more prone to drops. 
  * Root cause analysis: Examine the data collected by the eBPF program to understand the causes of packet drops. For example, are they a result of congestion, buffer issues, or specific network events? 
  * Performance optimization: With a clearer picture of packet drops, you can take steps to optimize network performance, such as adjust buffer sizes, reconfigure routing paths, or implement Quality of Service (QoS) measures. 



### 11.1.3.1. Packet Drops feature view

When packet-drop tracking is enabled, you can select the **Packet Drops** preconfigured feature view from the view selector in the **Network Traffic** page. This view automatically displays packet drop-specific panels and columns, simplifying packet drop analysis without manual configuration. 

When packet drop tracking is enabled, you can see the following panels in the **Overview** by default: 

  * **Top X packet dropped state stacked with total**
  * **Top X packet dropped cause stacked with total**
  * **Top X average dropped packets rates**
  * **Top X dropped packets rates stacked with total**



Other packet drop panels are available to add in **Manage panels** : 

  * **Top X average dropped bytes rates**
  * **Top X dropped bytes rates stacked with total**



### 11.1.3.2. Types of packet drops

Two kinds of packet drops are detected by network observability: host drops and OVS drops. Host drops are prefixed with `SKB_DROP` and OVS drops are prefixed with `OVS_DROP`. Dropped flows are shown in the side panel of the **Traffic flows** table along with a link to a description of each drop type. 

Examples of host drop reasons are as follows: 

  * `SKB_DROP_REASON_NO_SOCKET`: the packet dropped due to a missing socket. 
  * `SKB_DROP_REASON_TCP_CSUM`: the packet dropped due to a TCP checksum error. 



Examples of OVS drops reasons are as follows: 

  * `OVS_DROP_LAST_ACTION`: OVS packets dropped due to an implicit drop action, for example due to a configured network policy. 
  * `OVS_DROP_IP_TTL`: OVS packets dropped due to an expired IP TTL. 



See the "Additional resources" of this section for more information about enabling and working with packet drop tracking. 

## 11.1.4. Work with packet drops

Enable packet drop tracking in the Network Observability Operator by configuring the `FlowCollector` resource to monitor and visualize network data loss in the web console. 

Packet loss occurs when one or more packets of network flow data fail to reach their destination. You can track these drops by editing the `FlowCollector` to the specifications in the following YAML example. 

Important

CPU and memory usage increases when this feature is enabled. 

**Procedure**

  1. In the web console, navigate to **Ecosystem** **Installed Operators**. 
  2. Under the **Provided APIs** heading for the **NetObserv Operator** , select **Flow Collector**. 
  3. Select **cluster** , and then select the **YAML** tab. 
  4. Configure the `FlowCollector` custom resource for packet drops, for example: 

**Example`FlowCollector` configuration**

```yaml
apiVersion: flows.netobserv.io/v1beta2
kind: FlowCollector
metadata:
  name: cluster
spec:
  namespace: netobserv
  agent:
    type: eBPF
    ebpf:
      features:
       - PacketDrop
      privileged: true
```


where: 

`spec.agent.ebpf.features`
     Specifies the features to enable. Include `PacketDrop` to start reporting packet drops for each network flow. 
`spec.agent.ebpf.privileged`
     Specifies whether privileged mode is enabled. Must be set to `true` for packet drop tracking. 




**Verification**

  * When you refresh the **Network Traffic** page, the **Overview** , **Traffic Flow** , and **Topology** views display new information about packet drops: 

    1. Select the **Packet Drops** feature view from the view selector to display preconfigured packet drop panels and columns, or select new choices in **Manage panels** to select which graphical visualizations of packet drops to display in the **Overview**. 
    2. Select new choices in **Manage columns** to select which packet drop information to display in the **Traffic flows** table. 

       1. In the **Traffic Flows** view, you can also expand the side panel to view more information about packet drops. Host drops are prefixed with `SKB_DROP` and OVS drops are prefixed with `OVS_DROP`. 

    3. In the **Topology** view, connections with packet drops are displayed with red lines. 




**Additional resources**

  * [Network Observability metrics](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_observability/metrics-dashboards-alerts#network-observability-metrics_metrics-dashboards-alerts "14.2. Network observability metrics")



## 11.1.5. DNS tracking

Monitor DNS activity by using eBPF-based DNS tracking to gain insights into query patterns, detect security threats, and troubleshoot latency issues through dedicated graphical panels in the **Overview** view. 

You can configure graphical representation of Domain Name System (DNS) tracking of network flows in the **Overview** view. Using DNS tracking with extended Berkeley Packet Filter (eBPF) tracepoint hooks can serve various purposes: 

  * Network Monitoring: Gain insights into DNS queries and responses, helping network administrators identify unusual patterns, potential bottlenecks, or performance issues. 
  * Security Analysis: Detect suspicious DNS activities, such as domain name generation algorithms (DGA) used by malware, or identify unauthorized DNS resolutions that might indicate a security breach. 
  * Troubleshooting: Debug DNS-related issues by tracing DNS resolution steps, tracking latency, and identifying misconfigurations. 



### 11.1.5.1. DNS feature view

When DNS tracking is enabled, you can select the **DNS** preconfigured feature view from the view selector in the **Network Traffic** page. This view automatically displays DNS-specific panels and columns, providing faster access to DNS metrics without manual configuration. 

By default, when DNS tracking is enabled, you can see the following non-empty metrics represented in a donut or line chart in the **Overview** : 

  * Top X DNS Response Code 
  * Top X average DNS latencies with overall 
  * Top X 90th percentile DNS latencies 



Other DNS tracking panels can be added in **Manage panels** : 

  * Bottom X minimum DNS latencies 
  * Top X maximum DNS latencies 
  * Top X 99th percentile DNS latencies 



This feature is supported for IPv4 and IPv6 UDP and TCP protocols. 

See the "Additional resources" in this section for more information about enabling and working with this view. 

## 11.1.6. Work with DNS tracking

Configure the `FlowCollector` custom resource to enable DNS tracking for monitoring network performance, security analysis, and DNS troubleshooting in the web console. 

You can track DNS by editing the `FlowCollector` to the specifications in the following YAML example. 

Important

CPU and memory usage increases are observed in the eBPF agent when this feature is enabled. 

**Procedure**

  1. In the web console, navigate to **Ecosystem** **Installed Operators**. 
  2. Under the **Provided APIs** heading for **Network Observability** , select **Flow Collector**. 
  3. Select **cluster** then select the **YAML** tab. 
  4. Configure the `FlowCollector` custom resource. A sample configuration is as follows: 

**Configure`FlowCollector` for DNS tracking**

```yaml
apiVersion: flows.netobserv.io/v1beta2
kind: FlowCollector
metadata:
  name: cluster
spec:
  namespace: netobserv
  agent:
    type: eBPF
    ebpf:
      features:
       - DNSTracking
      sampling: 1
```


     * You can set the `spec.agent.ebpf.features` parameter list to enable DNS tracking of each network flow in the web console. 
     * You can set `sampling` to a value of `1` for more accurate metrics and to capture **DNS latency**. For a `sampling` value greater than 1, you can observe flows with **DNS Response Code** and **DNS Id** , and it is unlikely that **DNS Latency** can be observed. 

  5. When you refresh the **Network Traffic** page, there are new DNS representations you can select to view in the **Overview** and **Traffic Flow** views and new filters you can apply. 

     1. Select the **DNS** feature view from the view selector to display preconfigured DNS panels and columns, or select new DNS choices in **Manage panels** to display graphical visualizations and DNS metrics in the **Overview**. 
     2. Select new choices in **Manage columns** to add DNS columns to the **Traffic Flows** view. 
     3. Filter on specific DNS metrics, such as **DNS Id** , **DNS Error** **DNS** and **DNS Response Code** , and see more information from the side panel. The **DNS** and **DNS Response Code** columns are shown by default. 

Note

TCP handshake packets do not have DNS headers. TCP protocol flows without DNS headers are shown in the traffic flow data with **DNS** , **ID** , and **Response code** values of "N/A". You can filter out flow data to view only flows that have DNS headers by using the **Common** filter "DNSError" equal to "0". 




**Additional resources**

  * [Network Observability metrics](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_observability/metrics-dashboards-alerts#network-observability-metrics_metrics-dashboards-alerts "14.2. Network observability metrics")



## 11.1.7. Round-Trip Time

Analyze network flow latencies by using TCP Round-Trip Time (RTT) metrics, which use eBPF hookpoints to identify performance bottlenecks and troubleshoot TCP-related issues through dedicated panels in the Overview view. 

You can use TCP smoothed Round-Trip Time (sRTT) to analyze network flow latencies. You can use RTT captured from the `fentry/tcp_rcv_established` eBPF hookpoint to read sRTT from the TCP socket to help with the following: 

  * Network Monitoring: Gain insights into TCP latencies, helping network administrators identify unusual patterns, potential bottlenecks, or performance issues. 
  * Troubleshooting: Debug TCP-related issues by tracking latency and identifying misconfigurations. 



By default, when RTT is enabled, you can see the following TCP RTT metrics represented in the **Overview** : 

  * Top X 90th percentile TCP Round Trip Time with overall 
  * Top X average TCP Round Trip Time with overall 
  * Bottom X minimum TCP Round Trip Time with overall 



Other RTT panels can be added in **Manage panels** : 

  * Top X maximum TCP Round Trip Time with overall 
  * Top X 99th percentile TCP Round Trip Time with overall 



See the _Additional resources_ in this section for more information about enabling and working with this view. 

## 11.1.8. Work with RTT tracing

Enable Round Trip Time (RTT) tracing by configuring the `FlowCollector` custom resource to monitor and analyze network latency across your cluster by using the web console. 

You can track RTT by editing the `FlowCollector` to the specifications in the following YAML example. 

**Procedure**

  1. In the web console, navigate to **Ecosystem** **Installed Operators**. 
  2. In the **Provided APIs** heading for the **NetObserv Operator** , select **Flow Collector**. 
  3. Select **cluster** , and then select the **YAML** tab. 
  4. Configure the `FlowCollector` custom resource for RTT tracing, for example: 

**Example`FlowCollector` configuration**

```yaml
apiVersion: flows.netobserv.io/v1beta2
kind: FlowCollector
metadata:
  name: cluster
spec:
  namespace: netobserv
  agent:
    type: eBPF
    ebpf:
      features:
       - FlowRTT
```


where: 

`spec.agent.ebpf.features`
     Specifies the list of eBPF features to enable. Add `FlowRTT` to this list to start tracing Round-trip time (RTT) network flows. 




**Verification**

After the **Network Traffic** page is refreshed, the **Overview** , **Traffic flows** , and **Topology** views display RTT information. 

  1. In the **Overview** view, click **Manage panels** to select the RTT graphical visualizations to display. 
  2. In the **Traffic flows** table, verify that the **Flow RTT** column is visible by default. To manage columns, click **Manage columns**. 
  3. In the **Traffic flows** view, expand the side panel to view RTT metadata: 

     1. Filter the flow data for the **TCP** protocol by entering `protocol=TCP` in the filter search bar. 
     2. Verify that all TCP filtered flows have **FlowRTT** values greater than `0`. 
     3. Filter for **FlowRTT** values greater than `10,000,000` nanoseconds (10 ms) by entering `time_flow_rtt>=10000000` in the filter search bar. 
     4. Remove the filters. 

  4. In the **Topology** view, click the **Display** option drop-down menu. In the **Edge labels** list, select **RTT**. 



## 11.1.9. eBPF flow rule filter

Control packet capture volume by using eBPF flow rule filtering to specify capture criteria based on ports and CIDR notation, while monitoring filter performance through dedicated health dashboards and Prometheus metrics. 

You can use rule-based filtering to control the volume of packets cached in the eBPF flow table. For example, a filter can specify that only packets coming from port 100 should be captured. Then only the packets that match the filter are captured and the rest are dropped. 

You can apply multiple filter rules. 

### 11.1.9.1. Ingress and egress traffic filtering

Classless Inter-Domain Routing (CIDR) notation efficiently represents IP address ranges by combining the base IP address with a prefix length. For both ingress and egress traffic, the source IP address is first used to match filter rules configured with CIDR notation. If there is a match, then the filtering proceeds. If there is no match, then the destination IP is used to match filter rules configured with CIDR notation. 

After matching either the source IP or the destination IP CIDR, you can pinpoint specific endpoints using the `peerIP` to differentiate the destination IP address of the packet. Based on the provisioned action, the flow data is either cached in the eBPF flow table or not cached. 

### 11.1.9.2. Dashboard and metrics integrations

When this option is enabled, the **Netobserv/Health** dashboard for **eBPF agent statistics** now has the **Filtered flows rate** view. Additionally, in **Observe** **Metrics** you can query `netobserv_agent_filtered_flows_total` to observe metrics with the reason in **FlowFilterAcceptCounter** , **FlowFilterNoMatchCounter** or **FlowFilterRecjectCounter**. 

### 11.1.9.3. Flow filter configuration parameters

Reference the required and optional parameters for configuring flow filter rules in the `FlowCollector` resource, including CIDR ranges, filter actions, protocols, and specific port configurations. 

Table 11.1. Required configuration parametersParameter| Description  
---|---  
`enable` |  Set `enable` to `true` to enable the eBPF flow filtering feature.   
`cidr` |  Provides the IP address and CIDR mask for the flow filter rule. Supports both IPv4 and IPv6 address format. If you want to match against any IP, you can use `0.0.0.0/0` for IPv4 or `::/0` for IPv6.   
`action` |  Describes the action that is taken for the flow filter rule. The possible values are `Accept` or `Reject`. 

  * For the `Accept` action matching rule, the flow data is cached in the eBPF table and updated with the global metric, `FlowFilterAcceptCounter`. 
  * For the `Reject` action matching rule, the flow data is dropped and not cached in the eBPF table. The flow data is updated with the global metric, `FlowFilterRejectCounter`. 
  * If the rule is not matched, the flow is cached in the eBPF table and updated with the global metric, `FlowFilterNoMatchCounter`. 

  
Show more

Table 11.2. Optional configuration parametersParameter| Description  
---|---  
`direction` |  Defines the direction of the flow filter rule. Possible values are `Ingress` or `Egress`.   
`protocol` |  Defines the protocol of the flow filter rule. Possible values are `TCP`, `UDP`, `SCTP`, `ICMP`, and `ICMPv6`.   
`tcpFlags` |  Defines the TCP flags to filter flows. Possible values are `SYN`, `SYN-ACK`, `ACK`, `FIN`, `RST`, `PSH`, `URG`, `ECE`, `CWR`, `FIN-ACK`, and `RST-ACK`.   
`ports` |  Defines the ports to use for filtering flows. It can be used for either source or destination ports. To filter a single port, set a single port as an integer value. For example `ports: 80`. To filter a range of ports, use a "start-end" range in string format. For example `ports: "80-100"`  
`sourcePorts` |  Defines the source port to use for filtering flows. To filter a single port, set a single port as an integer value, for example `sourcePorts: 80`. To filter a range of ports, use a "start-end" range, string format, for example `sourcePorts: "80-100"`.   
`destPorts` |  DestPorts defines the destination ports to use for filtering flows. To filter a single port, set a single port as an integer value, for example `destPorts: 80`. To filter a range of ports, use a "start-end" range in string format, for example `destPorts: "80-100"`.   
`icmpType` |  Defines the ICMP type to use for filtering flows.   
`icmpCode` |  Defines the ICMP code to use for filtering flows.   
`peerIP` |  Defines the IP address to use for filtering flows, for example: `10.10.10.10`.   
Show more

## 11.1.10. Filter eBPF flow data using multiple rules

Configure multiple filtering rules in the `FlowCollector` custom resource to refine network traffic data collection by accepting or rejecting specific eBPF flows based on IP addresses and packet conditions. 

Important

  * You cannot use duplicate Classless Inter-Domain Routing (CIDRs) in filter rules. 
  * When an IP address matches multiple filter rules, the rule with the most specific CIDR prefix (longest prefix) takes precedence. 



**Procedure**

  1. In the web console, navigate to **Ecosystem** **Installed Operators**. 
  2. Under the **Provided APIs** heading for **Network Observability** , select **Flow Collector**. 
  3. Select **cluster** , then select the **YAML** tab. 
  4. Configure the `FlowCollector` custom resource. 



## 11.1.11. eBPF flow data filtering examples

Use these `FlowCollector` custom resource examples to filter eBPF flows using multiple rules to control the flow of packets cached in the eBPF flow table. 

### 11.1.11.1. Example YAML to sample all North-South traffic, and 1:50 East-West traffic

By default, all other flows are rejected. 

```yaml
apiVersion: flows.netobserv.io/v1beta2
kind: FlowCollector
metadata:
  name: cluster
spec:
  namespace: netobserv
  deploymentModel: Service
  agent:
    type: eBPF
    ebpf:
      flowFilter:
        enable: true
        rules:
         - action: Accept
           cidr: 0.0.0.0/0
           sampling: 1
         - action: Accept
           cidr: 10.128.0.0/14
           peerCIDR: 10.128.0.0/14
         - action: Accept
           cidr: 172.30.0.0/16
           peerCIDR: 10.128.0.0/14
           sampling: 50
```


where: 

`spec.agent.ebpf.flowFilter.enable`
     Specifies whether to enable `eBPF` flow filtering. Set to `true` to enable flow filtering. 
`spec.agent.ebpf.flowFilter.rules.action`
     Specifies the action for the flow filter rule. Valid values are `Accept` or `Reject`. 
`spec.agent.ebpf.flowFilter.rules.cidr`
     Specifies the IP address and `CIDR` mask for the flow filter rule. This parameter supports both `IPv4` and `IPv6` address formats. Use `0.0.0.0/0` for `IPv4` or `::/0` for `IPv6` to match any IP address. 
`spec.agent.ebpf.flowFilter.rules.peerCIDR`
     Specifies the Peer IP `CIDR` used to filter flows. 
`spec.agent.ebpf.flowFilter.rules.sampling`
     Specifies the sampling interval for matched flows. This value overrides the global sampling setting defined in `spec.agent.ebpf.sampling`. 

### 11.1.11.2. Example YAML to filter flows with packet drops

By default, all other flows are rejected. 

```yaml
apiVersion: flows.netobserv.io/v1beta2
kind: FlowCollector
metadata:
  name: cluster
spec:
  namespace: netobserv
  deploymentModel: Service
  agent:
    type: eBPF
    ebpf:
      privileged: true
      features:
        - PacketDrop
      flowFilter:
        enable: true
        rules:
        - action: Accept
          cidr: 172.30.0.0/16
          pktDrops: true
```


where: 

`spec.agent.ebpf.privileged`
     Specifies whether to enable privileged mode, which is required for reporting packet drops. 
`spec.agent.ebpf.features`
     Specifies the list of eBPF features to enable. Adding the `PacketDrop` value to this list reports packet drops for each network flow. 
`spec.agent.ebpf.flowFilter.enable`
     Specifies whether to enable `eBPF` flow filtering. 
`spec.agent.ebpf.flowFilter.rules.action`
     Specifies the action for the flow filter rule. Valid values are `Accept` or `Reject`. 
`spec.agent.ebpf.flowFilter.rules.pktDrops`
     Specifies whether to filter for flows that contain packet drops. 

**Additional resources**

  * [Network Observability metrics](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_observability/metrics-dashboards-alerts#network-observability-metrics_metrics-dashboards-alerts "14.2. Network observability metrics")
  * [Health dashboards](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_observability/network-observability-operator-monitoring#network-observability-health-dashboard-overview_network_observability "15.1. Health dashboards")



## 11.1.12. User-defined networks

Understand how you can use user-defined networks (UDN) for flexible network segmentation and leverage the Network Observability Operator to monitor these segments through dedicated labels and name filters in the traffic flow table. 

User-defined networks (UDN) improve the flexibility and segmentation capabilities of the default Layer 3 topology for a Kubernetes pod network by enabling custom Layer 2 and Layer 3 network segments, where all these segments are isolated by default. These segments act as primary or secondary networks for container pods and virtual machines that use the default OVN-Kubernetes CNI plugin. 

UDNs enable a wide range of network architectures and topologies, enhancing network flexibility, security, and performance. 

When the `UDNMapping` feature is enabled with Network Observability, the **Traffic** flow table has a **UDN labels** column. You can filter on **Source Network Name** and **Destination Network Name**. 

## 11.1.13. Work with user-defined networks

Configure the `FlowCollector` custom resource to enable user-defined network (UDN) mapping, providing visibility into traffic across custom network interfaces within the web console. 

You can enable user-defined networks (UDN) in network observability resources. The following example shows the configuration for the `FlowCollector` resource. 

**Prerequisite**

  * You have configured UDN in Red Hat OpenShift Networking. For more information, see "Creating a UserDefinedNetwork by using the CLI" or "Creating a UserDefinedNetwork by using the web console." 



**Procedure**

  1. Edit the network observability `FlowCollector` resource by running the following command: 

```shell-session
$ oc edit flowcollector
```


  2. Configure the `ebpf` section of the `FlowCollector` resource: 

```yaml
apiVersion: flows.netobserv.io/v1beta2
kind: FlowCollector
metadata:
  name: cluster
spec:
  agent:
    ebpf:
      sampling: 1
      privileged: true
      features:
      - UDNMapping
```


where: 

`spec.agent.ebpf.sampling`
     Specifies sampling rate for network events. Set to a value of `1` to capture all network events. If sampling `1` is too resource heavy, set sampling to something more appropriate for your needs. 
`spec.agent.ebpf.privileged`
     Specifies whether privileged mode is enabled. Must be set to `true` for user-defined network mapping. 




**Verification**

  * Refresh the **Network Traffic** page to view updated UDN information in the **Traffic Flow** and **Topology** views: 

    * In **Network Traffic** > **Traffic flows** , you can view UDNs under the `SrcK8S_NetworkName` and `DstK8S_NetworkName` fields. 
    * In the **Topology** view, you can set **Network** as **Scope** or **Group**. 




**Additional resources**

  * [About user-defined networks](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/multiple_networks/#about-user-defined-networks)
  * [Creating a UserDefinedNetwork by using the CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/multiple_networks/#nw-udn-cr_about-user-defined-networks)
  * [Creating a UserDefinedNetwork by using the web console](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/multiple_networks/#nw-udn-cr-ui_about-user-defined-networks)



## 11.1.14. OVN-Kubernetes networking events

Use OVN-Kubernetes network event tracking to monitor and audit network policies, admin network policies, and egress firewall rules in your cluster. 

Important

OVN-Kubernetes networking events tracking is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. 

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/). 

You can use the insights from tracking network events to help with the following tasks: 

  * Network monitoring: Monitor allowed and blocked traffic, detecting whether packets are allowed or blocked based on network policies and admin network policies. 
  * Network security: You can track outbound traffic and see whether it adheres to egress firewall rules. Detect unauthorized outbound connections and flag outbound traffic that violates egress rules. 



### 11.1.14.1. Network Events feature view

When OVN-Kubernetes network event tracking is enabled, you can select the **Network Events** preconfigured feature view from the view selector in the **Network Traffic** page. 

This view automatically displays network event-specific panels and columns, providing faster access to network event data without manual configuration. 

See the "Additional resources" for more information about enabling and working with this view. 

## 11.1.15. View network events

Configure the `FlowCollector` custom resource to enable network event tracking for auditing how security policies, firewalls, and isolation rules affect traffic flows in the web console. 

Important

OVN-Kubernetes networking events tracking is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. 

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/). 

You can edit the `FlowCollector` to view information about network traffic events, such as network flows that are dropped or allowed by the following resources: 

  * `NetworkPolicy`
  * `AdminNetworkPolicy`
  * `BaselineAdminNetworkPolicy`
  * `EgressFirewall`
  * `UserDefinedNetwork` isolation 
  * Multicast ACLs 



**Prerequisites**

  * You must have `OVNObservability` enabled by setting the `TechPreviewNoUpgrade` feature set in the `FeatureGate` custom resource (CR) named `cluster`. For more information, see "Enabling feature sets using the CLI" and "Checking OVN-Kubernetes network traffic with OVS sampling using the CLI". 
  * You have created at least one of the following network APIs: `NetworkPolicy`, `AdminNetworkPolicy`, `BaselineAdminNetworkPolicy`, `UserDefinedNetwork` isolation, multicast, or `EgressFirewall`. 



**Procedure**

  1. In the web console, navigate to **Ecosystem** **Installed Operators**. 
  2. In the **Provided APIs** heading for the **NetObserv Operator** , select **Flow Collector**. 
  3. Select **cluster** , and then select the **YAML** tab. 
  4. Configure the `FlowCollector` CR to enable viewing `NetworkEvents`, for example: 

**Example`FlowCollector` configuration**

```yaml
apiVersion: flows.netobserv.io/v1beta2
kind: FlowCollector
metadata:
  name: cluster
spec:
   agent:
    type: eBPF
    ebpf:
  #   sampling: 1
      privileged: true
      features:
       - "NetworkEvents"
```


where: 

`spec.agent.ebpf.sampling`
     Specifies the sampling rate for network events. Set to a value of `1` to capture all network events. If the sampling `1` is too resource heavy, set sampling to something more appropriate for your needs. This value is optional. 
`spec.agent.ebpf.privileged`
     Specifies whether the eBPF agent runs in privileged mode. Set to `true` because the OVN observability library needs to access local Open vSwitch (OVS) socket and Open Virtual Network (OVN) databases. 




**Verification**

  1. Navigate to the **Network Traffic** view. 
  2. Select the **Network Events** feature view from the view selector to display preconfigured network event panels and columns, or select the **Traffic flows** table to manually view network event columns. 
  3. The **Network Events** column displays information about impacts of one of the following network APIs you have enabled: `NetworkPolicy`, `AdminNetworkPolicy`, `BaselineAdminNetworkPolicy`, `UserDefinedNetwork` isolation, multicast, or egress firewalls. 

An example of the kind of events you could see in this column is as follows: 

**Example of Network Events output**

```plaintext
<Dropped_or_Allowed> by <network_event_and_event_name>, direction <Ingress_or_Egress>
```


**Additional resources**

  * [Enabling feature sets using the CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#nodes-cluster-enabling-features-cli_nodes-cluster-enabling-features)
  * [Checking OVN-Kubernetes network traffic with OVS sampling using the CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/ovn-kubernetes_network_plugin/#nw-ovn-kubernetes-observability_ovn-kubernetes-sources-of-troubleshooting-information)
