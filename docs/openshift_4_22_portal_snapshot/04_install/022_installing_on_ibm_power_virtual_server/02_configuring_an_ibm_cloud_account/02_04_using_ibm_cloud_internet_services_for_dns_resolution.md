# 2.4. Using IBM Cloud Internet Services for DNS resolution

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


     2. Log in to IBM Cloud® by using the CLI: 

```shell-session
$ ibmcloud login
```


     3. Create the CIS instance: 

```shell-session
$ ibmcloud cis instance-create <instance_name> standard-next
```


At a minimum, you require a `Standard Next` plan for CIS to manage the cluster subdomain and its DNS records. 

Note

After you have configured your registrar or DNS provider, it can take up to 24 hours for the changes to take effect. 

  2. Connect an existing domain to your CIS instance: 

     1. Set the context instance for CIS: 

```shell-session
$ ibmcloud cis instance-set <instance_CRN>
```


Replace `<instance_CRN>` with the instance CRN (Cloud Resource Name). For example: `ibmcloud cis instance-set crn:v1:bluemix:public:power-iaas:osa21:a/65b64c1f1c29460d8c2e4bbfbd893c2c:c09233ac-48a5-4ccb-a051-d1cfb3fc7eb5::`

     2. Add the domain for CIS: 

```shell-session
$ ibmcloud cis domain-add <domain_name>
```


Replace `<domain_name>` with the fully qualified domain name. You can use either the root domain or subdomain value as the domain name, depending on which you plan to configure. 

Note

A root domain uses the form `openshiftcorp.com`. A subdomain uses the form `clusters.openshiftcorp.com`. 

  3. Open the CIS web console, navigate to the **Overview** page, and note your CIS name servers. These name servers are used in the next step. For more information, see "CIS web console". 
  4. Configure the name servers for your domains or subdomains at the domain’s registrar or DNS provider. For more information, see the IBM Cloud® documentation for "Configuring name servers".
