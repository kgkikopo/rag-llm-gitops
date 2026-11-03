# Chapter 4. Tracing Openflow with ovnkube-trace

To trace Open vSwitch and OVN traffic flows in OpenShift Container Platform, you can use the `ovnkube-trace` utility, which runs `ovn-trace`, `ovs-appctl ofproto/trace`, and `ovn-detrace` in a single correlated output. 

You can execute the `ovnkube-trace` binary from a dedicated container. For releases after OpenShift Container Platform 4.7, you can also copy the binary to a local host and execute it from that host.

- [4.1. Installing the ovnkube-trace on local host](04_01_installing_the_ovnkube_trace_on_local_host.md)
- [4.2. Running ovnkube-trace](04_02_running_ovnkube_trace.md)
- [4.3. Testing a default deny policy with ovnkube-trace](04_03_testing_a_default_deny_policy_with_ovnkube_trace.md)
- [4.4. Additional resources](04_04_additional_resources.md)
