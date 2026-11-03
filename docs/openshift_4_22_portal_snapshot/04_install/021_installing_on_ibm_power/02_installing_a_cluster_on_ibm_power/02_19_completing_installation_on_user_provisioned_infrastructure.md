# 2.19. Completing installation on user-provisioned infrastructure

To finalize the installation on user-provisioned infrastructure, complete the cluster deployment after configuring the Operators. This ensures the cluster is fully operational on the infrastructure that you provide. 

**Prerequisites**

  * Your control plane has initialized. 
  * You have completed the initial Operator configuration. 



**Procedure**

  1. Confirm that all the cluster components are online with the following command: 

```shell-session
$ watch -n5 oc get clusteroperators
```


**Example output**

```shell-session
NAME                                       VERSION   AVAILABLE   PROGRESSING   DEGRADED   SINCE
authentication                             4.22.0    True        False         False      19m
baremetal                                  4.22.0    True        False         False      37m
cloud-credential                           4.22.0    True        False         False      40m
cluster-autoscaler                         4.22.0    True        False         False      37m
config-operator                            4.22.0    True        False         False      38m
console                                    4.22.0    True        False         False      26m
csi-snapshot-controller                    4.22.0    True        False         False      37m
dns                                        4.22.0    True        False         False      37m
etcd                                       4.22.0    True        False         False      36m
image-registry                             4.22.0    True        False         False      31m
ingress                                    4.22.0    True        False         False      30m
insights                                   4.22.0    True        False         False      31m
kube-apiserver                             4.22.0    True        False         False      26m
kube-controller-manager                    4.22.0    True        False         False      36m
kube-scheduler                             4.22.0    True        False         False      36m
kube-storage-version-migrator              4.22.0    True        False         False      37m
machine-api                                4.22.0    True        False         False      29m
machine-approver                           4.22.0    True        False         False      37m
machine-config                             4.22.0    True        False         False      36m
marketplace                                4.22.0    True        False         False      37muser
monitoring                                 4.22.0    True        False         False      29m
network                                    4.22.0    True        False         False      38m
node-tuning                                4.22.0    True        False         False      37m
openshift-apiserver                        4.22.0    True        False         False      32muser
openshift-controller-manager               4.22.0    True        False         False      30m
openshift-samples                          4.22.0    True        False         False      32m
operator-lifecycle-manager                 4.22.0    True        False         False      37m
operator-lifecycle-manager-catalog         4.22.0    True        False         False      37m
operator-lifecycle-manager-packageserver   4.22.0    True        False         False      32m
service-ca                                 4.22.0    True        False         False      38m
storage                                    4.22.0    True        False         False      37m
```


Alternatively, the following command notifies you when all of the clusters are available. The command also retrieves and displays credentials: 

```shell-session
$ ./openshift-install --dir <installation_directory> wait-for install-complete
```


where: 

`<installation_directory>`
    

Specifies the path to the directory that you stored the installation files in. 

**Example output**

```shell-session
INFO Waiting up to 30m0s for the cluster to initialize...
```


The command succeeds when the Cluster Version Operator finishes deploying the OpenShift Container Platform cluster from Kubernetes API server. 

Important

     * The Ignition config files that the installation program generates contain certificates that expire after 24 hours, which are then renewed at that time. If the cluster is shut down before renewing the certificates and the cluster is later restarted after the 24 hours have elapsed, the cluster automatically recovers the expired certificates. The exception is that you must manually approve the pending `node-bootstrapper` certificate signing requests (CSRs) to recover kubelet certificates. See the documentation for _Recovering from expired control plane certificates_ for more information. 
     * It is recommended that you use Ignition config files within 12 hours after they are generated because the 24-hour certificate rotates from 16 to 22 hours after the cluster is installed. By using the Ignition config files within 12 hours, you can avoid installation failure if the certificate update runs during installation. 

  2. Confirm that the Kubernetes API server is communicating with the pods. 

     1. To view a list of all pods, use the following command: 

```shell-session
$ oc get pods --all-namespaces
```


**Example output**

```shell-session
NAMESPACE                         NAME                                            READY   STATUS      RESTARTS   AGE
openshift-apiserver-operator      openshift-apiserver-operator-85cb746d55-zqhs8   1/1     Running     1          9m
openshift-apiserver               apiserver-67b9g                                 1/1     Running     0          3m
openshift-apiserver               apiserver-ljcmx                                 1/1     Running     0          1m
openshift-apiserver               apiserver-z25h4                                 1/1     Running     0          2m
openshift-authentication-operator authentication-operator-69d5d8bf84-vh2n8        1/1     Running     0          5m
```


     2. View the logs for a pod that is listed in the output of the previous command by using the following command: 

```shell-session
$ oc logs <pod_name> -n <namespace>
```


where: 

`<namespace>`
    

Specifies the pod name and namespace, as shown in the output of an earlier command. 

If the pod logs display, the Kubernetes API server can communicate with the cluster machines. 

  3. Additional steps are required to enable multipathing. Do not enable multipathing during installation. 

See "Enabling multipathing with kernel arguments on RHCOS" in the _Postinstallation machine configuration tasks_ documentation for more information.
