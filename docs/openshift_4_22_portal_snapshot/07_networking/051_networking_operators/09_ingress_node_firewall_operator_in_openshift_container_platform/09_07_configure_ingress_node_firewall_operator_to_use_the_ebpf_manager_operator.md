# 9.7. Configure Ingress Node Firewall Operator to use the eBPF Manager Operator

Configure the Ingress Node Firewall to use eBPF Manager for program lifecycle control. 

The Ingress Node Firewall uses [eBPF](https://www.kernel.org/doc/html/latest/bpf/index.html) programs to implement some of its key firewall functionality. By default these eBPF programs are loaded into the kernel using a mechanism specific to the Ingress Node Firewall. 

As a cluster administrator, you can configure the Ingress Node Firewall Operator to use the eBPF Manager Operator for loading and managing these programs instead, adding additional security and observability functionality. 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 
  * You have an account with administrator privileges. 
  * You installed the Ingress Node Firewall Operator. 
  * You have installed the eBPF Manager Operator. 



**Procedure**

  1. Apply the following labels to the `ingress-node-firewall-system` namespace: 

```shell-session
$ oc label namespace openshift-ingress-node-firewall \
    pod-security.kubernetes.io/enforce=privileged \
    pod-security.kubernetes.io/warn=privileged --overwrite
```


  2. Edit the `IngressNodeFirewallConfig` object named `ingressnodefirewallconfig` and set the `ebpfProgramManagerMode` field: 

**Ingress Node Firewall Operator configuration object**

```yaml
apiVersion: ingressnodefirewall.openshift.io/v1alpha1
kind: IngressNodeFirewallConfig
metadata:
  name: ingressnodefirewallconfig
  namespace: openshift-ingress-node-firewall
spec:
  nodeSelector:
    node-role.kubernetes.io/worker: ""
  ebpfProgramManagerMode: <ebpf_mode>
```


where: 

`<ebpf_mode>`: Specifies whether or not the Ingress Node Firewall Operator uses the eBPF Manager Operator to manage eBPF programs. Must be either `true` or `false`. If unset, eBPF Manager is not used.
