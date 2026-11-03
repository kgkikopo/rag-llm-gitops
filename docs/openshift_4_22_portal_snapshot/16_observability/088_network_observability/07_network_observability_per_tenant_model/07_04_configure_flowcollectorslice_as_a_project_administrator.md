# 7.4. Configure FlowCollectorSlice as a project administrator

Project administrators can manage flow collection and data enrichment within their own namespaces by configuring a `FlowCollectorSlice` custom resource for decentralized network traffic analysis. 

**Prerequisites**

  * The Network Observability Operator is installed. 
  * You have `project-admin` permissions for the namespace. 



**Procedure**

  1. Create a YAML file named `flowCollectorSlice.yaml`: 

```yaml
apiVersion: flows.netobserv.io/v1alpha1
kind: FlowCollectorSlice
metadata:
  name: flowcollectorslice-sample
  namespace: my-app
spec:
  sampling: 1
  subnetLabels:
    - name: EXT:Database
      cidrs:
        - 192.168.50.0/24
```


  2. Apply the configuration by running the following command: 

```shell-session
$ oc apply -f flowCollectorSlice.yaml
```


**Verification**

  1. In the OpenShift Container Platform console, navigate to **Observe** **Network Traffic**. 
  2. Ensure flows to `192.168.50.0/24` subnet are observed with the `EXT:Database` label.
