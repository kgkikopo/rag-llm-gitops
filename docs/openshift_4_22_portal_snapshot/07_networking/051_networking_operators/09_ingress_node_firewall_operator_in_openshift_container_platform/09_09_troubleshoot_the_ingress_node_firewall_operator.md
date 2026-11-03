# 9.9. Troubleshoot the Ingress Node Firewall Operator

You can verify the status and view the logs to diagnose ingress firewall deployment or rule issues. 

**Procedure**

  * Run the following command to list installed Ingress Node Firewall custom resource definitions (CRD): 

```shell-session
$ oc get crds | grep ingressnodefirewall
```


**Example output**

```shell-session
NAME               READY   UP-TO-DATE   AVAILABLE   AGE
ingressnodefirewallconfigs.ingressnodefirewall.openshift.io       2022-08-25T10:03:01Z
ingressnodefirewallnodestates.ingressnodefirewall.openshift.io    2022-08-25T10:03:00Z
ingressnodefirewalls.ingressnodefirewall.openshift.io             2022-08-25T10:03:00Z
```


  * Run the following command to view the state of the Ingress Node Firewall Operator: 

```shell-session
$ oc get pods -n openshift-ingress-node-firewall
```


**Example output**

```shell-session
NAME                                       READY  STATUS         RESTARTS  AGE
ingress-node-firewall-controller-manager   2/2    Running        0         5d21h
ingress-node-firewall-daemon-pqx56         3/3    Running        0         5d21h
```


The following fields provide information about the status of the Operator: `READY`, `STATUS`, `AGE`, and `RESTARTS`. The `STATUS` field is `Running` when the Ingress Node Firewall Operator is deploying a daemon set to the assigned nodes. 

  * Run the following command to collect all ingress firewall node pods' logs: 

```shell-session
$ oc adm must-gather – gather_ingress_node_firewall
```


The logs are available in the sos node’s report containing eBPF `bpftool` outputs at `/sos_commands/ebpf`. These reports include lookup tables used or updated as the ingress firewall XDP handles packet processing, updates statistics, and emits events.
