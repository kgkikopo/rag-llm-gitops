# 5.3. Creating persistent naming rules

In some cases, device names won’t persist following a reboot. For example, on R760xa systems Mellanox devices might be renamed after a reboot. You can avoid this problem by using a `MachineConfig` to set persistence. 

**Procedure**

  1. Gather the MAC address names from the worker nodes for the node into a file and provide names for the interfaces that need to persist. This example uses the file `70-persistent-net.rules` and stashes the details in it. 

```shell-session
$ cat <<EOF > 70-persistent-net.rules
SUBSYSTEM=="net",ACTION=="add",ATTR{address}=="b8:3f:d2:3b:51:28",ATTR{type}=="1",NAME="ibs2f0"
SUBSYSTEM=="net",ACTION=="add",ATTR{address}=="b8:3f:d2:3b:51:29",ATTR{type}=="1",NAME="ens8f0np0"
SUBSYSTEM=="net",ACTION=="add",ATTR{address}=="b8:3f:d2:f0:36:d0",ATTR{type}=="1",NAME="ibs2f0"
SUBSYSTEM=="net",ACTION=="add",ATTR{address}=="b8:3f:d2:f0:36:d1",ATTR{type}=="1",NAME="ens8f0np0"
EOF
```


  2. Convert that file into a base64 string without line breaks and set the output to the variable `PERSIST`: 

```shell-session
$ PERSIST=`cat 70-persistent-net.rules| base64 -w 0`
```


```shell-session
$ echo $PERSIST
```


```shell-session
U1VCU1lTVEVNPT0ibmV0IixBQ1RJT049PSJhZGQiLEFUVFJ7YWRkcmVzc309PSJiODozZjpkMjozYjo1MToyOCIsQVRUUnt0eXBlfT09IjEiLE5BTUU9ImliczJmMCIKU1VCU1lTVEVNPT0ibmV0IixBQ1RJT049PSJhZGQiLEFUVFJ7YWRkcmVzc309PSJiODozZjpkMjozYjo1MToyOSIsQVRUUnt0eXBlfT09IjEiLE5BTUU9ImVuczhmMG5wMCIKU1VCU1lTVEVNPT0ibmV0IixBQ1RJT049PSJhZGQiLEFUVFJ7YWRkcmVzc309PSJiODozZjpkMjpmMDozNjpkMCIsQVRUUnt0eXBlfT09IjEiLE5BTUU9ImliczJmMCIKU1VCU1lTVEVNPT0ibmV0IixBQ1RJT049PSJhZGQiLEFUVFJ7YWRkcmVzc309PSJiODozZjpkMjpmMDozNjpkMSIsQVRUUnt0eXBlfT09IjEiLE5BTUU9ImVuczhmMG5wMCIK
```


  3. Create a machine configuration and set the base64 encoding in the custom resource file by running the following command: 

```shell-session
$ cat <<EOF > 99-machine-config-udev-network.yaml
```


```yaml
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
   labels:
     machineconfiguration.openshift.io/role: worker
   name: 99-machine-config-udev-network
spec:
   config:
     ignition:
       version: 3.2.0
     storage:
       files:
       - contents:
           source: data:text/plain;base64,$PERSIST
         filesystem: root
         mode: 420
         path: /etc/udev/rules.d/70-persistent-net.rules
```


  4. Create the machine configuration on the cluster by running the following command. After running the command, the expected output shows `machineconfig.machineconfiguration.openshift.io/99-machine-config-udev-network created`. 

```shell-session
$ oc create -f 99-machine-config-udev-network.yaml
```


  5. Use the `get mcp` command to view the machine configuration status: 

```shell-session
$ oc get mcp
```


**Example output**

```shell-session
NAME     CONFIG                                             UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
master   rendered-master-9adfe851c2c14d9598eea5ec3df6c187   True      False      False      1              1                   1                     0                      6h21m
worker   rendered-worker-4568f1b174066b4b1a4de794cf538fee   False     True       False      2              0                   0                     0                      6h21m
```


The nodes will reboot and when the updating field returns to `false`, you can validate on the nodes by looking at the devices in a debug pod.
