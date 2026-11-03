# 14.1. About bare metal hosts and nodes

To provision a Red Hat Enterprise Linux CoreOS (RHCOS) bare-metal host as a node in your cluster, first create a `MachineSet` custom resource (CR) object that corresponds to bare-metal host hardware. 

Bare-metal host compute machine sets describe infrastructure components specific to your configuration. You apply specific Kubernetes labels to these compute machine sets and then update the infrastructure components to run on only those machines. 

When you scale up the relevant `MachineSet` CR that contains a `metal3.io/autoscale-to-hosts` annotation, `Machine` CRs are created automatically. OpenShift Container Platform uses `Machine` CRs to provision the bare-metal node that corresponds to the host as specified in the `MachineSet` CR.
