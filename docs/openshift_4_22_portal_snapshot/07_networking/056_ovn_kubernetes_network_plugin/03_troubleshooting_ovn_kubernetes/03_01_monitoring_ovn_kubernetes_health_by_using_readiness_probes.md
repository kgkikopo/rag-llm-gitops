# 3.1. Monitoring OVN-Kubernetes health by using readiness probes

To monitor OVN-Kubernetes component health in OpenShift Container Platform, you can review readiness probe configuration and status for `ovnkube-control-plane` and `ovnkube-node` pods. 

**Prerequisites**

  * Access to the OpenShift CLI (`oc`). 
  * You have access to the cluster with `cluster-admin` privileges. 
  * You have installed `jq`. 



**Procedure**

  1. Review the details of the `ovnkube-node` readiness probe by running the following command: 

```shell-session
$ oc get pods -n openshift-ovn-kubernetes -l app=ovnkube-node \
-o json | jq '.items[0].spec.containers[] | .name,.readinessProbe'
```


The readiness probe for the northbound and southbound database containers in the `ovnkube-node` pod checks for the health of the databases and the `ovnkube-controller` container. 

The `ovnkube-controller` container in the `ovnkube-node` pod has a readiness probe to verify the presence of the OVN-Kubernetes CNI configuration file, the absence of which would indicate that the pod is not running or is not ready to accept requests to configure pods. 

  2. Show all events including the probe failures, for the namespace by using the following command: 

```shell-session
$ oc get events -n openshift-ovn-kubernetes
```


  3. Show the events for just a specific pod: 

```shell-session
$ oc describe pod ovnkube-node-9lqfk -n openshift-ovn-kubernetes
```


  4. Show the messages and statuses from the cluster network operator: 

```shell-session
$ oc get co/network -o json | jq '.status.conditions[]'
```


  5. Show the `ready` status of each container in `ovnkube-node` pods by running the following script: 

```shell-session
$ for p in $(oc get pods --selector app=ovnkube-node -n openshift-ovn-kubernetes \
-o jsonpath='{range.items[*]}{" "}{.metadata.name}'); do echo === $p ===;  \
oc get pods -n openshift-ovn-kubernetes $p -o json | jq '.status.containerStatuses[] | .name, .ready'; \
done
```


Note

The expectation is all container statuses are reporting as `true`. Failure of a readiness probe sets the status to `false`. 




**Additional resources**

  * [Monitoring application health by using health checks](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/building_applications/#application-health)
