# 2.9. Restoring the network

If you want to reconnect a disconnected cluster and pull images from online registries, delete the cluster’s ImageContentSourcePolicy (ICSP) objects. Without the ICSP, pull requests to external registries are no longer redirected to the mirror registry. 

**Procedure**

  1. View the ICSP objects in your cluster: 

```shell-session
$ oc get imagecontentsourcepolicy
```


**Example output**

```shell-session
NAME                 AGE
mirror-ocp           6d20h
ocp4-index-0         6d18h
qe45-index-0         6d15h
```


  2. Delete all the ICSP objects you created when disconnecting your cluster: 

```shell-session
$ oc delete imagecontentsourcepolicy <icsp_name> <icsp_name> <icsp_name>
```


For example: 

```shell-session
$ oc delete imagecontentsourcepolicy mirror-ocp ocp4-index-0 qe45-index-0
```


**Example output**

```shell-session
imagecontentsourcepolicy.operator.openshift.io "mirror-ocp" deleted
imagecontentsourcepolicy.operator.openshift.io "ocp4-index-0" deleted
imagecontentsourcepolicy.operator.openshift.io "qe45-index-0" deleted
```


  3. Wait for all the nodes to restart and return to the READY status and verify that the `registries.conf` file is pointing to the original registries and not the mirror registries: 

     1. Log in to a node: 

```shell-session
$ oc debug node/<node_name>
```


     2. Set `/host` as the root directory within the debug shell: 

```shell-session
sh-4.4# chroot /host
```


     3. Examine the `registries.conf` file: 

```shell-session
sh-4.4# cat /etc/containers/registries.conf
```


**Example output**

```shell-session
unqualified-search-registries = ["registry.access.redhat.com", "docker.io"]
```


The `registry` and `registry.mirror` entries created by the ICSPs you deleted are removed.
