# 13.6. Security

## 13.6.1. Security basics

Security is a critical component of OpenShift Container Platform deployments, particularly when running cloud-native applications. 

You can enhance security for high-bandwidth network deployments by following key security considerations. By implementing these standards and best practices, you can strengthen security in most use cases. 

### 13.6.1.1. RBAC overview

Role-based access control (RBAC) objects determine whether a user is allowed to perform a given action within a project. 

Cluster administrators can use the cluster roles and bindings to control who has various access levels to the OpenShift Container Platform platform itself and all projects. 

Developers can use local roles and bindings to control who has access to their projects. Authorization is a separate step from authentication, which is more about determining the identity of who is taking the action. 

Authorization is managed using the following authorization objects: 

Rules
     Sets of permitted actions on specific objects. For example, a rule can determine whether a user or service account can create pods. Each rule specifies an API resource, the resource within that API, and the allowed action. 
Roles
    

Collections of rules that define what actions users or groups can perform. You can associate or bind rules to multiple users or groups. A role file can contain one or more rules that specify the actions and resources allowed for that role. 

Roles are categorized into the following types: 

  * Cluster roles can be defined at the cluster level. They are not tied to a single namespace. They can apply across all namespaces or specific namespaces when you bind them to users, groups, or service accounts. 
  * Project roles can be created within a specific namespace, and they only apply to that namespace. You can assign permissions to specific users to create roles and role bindings within their namespace, ensuring they do not affect other namespaces. 



Bindings
    

Associations between users and groups with a role. You can create a role binding to connect the rules in a role to a specific user ID or group. This brings together the role and the user or group, defining what actions they can perform. 

Note

You can bind more than one role to a user or group. 

For more information on RBAC, see "Using RBAC to define and apply permissions". 

#### 13.6.1.1.1. Operational RBAC considerations

To reduce operational overhead, manage access through groups rather than handling individual user IDs across multiple clusters. By managing groups at an organizational level, you can streamline access control and simplify administration across your organization. 

**Additional resources**

  * [Using RBAC to define and apply permissions](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/#authorization-overview_using-rbac)



### 13.6.1.2. Security accounts overview

A service account is an OpenShift Container Platform account that allows a component to directly access the API. Service accounts are API objects that exist within each project. Service accounts provide a flexible way to control API access without sharing a regular user’s credentials. 

You can use service accounts to apply role-based access control (RBAC) to pods. By assigning service accounts to workloads, such as pods and deployments, you can grant additional permissions, such as pulling from different registries. This also allows you to assign lower privileges to service accounts, reducing the security footprint of the pods that run under them. 

For more information about service accounts, see "Understanding and creating service accounts". 

**Additional resources**

  * [Understanding and creating service accounts](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/#understanding-and-creating-service-accounts)



### 13.6.1.3. Identity provider configuration

Configuring an identity provider is the first step in setting up users on the cluster. You can manage groups at the organizational level by using an identity provider. 

The identity provider can pull in specific user groups that are maintained at the organizational level, rather than the cluster level. This allows you to add and remove users from groups that follow your organization’s established practices. 

Note

You must set up a cron job to run frequently to pull any changes into the cluster. 

You can use an identity provider to manage access levels for specific groups within your organization. For example, you can perform the following actions to manage access levels: 

  * Assign the `cluster-admin` role to teams that require cluster-level privileges. 
  * Grant application administrators specific privileges to manage only their respective projects. 
  * Provide operational teams with `view` access across the cluster to enable monitoring without allowing modifications. 



For information about configuring an identity provider, see "Understanding identity provider configuration". 

**Additional resources**

  * [Understanding identity provider configuration](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/#understanding-identity-provider)



### 13.6.1.4. Replacing the kubeadmin user with a cluster-admin user

The `kubeadmin` user with the `cluster-admin` privileges is created on every cluster by default. To enhance the cluster security, you can replace the `kubeadmin` user with a `cluster-admin` user and then disable or remove the `kubeadmin` user. 

**Prerequisites**

  * You have created a user with `cluster-admin` privileges. 
  * You have installed the OpenShift CLI (`oc`). 
  * You have administrative access to a virtual vault for secure storage. 



**Procedure**

  1. Create an emergency `cluster-admin` user by using the `htpasswd` identity provider. For more information, see "About htpasswd authentication". 
  2. Assign the `cluster-admin` privileges to the new user by running the following command: 

```shell-session
$ oc adm policy add-cluster-role-to-user cluster-admin <emergency_user>
```


  3. Verify the emergency user access: 

     1. Log in to the cluster using the new emergency user. 
     2. Confirm that the user has `cluster-admin` privileges by running the following command: 

```shell-session
$ oc whoami
```


Ensure the output shows the ID of the emergency user. 

  4. Store the password or authentication key for the emergency user securely in a virtual vault. 

Note

Follow the best practices of your organization for securing sensitive credentials. 

  5. Disable or remove the `kubeadmin` user to reduce security risks by running the following command: 

```shell-session
$ oc delete secrets kubeadmin -n kube-system
```


**Additional resources**

  * [Configuring an htpasswd identity provider](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/#identity-provider-htpasswd-about_configuring-htpasswd-identity-provider)



### 13.6.1.5. Security considerations

Workloads might handle sensitive data and demand high reliability. A single security vulnerability might lead to broader, cluster-wide compromises. 

With numerous components running on an OpenShift Container Platform cluster, you must secure each component to prevent any breach from escalating. Ensuring security across the entire infrastructure, including all components, is essential to maintaining the integrity of the network and avoiding vulnerabilities. 

The following key security features are essential for all industries that handle sensitive data: 

  * Security Context Constraints (SCCs): Provide granular control over pod security in the OpenShift Container Platform clusters. 
  * Pod Security Admission (PSA): Kubernetes-native pod security controls. 
  * Encryption: Ensures data confidentiality in high-throughput network environments. 



### 13.6.1.6. Advancement of pod security in Kubernetes and OpenShift Container Platform

Kubernetes initially had limited pod security. When OpenShift Container Platform integrated Kubernetes, Red Hat added pod security through Security Context Constraints (SCCs). 

In Kubernetes version 1.3, `PodSecurityPolicy` (PSP) was introduced as a similar feature. However, Pod Security Admission (PSA) was introduced in Kubernetes version 1.21, which resulted in the deprecation of PSP in Kubernetes version 1.25. 

PSA also became available in OpenShift Container Platform version 4.11. While PSA improves pod security, it lacks features provided by SCCs that are still necessary for certain use cases. Therefore, OpenShift Container Platform continues to support both PSA and SCCs. 

### 13.6.1.7. Bare-metal infrastructure

Bare-metal infrastructure for OpenShift Container Platform clusters in telco and finance industries requires specific hardware and network configurations. 

Hardware requirements
     In several industries, such as telco and finance, clusters are primarily built on bare-metal hardware. This means that the Red Hat Enterprise Linux CoreOS (RHCOS) operating system is installed directly on the physical machines, without using virtual machines. This reduces network connectivity complexity, minimizes latency, and optimizes CPU usage for applications. 
Network requirements
     Networks in these industries sometimes require much higher bandwidth compared to standard IT networks. For example, Telco networks commonly use dual-port 25 GB connections or 100 GB network interface cards (NICs) to handle massive data throughput. Security is critical, requiring encrypted connections and secure endpoints to protect sensitive personal data. 

### 13.6.1.8. Lifecycle management

Upgrades are critical for security. When a vulnerability is discovered, it is patched in the latest z-stream release. 

This fix is then rolled back through each lower y-stream release until all supported versions are patched. Releases that are no longer supported do not receive patches. Therefore, it is important to upgrade OpenShift Container Platform clusters regularly to stay within a supported release and ensure they remain protected against vulnerabilities. 

For more information about lifecycle management and upgrades, see "Upgrading OpenShift Container Platform clusters". 

**Additional resources**

  * [Upgrading an OpenShift cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/postinstallation_configuration/day-2-operations-for-openshift-container-platform-clusters#update-welcome "13.2.1. Upgrading an OpenShift Container Platform cluster")



## 13.6.2. Host security

### 13.6.2.1. Red Hat Enterprise Linux CoreOS (RHCOS)

Red Hat Enterprise Linux CoreOS (RHCOS) is different from Red Hat Enterprise Linux (RHEL) in key areas. For more information, see "About RHCOS". 

A major distinction is the control of `rpm-ostree`, which is updated through the Machine Config Operator. 

RHCOS follows the same immutable design used for pods in OpenShift Container Platform. This ensures that the operating system remains consistent across the cluster. For information about RHCOS architecture, see "Red Hat Enterprise Linux CoreOS (RHCOS)". 

To manage hosts effectively while maintaining security, avoid direct access whenever possible. Instead, you can use the following methods for host management: 

  * Debug pod 
  * Direct SSH 
  * Console access 



Review the following RHCOS security mechanisms that are integral to maintaining host security: 

Linux namespaces
     Provide isolation for processes and resources. Each container keeps its processes and files within its own namespace. If a user escapes from the container namespace, they could gain access to the host operating system, potentially compromising security. 
Security-Enhanced Linux (SELinux)
    

Enforces mandatory access controls to restrict access to files and directories by processes. SELinux adds an extra layer of security by preventing unauthorized access to files if a process tries to break its confinement. 

SELinux follows the security policy of denying everything unless explicitly allowed. If a process attempts to modify or access a file without permission, SELinux denies access. For more information, see "Introduction to SELinux". 

Linux capabilities
     Assign specific privileges to processes at a granular level, minimizing the need for full root permissions. For more information, see "Linux capabilities". 
Control groups (cgroups)
     Allocate and manage system resources, such as CPU and memory for processes and containers, ensuring efficient usage. As of OpenShift Container Platform 4.16, there are two versions of cgroups. cgroup v2 is now configured by default. 
CRI-O
     Serves as a lightweight container runtime that enforces security boundaries and manages container workloads. 

#### 13.6.2.1.1. Additional resources

  * [Introduction to SELinux](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/using_selinux/index#introduction-to-selinux_getting-started-with-selinux)



**Additional resources**

  * [About RHCOS](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/architecture/#rhcos-about_architecture-rhcos)
  * [Red Hat Enterprise Linux CoreOS (RHCOS)](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/architecture/#red-hat-enterprise-linux-coreos)
  * [Linux capabilities](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/postinstallation_configuration/day-2-operations-for-openshift-container-platform-clusters#security-linux-capabilities-overview_security-host-sec "13.6.2.3. Linux capabilities")



### 13.6.2.2. Command-line host access

Configure an external authenticator to restrict direct access and prevent unauthorized modifications. The Machine Config Operator (MCO) manages these logins and maintains consistency across your cluster. 

Examples of external authenticators include lightweight directory access protocol (LDAP) and System Security Services Daemon (SSSD). If a node reboot leads to timeout issues, create a node disruption policy. With this policy, you can configure an external authenticator on a host without requiring a node reboot. For more information, see "Using node disruption policies to minimize disruption from machine config changes" in the _Additional resources_ section. 

Important

Do not configure direct access to the root ID on any OpenShift Container Platform cluster server. 

You can connect to a node in the cluster by using the following methods: 

Using debug pod
    

Red Hat recommends this method to access a node. To debug or connect to a node, run the following command: 

```shell-session
$ oc debug node/<worker_node_name>
```


After connecting to the node, run the following command to get access to the root file system: 

```shell-session
# chroot /host
```


This gives you root access within a debug pod on the node. For more information, see "Starting debug pods with root access". 

Direct SSH
    

Avoid using the root user. Instead, use the core user ID (or your own ID). To connect to the node by using SSH, run the following command: 

```shell-session
$ ssh core@<worker_node_name>
```


Important

The core user ID is initially given `sudo` privileges within the cluster. 

If you cannot connect to a node by using SSH, add your SSH key to the core user. For more information, see "How to connect to OpenShift Container Platform 4.x Cluster nodes using SSH bastion pod" in the _Additional resources_ section. 

After connecting to the node using SSH, run the following command to get access to the root shell: 

```shell-session
$ sudo -i
```


Console Access
    

Ensure that consoles are secure. Do not allow direct login with the root ID, instead use individual IDs. 

Note

Follow the best practices of your organization for securing console access. 

**Additional resources**

  * [Using node disruption policies to minimize disruption from machine config changes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_configuration/#machine-configs-configure_machine-config-node-disruption)
  * [Starting debug pods with root access](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/support/#starting-debug-pods-with-root-access_investigating-pod-issues)
  * [How to connect to OpenShift Container Platform 4.x Cluster nodes using SSH bastion pod](https://access.redhat.com/solutions/4073041)



### 13.6.2.3. Linux capabilities

Linux capabilities define the actions a process can perform on the host system. By default, pods are granted several capabilities unless security measures are applied. These default capabilities are as follows: 

  * `CHOWN`
  * `DAC_OVERRIDE`
  * `FSETID`
  * `FOWNER`
  * `SETGID`
  * `SETUID`
  * `SETPCAP`
  * `NET_BIND_SERVICE`
  * `KILL`



You can modify which capabilities that a pod can receive by configuring Security Context Constraints (SCCs). 

Important

You must not assign the following capabilities to a pod: 

  * `SYS_ADMIN`: A powerful capability that grants elevated privileges. Allowing this capability can break security boundaries and pose a significant security risk. 
  * `NET_ADMIN`: Allows control over networking, like SR-IOV ports, but can be replaced with alternative solutions in modern setups. 



For more information about Linux capabilities, see "Linux capabilities". 

#### 13.6.2.3.1. Additional resources

  * [Linux capabilities](https://man7.org/linux/man-pages/man7/capabilities.7.html)



## 13.6.3. Security context constraints

Similar to the way that RBAC resources control user access, administrators can use security context constraints (SCCs) to control permissions for pods. These permissions determine the actions that a pod can perform and what resources it can access. You can use SCCs to define a set of conditions that a pod must run. 

Security context constraints allow an administrator to control the following security constraints: 

  * Whether a pod can run privileged containers with the `allowPrivilegedContainer` flag 
  * Whether a pod is constrained with the `allowPrivilegeEscalation` flag 
  * The capabilities that a container can request 
  * The use of host directories as volumes 
  * The SELinux context of the container 
  * The container user ID 
  * The use of host namespaces and networking 
  * The allocation of an `FSGroup` that owns the pod volumes 
  * The configuration of allowable supplemental groups 
  * Whether a container requires write access to its root file system 
  * The usage of volume types 
  * The configuration of allowable `seccomp` profiles 



Default SCCs are created during installation and when you install some Operators or other components. As a cluster administrator, you can also create your own SCCs by using the OpenShift CLI (`oc`). 

For information about default security context constraints, see [Default security context constraints](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/#default-sccs_configuring-internal-oauth). 

Important

Do not modify the default SCCs. Customizing the default SCCs can lead to issues when some of the platform pods deploy or OpenShift Container Platform is upgraded. Additionally, the default SCC values are reset to the defaults during some cluster upgrades, which discards all customizations to those SCCs. 

Instead of modifying the default SCCs, create and modify your own SCCs as needed. For detailed steps, see [Creating security context constraints](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/#security-context-constraints-creating_configuring-internal-oauth). 

You can use the following basic SCCs: 

  * `restricted`
  * `restricted-v2`



The `restricted-v2` SCC is the most restrictive SCC provided by a new installation and is used by default for authenticated users. It aligns with Pod Security Admission (PSA) restrictions and improves security, as the original `restricted` SCC is less restrictive. It also helps transition from the original SCCs to v2 across multiple releases. Eventually, the original SCCs get deprecated. Therefore, it is recommended to use the `restricted-v2` SCC. 

You can examine the `restricted-v2` SCC by running the following command: 

```shell-session
$ oc describe scc restricted-v2
```


**Example output**

```shell-session
Name:                                           restricted-v2
Priority:                                       <none>
Access:
  Users:                                        <none>
  Groups:                                       <none>
Settings:
  Allow Privileged:                             false
  Allow Privilege Escalation:                   false
  Default Add Capabilities:                     <none>
  Required Drop Capabilities:                   ALL
  Allowed Capabilities:                         NET_BIND_SERVICE
  Allowed Seccomp Profiles:                     runtime/default
  Allowed Volume Types:                         configMap,downwardAPI,emptyDir,ephemeral,persistentVolumeClaim,projected,secret
  Allowed Flexvolumes:                          <all>
  Allowed Unsafe Sysctls:                       <none>
  Forbidden Sysctls:                            <none>
  Allow Host Network:                           false
  Allow Host Ports:                             false
  Allow Host PID:                               false
  Allow Host IPC:                               false
  Read Only Root Filesystem:                    false
  Run As User Strategy: MustRunAsRange
    UID:                                        <none>
    UID Range Min:                              <none>
    UID Range Max:                              <none>
  SELinux Context Strategy: MustRunAs
    User:                                       <none>
    Role:                                       <none>
    Type:                                       <none>
    Level:                                      <none>
  FSGroup Strategy: MustRunAs
    Ranges:                                     <none>
  Supplemental Groups Strategy: RunAsAny
    Ranges:                                     <none>
```


The `restricted-v2` SCC explicitly denies everything except what it explicitly allows. The following settings define the allowed capabilities and security restrictions: 

  * Default add capabilities: Set to `<none>`. It means that no capabilities are added to a pod by default. 
  * Required drop capabilities: Set to `ALL`. This drops all the default Linux capabilities of a pod. 
  * Allowed capabilities: `NET_BIND_SERVICE`. A pod can request this capability, but it is not added by default. 
  * Allowed `seccomp` profiles: `runtime/default`. 



For more information, see [Managing security context constraints](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/#managing-security-context-constraints).
