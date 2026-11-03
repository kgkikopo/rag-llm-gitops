# 5.12. OpenShift Container Platform installation on the hub cluster

The reference method for installing OpenShift Container Platform on the hub cluster uses the Agent-based Installer, which requires no additional centralized infrastructure. 

You can apply the reference configuration custom resources (CRs) manually or through ArgoCD after installation is complete. 

Description
    

The reference method for installing OpenShift Container Platform for the hub cluster is through the Agent-based Installer. 

Agent-based Installer provides installation capabilities without additional centralized infrastructure. The Agent-based Installer creates an ISO image, which you mount to the server to be installed. When you boot the server, OpenShift Container Platform is installed alongside optionally supplied extra manifests, such as Red Hat OpenShift GitOps custom resources. 

Note

You can also install OpenShift Container Platform in the hub cluster by using other installation methods. 

If hub cluster functions are being applied to an existing OpenShift Container Platform cluster, the Agent-based Installer installation is not required. The remaining steps to install Day 2 Operators and configure the cluster for these functions remains the same. When OpenShift Container Platform installation is complete, the set of additional Operators and their configuration must be installed on the hub cluster. 

The reference configuration includes all of these custom resources (CRs), which you can apply manually, for example: 

```shell-session
$ oc apply -f <reference_cr>
```


You can also add the reference configuration to the Git repository and apply it using ArgoCD. 

Note

If you apply the CRs manually, ensure you apply the CRs in the order of their dependencies. For example, apply namespaces before Operators and apply Operators before configurations. 

Limits and requirements
    

  * Agent-based Installer requires an accessible image repository containing all required OpenShift Container Platform and Day 2 Operator images. 
  * Agent-based Installer builds ISO images based on a specific OpenShift releases and specific cluster details. Installation of a second hub requires a separate ISO image to be built. 



Engineering considerations
    

  * Agent-based Installer provides a baseline OpenShift Container Platform installation. You apply Day 2 Operators and other configuration CRs after the cluster is installed. 
  * The reference configuration supports Agent-based Installer installation in a disconnected environment. 
  * A limited set of additional manifests can be supplied at installation time. 



**Additional resources**

  * [OpenShift Container Platform installation overview](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_overview/#installation-overview_ocp-installation-overview)
  * [Installing a cluster with customizations](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_an_on-premise_cluster_with_the_agent-based_installer/#installing-with-agent-based-installer)
  * [Preparing to install with the Agent-based Installer](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_an_on-premise_cluster_with_the_agent-based_installer/#preparing-to-install-with-agent-based-installer)
