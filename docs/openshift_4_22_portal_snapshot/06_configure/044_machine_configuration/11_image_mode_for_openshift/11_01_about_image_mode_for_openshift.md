# 11.1. About image mode for OpenShift

Image mode for OpenShift allows you to customize the underlying node operating system on any of your cluster nodes. This helps keep everything up-to-date, including the node operating system and any added customizations such as specialized software. 

You create a custom layered image by using a Containerfile and applying it to nodes by using a custom object. At any time, you can remove the custom layered image by deleting that custom object. 

With image mode for OpenShift, you can install RPMs into your base image, and your custom content will be booted alongside RHCOS. The Machine Config Operator (MCO) can roll out these custom layered images and monitor these custom containers in the same way it does for the default RHCOS image. Image mode for OpenShift gives you greater flexibility in how you manage your RHCOS nodes. 

Important

Installing realtime kernel and extensions RPMs as custom layered content is not recommended. This is because these RPMs can conflict with RPMs installed by using a machine config. If there is a conflict, the MCO enters a `degraded` state when it tries to install the machine config RPM. You need to remove the conflicting extension from your machine config before proceeding. 

When you apply the custom layered image to your cluster, you assume the responsibility for the package you applied with the custom layered image and any issues that might arise with the package. 

There are three methods for deploying a custom layered image onto your nodes: 

On-cluster image mode
     With on-cluster image mode, you create a `MachineOSConfig` object where you include the Containerfile and other parameters. The build is performed on your cluster and the resulting custom layered image is automatically pushed to your repository and applied to the machine config pool that you specified in the `MachineOSConfig` object. The entire process is performed completely within your cluster. 
Out-of-cluster image mode
     With out-of-cluster image mode, you create a Containerfile that references an OpenShift Container Platform image and the RPM that you want to apply, build the layered image in your own environment, and push the image to your repository. Then, in your cluster, create a `MachineConfig` object for the targeted node pool that points to the new image. The Machine Config Operator overrides the base RHCOS image, as specified by the `osImageURL` value in the associated machine config, and boots the new image. 
During OpenShift Container Platform installation
     You can apply a pre-built custom layered image to specific nodes during OpenShift Container Platform installation. 

Important

For these methods, use the same base RHCOS image installed on the rest of your cluster. Use the `oc adm release info --image-for rhel-coreos` command to obtain the base image used in your cluster.
