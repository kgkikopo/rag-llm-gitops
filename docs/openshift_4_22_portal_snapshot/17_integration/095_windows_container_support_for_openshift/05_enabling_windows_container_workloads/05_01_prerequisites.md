# 5.1. Prerequisites

* You have access to an OpenShift Container Platform cluster using an account with `cluster-admin` permissions. 
  * You have installed the OpenShift CLI (`oc`). 
  * You have installed your cluster using one of the following infrastructures: 

    * Any installer-provisioned infrastructure 
    * A user-provisioned infrastructure with the `platform: none` field set in your `install-config.yaml` file 

  * You have configured hybrid networking with OVN-Kubernetes for your cluster. For more information, see "Configuring hybrid networking". 
  * You are running an OpenShift Container Platform cluster version 4.6.8 or later. 



Note

Windows instances deployed by the WMCO are configured with the containerd container runtime. Because WMCO installs and manages the runtime, it is recommended that you do not manually install containerd on nodes. 

For the comprehensive prerequisites for the Windows Machine Config Operator, see "Windows Machine Config Operator prerequisites".
