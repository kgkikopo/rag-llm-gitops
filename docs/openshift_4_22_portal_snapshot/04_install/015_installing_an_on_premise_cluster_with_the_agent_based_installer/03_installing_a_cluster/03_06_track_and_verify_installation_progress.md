# 3.6. Track and verify installation progress

After the installation has started, you can track installation progress and verify a successful installation. 

**Prerequisites**

  * You have configured a DNS record for the Kubernetes API server. 



**Procedure**

  1. Optional: To know when the bootstrap host (rendezvous host) reboots, run the following command: 

```shell-session
$ ./openshift-install --dir <install_directory> agent wait-for bootstrap-complete \
    --log-level=info
```


where: 

`--dir`
     specifies the path to the directory where the agent ISO was generated. 
`--log-level`
     Specifies the level of installation details. Valid values are `info`, `warn`, `debug`, and `error`. 

**Example output**

```shell-session
...................................................................
...................................................................
INFO Bootstrap configMap status is complete
INFO cluster bootstrap is complete
```


The command succeeds when the Kubernetes API server signals that it has been bootstrapped on the control plane machines. 

  2. Track the progress and verify successful installation by running the following command: 

```shell-session
$ openshift-install --dir <install_directory> agent wait-for install-complete 
```


1

```shell-session

```


Replace `<install_directory>` with the path to the directory where the agent ISO was generated. 

**Example output**

```shell-session
...................................................................
...................................................................
INFO Cluster is installed
INFO Install complete!
INFO To access the cluster as the system:admin user when using 'oc', run
INFO     export KUBECONFIG=/home/core/installer/auth/kubeconfig
INFO Access the OpenShift web-console here: https://console-openshift-console.apps.sno-cluster.test.example.com
```
