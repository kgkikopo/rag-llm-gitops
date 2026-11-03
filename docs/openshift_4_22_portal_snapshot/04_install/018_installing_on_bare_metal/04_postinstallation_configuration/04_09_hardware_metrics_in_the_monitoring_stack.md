# 4.9. Hardware metrics in the Monitoring stack

Hardware metrics can be exported to the cluster by enabling the Ironic Prometheus Exporter (IPE). 

IPE is a tool that exposes the hardware sensor data of cluster nodes in the Prometheus format. When you enable IPE in your cluster, the tool collects data from the baseboard management controller (BMC) of each node and exports the data to the cluster’s monitoring stack. 

Note

This method of collecting hardware metrics works only on Redfish-compatible BMCs. 

You can then view these hardware metrics alongside other metrics in the **Observe** tab of the web console. 

Important

Monitoring bare metal hardware metrics is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. 

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/). 

## 4.9.1. Adding node hardware metrics to the Monitoring stack

To access hardware metrics for your bare-metal nodes in the web console, enable the Ironic Prometheus Exporter in your cluster. 

**Prerequisites**

  * You have enabled the `TechPreviewNoUpgrade` feature set in your cluster’s `FeatureGate` custom resource (CR). For more information, see "Enabling features using feature gates". 
  * You bare-metal nodes use Redfish-compatible baseboard management controllers (BMCs). 



**Procedure**

  1. Enable the Ironic Prometheus Exporter by running the following command: 

```shell-session
$ oc patch provisioning provisioning-configuration \
    --type=merge \
    -p '{"spec":{"prometheusExporter":{"enabled":true}}}'
```


  2. Optional: Configure the data collection interval by running the following command: 

```shell-session
$ oc patch provisioning provisioning-configuration \
    --type=merge \
    -p '{"spec":{"prometheusExporter":{"sensorCollectionInterval":<interval>}}}'
```


Replace `<interval>` with the interval in seconds for collecting sensor data from BMCs. The minimum value is `60`. 

  3. Optional: Disable default alerting rules for hardware metrics by running the following command: 

```shell-session
$ oc patch provisioning provisioning-configuration \
    --type=merge \
    -p '{"spec":{"prometheusExporter":{"disableDefaultPrometheusRules":true}}}'
```


When `disableDefaultPrometheusRules` is set to `true`, the configuration prevents deployment of default alerting rules for hardware metrics. 

  4. Optional: Disable the Ironic Prometheus Exporter by running the following command: 

```shell-session
$ oc patch provisioning provisioning-configuration \
    --type=merge \
    -p '{"spec":{"prometheusExporter":{"enabled":false}}}'
```


**Verification**

  1. From the web console, click **Observe** **Metrics** and enter "baremetal" into the **Expression** field. Several autocomplete suggestions should appear, such as the following examples: 

`baremetal_power_status`

`baremetal_temperature_status`

`baremetal_drive_status`

`baremetal_fan_status`

  2. Select one of the autocomplete suggestions and click **Run Queries**. 
  3. Verify that the queried hardware metrics appear in the UI. 
  4. If you did not disable default alerting rules, view them by running the following command: 

```shell-session
$ oc -n openshift-machine-api get promrule metal3-defaults -oyaml
```


**Additional resources**

  * [Enabling features using feature gates](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#nodes-cluster-enabling-features)
