# 14.6. Proxy support for hosted control planes

To ensure that control-plane workloads, compute nodes, management clusters, and hosted clusters have the access they need for optimal performance, you can configure proxy support. 

In standalone OpenShift Container Platform, the primary purposes of proxy support are ensuring that workloads in the cluster are configured to use the HTTP or HTTPS proxy to access external services, honoring the `NO_PROXY` setting if one is configured, and accepting any trust bundle that is configured for the proxy. 

In hosted control planes, proxy support includes use cases beyond those in standalone OpenShift Container Platform. 

## 14.6.1. Control plane workloads that need to access external services

Operators that run in the control plane need to access external services through the proxy that is configured for the hosted cluster. The proxy is usually accessible only through the data plane. 

The control plane workloads are as follows: 

  * The Control Plane Operator needs to validate and obtain endpoints from certain identity providers when it creates the OAuth server configuration. 
  * The OAuth server needs non-LDAP identity provider access. 
  * The OpenShift API server handles image registry metadata import. 
  * The Ingress Operator needs access to validate external canary routes. 
  * You must open the firewall port `53` on Transmission Control Protocol (TCP) and User Datagram Protocol (UDP) to allow the Domain Name Service (DNS) protocol to work as expected. 



In a hosted cluster, you must send traffic that originates from the Control Plane Operator, Ingress Operator, OAuth server, and OpenShift API server pods through the data plane to the configured proxy and then to its final destination. 

Note

Some operations are not possible when a hosted cluster is reduced to zero compute nodes; for example, when you import OpenShift image streams from a registry that requires proxy access. 

## 14.6.2. Compute nodes that need to access an ignition endpoint

When compute nodes need a proxy to access the ignition endpoint, you must configure the proxy in the user-data stub that is configured on the compute node when it is created. 

For cases where machines need a proxy to access the ignition URL, the proxy configuration is included in the stub. 

The stub resembles the following example: 

```shell-session
{"ignition":{"config":{"merge":[{"httpHeaders":[{"name":"Authorization","value":"Bearer ..."},{"name":"TargetConfigVersionHash","value":"a4c1b0dd"}],"source":"https://ignition.controlplanehost.example.com/ignition","verification":{}}],"replace":{"verification":{}}},"proxy":{"httpProxy":"http://proxy.example.org:3128", "httpsProxy":"https://proxy.example.org:3129", "noProxy":"host.example.org"},"security":{"tls":{"certificateAuthorities":[{"source":"...","verification":{}}]}},"timeouts":{},"version":"3.2.0"},"passwd":{},"storage":{},"systemd":{}}
```


## 14.6.3. Compute nodes that need to access the API server

For control plane communications, hosted control planes uses a local proxy on each compute node that listens on 172.20.0.1 and forwards traffic to the API server. If accessing the API server requires an external proxy, the local proxy forwards traffic through it. 

When a proxy is not needed, hosted control planes uses `haproxy` for the local proxy, which only forwards packets via TCP. When a proxy is needed, hosted control planes uses a custom proxy, `control-plane-operator-kubernetes-default-proxy`, to send traffic through the external proxy. 

Note

This use case is relevant to self-managed hosted control planes, not to Red Hat OpenShift Service on AWS. 

## 14.6.4. Management clusters that need external access

The HyperShift Operator has a controller that monitors the OpenShift global proxy configuration of the management cluster and sets the proxy environment variables on its own deployment. 

Control plane deployments that need external access are configured with the proxy environment variables of the management cluster. 

## 14.6.5. Management cluster with a proxy and a hosted cluster with a secondary network and no default pod network

If a management cluster uses a proxy configuration and you are configuring a hosted cluster with a secondary network but are not attaching the default pod network, add the CIDR of the secondary network to the proxy configuration. 

Specifically, you need to add the CIDR of the secondary network to the `noProxy` section of the proxy configuration for the management cluster. Otherwise, the Kubernetes API server will route some API requests through the proxy. In the hosted cluster configuration, the CIDR of the secondary network is automatically added to the `noProxy` section. 

**Additional resources**

  * [Troubleshooting internal subnets for hosted clusters](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hosted_control_planes/hcp-troubleshooting#hcp-ts-internal-subnets_hcp-troubleshooting "15.9. Known limitations for internal subnets for hosted clusters")
  * [Creating a hosted cluster by using the CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hosted_control_planes/deploying-hosted-control-planes#hcp-bm-hc_hcp-deploy-bm "4.3.6.1. Creating a hosted cluster by using the CLI")
  * [About the OVN-Kubernetes network plugin](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/ovn-kubernetes_network_plugin/#about-the-ovn-kubernetes-network-plugin)
  * [Configuring the cluster-wide proxy](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/configuring_network_settings/#enable-cluster-wide-proxy)
