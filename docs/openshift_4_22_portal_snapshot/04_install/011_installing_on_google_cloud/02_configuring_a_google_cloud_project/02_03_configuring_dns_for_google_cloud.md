# 2.3. Configuring DNS for Google Cloud

Configure a public hosted zone in your Google Cloud account to provide DNS resolution and name lookup for your OpenShift Container Platform cluster. 

To install OpenShift Container Platform, the Google Cloud account you use must have a dedicated public hosted zone in the same project that you host the OpenShift Container Platform cluster. This zone must be authoritative for the domain. The DNS service provides cluster DNS resolution and name lookup for external connections to the cluster. 

**Procedure**

  1. Identify your domain, or subdomain, and registrar. You can transfer an existing domain and registrar or obtain a new one through Google Cloud or another source. 

Note

If you purchase a new domain, it can take time for the relevant DNS changes to propagate. For more information about purchasing domains through Google, see [Google Domains](https://domains.google/). 

  2. Create a public hosted zone for your domain or subdomain in your Google Cloud project. See [Creating public zones](https://cloud.google.com/dns/zones/#creating_public_zones) in the Google Cloud documentation. 

Use an appropriate root domain, such as `openshiftcorp.com`, or subdomain, such as `clusters.openshiftcorp.com`. 

  3. Extract the new authoritative name servers from the hosted zone records. See [Look up your Cloud DNS name servers](https://cloud.google.com/dns/docs/update-name-servers#look_up_your_name_servers) in the Google Cloud documentation. 

You typically have four name servers. 

  4. Update the registrar records for the name servers that your domain uses. For example, if you registered your domain to Google Domains, see the following topic in the Google Domains Help: [How to switch to custom name servers](https://support.google.com/domains/answer/3290309?hl=en). 
  5. If you migrated your root domain to Google Cloud DNS, migrate your DNS records. See [Migrating to Cloud DNS](https://cloud.google.com/dns/docs/migrating) in the Google Cloud documentation. 
  6. If you use a subdomain, follow your company’s procedures to add its delegation records to the parent domain. This process might include a request to your company’s IT department or the division that controls the root domain and DNS services for your company.
