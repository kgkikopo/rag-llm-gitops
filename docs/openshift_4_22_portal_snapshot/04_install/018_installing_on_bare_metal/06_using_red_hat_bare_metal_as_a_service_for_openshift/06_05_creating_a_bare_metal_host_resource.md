# 6.5. Creating a bare-metal host resource

To deploy a bare-metal host, you must create a `BareMetalHost` resource. 

**Procedure**

  1. Create a `BareMetalHost` custom resource (CR) file by running the following command: 

```shell-session
$ vim bmaas-<name>-bmh.yaml
```


<name>
     Replace `<name>` with the name of the bare-metal host. 

  2. Edit the CR: 

```yaml
apiVersion: metal3.io/v1alpha1
kind: BareMetalHost
metadata:
  name: bmaas-<name>
  namespace:  bmaas
spec:
  online: true
  bootMACAddress: <mac_addr>
  bmc:
    address: redfish-virtualmedia+<address>/redfish/v1/Systems/System.Embedded.1
    credentialsName: bmaas-<num>-bmc-secret
```


<mac_addr>
     Replace `<mac_addr>` with the MAC address of the first NIC on the bare-metal host. 
<address>
     Replace `<address>` with IP address or FQDN of the host. 

  3. Apply the CR by running the following command: 

```shell-session
$ oc apply -f bmaas-<name>-bmh.yaml
```


**Verification**

  * Check the `BareMetalHost` state by running the following command: 

```shell-session
$ oc get baremetalhost -n bmaas
```


The state progresses from **registering** , to **inspecting** , and finally to **available**.
