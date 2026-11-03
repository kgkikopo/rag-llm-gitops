# 2.2. Infrastructure requirements for installing OpenShift Container Platform on IBM PowerVC

To support an OpenShift Container Platform installation by using the installation program, you need to prepare your IBM PowerVC environment. 

## 2.2.1. IBM PowerVC account privilege requirements

When installing OpenShift Container Platform on IBM PowerVC by using the installation program, you must use an administrative account to ensure that you have all required permissions. 

## 2.2.2. IBM PowerVC image requirements

You must import a Red Hat Enterprise Linux CoreOS (RHCOS) image. This can be found by using the installation program. 

```shell-session
$ openshift-install coreos print-stream-json | jq -r '.architectures.ppc64le.artifacts.openstack' | jq -r '.formats."qcow2.gz".disk.location'
```


After downloading the image from the resultant URL, you can import the image into IBM PowerVC by using the `powervc-image-import` tool. 

## 2.2.3. Networking requirements

## 2.2.4. IBM PowerVC network

Installation requires at least one PowerVC network. Ideally the network should be dedicated to your OpenShift Container Platform cluster and not shared with other workloads. 

IBM recommends that the network is set as a DHCP network in IBM PowerVC. You must have a DHCP server set up to assign addresses for this network. When using this type of network, IBM PowerVC is not aware of the IP address that is assigned to the created servers. 

## 2.2.5. DNS records

DNS records pointing to a `LoadBalancer` service are required for installation. In each record, `<cluster_name>` is the cluster name and `<base_domain>` is the cluster base domain that you specify when you install the cluster. A complete DNS record takes the form: `<component>.<cluster_name>.<base_domain>.`. 

Table 2.1. Required DNS recordsComponent| Record| Description  
---|---|---  
API VIP  |  `api.<cluster_name>.<base_domain>.` |  This DNS A/AAAA or CNAME (Canonical Name) record must point to the load balancer for the cluster. This record must be resolvable by both clients external to the cluster and from all the nodes within the cluster.   
API VIP  |  `api-int.<cluster_name>.<base_domain>.` |  This DNS A/AAAA or CNAME (Canonical Name) record must point to the load balancer for the cluster. This record must be resolvable by all the nodes within the cluster.   
Ingress VIP  |  `*.apps.<cluster_name>.<base_domain>.` |  A wildcard DNS A/AAAA or CNAME record that points to the load balancer that targets the machines that run the Ingress router pods, which are the compute nodes by default. This record must be resolvable by both clients external to the cluster and from all the nodes within the cluster.   
Show more
