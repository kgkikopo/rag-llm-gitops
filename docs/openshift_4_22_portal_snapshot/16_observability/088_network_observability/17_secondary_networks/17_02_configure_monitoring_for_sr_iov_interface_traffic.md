# 17.2. Configure monitoring for SR-IOV interface traffic

Configure the `FlowCollector` resource to monitor traffic on Single Root I/O Virtualization (SR-IOV) device by setting the `spec.agent.ebpf.privileged` field to `true`, which enables the eBPF agent to monitor other network namespaces. 

The eBPF agent monitors other network namespaces in addition to the host network namespaces, which are monitored by default. When a pod with a virtual functions (VF) interface is created, a new network namespace is created. With `SRIOVNetwork` policy `IPAM` configurations specified, the VF interface is migrated from the host network namespace to the pod network namespace. 

**Prerequisites**

  * Access to an OpenShift Container Platform cluster with a SR-IOV device. 
  * The `SRIOVNetwork` custom resource (CR) `spec.ipam` configuration must be set with an IP address from the range that the interface lists or from other plugins. 



**Procedure**

  1. In the web console, navigate to **Ecosystem** **Installed Operators**. 
  2. Under the **Provided APIs** heading for the **NetObserv Operator** , select **Flow Collector**. 
  3. Select **cluster** and then select the **YAML** tab. 
  4. Configure the `FlowCollector` custom resource. A sample configuration is as follows: 

**Configure`FlowCollector` for SR-IOV monitoring**

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
```


     * The `spec.agent.ebpf.privileged` field value must be set to `true` to enable SR-IOV monitoring. 




**Additional resources**

  * [Configuring an SR-IOV network device](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/hardware_networks/#cnf-creating-an-additional-sriov-network-with-vrf-plug-in_configuring-sriov-device)
