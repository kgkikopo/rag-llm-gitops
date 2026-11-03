# 17.11. Managing device interrupt processing for guaranteed pod isolated CPUs

The Node Tuning Operator can manage host CPUs by dividing them into reserved CPUs for cluster and operating system housekeeping duties, including pod infra containers, and isolated CPUs for application containers to run the workloads. 

By completing these tasks, you can set CPUs for low-latency workloads as isolated workloads. 

Device interrupts are load balanced between all isolated and reserved CPUs to avoid CPUs being overloaded, with the exception of CPUs where there is a guaranteed pod running. Guaranteed pod CPUs are prevented from processing device interrupts when the relevant annotations are set for the pod. 

In the performance profile, `globallyDisableIrqLoadBalancing` is used to manage whether device interrupts are processed or not. For certain workloads, the reserved CPUs are not always sufficient for dealing with device interrupts, and for this reason, device interrupts are not globally disabled on the isolated CPUs. By default, Node Tuning Operator does not disable device interrupts on isolated CPUs. 

## 17.11.1. Finding the effective IRQ affinity setting for a node

Some IRQ controllers lack support for an IRQ affinity setting and might always expose all online CPUs as the IRQ mask. Because these IRQ controllers effectively run on CPU 0, you must find the effective IRQ affinity setting for a node. 

The following are examples of drivers and hardware that Red Hat are aware lack support for IRQ affinity setting. The list is, by no means, exhaustive: 

  * Some RAID controller drivers, such as `megaraid_sas`
  * Many non-volatile memory express (NVMe) drivers 
  * Some LAN on motherboard (LOM) network controllers 
  * The driver uses `managed_irqs`



Note

The reason they do not support IRQ affinity setting might be associated with factors such as the type of processor, the IRQ controller, or the circuitry connections in the motherboard. 

If the effective affinity of any IRQ is set to an isolated CPU, it might be a sign of some hardware or driver not supporting IRQ affinity setting. To find the effective affinity, log in to the host and run the following command: 

```shell-session
$ find /proc/irq -name effective_affinity -printf "%p: " -exec cat {} \;
```


**Example output**

```shell-session
/proc/irq/0/effective_affinity: 1
/proc/irq/1/effective_affinity: 8
/proc/irq/2/effective_affinity: 0
/proc/irq/3/effective_affinity: 1
/proc/irq/4/effective_affinity: 2
/proc/irq/5/effective_affinity: 1
/proc/irq/6/effective_affinity: 1
/proc/irq/7/effective_affinity: 1
/proc/irq/8/effective_affinity: 1
/proc/irq/9/effective_affinity: 2
/proc/irq/10/effective_affinity: 1
/proc/irq/11/effective_affinity: 1
/proc/irq/12/effective_affinity: 4
/proc/irq/13/effective_affinity: 1
/proc/irq/14/effective_affinity: 1
/proc/irq/15/effective_affinity: 1
/proc/irq/24/effective_affinity: 2
/proc/irq/25/effective_affinity: 4
/proc/irq/26/effective_affinity: 2
/proc/irq/27/effective_affinity: 1
/proc/irq/28/effective_affinity: 8
/proc/irq/29/effective_affinity: 4
/proc/irq/30/effective_affinity: 4
/proc/irq/31/effective_affinity: 8
/proc/irq/32/effective_affinity: 8
/proc/irq/33/effective_affinity: 1
/proc/irq/34/effective_affinity: 2
```


Some drivers use `managed_irqs`, whose affinity is managed internally by the kernel and userspace cannot change the affinity. In some cases, these IRQs might be assigned to isolated CPUs. For more information about `managed_irqs`, see "Affinity of managed interrupts cannot be changed even if they target isolated CPU". 

**Additional resources**

  * [Affinity of managed interrupts cannot be changed even if they target isolated CPU](https://access.redhat.com/solutions/4819541)



## 17.11.2. Configure node interrupt affinity

Configure a cluster node for IRQ dynamic load balancing to control which cores can receive device interrupt requests (IRQ). 

**Prerequisites**

  * For core isolation, all server hardware components must support IRQ affinity. To check if the hardware components of your server support IRQ affinity, view the hardware specifications of the server or contact your hardware provider. 



**Procedure**

  1. Log in to the OpenShift Container Platform cluster as a user with cluster-admin privileges. 
  2. Set the performance profile `apiVersion` to use `performance.openshift.io/v2`. 
  3. Remove the `globallyDisableIrqLoadBalancing` field or set it to `false`. 
  4. Set the appropriate isolated and reserved CPUs. The following snippet illustrates a profile that reserves 2 CPUs. IRQ load-balancing is enabled for pods running on the `isolated` CPU set: 

```yaml
apiVersion: performance.openshift.io/v2
kind: PerformanceProfile
metadata:
  name: dynamic-irq-profile
spec:
  cpu:
    isolated: 2-5
    reserved: 0-1
...
```


Note

When you configure reserved and isolated CPUs, operating system processes, kernel processes, and systemd services run on reserved CPUs. Infrastructure pods run on any CPU except where the low latency workload is running. Low latency workload pods run on exclusive CPUs from the isolated pool. For more information, see "Partitioning CPUs for infra and application containers".
