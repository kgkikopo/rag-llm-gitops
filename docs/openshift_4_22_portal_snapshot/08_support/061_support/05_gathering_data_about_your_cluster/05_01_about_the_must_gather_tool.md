# 5.1. About the must-gather tool

The `oc adm must-gather` CLI command collects the information from your cluster that is most likely needed for debugging issues, including: 

  * Resource definitions 
  * Service logs 



By default, the `oc adm must-gather` command uses the default plugin image and writes into `./must-gather.local`. 

Alternatively, you can collect specific information by running the command with the appropriate arguments as described in the following sections: 

  * To collect data related to one or more specific features, use the `--image` argument with an image, as listed in a following section. 

For example: 

```shell-session
$ oc adm must-gather \
  --image=registry.redhat.io/container-native-virtualization/cnv-must-gather-rhel9:v4.22.9
```


  * To collect the audit logs, use the `-- /usr/bin/gather_audit_logs` argument, as described in a following section. 

For example: 

```shell-session
$ oc adm must-gather -- /usr/bin/gather_audit_logs
```


Note

    * Audit logs are not collected as part of the default set of information to reduce the size of the files. 
    * On a Windows operating system, install the `cwRsync` client and add to the `PATH` variable for use with the `oc rsync` command. 




When you run `oc adm must-gather`, a new pod with a random name is created in a new project on the cluster. The data is collected on that pod and saved in a new directory that starts with `must-gather.local` in the current working directory. 

For example: 

```shell-session
NAMESPACE                      NAME                 READY   STATUS      RESTARTS      AGE
...
openshift-must-gather-5drcj    must-gather-bklx4    2/2     Running     0             72s
openshift-must-gather-5drcj    must-gather-s8sdh    2/2     Running     0             72s
...
```


Optionally, you can run the `oc adm must-gather` command in a specific namespace by using the `--run-namespace` option. 

For example: 

```shell-session
$ oc adm must-gather --run-namespace <namespace> \
  --image=registry.redhat.io/container-native-virtualization/cnv-must-gather-rhel9:v4.22.9
```


## 5.1.1. Gathering data about your cluster for Red Hat Support

You can gather debugging information about your cluster by using the `oc adm must-gather` CLI command. 

If you are gathering information to debug a self-managed hosted cluster, see "Gathering information to troubleshoot hosted control planes". 

**Prerequisites**

  * You have access to the cluster as a user with the `cluster-admin` role. 
  * The OpenShift Container Platform CLI (`oc`) is installed. 



**Procedure**

  1. Navigate to the directory where you want to store the `must-gather` data. 

Note

If your cluster is in a disconnected environment, you must take additional steps. If your mirror registry has a trusted CA, you must first add the trusted CA to the cluster. For all clusters in disconnected environments, you must import the default `must-gather` image as an image stream. 

```shell-session
$ oc import-image is/must-gather -n openshift
```


  2. Run the `oc adm must-gather` command: 

```shell-session
$ oc adm must-gather
```


Important

If you are in a disconnected environment, use the `--image` flag as part of must-gather and point to the payload image. 

Note

Because this command picks a random control plane node by default, the pod might be scheduled to a control plane node that is in the `NotReady` and `SchedulingDisabled` state. 

     1. If this command fails, for example, if you cannot schedule a pod on your cluster, then use the `oc adm inspect` command to gather information for particular resources. 

Note

Contact Red Hat Support for the recommended resources to gather. 

  3. Create a compressed file from the `must-gather` directory that was just created in your working directory. Make sure you provide the date and cluster ID for the unique must-gather data. For more information about how to find the cluster ID, see [How to find the cluster-id or name on OpenShift cluster](https://access.redhat.com/solutions/5280291). For example, on a computer that uses a Linux operating system, run the following command: 

```shell-session
$ tar cvaf must-gather-`date +"%m-%d-%Y-%H-%M-%S"`-<cluster_id>.tar.gz <must_gather_local_dir>
```


where: 

`<must_gather_local_dir>`
     Replace with the actual directory name. 

  4. Attach the compressed file to your support case on the [the **Customer Support** page](https://access.redhat.com/support/cases/#/case/list) of the Red Hat Customer Portal.
