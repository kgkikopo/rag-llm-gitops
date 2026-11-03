# 8.6. SSH access

## 8.6.1. SSH access for virtual machines

You can use SSH to securely access your virtual machines (VMs) from the command line. You can set up your SSH configuration using the `virtctl ssh` command, `virtctl port-forward` command, a service, or a secondary network. 

### 8.6.1.1. Options for connecting to VMs

Your goal determines the best way to connect to a virtual machine (VM), whether troubleshooting, automating configuration with Ansible, or providing access to clients outside the cluster. 

Note

Services provide excellent performance and are recommended for applications that are accessed from outside the cluster. 

If the internal cluster network cannot handle the traffic load, you can configure a secondary network. 

`virtctl ssh` and `virtctl port-forwarding` commands
    

  * Simple to configure. 
  * Recommended for troubleshooting VMs. 
  * `virtctl port-forwarding` recommended for automated configuration of VMs with Ansible. 
  * Dynamic public SSH keys can be used to provision VMs with Ansible. 
  * Not recommended for high-traffic applications such as Rsync or Remote Desktop Protocol because of the burden on the API server. 
  * The API server must be able to handle the traffic load. 
  * The clients must be able to access the API server. 
  * The clients must have access credentials for the cluster. 



Cluster IP service
    

  * The internal cluster network must be able to handle the traffic load. 
  * The clients must be able to access an internal cluster IP address. 



Node port service
    

  * The internal cluster network must be able to handle the traffic load. 
  * The clients must be able to access at least one node. 



Load balancer service
    

  * A load balancer must be configured. 
  * Each node must be able to handle the traffic load of one or more load balancer services. 



Secondary network
    

  * Excellent performance because traffic does not go through the internal cluster network. 
  * Allows a flexible approach to network topology. 
  * Guest operating system must be configured with appropriate security because the VM is exposed directly to the secondary network. If a VM is compromised, an intruder could gain access to the secondary network. 



### 8.6.1.2. Additional resources

  * [OpenShift Virtualization Tuning & Scaling Guide](https://access.redhat.com/articles/6994974)
  * [Connecting a virtual machine to a Linux bridge network](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/networking#virt-connecting-vm-to-linux-bridge "9.7. Connecting a virtual machine to a Linux bridge network")
  * [Connecting a virtual machine to an SR-IOV network](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/networking#virt-connecting-vm-to-sriov "9.8. Connecting a virtual machine to an SR-IOV network")
  * [Create a Linux bridge NAD by using the web console](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/networking#virt-creating-linux-bridge-nad-web_virt-connecting-vm-to-linux-bridge "9.7.2. Create a Linux bridge NAD by using the web console")
  * [Configure an SR-IOV additional network](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/networking#nw-sriov-additional-network_virt-connecting-vm-to-sriov "9.8.2. Configuring SR-IOV additional network")
  * [Accessing a virtual machine by using its external FQDN](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/networking#virt-accessing-vm-secondary-network-fqdn "9.18. Accessing a virtual machine by using its external FQDN")



## 8.6.2. Configure SSH by using the virtctl CLI tool

You can add a public SSH key to a virtual machine (VM) and connect to the VM by running the `virtctl ssh` command, or add the `virtctl port-foward` command to your `.ssh/config` file and connect to the VM by using OpenSSH. 

Important

The `virtctl ssh` command method is not recommended for high traffic loads because it places a burden on the API server. 

You can add public SSH keys to Red Hat Enterprise Linux (RHEL) 9 VMs at runtime or at first boot to VMs with guest operating systems that can be configured by using a cloud-init data source. 

Tip

You can copy the `virtctl ssh` command in the web console by selecting **Copy SSH command** from the options ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Virtualization-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) menu beside a VM on the **VirtualMachines** page. 

Alternatively, right-click the VM in the tree view and select **Copy SSH command** from the menu to copy the `virtctl ssh` command. 

### 8.6.2.1. About static and dynamic SSH key management

You can add public SSH keys to virtual machines (VMs) statically at first boot or dynamically at runtime. A dynamically managed key can also be updated or revoked while the VM runs. 

Note

Only Red Hat Enterprise Linux (RHEL) 9 supports dynamic key injection. 

#### 8.6.2.1.1. Static SSH key management

You can add a statically managed SSH key to a VM with a guest operating system that supports configuration by using a cloud-init data source. The key is added to the virtual machine (VM) at first boot. 

You can add the key by using one of the following methods: 

  * Add a key to a single VM when you create it by using the web console or the command line. 
  * Add a key to a project by using the web console. Afterwards, the key is automatically added to the VMs that you create in this project. 



Use cases: 

  * As a VM owner, you can provision all your newly created VMs with a single key. 



#### 8.6.2.1.2. Dynamic SSH key management

You can enable dynamic SSH key management for a VM with Red Hat Enterprise Linux (RHEL) 9 installed. Afterwards, you can update the key during runtime. The key is added by the QEMU guest agent, which is installed with Red Hat boot sources. 

When dynamic key management is disabled, the default key management setting of a VM is determined by the image used for the VM. 

Use cases: 

  * Granting or revoking access to VMs: As a cluster administrator, you can grant or revoke remote VM access by adding or removing the keys of individual users from a `Secret` object that is applied to all VMs in a namespace. 
  * User access: You can add your access credentials to all VMs that you create and manage. 
  * Ansible provisioning: 

    * As an operations team member, you can create a single secret that contains all the keys used for Ansible provisioning. 
    * As a VM owner, you can create a VM and attach the keys used for Ansible provisioning. 

  * Key rotation: 

    * As a cluster administrator, you can rotate the Ansible provisioner keys used by VMs in a namespace. 
    * As a workload owner, you can rotate the key for the VMs that you manage. 




### 8.6.2.2. Manage static keys

You can add a statically managed public SSH key when you create a virtual machine (VM) by using the OpenShift Container Platform web console or the command line. Save the key to a project to add it automatically to every VM that you create there. 

You can also add a public SSH key to a project when you create a VM by using the web console. The key is saved as a secret and is added automatically to all VMs that you create. 

Note

If you add a secret to a project and then delete the VM, the secret is retained because it is a namespace resource. You must delete the secret manually. 

#### 8.6.2.2.1. Add a static SSH key by using the web console

You can add a statically managed public SSH key to a virtual machine (VM) in the creation wizard of the OpenShift Container Platform web console. The key is added at first boot and does not affect the cloud-init user data. 

You can also save the key to the project as a secret so that it is added automatically to the VMs that you create in the project. 

**Prerequisites**

  * You generated an SSH key pair by using the `ssh-keygen` command. 



**Procedure**

  1. In the OpenShift Container Platform web console, start creating a VM by using the creation wizard until you reach the **Customization** page. 
  2. Click the **SSH** tab. 
  3. Beside **Public SSH key** , click **Edit**. 
  4. Select one of the following options: 

     * **Use existing** : Select a secret from the secrets list. 
     * **Add new** : Add a key by performing the following steps: 

       1. Browse to the public SSH key file or paste the file in the key field. 
       2. Enter the secret name. 
       3. Optional: Select **Automatically apply this key to any new VirtualMachine you create in this project**. 

  5. Click **Save**. 
  6. Complete the remaining wizard steps to create the VM. 



#### 8.6.2.2.2. Add a static SSH key by using the CLI

You can add a statically managed public SSH key when you create a virtual machine (VM) by using the command line. The key is added at first boot and does not affect the cloud-init user data. 

The key is added to the VM as a cloud-init data source. This method separates the access credentials from the application data in the cloud-init user data. This method does not affect cloud-init user data. 

**Prerequisites**

  * You generated an SSH key pair by running the `ssh-keygen` command. 
  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  1. Create a manifest file for a `VirtualMachine` object and a `Secret` object. 

Example manifest: 

```yaml
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: example-vm
  namespace: example-namespace
spec:
  dataVolumeTemplates:
    - metadata:
        name: example-vm-volume
      spec:
        sourceRef:
          kind: DataSource
          name: rhel9
          namespace: openshift-virtualization-os-images
        storage:
          resources: {}
  instancetype:
    name: u1.medium
  preference:
    name: rhel.9
  runStrategy: Always
  template:
    spec:
      domain:
        devices: {}
      volumes:
        - dataVolume:
            name: example-vm-volume
          name: rootdisk
        - cloudInitNoCloud:
            userData: |-
              #cloud-config
              user: cloud-user
          name: cloudinitdisk
      accessCredentials:
        - sshPublicKey:
            propagationMethod:
              noCloud: {}
            source:
              secret:
                secretName: authorized-keys
---
apiVersion: v1
kind: Secret
metadata:
  name: authorized-keys
data:
  key: c3NoLXJzYSB...
```


     * `spec.template.spec.volumes.cloudInitNoCloud` specifies the `cloudInitNoCloud` data source. 
     * `spec.template.spec.accessCredentials.sshPublicKey.source.secret.secretName` specifies the `Secret` object name. 
     * `data.key` specifies the public SSH key. 

  2. Create the `VirtualMachine` and `Secret` objects by running the following command: 

```shell-session
$ oc create -f <manifest_file>.yaml
```


  3. Start the VM by running the following command: 

```shell-session
$ virtctl start vm example-vm -n example-namespace
```


**Verification**

  * Get the VM configuration: 

```shell-session
$ oc describe vm example-vm -n example-namespace
```


Example output: 

```yaml
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: example-vm
  namespace: example-namespace
spec:
  template:
    spec:
      accessCredentials:
        - sshPublicKey:
            propagationMethod:
              noCloud: {}
            source:
              secret:
                secretName: authorized-keys
# ...
```


### 8.6.2.3. Manage dynamic keys

You can enable dynamic SSH key injection for a virtual machine (VM) that runs Red Hat Enterprise Linux (RHEL) 9, and then update the public SSH key while the VM is running. 

Note

Only Red Hat Enterprise Linux (RHEL) 9 supports dynamic key injection. 

If you disable dynamic key injection, the VM inherits the key management method of the image from which it was created. 

#### 8.6.2.3.1. Enable dynamic SSH key injection by using the web console

You can enable dynamic SSH key injection in the OpenShift Container Platform web console for a virtual machine (VM) that runs Red Hat Enterprise Linux (RHEL) 9, and then update the public SSH key while the VM is running. 

The key is added to the VM by the QEMU guest agent, which is installed with Red Hat Enterprise Linux (RHEL) 9 and later. 

**Prerequisites**

  * The guest operating system is RHEL 9 or later. 



**Procedure**

  1. Navigate to **Virtualization** **VirtualMachines** in the web console. 
  2. Select a VM to open the **VirtualMachine details** page. 
  3. On the **Configuration** tab, click **Scripts**. 
  4. If you have not already added a public SSH key to your project, click the edit icon beside **Authorized SSH key** and select one of the following options: 

     * **Use existing** : Select a secret from the secrets list. 
     * **Add new** : 

       1. Browse to the SSH key file or paste the file in the key field. 
       2. Enter the secret name. 
       3. Optional: Select **Automatically apply this key to any new VirtualMachine you create in this project**. 

  5. Set **Dynamic SSH key injection** to on. 
  6. Click **Save**. 



#### 8.6.2.3.2. Enable dynamic SSH key injection by using the CLI

You can enable dynamic SSH key injection from the command line for a virtual machine (VM) that runs Red Hat Enterprise Linux (RHEL) 9, and then update the public SSH key while the VM is running. 

Note

Only Red Hat Enterprise Linux (RHEL) 9 supports dynamic key injection. 

The key is added to the VM by the QEMU guest agent, which is installed automatically with RHEL 9. 

**Prerequisites**

  * You generated an SSH key pair by running the `ssh-keygen` command. 
  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  1. Create a manifest file for a `VirtualMachine` object and a `Secret` object. 

Example manifest: 

```yaml
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: example-vm
  namespace: example-namespace
spec:
  dataVolumeTemplates:
    - metadata:
        name: example-vm-volume
      spec:
        sourceRef:
          kind: DataSource
          name: rhel9
          namespace: openshift-virtualization-os-images
        storage:
          resources: {}
  instancetype:
    name: u1.medium
  preference:
    name: rhel.9
  runStrategy: Always
  template:
    spec:
      domain:
        devices: {}
      volumes:
        - dataVolume:
            name: example-vm-volume
          name: rootdisk
        - cloudInitNoCloud:
            userData: |-
              #cloud-config
              runcmd:
              - [ setsebool, -P, virt_qemu_ga_manage_ssh, on ]
          name: cloudinitdisk
      accessCredentials:
        - sshPublicKey:
            propagationMethod:
              qemuGuestAgent:
                users: ["cloud-user"]
            source:
              secret:
                secretName: authorized-keys
---
apiVersion: v1
kind: Secret
metadata:
  name: authorized-keys
data:
  key: c3NoLXJzYSB...
```


     * `spec.template.spec.volumes.cloudInitNoCloud` defines the data source, for example `userData`. 
     * `spec.template.spec.accessCredentials.sshPublicKey.source.secret.secretName` defines the `secret` object name. 
     * `data.key` within the `secret` object defines the full public SSH key. 

  2. Create the `VirtualMachine` and `Secret` objects by running the following command: 

```shell-session
$ oc create -f <manifest_file>.yaml
```


  3. Start the VM by running the following command: 

```shell-session
$ virtctl start vm example-vm -n example-namespace
```


**Verification**

  * Get the VM configuration by running the following command: 

```shell-session
$ oc describe vm example-vm -n example-namespace
```


Example output: 

```yaml
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: example-vm
  namespace: example-namespace
spec:
  template:
    spec:
      accessCredentials:
        - sshPublicKey:
            propagationMethod:
              qemuGuestAgent:
                users: ["cloud-user"]
            source:
              secret:
                secretName: authorized-keys
# ...
```


#### 8.6.2.3.3. Connect to a VM by using the virtctl ssh command

You can open an SSH session to a running virtual machine (VM) by using the `virtctl ssh` command. The command accepts a VM or a virtual machine instance (VMI) as the target. 

**Prerequisites**

  * You installed the `virtctl` command-line tool. 
  * You added a public SSH key to the VM. 
  * You have an SSH client installed. 
  * The environment where you installed the `virtctl` tool has the cluster permissions required to access the VM. For example, you ran `oc login` or you set the `KUBECONFIG` environment variable. 



**Procedure**

  1. Run the `virtctl ssh` command: 

```shell-session
$ virtctl -n <namespace> ssh <username>@vm/<vm_name> -i <ssh_key>
```


You must specify the resource type (`vmi/` or `vm/`) before the VM name. 

For example: 

```shell-session
$ virtctl -n my-namespace ssh cloud-user@vm/example-vm -i my-key
```


### 8.6.2.4. Connect to a VM by using the virtctl port-forward command

You can use your local OpenSSH client and the `virtctl port-forward` command to connect to a running virtual machine (VM). Use this method with Ansible to automate the configuration of VMs. 

This method is recommended for low-traffic applications because port-forwarding traffic is sent over the control plane. This method is not recommended for high-traffic applications such as Rsync or Remote Desktop Protocol because it places a heavy burden on the API server. 

**Prerequisites**

  * You have installed the `virtctl` client. 
  * The virtual machine you want to access is running. 
  * The environment where you installed the `virtctl` tool has the cluster permissions required to access the VM. For example, you ran `oc login` or you set the `KUBECONFIG` environment variable. 



**Procedure**

  1. Add the following text to the `~/.ssh/config` file on your client machine: 

```shell-session
Host vm/*
  ProxyCommand virtctl port-forward --stdio=true %h %p
```


  2. Connect to the VM by running the following command: 

```shell-session
$ ssh <user>@vm/<vm_name>.<namespace>
```


### 8.6.2.5. Additional resources

  * [Create virtual machines by using the web console](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/creating-virtual-machines#virt-creating-vms-web "7.1. Create virtual machines by using the web console")
  * [Virtual machine creation wizard reference](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/creating-virtual-machines#virt-vm-creation-considerations-web_virt-creating-vms-web "7.1.5. Virtual machine creation wizard reference")



## 8.6.3. Use a secondary network for SSH access

You can configure a secondary network, attach a virtual machine (VM) to the secondary network interface, and connect to the DHCP-allocated IP address by using SSH. 

Important

Secondary networks provide excellent performance because the traffic is not handled by the cluster network stack. However, the VMs are exposed directly to the secondary network and are not protected by firewalls. If a VM is compromised, an intruder could gain access to the secondary network. You must configure appropriate security within the operating system of the VM if you use this method. 

For additional information about networking options, see the Multus and SR-IOV documentation in the "OpenShift Virtualization Tuning & Scaling Guide". 

Note

You can also access a VM attached to a secondary network interface by using the cluster FQDN. 

### 8.6.3.1. Prerequisites

  * You configured a secondary network such as Linux bridge or SR-IOV. 
  * You created a network attachment definition for a Linux bridge network or the SR-IOV Network Operator created a network attachment definition when you created an `SriovNetwork` object. 



### 8.6.3.2. Add a VM network interface in the web console

You can add a network interface to a virtual machine (VM) from the OpenShift Container Platform web console and attach it to an existing network attachment definition. Restart or live migrate the VM to apply the change. 

**Prerequisites**

  * You created a network attachment definition for the network. 



**Procedure**

  1. Navigate to **Virtualization** **VirtualMachines**. 
  2. Click a VM to view the **VirtualMachine details** page. 
  3. On the **Configuration** tab, click the **Network interfaces** tab. 
  4. Click **Add network interface**. 
  5. Enter the interface name and select the network attachment definition from the **Network** list. 
  6. Click **Save**. 
  7. Restart or live migrate the VM to apply the changes. 



### 8.6.3.3. Connect to a VM on a secondary network by using SSH

You can connect to a virtual machine (VM) attached to a secondary network by using SSH. 

**Prerequisites**

  * You attached a VM to a secondary network with a DHCP server. 
  * You have an SSH client installed. 
  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  1. Obtain the IP address of the VM by running the following command: 

```shell-session
$ oc describe vm <vm_name> -n <namespace>
```


Example output: 

```shell-session
# ...
Interfaces:
  Interface Name:  eth0
  Ip Address:      10.244.0.37/24
  Ip Addresses:
    10.244.0.37/24
    fe80::858:aff:fef4:25/64
  Mac:             0a:58:0a:f4:00:25
  Name:            default
# ...
```


  2. Connect to the VM by running the following command: 

```shell-session
$ ssh <user_name>@<ip_address> -i <ssh_key>
```


Example command: 

```shell-session
$ ssh cloud-user@10.244.0.37 -i ~/.ssh/id_rsa_cloud-user
```


## 8.6.4. Create a service to connect with SSH

You can create a service for a virtual machine (VM) and connect to the IP address and port exposed by the service. Services provide excellent performance and are recommended for applications that are accessed from outside the cluster or within the cluster. Ingress traffic is protected by firewalls. 

After you create a service with `virtctl`, you must add `special: key` to the `spec.template.metadata.labels` stanza of the `VirtualMachine` manifest. If the cluster network cannot handle the traffic load, consider using a secondary network for VM access. 

### 8.6.4.1. Service types for VM network access

A Kubernetes service exposes an application running on a set of pods to network clients. Services provide abstraction and load balancing, and the `NodePort` and `LoadBalancer` types also expose the application outside the cluster. 

`ClusterIP`
     Exposes the service on an internal IP address and as a DNS name to other applications within the cluster. A single service can map to multiple virtual machines. When a client tries to connect to the service, the client’s request is load balanced among available backends. `ClusterIP` is the default service type. 
`NodePort`
     Exposes the service on the same port of each selected node in the cluster. `NodePort` makes a port accessible from outside the cluster, provided that the node itself is externally accessible to the client. 
`LoadBalancer`
     Creates an external load balancer in the current cloud (if supported) and assigns a fixed, external IP address to the service. 

Note

For on-premise clusters, you can configure a load balancing service by deploying the MetalLB Operator. 

### 8.6.4.2. Enable load balancer services by using the web console

You can enable the creation of load balancer services for a virtual machine (VM) from the OpenShift Container Platform web console. This setting must be on before you can create a load balancer service for SSH access. 

**Prerequisites**

  * You have configured a load balancer for the cluster. 
  * You have logged in as a user with the `cluster-admin` role. 
  * You created a network attachment definition for the network. 



**Procedure**

  1. Go to **Virtualization** **Settings**. 
  2. Click **Cluster**. 
  3. Expand **General settings** and **SSH configuration**. 
  4. Set **SSH over LoadBalancer service** to on. 



### 8.6.4.3. Create a service by using the web console

You can create a node port or load balancer service for a virtual machine (VM) from the OpenShift Container Platform web console. A service gives clients outside the cluster a way to reach the VM over SSH. 

**Prerequisites**

  * You configured the cluster network to support either a load balancer or a node port. 
  * To create a load balancer service, you enabled the creation of load balancer services. 



**Procedure**

  1. Navigate to **VirtualMachines** and select a virtual machine to view the **VirtualMachine details** page. 
  2. On the **Details** tab, select **SSH over LoadBalancer** from the **SSH service type** list. 
  3. Optional: Click the copy icon to copy the `SSH` command to your clipboard. 



**Verification**

  * Check the **Services** pane on the **Details** tab to view the new service. 



### 8.6.4.4. Create a service by using virtctl

You can create a service for a virtual machine (VM) with a single `virtctl` command. Choose the service type and the port to expose, such as port 22 for SSH access. 

**Prerequisites**

  * You installed the `virtctl` command-line tool. 
  * You configured the cluster network to support the service. 
  * The environment where you installed `virtctl` has the cluster permissions required to access the VM. For example, you ran `oc login` or you set the `KUBECONFIG` environment variable. 



**Procedure**

  * Create a service by running the following command: 

```shell-session
$ virtctl expose vm <vm_name> --name <service_name> --type <service_type> --port <port>
```


where: 

`<vm_name>`
     Specifies the name of the VM you are exposing. 
`<service_name>`
     Specifies a user-defined name for the service you are creating. 
`<service_type>`
     Specifies one of `ClusterIP`, `NodePort`, or `LoadBalancer`. 
`<port>`
    

Specifies the network port on the VM that the service will expose. 

Example: 

```shell-session
$ virtctl expose vm example-vm --name example-service --type NodePort --port 22
```


**Verification**

  * Verify the service by running the following command: 

```shell-session
$ oc get service
```


### 8.6.4.5. Expose a VM as a service by using the CLI

You can use the command line to create a service and associate it with a virtual machine (VM). You must create a label on the VM that matches the selector in the `Service` manifest. 

**Prerequisites**

  * You configured the cluster network to support the service. 
  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  1. Edit the `VirtualMachine` manifest to add the label for service creation. Add `special: key` to the `spec.template.metadata.labels` stanza: 

```yaml
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: example-vm
  namespace: example-namespace
spec:
  runStrategy: Halted
  template:
    metadata:
      labels:
        special: key
# ...
```


Note

Labels on a virtual machine pass through to the pod. The `special: key` label must match the label in the `spec.selector` attribute of the `Service` manifest. 

  2. Save the `VirtualMachine` manifest file to apply your changes. 
  3. Create a `Service` manifest to expose the VM: 

```yaml
apiVersion: v1
kind: Service
metadata:
  name: example-service
  namespace: example-namespace
spec:
# ...
  selector:
    special: key
  type: NodePort
  ports:
    protocol: TCP
    port: 80
    targetPort: 9376
    nodePort: 30000
```


     * `spec.selector` defines the label that you added to the `spec.template.metadata.labels` stanza of the `VirtualMachine` manifest. 
     * `spec.type` defines the type of service by the way it is exposed. Choose one of `ClusterIP`, `NodePort`, or `LoadBalancer`. 
     * `spec.ports` defines a collection of network ports and protocols to expose from the virtual machine. 

  4. Save the `Service` manifest file. 
  5. Create the service by running the following command: 

```shell-session
$ oc create -f example-service.yaml
```


  6. Restart the VM to apply the changes. 



**Verification**

  * Query the `Service` object to verify that it is available: 

```shell-session
$ oc get service -n example-namespace
```


### 8.6.4.6. Connect to a VM through a service

You can connect to a virtual machine (VM) that a service exposes by using SSH. 

**Prerequisites**

  * You created a service to expose the VM. 
  * You have an SSH client installed. 
  * You are logged in to the cluster. 



**Procedure**

  * Run the following command to access the VM: 

```shell-session
$ ssh <user_name>@<ip_address> -p <port>
```


where: 

`<ip_address>`
     Specifies the cluster IP for a cluster IP service, the node IP for a node port service, or the external IP address for a load balancer service.
