# 15.10. Troubleshooting connectivity for hosted control planes

By using connectivity metrics, you can diagnose whether any issues are related to connectivity from a hosted control plane to a data plane. 

## 15.10.1. Troubleshooting connectivity from the control plane to the data plane

To diagnose connectivity issues from a hosted control plane to the compute nodes in a data plane, check the status of the `DataPlaneConnectionAvailable` condition. 

If the status of the `DataPlaneConnectionAvailable` condition is `True`, the control plane can successfully reach the data plane nodes through the `konnectivity-agent` pods. If the status is `False`, take the following steps to determine why the control plane cannot reach the data plane. 

**Procedure**

  1. Check the network policies that might block the `Konnectivity` service traffic. 
  2. Review the firewall rules between the control plane and the data plane. 
  3. View the status of the `konnectivity-agent` pods in the data plane. 
  4. In the control plane, review the `Konnectivity` server deployment. 



**Additional resources**

  * [Connectivity monitoring for hosted control planes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hosted_control_planes/hcp-observability#hcp-connectivity-metrics_hcp-observability "13.4. Connectivity monitoring for hosted control planes")
