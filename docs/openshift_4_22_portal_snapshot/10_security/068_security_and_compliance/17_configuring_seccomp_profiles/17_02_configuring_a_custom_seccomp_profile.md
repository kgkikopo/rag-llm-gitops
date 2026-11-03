# 17.2. Configuring a custom seccomp profile

You can configure a custom seccomp profile, which allows you to update the filters based on the application requirements. This allows cluster administrators to have greater control over the security of workloads running in OpenShift Container Platform. 

Seccomp security profiles list the system calls (syscalls) a process can make. Permissions are broader than SELinux, which restrict operations, such as `write`, system-wide. 

## 17.2.1. Create seccomp profiles

You can use the `MachineConfig` object to create profiles. 

Seccomp can restrict system calls (syscalls) within a container, limiting the access of your application. 

**Prerequisites**

  * You have cluster admin permissions. 
  * You have created a custom security context constraints (SCC). For more information, see _Additional resources_. 



**Procedure**

  * Create the `MachineConfig` object: 

```yaml
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: worker
  name: custom-seccomp
spec:
  config:
    ignition:
      version: 3.2.0
    storage:
      files:
      - contents:
          source: data:text/plain;charset=utf-8;base64,<hash>
        filesystem: root
        mode: 0644
        path: /var/lib/kubelet/seccomp/seccomp-nostat.json
```


## 17.2.2. Set up the custom seccomp profile

You can configure a custom seccomp profile for use with your workloads. 

**Prerequisite**

  * You have cluster administrator permissions. 
  * You have created a custom security context constraints (SCC). For more information, see "Additional resources". 
  * You have created a custom seccomp profile. 



**Procedure**

  1. Upload your custom seccomp profile to `/var/lib/kubelet/seccomp/<custom-name>.json` by using the Machine Config. See "Additional resources" for detailed steps. 
  2. Update the custom SCC by providing reference to the created custom seccomp profile: 

```yaml
seccompProfiles:
- localhost/<custom-name>.json
```


where: 

`<custom-name>`
     Specifies the name of your custom seccomp profile. 




## 17.2.3. Apply the custom seccomp profile to the workload

You can apply a custom seccomp profile to your workload to restrict the system calls available to your containers. 

**Prerequisite**

  * The cluster administrator has set up the custom seccomp profile. For more details, see "Setting up the custom seccomp profile". 



**Procedure**

  * Apply the seccomp profile to the workload by setting the `securityContext.seccompProfile.type` field as following: 

Example: 

```yaml
spec:
  securityContext:
    seccompProfile:
      type: Localhost
      localhostProfile: <custom-name>.json
```


where: 

`<custom-name>`
    

Specifies the name of your custom seccomp profile. 

Alternatively, you can use the pod annotations `seccomp.security.alpha.kubernetes.io/pod: localhost/<custom-name>.json`. However, this method is deprecated in OpenShift Container Platform 4.22. 




During deployment, the admission controller validates the following: 

  * The annotations against the current SCCs allowed by the user role. 
  * The SCC, which includes the seccomp profile, is allowed for the pod. 



If the SCC is allowed for the pod, the kubelet runs the pod with the specified seccomp profile. 

Important

Ensure that the seccomp profile is deployed to all worker nodes. 

Note

The custom SCC must have the appropriate priority to be automatically assigned to the pod or meet other conditions required by the pod, such as allowing CAP_NET_ADMIN.
