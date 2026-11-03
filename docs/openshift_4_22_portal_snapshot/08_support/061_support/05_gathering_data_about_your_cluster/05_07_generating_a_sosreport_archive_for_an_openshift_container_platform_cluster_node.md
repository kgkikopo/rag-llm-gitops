# 5.7. Generating a sosreport archive for an OpenShift Container Platform cluster node

The recommended way to generate a `sosreport` for an OpenShift Container Platform 4.22 cluster node is through a debug pod. 

**Prerequisites**

  * You have access to the cluster as a user with the `cluster-admin` role. 
  * You have SSH access to your hosts. 
  * You have installed the OpenShift CLI (`oc`). 
  * You have a Red Hat standard or premium Subscription. 
  * You have a Red Hat Customer Portal account. 
  * You have an existing Red Hat Support case ID. 



**Procedure**

  1. Obtain a list of cluster nodes: 

```shell-session
$ oc get nodes
```


  2. Enter into a debug session on the target node. This step instantiates a debug pod called `<node_name>-debug`: 

```shell-session
$ oc debug node/my-cluster-node
```


To enter into a debug session on the target node that is tainted with the `NoExecute` effect, add a toleration to a dummy namespace, and start the debug pod in the dummy namespace: 

```shell-session
$ oc new-project dummy
```


```shell-session
$ oc patch namespace dummy --type=merge -p '{"metadata": {"annotations": { "scheduler.alpha.kubernetes.io/defaultTolerations": "[{\"operator\": \"Exists\"}]"}}}'
```


```shell-session
$ oc debug node/my-cluster-node
```


  3. Set `/host` as the root directory within the debug shell. The debug pod mounts the host’s root file system in `/host` within the pod. By changing the root directory to `/host`, you can run binaries contained in the host’s executable paths: 

```shell-session
# chroot /host
```


Note

OpenShift Container Platform 4.22 cluster nodes running Red Hat Enterprise Linux CoreOS (RHCOS) are immutable and rely on Operators to apply cluster changes. Accessing cluster nodes by using SSH is not recommended. However, if the OpenShift Container Platform API is not available, or the kubelet is not properly functioning on the target node, `oc` operations will be impacted. In such situations, it is possible to access nodes using `ssh core@<node>.<cluster_name>.<base_domain>` instead. 

  4. Start a `toolbox` container, which includes the required binaries and plugins to run `sosreport`: 

```shell-session
# toolbox
```


Note

If an existing `toolbox` pod is already running, the `toolbox` command outputs `'toolbox-' already exists. Trying to start…​`. Remove the running toolbox container with `podman rm toolbox-` and spawn a new toolbox container, to avoid issues with `sosreport` plugins. 

  5. Collect a `sosreport` archive. 

     1. Run the `sos report` command to collect necessary troubleshooting data on `crio` and `podman`: 

```shell-session
# sos report -k crio.all=on -k crio.logs=on  -k podman.all=on -k podman.logs=on
```


where
    

        * `-k` enables you to define `sosreport` plugin parameters outside of the defaults. 

     2. Optional: To include information on OVN-Kubernetes networking configurations from a node in your report, run the following command: 

```shell-session
# sos report --all-logs
```


     3. Press **Enter** when prompted, to continue. 
     4. Provide the Red Hat Support case ID. `sosreport` adds the ID to the archive’s file name. 
     5. The `sosreport` output provides the archive’s location and checksum. The following sample output references support case ID `01234567`: 

```shell-session
Your sosreport has been generated and saved in:
  /host/var/tmp/sosreport-my-cluster-node-01234567-2020-05-28-eyjknxt.tar.xz

The checksum is: 382ffc167510fd71b4f12a4f40b97a4e
```


where
    

        * The `sosreport` archive’s file path is outside of the `chroot` environment because the toolbox container mounts the host’s root directory at `/host`. 

  6. Provide the `sosreport` archive to Red Hat Support for analysis, using one of the following methods. 

     * Upload the file to an existing Red Hat support case. 

       1. Concatenate the `sosreport` archive by running the `oc debug node/<node_name>` command and redirect the output to a file. This command assumes you have exited the previous `oc debug` session: 

```shell-session
$ oc debug node/my-cluster-node -- bash -c 'cat /host/var/tmp/sosreport-my-cluster-node-01234567-2020-05-28-eyjknxt.tar.xz' > /tmp/sosreport-my-cluster-node-01234567-2020-05-28-eyjknxt.tar.xz
```


where
    

     * The debug container mounts the host’s root directory at `/host`. Reference the absolute path from the debug container’s root directory, including `/host`, when specifying target files for concatenation. 

Note

OpenShift Container Platform 4.22 cluster nodes running Red Hat Enterprise Linux CoreOS (RHCOS) are immutable and rely on Operators to apply cluster changes. Transferring a `sosreport` archive from a cluster node by using `scp` is not recommended. However, if the OpenShift Container Platform API is not available, or the kubelet is not properly functioning on the target node, `oc` operations will be impacted. In such situations, it is possible to copy a `sosreport` archive from a node by running `scp core@<node>.<cluster_name>.<base_domain>:<file_path> <local_path>`. 

       1. Navigate to an existing support case within [the **Customer Support** page](https://access.redhat.com/support/cases/#/case/list) of the Red Hat Customer Portal. 
       2. Select **Attach files** and follow the prompts to upload the file.
