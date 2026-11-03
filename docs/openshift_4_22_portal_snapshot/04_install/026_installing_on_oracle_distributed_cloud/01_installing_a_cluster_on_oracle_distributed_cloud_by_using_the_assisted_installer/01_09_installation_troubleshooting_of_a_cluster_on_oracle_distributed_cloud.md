# 1.9. Installation troubleshooting of a cluster on Oracle Distributed Cloud

If you experience issues with using the Assisted Installer to install an OpenShift Container Platform cluster on Oracle® Distributed Cloud, you can troubleshoot the installation. 

Read the following sections to troubleshoot common problems. 

## 1.9.1. The Ingress Load Balancer in Oracle Distributed Cloud is not at a healthy status

This issue is classed as a `Warning` because by using Oracle Distributed Cloud to create a stack, you created a pool of compute nodes, 3 by default, that are automatically added as backend listeners for the Ingress Load Balancer. By default, the OpenShift Container Platform deploys 2 router pods, which are based on the default values from the OpenShift Container Platform manifest files. The `Warning` is expected because a mismatch exists with the number of router pods available, 2, to run on the 3 compute nodes. 

**Figure 1.2. Example of a`Warning` message that is under the Backend set information tab on Oracle Distributed Cloud**

![Example of an warning message that is under the Backend set information tab on Oracle Distributed Cloud](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Installing_on_Oracle_Distributed_Cloud-en-US/images/5ccdeb8023fde79651d16fecc8ba1cfa/ingress_load_balancer_warning_message.png) ![Example of an warning message that is under the Backend set information tab on Oracle Distributed Cloud](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Installing_on_Oracle_Distributed_Cloud-en-US/images/5ccdeb8023fde79651d16fecc8ba1cfa/ingress_load_balancer_warning_message.png)

You do not need to modify the Ingress Load Balancer configuration. Instead, you can point the Ingress Load Balancer to specific compute nodes that operate in your cluster on OpenShift Container Platform. To do this, use placement mechanisms, such as annotations, on OpenShift Container Platform to ensure router pods only run on the compute nodes that you originally configured on the Ingress Load Balancer as backend listeners. 

## 1.9.2. Oracle Distributed Cloud create stack operation fails with an Error: 400-InvalidParameter message

On attempting to create a stack on Oracle Distributed Cloud, you identified that the **Logs** section of the job outputs an error message. For example: 

```shell-session
Error: 400-InvalidParameter, DNS Label oci-demo does not follow Oracle requirements
Suggestion: Please update the parameter(s) in the Terraform config as per error message DNS Label oci-demo does not follow Oracle requirements
Documentation: https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/core_vcn
```


Go to the **Install OpenShift with the Assisted Installer** page on the Hybrid Cloud Console, and check the **Cluster name** field on the **Cluster Details** step. Remove any special characters, such as a hyphen (`-`), from the name, because these special characters are not compatible with the OCI naming conventions. For example, change `oci-demo` to `ocidemo`. 

For more information, see "Red Hat Hybrid Cloud Console".
