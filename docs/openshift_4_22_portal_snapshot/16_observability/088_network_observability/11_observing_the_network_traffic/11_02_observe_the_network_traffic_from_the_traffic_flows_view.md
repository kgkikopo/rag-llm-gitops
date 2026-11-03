# 11.2. Observe the network traffic from the Traffic flows view

Use the **Traffic flows** view to monitor cluster network communication, audit eBPF flow data, validate network policies, and export metrics for external analysis. 

The **Traffic flows** view in the Network Observability Operator provides a granular, tabular representation of network activity across a OpenShift Container Platform cluster. By leveraging eBPF technology to collect flow data, this view allows administrators to monitor real-time and historical communication between pods, services, and nodes. This visibility is essential for auditing network traffic, validating network policies, and identifying unexpected communication patterns within the cluster infrastructure. 

In the **Traffic flows** interface, you can analyze specific connection details by interacting with individual rows to retrieve detailed flow information. The view supports advanced customization through the **Display options** menu, where you can adjust row density and manage columns. By selecting and reordering specific columns, you can tailor the table to highlight the most relevant data points for your environment, such as source and destination endpoints or traffic volume. 

To support external analysis and reporting, the **Traffic flows** view includes data export capabilities. You can export the entire dataset or select specific fields to generate a targeted report of network activity. This functionality ensures that network flow data is accessible for long-term auditing or for use in third-party monitoring tools, providing a flexible way to document and analyze the network health of your OpenShift Container Platform environment. 

## 11.2.1. Work with the Traffic flows view

View and analyze detailed network flow information in the **Traffic flows** table to troubleshoot connectivity issues and monitor traffic patterns between cluster components. 

As an administrator, you can navigate to **Traffic flows** table to see network flow information. 

**Prerequisite**

  * You have administrator access. 



**Procedure**

  1. Navigate to **Observe** **Network Traffic**. 
  2. In the **Network Traffic** page, click the **Traffic flows** tab. 
  3. Click on each row to get the corresponding flow information. 



## 11.2.2. Traffic flow display settings

The **Traffic flows** view contains settings to customize the display density, data columns, and data export options. 

### 11.2.2.1. Display options

The following elements are available in the **Traffic flows** view: 

**Show advanced options**
     Specifies a menu to customize and export the current view. 
**Display options** drop-down
     Specifies the row size for the data table. The default value is **Normal**. 
**Manage columns**
     Specifies a dialog to select and reorder the columns displayed in the **Traffic flows** table. 

## 11.2.3. Export traffic flow data

Export network flow data from the **Traffic flows** view to a CSV file for external analysis or reporting. 

**Procedure**

  1. Click **Export data**. 
  2. In the window, select the **Export all data** checkbox to export all the data, and clear the checkbox to select the required fields to be exported. 
  3. Click **Export**. 



## 11.2.4. Configure IPsec with the FlowCollector custom resource

Enable IPsec tracking in the `FlowCollector` resource to monitor encrypted traffic, adding an IPsec status column to the traffic flow view and generating a dedicated encryption dashboard. 

In OpenShift Container Platform, IPsec is disabled by default. You can enable IPsec by following the instructions in "Configuring IPsec encryption". 

**Prerequisite**

  * You have enabled IPsec encryption on OpenShift Container Platform. 



**Procedure**

  1. In the web console, navigate to **Ecosystem** **Installed Operators**. 
  2. Under the **Provided APIs** heading for the **NetObserv Operator** , select **Flow Collector**. 
  3. Select **cluster** then select the **YAML** tab. 
  4. Configure the `FlowCollector` custom resource for IPsec: 

**Example configuration of`FlowCollector` for IPsec**

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
      - "IPSec"
```


**Verification**

When IPsec is enabled: 

  * A new column named **IPsec Status** is displayed in the network observability **Traffic flows** view to show whether a flow was successfully IPsec-encrypted or if there was an error during encryption/decryption. 
  * A new dashboard showing the percent of encrypted traffic is generated. 



**Additional resources**

  * [Configuring IPsec encryption](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_security/#configuring-ipsec-ovn)



## 11.2.5. Work with conversation tracking

Configure the `FlowCollector` custom resource to enable conversation tracking for grouping and analyzing related network flows in the web console. 

As an administrator, you can group network flows that are part of the same conversation. A conversation is defined as a grouping of peers that are identified by their IP addresses, ports, and protocols, resulting in an unique **Conversation Id**. You can query conversation events in the web console. These events are represented in the web console as follows: 

  * **Conversation start** : This event happens when a connection is starting or TCP flag intercepted 
  * **Conversation tick** : This event happens at each specified interval defined in the `FlowCollector` `spec.processor.conversationHeartbeatInterval` parameter while the connection is active. 
  * **Conversation end** : This event happens when the `FlowCollector` `spec.processor.conversationEndTimeout` parameter is reached or the TCP flag is intercepted. 
  * **Flow** : This is the network traffic flow that occurs within the specified interval. 



**Procedure**

  1. In the web console, navigate to **Ecosystem** **Installed Operators**. 
  2. Under the **Provided APIs** heading for the **NetObserv Operator** , select **Flow Collector**. 
  3. Select **cluster** then select the **YAML** tab. 
  4. Configure the `FlowCollector` custom resource so that `spec.processor.logTypes`, `conversationEndTimeout`, and `conversationHeartbeatInterval` parameters are set according to your observation needs. A sample configuration is as follows: 

**Configure`FlowCollector` for conversation tracking**

```yaml
apiVersion: flows.netobserv.io/v1beta2
kind: FlowCollector
metadata:
  name: cluster
spec:
 processor:
  logTypes: Flows
  advanced:
   conversationEndTimeout: 10s
   conversationHeartbeatInterval: 30s
```


where: 

`spec.processor.logTypes`
     Specifies the types of events to export. When set to `Flows`, only the Flow event is exported. When set to `All`, both conversation and flow events are exported and visible in the **Network Traffic** page. To focus only on conversation events, specify `Conversations` to export **Conversation start** , **Conversation tick** , and **Conversation end** events. To export only the **Conversation end** events, specify `EndedConversations`. Storage requirements are highest for `All` and lowest for `EndedConversations`. 
`spec.processor.advanced.conversationEndTimeout`
     Specifies the duration at which a **Conversation end** event is triggered once the timeout is reached or a TCP flag is intercepted. 
`spec.processor.advanced.conversationHeartbeatInterval`
    

Specifies the interval for the **Conversation tick** event while the network connection is active. 

Note

If you update the `logType` option, the flows from the previous selection do not clear from the console plugin. For example, if you initially set `logType` to `Conversations` for a span of time until 10 AM and then move to `EndedConversations`, the console plugin shows all conversation events before 10 AM and only ended conversations after 10 AM. 

  5. Refresh the **Network Traffic** page on the **Traffic flows** tab. Notice there are two new columns, **Event/Type** and **Conversation Id**. All the **Event/Type** fields are `Flow` when **Flow** is the selected query option. 
  6. Select **Query Options** and choose the **Log Type** , **Conversation**. Now the **Event/Type** shows all of the desired conversation events. 
  7. Next you can filter on a specific conversation ID or switch between the **Conversation** and **Flow** log type options from the side panel. 



## 11.2.6. Work with the eBPF Manager Operator

Integrate the eBPF Manager Operator with Network Observability to manage eBPF programs and reduce the need for privileged agent permissions. 

The eBPF Manager Operator reduces the attack surface and ensures compliance, security, and conflict prevention by managing all eBPF programs. Network observability can use the eBPF Manager Operator to load hooks. As a result, you no longer need to provide the eBPF Agent with privileged mode or additional Linux capabilities such as `CAP_BPF` and `CAP_PERFMON`. The eBPF Manager Operator with network observability is only supported on 64-bit AMD architecture. 

Important

eBPF Manager Operator with network observability is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. 

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/). 

**Procedure**

  1. In the web console, navigate to **Ecosystem** **Operator Hub**. 
  2. Install **eBPF Manager**. 
  3. Check **Workloads** **Pods** in the `bpfman` namespace to make sure they are all up and running. 
  4. Configure the `FlowCollector` custom resource to use the eBPF Manager Operator: 

**Example`FlowCollector` configuration**

```yaml
apiVersion: flows.netobserv.io/v1beta2
kind: FlowCollector
metadata:
  name: cluster
spec:
  agent:
    ebpf:
      features:
        - EbpfManager
```


**Verification**

  1. In the web console, navigate to **Ecosystem** **Installed Operators**. 
  2. Click **eBPF Manager Operator** **All instances** tab. 

For each node, verify that a `BpfApplication` named `netobserv` and a pair of `BpfProgram` objects, one for Traffic Control (TCx) ingress and another for TCx egress, exist. If you enable other eBPF Agent features, you might have more objects. 




**Additional resources**

  * [Installing the eBPF Manager Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/networking_operators/#installing-the-ebpf-manager-operator)



## 11.2.7. Use the histogram

The histogram provides a visualization of network flow logs that you can use to analyze traffic volume trends and filter flow data by specific time intervals. 

You can click **Show histogram** to display a toolbar view for visualizing the history of flows as a bar chart. The histogram shows the number of logs over time. You can select a part of the histogram to filter the network flow data in the table that follows the toolbar. 

## 11.2.8. Work with availability zones

Configure the `FlowCollector` custom resource to collect availability zone data, enabling the visualization and analysis of network traffic across different cluster zones in the web console. 

You can configure the `FlowCollector` to collect information about the cluster availability zones. This allows you to enrich network flow data with the [`topology.kubernetes.io/zone`](https://kubernetes.io/docs/reference/labels-annotations-taints/#topologykubernetesiozone) label value applied to the nodes. 

**Procedure**

  1. In the web console, go to **Ecosystem** **Installed Operators**. 
  2. Under the **Provided APIs** heading for the **NetObserv Operator** , select **Flow Collector**. 
  3. Select **cluster** then select the **YAML** tab. 
  4. Configure the `FlowCollector` custom resource so that the `spec.processor.addZone` parameter is set to `true`. A sample configuration is as follows: 

**Configure`FlowCollector` for availability zones collection**

```yaml
apiVersion: flows.netobserv.io/v1beta2
kind: FlowCollector
metadata:
  name: cluster
spec:
# ...
 processor:
   addZone: true
# ...
```


**Verification**

When you refresh the **Network Traffic** page, the **Overview** , **Traffic Flow** , and **Topology** views display new information about availability zones: 

  1. In the **Overview** tab, you can see **Zones** as an available **Scope**. 
  2. In **Network Traffic** **Traffic flows** , **Zones** are viewable under the SrcK8S_Zone and DstK8S_Zone fields. 
  3. In the **Topology** view, you can set **Zones** as **Scope** or **Group**. 



**Additional resources**

  * [Conntrack Zone ID](https://lwn.net/Articles/370152/#:~:text=A%20zone%20is%20simply%20a,to%20seperate%20conntrack%20defragmentation%20queues.)



## 11.2.9. Endpoint translation (xlat)

Endpoint translation (xlat) uses eBPF to enrich network flow logs with translated pod-level metadata, providing visibility into the specific backend pods serving traffic behind services or load balancers. 

You can gain visibility into the endpoints serving traffic in a consolidated view using network observability and extended Berkeley Packet Filter (eBPF). Typically, when traffic flows through a service, egressIP, or load balancer, the traffic flow information is abstracted as it is routed to one of the available pods. If you try to get information about the traffic, you can only view service related info, such as service IP and port, and not information about the specific pod that is serving the request. Often the information for both the service traffic and the virtual service endpoint is captured as two separate flows, which complicates troubleshooting. 

To solve this, endpoint xlat can help in the following ways: 

  * Capture the network flows at the kernel level, which has a minimal impact on performance. 
  * Enrich the network flows with translated endpoint information, showing not only the service but also the specific backend pod, so you can see which pod served a request. 



As network packets are processed, the eBPF hook enriches flow logs with metadata about the translated endpoint that includes the following pieces of information that you can view in the **Network Traffic** page in a single row: 

  * Source Pod IP 
  * Source Port 
  * Destination Pod IP 
  * Destination Port 
  * Conntrack Zone ID 



## 11.2.10. Work with endpoint translation (xlat)

Enable endpoint translation (xlat) in the `FlowCollector` resource to enrich network flows with translated packet information. You can use this information to identify the specific pods and objects serving service traffic through dedicated xlat columns. 

You can use network observability and eBPF to enrich network flows from a Kubernetes service with translated endpoint information, gaining insight into the endpoints serving traffic. 

**Procedure**

  1. In the web console, navigate to **Ecosystem** **Installed Operators**. 
  2. In the **Provided APIs** heading for the **NetObserv Operator** , select **Flow Collector**. 
  3. Select **cluster** , and then select the **YAML** tab. 
  4. Configure the `FlowCollector` custom resource for `PacketTranslation`, for example: 

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
       - PacketTranslation
```


     * You can start enriching network flows with translated packet information by listing the `PacketTranslation` parameter in the `spec.agent.ebpf.features` specification list. 

  5. Refresh the **Network Traffic** page to filter for information about translated packets: 

     1. Filter the network flow data based on **Destination kind: Service**. 
     2. You can see the **xlat** column, which distinguishes where translated information is displayed, and the following default columns: 

        * **Xlat Zone ID**
        * **Xlat Src Kubernetes Object**
        * **Xlat Dst Kubernetes Object**

     3. You can manage the display of additional **xlat** columns in **Manage columns**.
