# 5.2. Replacing a bare-metal control plane node

Replace a failed or unhealthy control plane node by removing the old `BareMetalHost` and `Machine` objects, then creating new ones to maintain cluster high availability. 

Important

If you reuse the `BareMetalHost` object definition from an existing control plane host, do not leave the `externallyProvisioned` field set to `true`. 

Existing control plane `BareMetalHost` objects might have the `externallyProvisioned` flag set to `true` if they were provisioned by the OpenShift Container Platform installation program. 

**Prerequisites**

  * You have access to the cluster as a user with the `cluster-admin` role. 
  * You have taken an etcd backup. 

Important

Take an etcd backup before performing this procedure so that you can restore your cluster if you encounter any issues. For more information about taking an etcd backup, see the _Additional resources_ section. 




**Procedure**

  1. Ensure that the Bare Metal Operator is available: 

```shell-session
$ oc get clusteroperator bare-metal
```


**Example output**

```shell-session
NAME        VERSION   AVAILABLE   PROGRESSING   DEGRADED   SINCE   MESSAGE
baremetal   4.22     True          False      False   3d15h
```


  2. Remove the old `BareMetalHost` and `Machine` objects: 

```shell-session
$ oc delete bmh -n openshift-machine-api <host_name>
```


```shell-session
$ oc delete machine -n openshift-machine-api <machine_name>
```


Replace `<host_name>` with the name of the host and `<machine_name>` with the name of the machine. The machine name is displayed under the `CONSUMER` field. 

After you remove the `BareMetalHost` and `Machine` objects, then the machine controller automatically deletes the `Node` object. 

  3. Create the new `BareMetalHost` object and the secret to store the BMC credentials. Set the following parameters: 

`spec.bmc.credentialsName: control-plane-<num>-bmc-secret`
     Specifies the BMC credentials secret name. Replace `<num>` with the control plane number of the bare-metal node in the `name` fields and the `credentialsName` field. 
`data.username: <base64_of_uid>`
     Specifies the base64-encoded user name. Replace `<base64_of_uid>` with the `base64` string of the user name. 
`data.password: <base64_of_pwd>`
     Specifies the base64-encoded password. Replace `<base64_of_pwd>` with the `base64` string of the password. 
`spec.bmc.address: <protocol>://<bmc_ip>`
     Specifies the BMC address. Replace `<protocol>` with the BMC protocol, such as `redfish`, `redfish-virtualmedia`, `idrac-virtualmedia`, or others. Replace `<bmc_ip>` with the IP address of the bare-metal node’s baseboard management controller. For additional BMC configuration options, see "BMC addressing" in the _Additional resources_ section. 
`spec.bootMACAddress: <NIC1_mac_address>`
     Specifies the MAC address of the bare-metal node’s first NIC. Replace `<NIC1_mac_address>` with the MAC address. 

  4. Run the following command: 

```shell-session
$ cat <<EOF | oc apply -f -
```


```yaml
apiVersion: v1
kind: Secret
metadata:
  name: control-plane-<num>-bmc-secret
  namespace: openshift-machine-api
data:
  username: <base64_of_uid>
  password: <base64_of_pwd>
type: Opaque
---
apiVersion: metal3.io/v1alpha1
kind: BareMetalHost
metadata:
  name: control-plane-<num>
  namespace: openshift-machine-api
spec:
  automatedCleaningMode: disabled
  bmc:
    address: <protocol>://<bmc_ip>
    credentialsName: control-plane-<num>-bmc-secret
  bootMACAddress: <NIC1_mac_address>
  bootMode: UEFI
  externallyProvisioned: false
  online: true
EOF
```


After the inspection is complete, the `BareMetalHost` object is created and available to be provisioned. 

  5. View available `BareMetalHost` objects: 

```shell-session
$ oc get bmh -n openshift-machine-api
```


**Example output**

```shell-session
NAME                          STATE                    CONSUMER                   ONLINE   ERROR   AGE
control-plane-1.example.com   available                control-plane-1            true             1h10m
control-plane-2.example.com   externally provisioned   control-plane-2            true             4h53m
control-plane-3.example.com   externally provisioned   control-plane-3            true             4h53m
compute-1.example.com         provisioned              compute-1-ktmmx            true             4h53m
compute-1.example.com         provisioned              compute-2-l2zmb            true             4h53m
```


Note

There are no `MachineSet` objects for control plane nodes, so you must create a `Machine` object instead. You can copy the `providerSpec` from another control plane `Machine` object. 

  6. Create a `Machine` object: 

```shell-session
$ cat <<EOF | oc apply -f -
apiVersion: machine.openshift.io/v1beta1
kind: Machine
metadata:
  annotations:
    metal3.io/BareMetalHost: openshift-machine-api/control-plane-<num>
  labels:
    machine.openshift.io/cluster-api-cluster: control-plane-<num>
    machine.openshift.io/cluster-api-machine-role: master
    machine.openshift.io/cluster-api-machine-type: master
  name: control-plane-<num>
  namespace: openshift-machine-api
spec:
  metadata: {}
  providerSpec:
    value:
      apiVersion: baremetal.cluster.k8s.io/v1alpha1
      customDeploy:
        method: install_coreos
      hostSelector: {}
      image:
        checksum: ""
        url: ""
      kind: BareMetalMachineProviderSpec
      metadata:
        creationTimestamp: null
      userData:
        name: master-user-data-managed
EOF
```


Replace `<num>` with the control plane number of the bare-metal node in the `annotations`, `labels` and `name` fields. 

  7. To view the `BareMetalHost` objects, run the following command: 

```shell-session
$ oc get bmh -A
```


**Example output**

```shell-session
NAME                          STATE                    CONSUMER                   ONLINE   ERROR   AGE
control-plane-1.example.com   provisioned              control-plane-1            true             2h53m
control-plane-2.example.com   externally provisioned   control-plane-2            true             5h53m
control-plane-3.example.com   externally provisioned   control-plane-3            true             5h53m
compute-1.example.com         provisioned              compute-1-ktmmx            true             5h53m
compute-2.example.com         provisioned              compute-2-l2zmb            true             5h53m
```


  8. After the RHCOS installation, verify that the `BareMetalHost` is added to the cluster: 

```shell-session
$ oc get nodes
```


**Example output**

```shell-session
NAME                           STATUS      ROLES     AGE   VERSION
control-plane-1.example.com    available   master    4m2s  v1.35.4
control-plane-2.example.com    available   master    141m  v1.35.4
control-plane-3.example.com    available   master    141m  v1.35.4
compute-1.example.com          available   worker    87m   v1.35.4
compute-2.example.com          available   worker    87m   v1.35.4
```


Note

After replacement of the new control plane node, the etcd pod running in the new node is in `crashloopback` status. See "Replacing an unhealthy etcd member" in the _Additional resources_ section for more information. 




**Additional resources**

  * [Replacing an unhealthy etcd member](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/backup_and_restore/#replacing-the-unhealthy-etcd-member)
  * [Backing up etcd](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/backup_and_restore/#backing-up-etcd-data_backup-etcd)
  * [Configuration using the Bare Metal Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_bare_metal/bare-metal-post-installation-configuration#bmo-config-using-bare-metal-operator_bare-metal-postinstallation-configuration "4.10. Configuration using the Bare Metal Operator")
  * [BMC addressing](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_bare_metal/installer-provisioned-infrastructure#bmc-addressing_ipi-install-installation-workflow "3.3.15.2. BMC addressing")
