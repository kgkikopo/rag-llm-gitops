# 6.6. Update the FlowCollector resource

As an alternative to using the web console, use the `oc patch` command with the `flowcollector` custom resource to quickly update specific specifications, such as eBPF sampling 

**Procedure**

  1. Run the following command to patch the `flowcollector` CR and update the `spec.agent.ebpf.sampling` value: 

```shell-session
$ oc patch flowcollector cluster --type=json -p "[{"op": "replace", "path": "/spec/agent/ebpf/sampling", "value": <new value>}] -n netobserv"
```
