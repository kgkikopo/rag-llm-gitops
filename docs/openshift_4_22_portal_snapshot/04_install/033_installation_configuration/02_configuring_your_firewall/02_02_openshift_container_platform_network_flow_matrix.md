# 2.2. OpenShift Container Platform network flow matrix

You can use the information in the appropriate network flow matrix to manage ingress traffic for your specific environment. You can restrict ingress traffic to essential flows to improve network security. 

The following network flow matrixes describe the ingress flows to OpenShift Container Platform services for the following environments: 

  * OpenShift Container Platform on bare metal 
  * Single-node OpenShift with other platforms 
  * OpenShift Container Platform on Amazon Web Services (AWS) 
  * Single-node OpenShift on AWS 



Note

You can use the `commatrix` plugin for the `oc` command to generate local network flow data for your cluster. For more information see "Generating ingress network flow data using the `commatrix` plugin". 

Additionally, consider the following dynamic port ranges when managing ingress traffic for both bare metal and cloud environments: 

  * `9000-9999`: Reserved for internal OpenShift Container Platform components. Do not assign user workloads or services to ports in this range. 
  * `30000-32767`: Kubernetes `NodePort` service ports. These ports are required only if you expose services by using the `NodePort` service type. If `NodePort` services are not used, you can block this port range. 



To view or download the complete raw CSV content for an environment, see the following resources: 

  * [OpenShift Container Platform on bare metal](https://raw.githubusercontent.com/openshift-kni/commatrix/release-4.22/docs/stable/raw/bm.csv)
  * [Single-node OpenShift with other platforms](https://raw.githubusercontent.com/openshift-kni/commatrix/release-4.22/docs/stable/raw/none-sno.csv)
  * [OpenShift Container Platform on AWS](https://raw.githubusercontent.com/openshift-kni/commatrix/release-4.22/docs/stable/raw/aws.csv)
  * [Single-node OpenShift on AWS](https://raw.githubusercontent.com/openshift-kni/commatrix/release-4.22/docs/stable/raw/aws-sno.csv)



Note

The network flow matrixes describe ingress traffic flows for a base OpenShift Container Platform or single-node OpenShift installation. The matrixes do not apply for hosted control planes, Red Hat build of MicroShift, or standalone clusters. 

## 2.2.1. Base network flows

The following matrixes describe the base ingress flows to OpenShift Container Platform services. 

Note

For base ingress flows to single-node OpenShift clusters, see the _Control plane node base flows_ matrix only. 

Table 2.1. Control plane node base flowsDirection| Protocol| Port| Namespace| Service| Pod| Container| Node Role| Optional  
---|---|---|---|---|---|---|---|---  
Ingress  |  TCP  |  22  |  Host system service  |  sshd  |  |  |  master  |  TRUE   
Ingress  |  TCP  |  111  |  Host system service  |  rpcbind  |  |  |  master  |  TRUE   
Ingress  |  TCP  |  2379  |  openshift-etcd  |  etcd  |  etcd  |  etcdctl  |  master  |  FALSE   
Ingress  |  TCP  |  2380  |  openshift-etcd  |  healthz  |  etcd  |  etcd  |  master  |  FALSE   
Ingress  |  TCP  |  6080  |  openshift-kube-apiserver  |  |  kube-apiserver  |  kube-apiserver-insecure-readyz  |  master  |  FALSE   
Ingress  |  TCP  |  6443  |  openshift-kube-apiserver  |  apiserver  |  kube-apiserver  |  kube-apiserver  |  master  |  FALSE   
Ingress  |  TCP  |  8798  |  openshift-machine-config-operator  |  machine-config-daemon  |  machine-config-daemon  |  machine-config-daemon  |  master  |  FALSE   
Ingress  |  TCP  |  9001  |  openshift-machine-config-operator  |  machine-config-daemon  |  machine-config-daemon  |  kube-rbac-proxy  |  master  |  FALSE   
Ingress  |  TCP  |  9099  |  openshift-cluster-version  |  cluster-version-operator  |  cluster-version-operator  |  cluster-version-operator  |  master  |  FALSE   
Ingress  |  TCP  |  9100  |  openshift-monitoring  |  node-exporter  |  node-exporter  |  kube-rbac-proxy  |  master  |  FALSE   
Ingress  |  TCP  |  9103  |  openshift-ovn-kubernetes  |  ovn-kubernetes-node  |  ovnkube-node  |  kube-rbac-proxy-node  |  master  |  FALSE   
Ingress  |  TCP  |  9104  |  openshift-network-operator  |  metrics  |  network-operator  |  network-operator  |  master  |  FALSE   
Ingress  |  TCP  |  9105  |  openshift-ovn-kubernetes  |  ovn-kubernetes-node  |  ovnkube-node  |  kube-rbac-proxy-ovn-metrics  |  master  |  FALSE   
Ingress  |  TCP  |  9107  |  openshift-ovn-kubernetes  |  egressip-node-healthcheck  |  ovnkube-node  |  ovnkube-controller  |  master  |  FALSE   
Ingress  |  TCP  |  9108  |  openshift-ovn-kubernetes  |  ovn-kubernetes-control-plane  |  ovnkube-control-plane  |  kube-rbac-proxy  |  master  |  FALSE   
Ingress  |  TCP  |  9192  |  openshift-cluster-machine-approver  |  machine-approver  |  machine-approver  |  kube-rbac-proxy  |  master  |  FALSE   
Ingress  |  TCP  |  9258  |  openshift-cloud-controller-manager-operator  |  machine-approver  |  cluster-cloud-controller-manager  |  cluster-cloud-controller-manager  |  master  |  FALSE   
Ingress  |  TCP  |  9443  |  openshift-cloud-controller-manager-operator  |  cloud-controller-manager-operator  |  cluster-cloud-controller-manager-operator  |  cluster-cloud-controller-manager  |  master  |  FALSE   
Ingress  |  TCP  |  9637  |  openshift-machine-config-operator  |  kube-rbac-proxy-crio  |  kube-rbac-proxy-crio  |  kube-rbac-proxy-crio  |  master  |  FALSE   
Ingress  |  TCP  |  9978  |  openshift-etcd  |  etcd  |  etcd  |  etcd-metrics  |  master  |  FALSE   
Ingress  |  TCP  |  9979  |  openshift-etcd  |  etcd  |  etcd  |  etcd-metrics  |  master  |  FALSE   
Ingress  |  TCP  |  9980  |  openshift-etcd  |  etcd  |  etcd  |  etcd  |  master  |  FALSE   
Ingress  |  TCP  |  10250  |  Host system service  |  kubelet  |  |  |  master  |  FALSE   
Ingress  |  TCP  |  10256  |  openshift-ovn-kubernetes  |  ovnkube  |  ovnkube  |  ovnkube-controller  |  master  |  FALSE   
Ingress  |  TCP  |  10257  |  openshift-kube-controller-manager  |  kube-controller-manager  |  kube-controller-manager  |  kube-controller-manager  |  master  |  FALSE   
Ingress  |  TCP  |  10259  |  openshift-kube-scheduler  |  scheduler  |  openshift-kube-scheduler  |  kube-scheduler  |  master  |  FALSE   
Ingress  |  TCP  |  17697  |  openshift-kube-apiserver  |  openshift-kube-apiserver-healthz  |  kube-apiserver  |  kube-apiserver-check-endpoints  |  master  |  FALSE   
Ingress  |  TCP  |  22623  |  openshift-machine-config-operator  |  machine-config-server  |  machine-config-server  |  machine-config-server  |  master  |  FALSE   
Ingress  |  TCP  |  22624  |  openshift-machine-config-operator  |  machine-config-server  |  machine-config-server  |  machine-config-server  |  master  |  FALSE   
Ingress  |  UDP  |  111  |  Host system service  |  rpcbind  |  |  |  master  |  TRUE   
Show more

Table 2.2. Worker node base flowsDirection| Protocol| Port| Namespace| Service| Pod| Container| Node Role| Optional  
---|---|---|---|---|---|---|---|---  
Ingress  |  TCP  |  22  |  Host system service  |  sshd  |  |  |  worker  |  TRUE   
Ingress  |  TCP  |  111  |  Host system service  |  rpcbind  |  |  |  worker  |  TRUE   
Ingress  |  TCP  |  8798  |  openshift-machine-config-operator  |  machine-config-daemon  |  machine-config-daemon  |  machine-config-daemon  |  worker  |  FALSE   
Ingress  |  TCP  |  9001  |  openshift-machine-config-operator  |  machine-config-daemon  |  machine-config-daemon  |  kube-rbac-proxy  |  worker  |  FALSE   
Ingress  |  TCP  |  9100  |  openshift-monitoring  |  node-exporter  |  node-exporter  |  kube-rbac-proxy  |  worker  |  FALSE   
Ingress  |  TCP  |  9103  |  openshift-ovn-kubernetes  |  ovn-kubernetes-node  |  ovnkube-node  |  kube-rbac-proxy-node  |  worker  |  FALSE   
Ingress  |  TCP  |  9105  |  openshift-ovn-kubernetes  |  ovn-kubernetes-node  |  ovnkube-node  |  kube-rbac-proxy-ovn-metrics  |  worker  |  FALSE   
Ingress  |  TCP  |  9107  |  openshift-ovn-kubernetes  |  egressip-node-healthcheck  |  ovnkube-node  |  ovnkube-controller  |  worker  |  FALSE   
Ingress  |  TCP  |  9637  |  openshift-machine-config-operator  |  kube-rbac-proxy-crio  |  kube-rbac-proxy-crio  |  kube-rbac-proxy-crio  |  worker  |  FALSE   
Ingress  |  TCP  |  10250  |  Host system service  |  kubelet  |  |  |  worker  |  FALSE   
Ingress  |  TCP  |  10256  |  openshift-ovn-kubernetes  |  ovnkube  |  ovnkube  |  ovnkube-controller  |  worker  |  FALSE   
Ingress  |  UDP  |  111  |  Host system service  |  rpcbind  |  |  |  worker  |  TRUE   
Show more

## 2.2.2. Additional network flows for OpenShift Container Platform on bare metal

In addition to the base network flows, the following matrix describes the ingress flows to OpenShift Container Platform services that are specific to OpenShift Container Platform on bare metal. 

Table 2.3. OpenShift Container Platform on bare metalDirection| Protocol| Port| Namespace| Service| Pod| Container| Node Role| Optional  
---|---|---|---|---|---|---|---|---  
Ingress  |  TCP  |  53  |  openshift-dns  |  dns-default  |  dns-default  |  dns  |  master  |  FALSE   
Ingress  |  TCP  |  6180  |  openshift-machine-api  |  metal3-state  |  metal3  |  metal3-httpd  |  master  |  FALSE   
Ingress  |  TCP  |  6183  |  openshift-machine-api  |  metal3-state  |  metal3  |  metal3-httpd  |  master  |  FALSE   
Ingress  |  TCP  |  6385  |  openshift-machine-api  |  metal3-state  |  metal3  |  metal3-httpd  |  master  |  FALSE   
Ingress  |  TCP  |  6388  |  openshift-machine-api  |  metal3-state  |  metal3  |  metal3-httpd  |  master  |  FALSE   
Ingress  |  TCP  |  9444  |  openshift-kni-infra  |  |  haproxy  |  haproxy  |  master  |  FALSE   
Ingress  |  TCP  |  9445  |  openshift-kni-infra  |  |  haproxy  |  haproxy  |  master  |  FALSE   
Ingress  |  TCP  |  9454  |  openshift-kni-infra  |  |  haproxy  |  haproxy  |  master  |  FALSE   
Ingress  |  TCP  |  18080  |  openshift-kni-infra  |  |  coredns  |  coredns  |  master  |  FALSE   
Ingress  |  UDP  |  53  |  openshift-dns  |  dns-default  |  dns-default  |  dns  |  master  |  FALSE   
Ingress  |  UDP  |  6081  |  openshift-ovn-kubernetes  |  ovn-kubernetes geneve  |  |  |  master  |  FALSE   
Ingress  |  TCP  |  53  |  openshift-dns  |  dns-default  |  dns-default  |  dns  |  worker  |  FALSE   
Ingress  |  TCP  |  80  |  openshift-ingress  |  router-internal-default  |  router-default  |  router  |  worker  |  FALSE   
Ingress  |  TCP  |  443  |  openshift-ingress  |  router-internal-default  |  router-default  |  router  |  worker  |  FALSE   
Ingress  |  TCP  |  1936  |  openshift-ingress  |  router-internal-default  |  router-default  |  router  |  worker  |  FALSE   
Ingress  |  TCP  |  18080  |  openshift-kni-infra  |  |  coredns  |  coredns  |  worker  |  FALSE   
Ingress  |  UDP  |  53  |  openshift-dns  |  dns-default  |  dns-default  |  dns  |  worker  |  FALSE   
Ingress  |  UDP  |  6081  |  openshift-ovn-kubernetes  |  ovn-kubernetes geneve  |  |  |  worker  |  FALSE   
Show more

## 2.2.3. Additional network flows for single-node OpenShift with other platforms

In addition to the base network flows, the following matrix describes the ingress flows to OpenShift Container Platform services that are specific to single-node OpenShift configured with `platform: none` in the installation manifest. 

Table 2.4. Single-node OpenShift with other platformsDirection| Protocol| Port| Namespace| Service| Pod| Container| Node Role| Optional  
---|---|---|---|---|---|---|---|---  
Ingress  |  TCP  |  80  |  openshift-ingress  |  router-internal-default  |  router-default  |  router  |  master  |  FALSE   
Ingress  |  TCP  |  443  |  openshift-ingress  |  router-internal-default  |  router-default  |  router  |  master  |  FALSE   
Ingress  |  TCP  |  1936  |  openshift-ingress  |  router-internal-default  |  router-default  |  router  |  master  |  FALSE   
Show more

## 2.2.4. Additional network flows for OpenShift Container Platform on AWS

In addition to the base network flows, the following matrix describes the ingress flows to OpenShift Container Platform services that are specific to OpenShift Container Platform on AWS. 

Table 2.5. OpenShift Container Platform on AWSDirection| Protocol| Port| Namespace| Service| Pod| Container| Node Role| Optional  
---|---|---|---|---|---|---|---|---  
Ingress  |  TCP  |  10258  |  openshift-cloud-controller-manager-operator  |  cloud-controller  |  cloud-controller-manager  |  cloud-controller-manager  |  master  |  FALSE   
Ingress  |  TCP  |  80  |  openshift-ingress  |  router-default  |  router-default  |  router  |  worker  |  FALSE   
Ingress  |  TCP  |  443  |  openshift-ingress  |  router-default  |  router-default  |  router  |  worker  |  FALSE   
Ingress  |  UDP  |  6081  |  openshift-ovn-kubernetes  |  ovn-kubernetes geneve  |  |  |  worker  |  FALSE   
Show more

## 2.2.5. Additional network flows for single-node OpenShift on AWS

In addition to the base network flows, the following matrix describes the ingress flows to OpenShift Container Platform services that are specific to single-node OpenShift on AWS. 

Table 2.6. Single-node OpenShift on AWSDirection| Protocol| Port| Namespace| Service| Pod| Container| Node Role| Optional  
---|---|---|---|---|---|---|---|---  
Ingress  |  TCP  |  80  |  openshift-ingress  |  router-default  |  router-default  |  router  |  master  |  FALSE   
Ingress  |  TCP  |  443  |  openshift-ingress  |  router-default  |  router-default  |  router  |  master  |  FALSE   
Ingress  |  TCP  |  10258  |  openshift-cloud-controller-manager-operator  |  cloud-controller  |  cloud-controller-manager  |  cloud-controller-manager  |  master  |  FALSE   
Show more
