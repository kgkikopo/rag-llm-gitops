# 4.1. DNS considerations

The DNS domain of the target cluster is different from the domain of the source cluster. By default, applications get FQDNs of the target cluster after migration. 

To preserve the source DNS domain of migrated applications, select one of the two options described below. 

## 4.1.1. Isolating the DNS domain of the target cluster from the clients

You can allow the clients' requests sent to the DNS domain of the source cluster to reach the DNS domain of the target cluster without exposing the target cluster to the clients. 

**Procedure**

  1. Place an exterior network component, such as an application load balancer or a reverse proxy, between the clients and the target cluster. 
  2. Update the application FQDN on the source cluster in the DNS server to return the IP address of the exterior network component. 
  3. Configure the network component to send requests received for the application in the source domain to the load balancer in the target cluster domain. 
  4. Create a wildcard DNS record for the `*.apps.source.example.com` domain that points to the IP address of the load balancer of the source cluster. 
  5. Create a DNS record for each application that points to the IP address of the exterior network component in front of the target cluster. A specific DNS record has higher priority than a wildcard record, so no conflict arises when the application FQDN is resolved. 



Note

  * The exterior network component must terminate all secure TLS connections. If the connections pass through to the target cluster load balancer, the FQDN of the target application is exposed to the client and certificate errors occur. 
  * The applications must not return links referencing the target cluster domain to the clients. Otherwise, parts of the application might not load or work properly. 



## 4.1.2. Setting up the target cluster to accept the source DNS domain

You can set up the target cluster to accept requests for a migrated application in the DNS domain of the source cluster. 

**Procedure**

For both non-secure HTTP access and secure HTTPS access, perform the following steps: 

  1. Create a route in the target cluster’s project that is configured to accept requests addressed to the application’s FQDN in the source cluster: 

```shell-session
$ oc expose svc <app1-svc> --hostname <app1.apps.source.example.com> \
 -n <app1-namespace>
```


With this new route in place, the server accepts any request for that FQDN and sends it to the corresponding application pods. In addition, when you migrate the application, another route is created in the target cluster domain. Requests reach the migrated application using either of these hostnames. 

  2. Create a DNS record with your DNS provider that points the application’s FQDN in the source cluster to the IP address of the default load balancer of the target cluster. This will redirect traffic away from your source cluster to your target cluster. 

The FQDN of the application resolves to the load balancer of the target cluster. The default Ingress Controller router accept requests for that FQDN because a route for that hostname is exposed. 




For secure HTTPS access, perform the following additional step: 

  1. Replace the x509 certificate of the default Ingress Controller created during the installation process with a custom certificate. 
  2. Configure this certificate to include the wildcard DNS domains for both the source and target clusters in the `subjectAltName` field. 

The new certificate is valid for securing connections made using either DNS domain. 




**Additional resources**

  * See [Replacing the default ingress certificate](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/security_and_compliance/#replacing-default-ingress) for more information.
