# 3.12. Waiting for the bootstrap process to complete

After your cluster nodes first boot into the persistent RHCOS environment installed to disk, wait for the OpenShift Container Platform bootstrap process to complete. 

The configuration information provided through the Ignition config files is used to initialize the bootstrap process and install OpenShift Container Platform on the machines. 

**Prerequisites**

  * You have created the Ignition config files for your cluster. 
  * You have configured suitable network, DNS, and load balancing infrastructure. 
  * You have obtained the installation program and generated the Ignition config files for your cluster. 
  * You installed RHCOS on your cluster machines and provided the Ignition config files that the OpenShift Container Platform installation program generated. 



**Procedure**

  1. Monitor the bootstrap process: 

```shell-session
$ ./openshift-install --dir <installation_directory> wait-for bootstrap-complete \
    --log-level=info
```


where: 

`<installation_directory>`
     Specifies the path to the directory that stores the installation files. 
`--log-level=info`
    

Specifies `warn`, `debug`, or `error` instead of `info` to view different installation details. 

**Example output**

```shell-session
INFO Waiting up to 20m0s for the Kubernetes API at https://api.test.example.com:6443...
INFO API v1.35.4 up
INFO Waiting up to 1h0m0s for bootstrapping to complete...
INFO It is now safe to remove the bootstrap resources
```


The bootstrapping completion wait time varies per platform. 

The command succeeds when the Kubernetes API server signals that it has been bootstrapped on the control plane machines. 

  2. After the bootstrap process is complete, remove the bootstrap machine from the load balancer. 

Important

You must remove the bootstrap machine from the load balancer at this point. You can also remove or reformat the bootstrap machine itself.
