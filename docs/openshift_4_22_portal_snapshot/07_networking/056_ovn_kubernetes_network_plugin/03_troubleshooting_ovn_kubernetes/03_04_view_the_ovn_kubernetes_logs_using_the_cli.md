# 3.4. View the OVN-Kubernetes logs using the CLI

To view OVN-Kubernetes pod logs in OpenShift Container Platform, you can use the OpenShift CLI (`oc`) to examine logs from containers in the `openshift-ovn-kubernetes` namespace. 

**Prerequisites**

  * Access to the cluster as a user with the `cluster-admin` role. 
  * Access to the OpenShift CLI (`oc`). 
  * You have installed `jq`. 



**Procedure**

  1. View the log for a specific pod: 

```shell-session
$ oc logs -f <pod_name> -c <container_name> -n <namespace>
```


where: 

`-f`
     Optional: Specifies that the output follows what is being written into the logs. 
`<pod_name>`
     Specifies the name of the pod. 
`<container_name>`
     Optional: Specifies the name of a container. When a pod has more than one container, you must specify the container name. 
`<namespace>`
     Specify the namespace the pod is running in. 

For example: 

```shell-session
$ oc logs ovnkube-node-5dx44 -n openshift-ovn-kubernetes
```


```shell-session
$ oc logs -f ovnkube-node-5dx44 -c ovnkube-controller -n openshift-ovn-kubernetes
```


The contents of log files are printed out. 

  2. Examine the most recent entries in all the containers in the `ovnkube-node` pods: 

```shell-session
$ for p in $(oc get pods --selector app=ovnkube-node -n openshift-ovn-kubernetes \
-o jsonpath='{range.items[*]}{" "}{.metadata.name}'); \
do echo === $p ===; for container in $(oc get pods -n openshift-ovn-kubernetes $p \
-o json | jq -r '.status.containerStatuses[] | .name');do echo ---$container---; \
oc logs -c $container $p -n openshift-ovn-kubernetes --tail=5; done; done
```


  3. View the last 5 lines of every log in every container in an `ovnkube-node` pod using the following command: 

```shell-session
$ oc logs -l app=ovnkube-node -n openshift-ovn-kubernetes --all-containers --tail 5
```
