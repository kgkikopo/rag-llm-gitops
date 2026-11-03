# 4.2. Configure SR-IOV additional network

You can configure an additional network that uses SR-IOV hardware by creating an `SriovIBNetwork` object. When you create an `SriovIBNetwork` object, the SR-IOV Network Operator automatically creates a `NetworkAttachmentDefinition` object. 

Note

Do not modify or delete an `SriovIBNetwork` object if it is attached to any pods in a `running` state. 

**Prerequisites**

  * Install the OpenShift CLI (`oc`). 
  * Log in as a user with `cluster-admin` privileges. 



**Procedure**

  1. Create a `SriovIBNetwork` object, and then save the YAML in the `<name>.yaml` file, where `<name>` is a name for this additional network. The object specification might resemble the following example: 

```yaml
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovIBNetwork
metadata:
  name: attach1
  namespace: openshift-sriov-network-operator
spec:
  resourceName: net1
  networkNamespace: project2
  ipam: |-
    {
      "type": "host-local",
      "subnet": "10.56.217.0/24",
      "rangeStart": "10.56.217.171",
      "rangeEnd": "10.56.217.181",
      "gateway": "10.56.217.1"
    }
```


  2. To create the object, enter the following command: 

```shell-session
$ oc create -f <name>.yaml
```


where: 

`<name>`
     Specifies the name of the additional network. 

  3. Optional: To confirm that the `NetworkAttachmentDefinition` object that is associated with the `SriovIBNetwork` object that you created in the previous step exists, enter the following command. Replace `<namespace>` with the `networkNamespace` value you specified in the `SriovIBNetwork` object. 

```shell-session
$ oc get net-attach-def -n <namespace>
```
