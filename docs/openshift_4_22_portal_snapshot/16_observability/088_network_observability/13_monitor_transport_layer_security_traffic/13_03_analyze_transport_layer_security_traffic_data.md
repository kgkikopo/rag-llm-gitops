# 13.3. Analyze Transport Layer Security traffic data

View and filter Transport Layer Security (TLS) metadata to identify deprecated configurations and verify encryption compliance in the cluster. 

**Prerequisites**

  * The Network Observability Operator is installed. 
  * TLS tracking is enabled in the `FlowCollector` custom resource (CR). 
  * Access to the OpenShift Container Platform web console. 



**Procedure**

  1. Navigate to **Observe** **Network Traffic** in the OpenShift Container Platform web console and click the **Traffic flows** tab. 

Note

The **TLS Version** column is enabled by default. If the default TLS version column is not visible after enabling TLS tracking, click **Restore default columns** in **Manage columns** to refresh the table. 

  2. Add TLS-specific columns to the traffic table: 

     1. Click **Manage columns**. 
     2. Select the **TLS Cipher Suite** , **TLS Group** , and **TLS Types** checkboxes. 
     3. Click **Save**. 

  3. Filter traffic by message type to view complete TLS metadata: 

     1. In the filter bar, select **TLS Types** and select **ServerHello** from the dropdown menu. 

`ServerHello` messages contain negotiated TLS metadata such as cipher suite and cryptographic group information. 

  4. Filter traffic by TLS version to identify deprecated configurations: 

     1. In the filter bar, select **TLS Version**. 
     2. Select the versions you want to review: 

        * **1.0** : Deprecated 
        * **1.1** : Deprecated 
        * **1.2** : Legacy 
        * **1.3** : Current standard 

To identify all deprecated connections, filter for TLS versions 1.0 and 1.1. 

  5. Analyze TLS metrics in the overview panel: 

     1. Click the **Overview** tab. 
     2. Select the **TLS Tracking** feature view from the view selector to display preconfigured TLS panels and columns, or review the default TLS panels, which include **TLS usage (network flows per second)** and **TLS per version (network flows per second)**. 
     3. Optional: To view additional TLS metrics, click **Manage panels** to select and display additional panels, such as **TLS per group (network flows per second)** or **TLS per cipher suite (network flows per second)**. 

  6. Identify secure connections in the **Topology** view: 

     1. Click the **Topology** tab. 

Connections secured with TLS are marked with a lock icon. The color of the lock icon indicates the security level: 

        * **Red** : Deprecated TLS versions (1.0 or 1.1) 
        * **Yellow** : Legacy configurations (TLS 1.2) 
        * **Green** : Secure connections (TLS 1.3) 
        * **Blue** : Post-Quantum Cryptography (PQC) compliant 

Select a connection node to view its specific TLS version and cipher suite details. 

  7. View TLS metrics in the Network Observability dashboard: 

     1. Navigate to **Observe** **Dashboards**. 
     2. Search for **NetObserv** and review the available metrics: 

        * **TLS Traffic** : Displays overall TLS traffic metrics. 
        * **Flows rate per TLS version** : Displays traffic trends by TLS version over time. 
        * **Flows rate per TLS group** : Displays traffic by TLS group over time.
