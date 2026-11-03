# 3.8. Reducing pod timeouts using seLinuxChangePolicy

The SELinux mount option applies security contexts during mount without recursive relabeling, reducing pod startup times on volumes with many files. This optimization is enabled by default for ReadWriteOncePod volumes and will become the default for ReadWriteOnce and ReadWriteMany volumes. 

SELinux (Security-Enhanced Linux) is a security mechanism that assigns security labels (contexts) to all objects (files, processes, network ports, and so on) on a system. These labels determine what a process can access. In OpenShift Container Platform, SELinux helps prevent containers from escaping and accessing the host system or other containers. 

When a pod starts, the container runtime recursively relabels all files on a volume to match the pod’s SELinux context. For volumes with many files, this can significantly increase pod startup times. 

Mount option specifies avoiding recursive relabeling of all files by attempting to mount the volume with the correct SELinux label directly using the -o context mount option, thus helping to avoid pod timeout problems. 

## 3.8.1. RWOP and SELinux mount option

ReadWriteOncePod (RWOP) persistent volumes use the SELinux mount feature by default. 

The mount option feature is driver dependent, and enabled by default in AWS EBS , Azure Disk, GCP PD, IBM Cloud Block Storage volume, Cinder, vSphere, and Red Hat OpenShift Data Foundation. For third-party drivers, contact your storage vendor. 

## 3.8.2. RWO and RWX and SELinux mount option

ReadWriteOnce (RWO) and ReadWriteMany (RWX) volumes use recursive relabeling by default. 

Important

In a future OpenShift Container Platform version, RWO and RWX volumes will use **mount option by default**. 

To assist you with the upcoming move to the mount option default, OpenShift Container Platform 4.20 reports SELinux-related conflicts when creating pods, and on running pods, to make you aware of potential conflicts, and to help you resolve them. For more information about this reporting, see the Red Hat Knowledgebase article "OpenShift reports SELinux-related conflicts when creating Pods". 

If you are unable to resolve the SELinux-related conflicts, you can proactively opt-out of the future move to mount option as default for selected pods or namespaces. To opt out, see "Opting out of the SELinux mount option default". 

**Additional resources**

  * [OpenShift reports SELinux-related conflicts when creating Pods (Red Hat Knowledgebase)](https://access.redhat.com/solutions/7131398)
  * [Opting out of the SELinux mount option default](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage/understanding-persistent-storage#using_selinuxChangePolicy_pod-opt-out_understanding-persistent-storage "3.8.4. Opting out of the SELinux mount option default")



## 3.8.3. Testing the RWO and RWX and SELinux mount option feature

The SELinux mount option applies the correct security context during mount without recursive relabeling, reducing pod startup times on volumes with many files. In OpenShift Container Platform 4.21, you can evaluate the mount option feature for RWO and RWX volumes as a Technology Preview feature. 

Important

RWO/RWX SELinux mount is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. 

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/). 

**Procedure**

  * Enable Feature Gates. For information about enabling Feature Gates, see "Enabling features using feature gates". 

RWO and RWX volumes now have mount option as the default behavior. 




**Next step**

Carefully test your applications and observe how they are using storage. For more information, see the Red Hat Knowledgebase article "OpenShift reports SELinux-related conflicts when creating Pods", and consider opting out from using mount option if you are experiencing issues. For more information, see "Opting out of the SELinux mount option default". 

**Additional resources**

  * [OpenShift reports SELinux-related conflicts when creating Pods (Red Hat Knowledgebase)](https://access.redhat.com/solutions/7131398)
  * [Opting out of the SELinux mount option default](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage/understanding-persistent-storage#using_selinuxChangePolicy_pod-opt-out_understanding-persistent-storage "3.8.4. Opting out of the SELinux mount option default")



## 3.8.4. Opting out of the SELinux mount option default

If you want to opt out of the future move to mount option as default, you can affirmatively set the `seLinuxChangePolicy` parameter to `Recursive` at either the individual pod or namespace level. 

### 3.8.4.1. Changing seLinuxChangePolicy at the namespace level

Configure `seLinuxChangePolicy` to `Recursive` at the namespace level to opt out of the SELinux mount option default for all pods in that namespace. This setting applies automatically to new pods while allowing pod-level overrides when workloads require different SELinux relabeling behavior. 

**Prerequisites**

  * Logged in to a running OpenShift Container Platform cluster with administrator privileges. 
  * Access to the OpenShift Container Platform console. 



**Procedure**

  1. Select the needed namespace: 

     1. Click **Administration** > **Namespaces**. 
     2. On the **Namespaces** page, click the desired namespace. The **Namespace details** page appears. 

  2. Add the `seLinuxChangePolicy` label to the namespace: 

     1. On the **Namespace details** page, next to **Labels** , click **Edit**. 
     2. In the **Edit labels** dialog, add the label `storage.openshift.io/selinux-change-policy=Recursive`. 

This specifies recursively relabeling all files on pod volumes to the appropriate SELinux context. 

     3. Click **Save**. 

  3. Verify the results by starting up a pod in the previously edited namespace and observe that the parameter `spec.securityContext.seLinuxChangePolicy` is set to `Recursive`. 

**Example pod YAML file showing`seLinuxChangePolicy` setting**

```yaml
securityContext:
    seLinuxOptions:
      level: 's0:c27,c19'
    runAsNonRoot: true
    fsGroup: 1000740000
    seccompProfile:
      type: RuntimeDefault
    seLinuxChangePolicy: Recursive
  ...
```


     * The value for `securityContext.seLinuxChangePolicy` is inherited from the namespace. 




### 3.8.4.2. Changing seLinuxChangePolicy at the pod level

Set `seLinuxChangePolicy` to `Recursive` at the pod level to override namespace defaults or opt out of the SELinux mount option default for specific workloads. 

Configure the `seLinuxChangePolicy` parameter in deployment or statefulset specifications to apply it to managed pods, or set it directly when creating individual pods. You cannot modify this parameter on existing pods. 

This procedure describes how to set the `seLinuxChangePolicy` parameter in an existing deployment. 

**Prerequisites**

  * Access to the OpenShift Container Platform console. 



**Procedure**

  1. Click **Workloads** > **Deployments**. 
  2. On the **Deployment** page, click the required deployment. 
  3. On the **Deployment details** page, click the **YAML** tab. 
  4. Edit the deployment’s YAML file under `spec.template.spec.securityContext` similar to the following example file: 

**Example deployment YAML file setting`seLinuxChangePolicy`**

```yaml
  ...
securityContext:
  seLinuxChangePolicy: Recursive
  ...
```


     * `securityContext.seLinuxChangePolicy`: When set to `Recursive`, specifies recursively relabeling all files on all pod volumes to the appropriate SELinux context. 

  5. Click **Save**.
