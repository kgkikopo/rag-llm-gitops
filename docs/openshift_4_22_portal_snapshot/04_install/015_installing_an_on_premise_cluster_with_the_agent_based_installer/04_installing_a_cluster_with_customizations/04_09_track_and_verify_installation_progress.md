# 4.9. Track and verify installation progress

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


Note

If you are using the optional method of GitOps ZTP manifests, you can configure IP address endpoints for cluster nodes through the `AgentClusterInstall.yaml` file in three ways: 

     * IPv4 
     * IPv6 
     * IPv4 and IPv6 in parallel (dual-stack) 

IPv6 is supported only on bare metal platforms. 

**Example of dual-stack networking**

```yaml
apiVIP: 192.168.11.3
ingressVIP: 192.168.11.4
clusterDeploymentRef:
  name: mycluster
imageSetRef:
  name: openshift-4.22
networking:
  clusterNetwork:
  - cidr: 172.21.0.0/16
    hostPrefix: 23
  - cidr: fd02::/48
    hostPrefix: 64
  machineNetwork:
  - cidr: 192.168.11.0/16
  - cidr: 2001:DB8::/32
  serviceNetwork:
  - 172.22.0.0/16
  - fd03::/112
  networkType: OVNKubernetes
```
