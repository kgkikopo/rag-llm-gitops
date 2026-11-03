# 9.5. Ensure high disk performance with HyperPAV on z/VM

To improve I/O performance for Direct Access Storage Devices (DASD) disks in z/VM, configure HyperPAV alias devices. To increase control plane and compute node throughput, add YAML configurations with full-pack minidisks to Machine Config Operator (MCO) profiles for IBM Z clusters. 

DASD and Extended Count Key Data (ECKD) devices are commonly used disk types in IBM Z® environments. In a typical OpenShift Container Platform setup in z/VM environments, DASD disks are commonly used to support the local storage for the nodes. You can set up HyperPAV alias devices to provide more throughput and overall better I/O performance for the DASD disks that support the z/VM guests. 

Using HyperPAV for the local storage devices leads to a significant performance benefit. However, be aware of the trade-off between throughput and CPU costs. 

**Procedure**

  1. Copy the following MCO sample profile into a YAML file for the control plane node. For example, `05-master-kernelarg-hpav.yaml`: 

```shell-session
$ cat 05-master-kernelarg-hpav.yaml
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: master
  name: 05-master-kernelarg-hpav
spec:
  config:
    ignition:
      version: 3.1.0
  kernelArguments:
    - rd.dasd=800-805
# ...
```


  2. Copy the following MCO sample profile into a YAML file for the compute node. For example, `05-worker-kernelarg-hpav.yaml`: 

```shell-session
$ cat 05-worker-kernelarg-hpav.yaml
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: worker
  name: 05-worker-kernelarg-hpav
spec:
  config:
    ignition:
      version: 3.1.0
  kernelArguments:
    - rd.dasd=800-805
# ...
```


Note

You must modify the `rd.dasd` arguments to fit the device IDs. 

  3. Create the MCO profiles by entering the following commands: 

```shell-session
$ oc create -f 05-master-kernelarg-hpav.yaml
```


```shell-session
$ oc create -f 05-worker-kernelarg-hpav.yaml
```


  4. To deactivate the MCO profiles, enter the following commands: 

```shell-session
$ oc delete -f 05-master-kernelarg-hpav.yaml
```


```shell-session
$ oc delete -f 05-worker-kernelarg-hpav.yaml
```


**Additional resources**

  * [Using HyperPAV for ECKD DASD](https://www.ibm.com/docs/en/linux-on-systems?topic=io-using-hyperpav-eckd-dasd)
  * [Scaling HyperPAV alias devices on Linux guests on z/VM](https://public.dhe.ibm.com/software/dw/linux390/perf/zvm_hpav00.pdf)
