# 4.2. Resource guidelines for installing OpenShift Container Platform on RHOSP

To support an OpenShift Container Platform installation, your Red Hat OpenStack Platform (RHOSP) quota must meet certain requirements. 

Table 4.1. Recommended resources for a default OpenShift Container Platform cluster on RHOSPResource| Value  
---|---  
Floating IP addresses  |  3   
Ports  |  15   
Routers  |  1   
Subnets  |  1   
RAM  |  88 GB   
vCPUs  |  22   
Volume storage  |  275 GB   
Instances  |  7   
Security groups  |  3   
Security group rules  |  60   
Server groups  |  2 - plus 1 for each additional availability zone in each machine pool   
Show more

A cluster might function with fewer than recommended resources, but cluster performance is not guaranteed. 

Important

If RHOSP object storage (Swift) is available and operated by a user account with the `swiftoperator` role, Swift is used as the default backend for the OpenShift Container Platform image registry. In this case, the volume storage requirement is 175 GB. Swift space requirements vary depending on the size of the image registry. 

Note

By default, your security group and security group rule quotas might be low. If you encounter problems, run `openstack quota set --secgroups 3 --secgroup-rules 60 <project>` as an administrator to increase them. 

An OpenShift Container Platform deployment comprises control plane machines, compute machines, and a bootstrap machine. 

## 4.2.1. Control plane machines

By default, the OpenShift Container Platform installation process creates three control plane machines. 

Each machine requires: 

  * An instance from the RHOSP quota 
  * A port from the RHOSP quota 
  * A flavor with at least 16 GB memory and 4 vCPUs 
  * At least 100 GB storage space from the RHOSP quota 



## 4.2.2. Compute machines

By default, the OpenShift Container Platform installation process creates three compute machines. 

Each machine requires: 

  * An instance from the RHOSP quota 
  * A port from the RHOSP quota 
  * A flavor with at least 8 GB memory and 2 vCPUs 
  * At least 100 GB storage space from the RHOSP quota 



Tip

Compute machines host the applications that you run on OpenShift Container Platform; aim to run as many as you can. 

## 4.2.3. Bootstrap machine

During installation, a bootstrap machine is temporarily provisioned to stand up the control plane. After the production control plane is ready, the bootstrap machine is deprovisioned. 

The bootstrap machine requires: 

  * An instance from the RHOSP quota 
  * A port from the RHOSP quota 
  * A flavor with at least 16 GB memory and 4 vCPUs 
  * At least 100 GB storage space from the RHOSP quota
