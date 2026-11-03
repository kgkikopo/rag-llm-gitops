# 2.2. DNS resolution configuration

When installing a cluster on IBM Cloud®, the method for configuring DNS resolution depends on whether you are deploying a public or private cluster. 

How you configure DNS resolution depends on the type of OpenShift Container Platform cluster you are installing: 

  * If you are installing a public cluster, you use IBM Cloud Internet Services (CIS). 
  * If you are installing a private cluster, you use IBM Cloud® DNS Services (DNS Services). 



## 2.2.1. Using IBM Cloud Internet Services for DNS resolution

The installation program uses IBM Cloud® Internet Services (CIS) to configure cluster DNS resolution and provide name lookup for a public cluster. 

Note

This offering does not support IPv6, so dual stack or IPv6 environments are not possible. 

You must create a domain zone in CIS in the same account as your cluster. You must also ensure the zone is authoritative for the domain. You can do this using a root domain or subdomain. 

**Prerequisites**

  * You have installed the IBM Cloud® CLI. For more information, see "IBM Cloud® CLI". 
  * You have an existing domain and registrar. For more information, see the "IBM® DNS documentation". 



**Procedure**

  1. Create a CIS instance to use with your cluster: 

     1. Install the CIS plugin: 

```shell-session
$ ibmcloud plugin install cis
```


     2. Create the CIS instance: 

```shell-session
$ ibmcloud cis instance-create <instance_name> standard-next
```


At a minimum, you require a `Standard Next` plan for CIS to manage the cluster subdomain and its DNS records. 

Note

After you have configured your registrar or DNS provider, it can take up to 24 hours for the changes to take effect. 

  2. Connect an existing domain to your CIS instance: 

     1. Set the context instance for CIS: 

```shell-session
$ ibmcloud cis instance-set <instance_name>
```


Replace `<instance_name>` with the instance cloud resource name. 

     2. Add the domain for CIS: 

```shell-session
$ ibmcloud cis domain-add <domain_name>
```


Replace `<domain_name>` with the fully qualified domain name. You can use either the root domain or subdomain value as the domain name, depending on which you plan to configure. 

Note

A root domain uses the form `openshiftcorp.com`. A subdomain uses the form `clusters.openshiftcorp.com`. 

  3. Open the CIS web console, navigate to the **Overview** page, and note your CIS name servers. These name servers are used in the next step. For more information, see "CIS web console". 
  4. Configure the name servers for your domains or subdomains at the domain’s registrar or DNS provider. For more information, see the IBM Cloud® documentation for "Configuring name servers". 



**Additional resources**

  * [IBM Cloud® CLI (IBM Cloud® documentation)](https://www.ibm.com/cloud/cli)
  * [IBM® DNS documentation](https://cloud.ibm.com/docs/dns?topic=dns-getting-started)
  * [CIS web console (IBM Cloud® documentation)](https://cloud.ibm.com/catalog/services/internet-services)
  * [IBM Cloud® documentation for configuring name servers](https://cloud.ibm.com/docs/cis?topic=cis-getting-started#configure-your-name-servers-with-the-registrar-or-existing-dns-provider)



## 2.2.2. Using IBM Cloud DNS Services for DNS resolution

The installation program uses IBM Cloud® DNS Services to configure cluster DNS resolution and provide name lookup for a private cluster. 

You configure DNS resolution by creating a DNS services instance for the cluster, and then adding a DNS zone to the DNS Services instance. Ensure that the zone is authoritative for the domain. You can do this using a root domain or subdomain. 

Note

IBM Cloud® does not support IPv6, so dual stack or IPv6 environments are not possible. 

**Prerequisites**

  * You have installed the IBM Cloud® CLI. For more information, see "IBM Cloud® CLI". 
  * You have an existing domain and registrar. For more information, see the "IBM® DNS documentation". 



**Procedure**

  1. Create a DNS Services instance to use with your cluster: 

     1. Install the DNS Services plugin by running the following command: 

```shell-session
$ ibmcloud plugin install cloud-dns-services
```


     2. Create the DNS Services instance by running the following command: 

```shell-session
$ ibmcloud dns instance-create <instance-name> standard-dns
```


At a minimum, you require a `Standard DNS` plan for DNS Services to manage the cluster subdomain and its DNS records. 

Note

After you have configured your registrar or DNS provider, it can take up to 24 hours for the changes to take effect. 

  2. Create a DNS zone for the DNS Services instance: 

     1. Set the target operating DNS Services instance by running the following command: 

```shell-session
$ ibmcloud dns instance-target <instance-name>
```


     2. Add the DNS zone to the DNS Services instance by running the following command: 

```shell-session
$ ibmcloud dns zone-create <zone-name>
```


Replace `<zone-name>` with the fully qualified zone name. You can use either the root domain or subdomain value as the zone name, depending on which you plan to configure. A root domain uses the form `openshiftcorp.com`. A subdomain uses the form `clusters.openshiftcorp.com`. 

  3. Record the name of the DNS zone you have created. As part of the installation process, you must update the `install-config.yaml` file before deploying the cluster. Use the name of the DNS zone as the value for the `baseDomain` parameter. 

Note

You do not have to manage permitted networks or configure an "A" DNS resource record. As required, the installation program configures these resources automatically. 




**Additional resources**

  * [IBM Cloud® CLI (IBM Cloud® documentation)](https://www.ibm.com/cloud/cli)
  * [IBM® DNS documentation](https://cloud.ibm.com/docs/dns?topic=dns-getting-started)
