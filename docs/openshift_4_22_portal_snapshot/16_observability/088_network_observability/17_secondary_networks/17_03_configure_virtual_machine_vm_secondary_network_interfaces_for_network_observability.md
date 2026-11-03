# 17.3. Configure virtual machine (VM) secondary network interfaces for Network Observability

Configure the `FlowCollector` to monitor VM secondary network traffic by setting the eBPF agent to `privileged` mode and defining the indexing for secondary networks, enabling the capture and enrichment of flows from OpenShift Virtualization. 

Network flows coming from VMs that are connected to the default internal pod network are automatically captured by network observability. 

**Procedure**

  1. Get information about the virtual machine launcher pod by running the following command. This information is used in Step 5: 

```shell-session
$ oc get pod virt-launcher-<vm_name>-<suffix> -n <namespace> -o yaml
```


```yaml
apiVersion: v1
kind: Pod
metadata:
  annotations:
    k8s.v1.cni.cncf.io/network-status: |-
      [{
        "name": "ovn-kubernetes",
        "interface": "eth0",
        "ips": [
          "10.129.2.39"
        ],
        "mac": "0a:58:0a:81:02:27",
        "default": true,
        "dns": {}
      },
      {
        "name": "my-vms/l2-network",
        "interface": "podc0f69e19ba2",
        "ips": [
          "10.10.10.15"
        ],
        "mac": "02:fb:f8:00:00:12",
        "dns": {}
      }]
  name: virt-launcher-fedora-aqua-fowl-13-zr2x9
  namespace: my-vms
spec:
#  ...
status:
#  ...
```


where: 

`name`
     Specifies the name of the secondary network. 
`interface`
     Specifies the network interface of the secondary network. 
`ips`
     Specifies the list of IP addresses used by the secondary network. 
`mac`
     Specifies the MAC address used for the secondary network. 

  2. In the web console, navigate to **Ecosystem** **Installed Operators**. 
  3. Under the **Provided APIs** heading for the **NetObserv Operator** , select **Flow Collector**. 
  4. Select **cluster** and then select the **YAML** tab. 
  5. Configure `FlowCollector` based on the information you found from the additional network investigation: 

```yaml
apiVersion: flows.netobserv.io/v1beta2
kind: FlowCollector
metadata:
  name: cluster
spec:
  agent:
    ebpf:
      privileged: true
  processor:
    advanced:
      secondaryNetworks:
      - index:
        - MAC
        name: my-vms/l2-network
# ...
```


where: 

`spec.agent.ebpf.privileged`
     Specifies that the eBPF agent runs in `privileged` mode, which is required to collect flows from secondary network interfaces on virtual machine launcher pods. 
`spec.processor.advanced.secondaryNetworks.index`
     Specifies the fields to use for indexing the virtual machine launcher pods. It is recommended to use the `MAC` address as the indexing field to get network flows enrichment for secondary interfaces. If you have overlapping MAC addresses between pods, then additional indexing fields, such as `IP` and `Interface`, can be added to ensure accurate enrichment. 
`MAC`
     Specifies the MAC address as an indexing field value. Add `MAC` to the `index` field list if your additional network information includes a MAC address. 
`spec.processor.advanced.secondaryNetworks.name`
     Specifies the name of the secondary network as found in the `k8s.v1.cni.cncf.io/network-status` annotation of the virtual machine launcher pod. The format is typically `<namespace>/<network_attachment_definition_name>`. 




**Verification**

  1. Observe VM traffic: 

     1. Navigate to the **Network Traffic** page. 
     2. Filter by **Source** IP using your virtual machine IP found in `k8s.v1.cni.cncf.io/network-status` annotation. 
     3. View both **Source** and **Destination** fields, which should be enriched, and identify the VM launcher pods and the VM instance as owners.
