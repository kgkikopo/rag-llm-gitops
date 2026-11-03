# 4.13. Creating the Kubernetes manifest and Ignition config files

Because you manually provision infrastructure, you must generate the Kubernetes manifest and Ignition config files that the cluster requires. 

The installation program converts the installation configuration into Kubernetes manifests and then wraps them into Ignition configuration files. You use these Ignition files to configure the cluster machines. 

Important

  * The Ignition config files that the OpenShift Container Platform installation program generates contain certificates that expire after 24 hours, which the system then renews. If you shut down the cluster before the system renews the certificates and you later restart the cluster after the 24 hours have elapsed, the cluster automatically recovers the expired certificates. The exception is that you must manually approve the pending `node-bootstrapper` certificate signing requests (CSRs) to recover kubelet certificates. See the documentation for _Recovering from expired control plane certificates_ for more information. 
  * Use Ignition config files within 12 hours after you generate them, because the 24-hour certificate rotates from 16 to 22 hours after you install the cluster. By using the Ignition config files within 12 hours, you can avoid installation failure if the certificate update runs during installation. 



**Prerequisites**

  * You obtained the OpenShift Container Platform installation program. 
  * You created the `install-config.yaml` installation configuration file. 



**Procedure**

  1. Change to the directory that contains the OpenShift Container Platform installation program and generate the Kubernetes manifests for the cluster: 

```shell-session
$ ./openshift-install create manifests --dir <installation_directory>
```


where: 

`<installation_directory>`
     Specifies the installation directory that contains the `install-config.yaml` file you created. 

  2. Remove the Kubernetes manifest files that define the control plane machines, compute machine sets, and control plane machine sets: 

```shell-session
$ rm -f openshift/99_openshift-cluster-api_master-machines-*.yaml openshift/99_openshift-cluster-api_worker-machineset-*.yaml openshift/99_openshift-machine-api_master-control-plane-machine-set.yaml
```


Because you create and manage these resources yourself, you do not have to initialize them. You can preserve the compute machine set files to create compute machines by using the machine API, but you must update references to them to match your environment. 

  3. Verify that the `mastersSchedulable` parameter in the `<installation_directory>/manifests/cluster-scheduler-02-config.yml` Kubernetes manifest file is set to `false`. This setting prevents pods from being scheduled on the control plane machines: 

     1. Open the `<installation_directory>/manifests/cluster-scheduler-02-config.yml` file. 
     2. Locate the `mastersSchedulable` parameter and verify that it is set to `false`. 
     3. Save and exit the file. 

  4. To create the Ignition configuration files, run the following command from the directory that contains the installation program: 

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


  5. Export the metadata file’s `infraID` key as an environment variable: 

```shell-session
$ export INFRA_ID=$(jq -r .infraID metadata.json)
```


Tip

Extract the `infraID` key from `metadata.json` and use it as a prefix for all of the RHOSP resources that you create. By doing so, you avoid name conflicts when making multiple deployments in the same project.
