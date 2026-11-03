# 3.10. Creating the Kubernetes manifest and Ignition config files

Because you manually provision infrastructure, you must generate the Kubernetes manifest and Ignition config files that the cluster requires. 

The installation program converts the installation configuration into Kubernetes manifests and then wraps them into Ignition configuration files. You use these Ignition files to configure the cluster machines. 

Important

  * The Ignition config files that the OpenShift Container Platform installation program generates contain certificates that expire after 24 hours, which the system then renews. If you shut down the cluster before the system renews the certificates and you later restart the cluster after the 24 hours have elapsed, the cluster automatically recovers the expired certificates. The exception is that you must manually approve the pending `node-bootstrapper` certificate signing requests (CSRs) to recover kubelet certificates. See the documentation for _Recovering from expired control plane certificates_ for more information. 
  * Use Ignition config files within 12 hours after you generate them, because the 24-hour certificate rotates from 16 to 22 hours after you install the cluster. By using the Ignition config files within 12 hours, you can avoid installation failure if the certificate update runs during installation. 



Note

The installation program that generates the manifest and Ignition files is architecture specific. You can obtain it from the [client image mirror](https://mirror.openshift.com/pub/openshift-v4/ppc64le/clients/ocp/latest/). The Linux version of the installation program (without an architecture postfix) runs on ppc64le only. This installation program is also available as a macOS version. 

**Prerequisites**

  * You obtained the OpenShift Container Platform installation program. For a restricted network installation, these files are on your mirror host. 
  * You created the `install-config.yaml` installation configuration file. 



**Procedure**

  1. Change to the directory that contains the OpenShift Container Platform installation program and generate the Kubernetes manifests for the cluster: 

```shell-session
$ ./openshift-install create manifests --dir <installation_directory>
```


where: 

`<installation_directory>`
     Specifies the installation directory that contains the `install-config.yaml` file you created. 

Warning

If you are installing a three-node cluster, skip the following step to allow the control plane nodes to be schedulable. 

\+ 

Important

When you configure control plane nodes from the default unschedulable to schedulable, you require additional subscriptions because control plane nodes then become compute nodes. 

  2. Verify that the `mastersSchedulable` parameter in the `<installation_directory>/manifests/cluster-scheduler-02-config.yml` Kubernetes manifest file is set to `false`. This setting prevents pods from being scheduled on the control plane machines: 

     1. Open the `<installation_directory>/manifests/cluster-scheduler-02-config.yml` file. 
     2. Locate the `mastersSchedulable` parameter and verify that it is set to `false`. 
     3. Save and exit the file. 

  3. To create the Ignition configuration files, run the following command from the directory that contains the installation program: 

```shell-session
$ ./openshift-install create ignition-configs --dir <installation_directory>
```


where: 

`<installation_directory>`
    

Specifies the same installation directory. 

The installation program creates Ignition config files for the bootstrap, control plane, and compute nodes in the installation directory. The program also creates the `kubeadmin-password` and `kubeconfig` files in the `./<installation_directory>/auth` directory: 

```plaintext
.
├── auth
│   ├── kubeadmin-password
│   └── kubeconfig
├── bootstrap.ign
├── master.ign
├── metadata.json
└── worker.ign
```
