# 2.5. Generate ingress network flow data using the commatrix plugin

Use the `commatrix` plugin for the `oc` command to generate ingress network flow data from your cluster and identify any differences between open ports on the host and expected ingress flows for your environment. 

The plugin generates ingress flows to OpenShift Container Platform services for the following environments: 

  * OpenShift Container Platform on bare metal 
  * Single-node OpenShift with other platforms 
  * OpenShift Container Platform on Amazon Web Services (AWS) 
  * Single-node OpenShift on AWS 



**Prerequisites**

  * You installed the OpenShift CLI (`oc`). 
  * You logged in as a user with `cluster-admin` privileges. 
  * You installed Podman. 
  * You installed the `commatrix` plugin. 



**Procedure**

  1. Generate network flow data by running the following command: 

```bash
$ oc commatrix generate
```


Note

By default, the plugin generates the network flow data in CSV format in a `communication-matrix` directory in your current working directory. 




**Verification**

  * View the generated network flow data in the `communication-matrix` directory by running the following command: 

```bash
$ cat communication-matrix/communication-matrix.csv
```


```bash
Direction,Protocol,Port,Namespace,Service,Pod,Container,Node Role,Optional
Ingress,TCP,4194,kube-system,kubelet,konnectivity-agent,,,false
Ingress,TCP,9100,openshift-monitoring,node-exporter,node-exporter,kube-rbac-proxy,,false
Ingress,TCP,9103,openshift-ovn-kubernetes,ovn-kubernetes-node,ovnkube-node,kube-rbac-proxy-node,,false

...
```
