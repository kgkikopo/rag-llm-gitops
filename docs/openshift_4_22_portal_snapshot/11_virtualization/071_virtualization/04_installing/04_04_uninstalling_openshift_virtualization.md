# 4.4. Uninstalling OpenShift Virtualization

You can uninstall OpenShift Virtualization by using the web console or the command-line interface (CLI) to delete OpenShift Virtualization workloads, the Operator, and its resources. 

To uninstall OpenShift Virtualization, perform the following tasks: 

  1. Delete the `HyperConverged` CR. 
  2. Delete the OpenShift Virtualization Operator. 
  3. Delete the `openshift-cnv` namespace. 
  4. Delete the OpenShift Virtualization custom resource definitions (CRDs). 



## 4.4.1. Prerequisites

  * Delete all virtual machine instances. You cannot uninstall OpenShift Virtualization while its workloads remain on the cluster. 



## 4.4.2. Delete the HyperConverged custom resource

To uninstall OpenShift Virtualization, you first delete the `HyperConverged` custom resource (CR). 

**Prerequisites**

  * You have access to an OpenShift Container Platform cluster using an account with `cluster-admin` permissions. 



**Procedure**

  1. Navigate to the **Ecosystem** **Installed Operators** page. 
  2. Select the OpenShift Virtualization Operator. 
  3. Click the **OpenShift Virtualization Deployment** tab. 
  4. Click the Options menu ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Virtualization-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) beside `kubevirt-hyperconverged` and select **Delete HyperConverged**. 
  5. Click **Delete** in the confirmation window. 



## 4.4.3. Deleting Operators from a cluster using the web console

Cluster administrators can delete installed Operators from a selected namespace by using the web console. 

Warning

Failed Operator installations do not automatically remove created permissions. Audit and remove remaining permissions to secure the namespace. 

For more information, see [Audit and secure delegated Operator installations (Red Hat Knowledgebase)](https://access.redhat.com/articles/7149230). 

**Prerequisites**

  * You have access to the OpenShift Container Platform cluster web console using an account with `cluster-admin` permissions. 



**Procedure**

  1. Navigate to the **Ecosystem** **Installed Operators** page. 
  2. Scroll or enter a keyword into the **Filter by name** field to find the Operator that you want to remove. Then, click on it. 
  3. On the right side of the **Operator Details** page, select **Uninstall Operator** from the **Actions** list. 

An **Uninstall Operator?** dialog box is displayed. 

  4. Select **Uninstall** to remove the Operator, Operator deployments, and pods. Following this action, the Operator stops running and no longer receives updates. 

Note

This action does not remove resources managed by the Operator, including custom resource definitions (CRDs) and custom resources (CRs). Dashboards and navigation items enabled by the web console and off-cluster resources that continue to run might need manual clean up. To remove these after uninstalling the Operator, you might need to manually delete the Operator CRDs. 




## 4.4.4. Delete a namespace using the web console

You can delete a namespace by using the OpenShift Container Platform web console. 

**Prerequisites**

  * You have access to the OpenShift Container Platform cluster using an account with `cluster-admin` permissions. 



**Procedure**

  1. Navigate to **Administration** **Namespaces**. 
  2. Locate the namespace that you want to delete in the list of namespaces. 
  3. On the far right side of the namespace listing, select **Delete Namespace** from the Options menu ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Virtualization-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) . 
  4. When the **Delete Namespace** pane opens, enter the name of the namespace that you want to delete in the field. 
  5. Click **Delete**. 



## 4.4.5. Delete OpenShift Virtualization custom resource definitions

You can delete the OpenShift Virtualization custom resource definitions (CRDs) by using the web console. 

**Prerequisites**

  * You have access to the OpenShift Container Platform cluster using an account with `cluster-admin` permissions. 



**Procedure**

  1. Navigate to **Administration** **CustomResourceDefinitions**. 
  2. Select the **Label** filter and enter `operators.coreos.com/kubevirt-hyperconverged.openshift-cnv` in the **Search** field to display the OpenShift Virtualization CRDs. 
  3. Click the Options menu ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Virtualization-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) beside each CRD and select **Delete CustomResourceDefinition**. 



## 4.4.6. Uninstall OpenShift Virtualization by using the CLI

You can uninstall OpenShift Virtualization by using the OpenShift CLI (`oc`). 

**Prerequisites**

  * You have access to the OpenShift Container Platform cluster using an account with `cluster-admin` permissions. 
  * You have installed the OpenShift CLI (`oc`). 
  * You have deleted all virtual machines and virtual machine instances. You cannot uninstall OpenShift Virtualization while its workloads remain on the cluster. 



**Procedure**

  1. Delete the `HyperConverged` custom resource: 

```shell-session
$ oc delete HyperConverged kubevirt-hyperconverged -n openshift-cnv
```


  2. Delete the OpenShift Virtualization Operator subscription: 

```shell-session
$ oc delete subscription hco-operatorhub -n openshift-cnv
```


  3. Delete the OpenShift Virtualization `ClusterServiceVersion` resource: 

```shell-session
$ oc delete csv -n openshift-cnv -l operators.coreos.com/kubevirt-hyperconverged.openshift-cnv
```


  4. Delete the OpenShift Virtualization namespace: 

```shell-session
$ oc delete namespace openshift-cnv
```


  5. List the OpenShift Virtualization custom resource definitions (CRDs) by running the `oc delete crd` command with the `dry-run` option: 

```shell-session
$ oc delete crd --dry-run=client -l operators.coreos.com/kubevirt-hyperconverged.openshift-cnv
```


Example output: 

```plaintext
customresourcedefinition.apiextensions.k8s.io "cdis.cdi.kubevirt.io" deleted (dry run)
customresourcedefinition.apiextensions.k8s.io "hostpathprovisioners.hostpathprovisioner.kubevirt.io" deleted (dry run)
customresourcedefinition.apiextensions.k8s.io "hyperconvergeds.hco.kubevirt.io" deleted (dry run)
customresourcedefinition.apiextensions.k8s.io "kubevirts.kubevirt.io" deleted (dry run)
customresourcedefinition.apiextensions.k8s.io "networkaddonsconfigs.networkaddonsoperator.network.kubevirt.io" deleted (dry run)
customresourcedefinition.apiextensions.k8s.io "ssps.ssp.kubevirt.io" deleted (dry run)
customresourcedefinition.apiextensions.k8s.io "tektontasks.tektontasks.kubevirt.io" deleted (dry run)
```


  6. Delete the CRDs by running the `oc delete crd` command without the `dry-run` option: 

```shell-session
$ oc delete crd -l operators.coreos.com/kubevirt-hyperconverged.openshift-cnv
```


## 4.4.7. Additional resources

  * [Deleting the `HyperConverged` custom resource](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/installing#virt-deleting-deployment-custom-resource_uninstalling-virt "4.4.2. Delete the HyperConverged custom resource")
  * [Deleting Operators from a cluster using the web console](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/installing#olm-deleting-operators-from-a-cluster-using-web-console_uninstalling-virt "4.4.3. Deleting Operators from a cluster using the web console")
  * [Deleting a namespace using the web console](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/installing#deleting-a-namespace-using-the-web-console_uninstalling-virt "4.4.4. Delete a namespace using the web console")
  * [Deleting OpenShift Virtualization custom resource definitions](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/installing#virt-deleting-virt-crds-web_uninstalling-virt "4.4.5. Delete OpenShift Virtualization custom resource definitions")
  * [Deleting a virtual machine using the web console](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/managing-vms#virt-delete-vm-web_virt-delete-vms "8.10.1. Delete a VM by using the web console")
  * [Deleting a standalone virtual machine instance using the CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/managing-vms#virt-deleting-vmis-cli_virt-manage-vmis "8.13.6. Delete a standalone VMI by using the CLI")
