# 7.2. About installations in restricted networks

You can install OpenShift Container Platform 4.22 in a restricted network that lacks an active internet connection. These restricted installations use installer-provisioned or user-provisioned infrastructure, depending on your cloud platform. 

If you choose to perform a restricted network installation on a cloud platform, you still require access to its cloud APIs. Some cloud functions, such as Amazon Web Service’s Route 53 DNS and IAM services, require internet access. Depending on your network, you might require less internet access for an installation on bare-metal hardware, Nutanix, or on VMware vSphere. 

To complete a restricted network installation, you must create a registry that mirrors the contents of the OpenShift image registry and contains the installation media. You can create this registry on a mirror host, which can access both the internet and your closed network, or by using other methods that meet your restrictions. 

## 7.2.1. Additional limits

Clusters in restricted networks have the following additional limitations and restrictions: 

  * The `ClusterVersion` status includes an `Unable to retrieve available updates` error. 
  * By default, you cannot use the contents of the Developer Catalog because you cannot access the required image stream tags.
