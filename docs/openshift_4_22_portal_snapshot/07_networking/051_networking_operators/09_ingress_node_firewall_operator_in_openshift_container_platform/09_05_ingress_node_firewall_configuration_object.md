# 9.5. Ingress Node Firewall configuration object

Review configuration fields so you can define how the Operator deploys the firewall. 

The fields for the Ingress Node Firewall configuration object are described in the following table: 

Table 9.1. Ingress Node Firewall Configuration objectField| Type| Description  
---|---|---  
`metadata.name` |  `string` |  The name of the CR object. The name of the firewall rules object must be `ingressnodefirewallconfig`.   
`metadata.namespace` |  `string` |  Namespace for the Ingress Firewall Operator CR object. The `IngressNodeFirewallConfig` CR must be created inside the `openshift-ingress-node-firewall` namespace.   
`spec.nodeSelector` |  `string` |  A node selection constraint used to target nodes through specified node labels. For example:  `apiVersion: ingressnodefirewall.openshift.io/v1alpha1 kind: IngressNodeFirewallConfig metadata: name: ingressnodefirewallconfig namespace: openshift-ingress-node-firewall spec: nodeSelector: node-role.kubernetes.io/worker: ""` Note One label used in `nodeSelector` must match a label on the nodes in order for the daemon set to start. For example, if the node labels `node-role.kubernetes.io/worker` and `node-type.kubernetes.io/vm` are applied to a node, then at least one label must be set using `nodeSelector` for the daemon set to start.   
`spec.ebpfProgramManagerMode` |  `boolean` |  Specifies if the Node Ingress Firewall Operator uses the eBPF Manager Operator or not to manage eBPF programs. This capability is a Technology Preview feature.  For more information about the support scope of Red Hat Technology Preview features, see "Technology Preview Features Support Scope".   
Show more

Note

The Operator consumes the CR and creates an ingress node firewall daemon set on all the nodes that match the `nodeSelector`. 

## 9.5.1. Ingress Node Firewall Operator example configuration

A complete Ingress Node Firewall Configuration is specified in the following example: 

**Example of how to create an Ingress Node Firewall Configuration object**

```yaml
$ cat << EOF | oc create -f -
apiVersion: ingressnodefirewall.openshift.io/v1alpha1
kind: IngressNodeFirewallConfig
metadata:
  name: ingressnodefirewallconfig
  namespace: openshift-ingress-node-firewall
spec:
  nodeSelector:
    node-role.kubernetes.io/worker: ""
EOF
```


Note

The Operator consumes the CR object and creates an ingress node firewall daemon set on all the nodes that match the `nodeSelector`. 

**Additional resources**

  * [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/)



## 9.5.2. Ingress Node Firewall rules object

You can review rule fields and examples to define which ingress traffic is allowed or denied by using the Ingress Node Firewall rules object. 

The fields for the Ingress Node Firewall rules object are described in the following table: 

Table 9.2. Ingress Node Firewall rules objectField| Type| Description  
---|---|---  
`metadata.name` |  `string` |  The name of the CR object.   
`interfaces` |  `array` |  The fields for this object specify the interfaces to apply the firewall rules to. For example, `- en0` and `- en1`.   
`nodeSelector` |  `array` |  You can use `nodeSelector` to select the nodes to apply the firewall rules to. Set the value of your named `nodeselector` labels to `true` to apply the rule.   
`ingress` |  `object` |  `ingress` allows you to configure the rules that allow outside access to the services on your cluster.   
Show more

### 9.5.2.1. Ingress object configuration

The values for the `ingress` object are defined in the following table: 

Table 9.3. ingress objectField| Type| Description  
---|---|---  
`sourceCIDRs` |  `array` |  Allows you to set the CIDR block. You can configure multiple CIDRs from different address families.  Note Different CIDRs allow you to use the same order rule. In the case that there are multiple `IngressNodeFirewall` objects for the same nodes and interfaces with overlapping CIDRs, the `order` field will specify which rule is applied first. Rules are applied in ascending order.   
`rules` |  `array` |  Ingress firewall `rules.order` objects are ordered starting at `1` for each `source.CIDR` with up to 100 rules per CIDR. Lower order rules are executed first.  `rules.protocolConfig.protocol` supports the following protocols: TCP, UDP, SCTP, ICMP and ICMPv6. ICMP and ICMPv6 rules can match against ICMP and ICMPv6 types or codes. TCP, UDP, and SCTP rules can match against a single destination port or a range of ports using `<start : end-1>` format.  Set `rules.action` to `allow` to apply the rule or `deny` to disallow the rule.  Note Ingress firewall rules are verified using a verification webhook that blocks any invalid configuration. The verification webhook prevents you from blocking any critical cluster services such as the API server.   
Show more

### 9.5.2.2. Ingress Node Firewall rules object example

A complete Ingress Node Firewall configuration is specified in the following example: 

**Example Ingress Node Firewall configuration**

```yaml
apiVersion: ingressnodefirewall.openshift.io/v1alpha1
kind: IngressNodeFirewall
metadata:
  name: ingressnodefirewall
spec:
  interfaces:
  - eth0
  nodeSelector:
    matchLabels:
      <label_name>: <label_value>
  ingress:
  - sourceCIDRs:
       - 172.16.0.0/12
    rules:
    - order: 10
      protocolConfig:
        protocol: ICMP
        icmp:
          icmpType: 8 #ICMP Echo request
      action: Deny
    - order: 20
      protocolConfig:
        protocol: TCP
        tcp:
          ports: "8000-9000"
      action: Deny
  - sourceCIDRs:
       - fc00:f853:ccd:e793::0/64
    rules:
    - order: 10
      protocolConfig:
        protocol: ICMPv6
        icmpv6:
          icmpType: 128 #ICMPV6 Echo request
      action: Deny
```


\+ A `<label_name>` and a `<label_value>` must exist on the node and must match the `nodeselector` label and value applied to the nodes you want the `ingressfirewallconfig` CR to run on. The `<label_value>` can be `true` or `false`. By using `nodeSelector` labels, you can target separate groups of nodes to apply different rules to using the `ingressfirewallconfig` CR. 

### 9.5.2.3. Zero trust Ingress Node Firewall rules object example

Zero trust Ingress Node Firewall rules can provide additional security to multi-interface clusters. For example, you can use zero trust Ingress Node Firewall rules to drop all traffic on a specific interface except for SSH. 

A complete configuration of a zero trust Ingress Node Firewall rule for a network-interface cluster is specified in the following example: 

Important

Users need to add all ports their application will use to their allowlist in the following case to ensure proper functionality. 

**Example zero trust Ingress Node Firewall rules**

```yaml
apiVersion: ingressnodefirewall.openshift.io/v1alpha1
kind: IngressNodeFirewall
metadata:
 name: ingressnodefirewall-zero-trust
spec:
 interfaces:
 - eth1
 nodeSelector:
   matchLabels:
     <ingress_firewall_label_name>: <label_value>
 ingress:
 - sourceCIDRs:
      - 0.0.0.0/0
   rules:
   - order: 10
     protocolConfig:
       protocol: TCP
       tcp:
         ports: 22
     action: Allow
   - order: 20
     action: Deny
```


Important

eBPF Manager Operator integration is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. 

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).
