# 1.11. Example policy configurations that use dynamic matching and templating

The following example configuration snippets show node network policies that use dynamic matching and templating. 

Important

Applying node network configuration policies that use dynamic matching and templating is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. 

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/). 

## 1.11.1. Example: Linux bridge interface node network configuration policy to inherit static IP address from the NIC attached to the bridge

Create a Linux bridge interface on nodes in the cluster and transfer the static IP configuration of the NIC to the bridge by applying a single `NodeNetworkConfigurationPolicy` manifest to the cluster. 

The following YAML file is an example of a manifest for a Linux bridge interface. It includes sample values that you must replace with your own information. 

```yaml
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: br1-eth1-copy-ipv4-policy
spec:
  nodeSelector:
    node-role.kubernetes.io/worker: ""
  capture:
    eth1-nic: interfaces.name=="eth1"
    eth1-routes: routes.running.next-hop-interface=="eth1"
    br1-routes: capture.eth1-routes | routes.running.next-hop-interface := "br1"
  desiredState:
    interfaces:
      - name: br1
        description: Linux bridge with eth1 as a port
        type: linux-bridge
        state: up
        ipv4: "{{ capture.eth1-nic.interfaces.0.ipv4 }}"
        bridge:
          options:
            stp:
              enabled: false
          port:
            - name: eth1
     routes:
        config: "{{ capture.br1-routes.routes.running }}"
```


  * `metadata.name` defines the name of the policy. 
  * `spec.nodeSelector` defines the nodes in the cluster the networking policy is applied to. If not defined, the default is all nodes. This example uses the `node-role.kubernetes.io/worker: ""` node selector to select all worker nodes in the cluster. 
  * `spec.capture.eth1-nic` defines the reference to the node NIC to which the bridge attaches. 
  * `spec.desiredState.interfaces.type` defines the type of interface. This example creates a bridge. 
  * `spec.desiredState.interfaces.ipv4` defines the IP address of the bridge interface. This value matches the IP address of the NIC which is referenced by the `spec.capture.eth1-nic` entry. 
  * `spec.desiredState.interfaces.bridge.port.name` defines the node NIC to which the bridge attaches. 



**Additional resources**

  * [The NMPolicy project - Policy syntax](https://nmstate.io/nmpolicy/user-guide/102-policy-syntax.html)
