# 2.1. Configuring Route 53

To install OpenShift Container Platform, the Amazon Web Services (AWS) account you use must have a dedicated public hosted zone in your Route 53 service. This zone must be authoritative for the domain. The Route 53 service provides cluster DNS resolution and name lookup for external connections to the cluster. 

**Procedure**

  1. Identify your domain, or subdomain, and registrar. You can transfer an existing domain and registrar or obtain a new one through AWS or another source. 

Note

If you purchase a new domain through AWS, it takes time for the relevant DNS changes to propagate. For more information about purchasing domains through AWS, see [Registering Domain Names Using Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar.html) in the AWS documentation. 

  2. If you are using an existing domain and registrar, migrate its DNS to AWS. See [Making Amazon Route 53 the DNS Service for an Existing Domain](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/MigratingDNS.html) in the AWS documentation. 
  3. Create a public hosted zone for your domain or subdomain. See [Creating a Public Hosted Zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/CreatingHostedZone.html) in the AWS documentation. 

Use an appropriate root domain, such as `openshiftcorp.com`, or subdomain, such as `clusters.openshiftcorp.com`. 

  4. Extract the new authoritative name servers from the hosted zone records. See [Getting the Name Servers for a Public Hosted Zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/GetInfoAboutHostedZone.html) in the AWS documentation. 
  5. Update the registrar records for the AWS Route 53 name servers that your domain uses. For example, if you registered your domain to a Route 53 service in a different accounts, see the following topic in the AWS documentation: [Adding or Changing Name Servers or Glue Records](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-name-servers-glue-records.html#domain-name-servers-glue-records-procedure). 
  6. If you are using a subdomain, add its delegation records to the parent domain. This gives Amazon Route 53 responsibility for the subdomain. Follow the delegation procedure outlined by the DNS provider of the parent domain. See [Creating a subdomain that uses Amazon Route 53 as the DNS service without migrating the parent domain](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/CreatingNewSubdomain.html) in the AWS documentation for an example high level procedure. 



## 2.1.1. Ingress Operator endpoint configuration for AWS Route 53

Configure Ingress Operator endpoints for OpenShift Container Platform clusters in Amazon Web Services (AWS) GovCloud (US) regions. Verifying these settings helps to ensure that your cluster connects to the correct API endpoints. 

If you install in either AWS GovCloud (US) US-West or US-East region, the Ingress Operator uses `us-gov-west-1` region for Route53 and tagging API clients. 

The Ingress Operator uses `<https://tagging.us-gov-west-1.amazonaws.com>` as the tagging API endpoint if a tagging custom endpoint is configured that includes the string 'us-gov-east-1'. 

For more information on AWS GovCloud (US) endpoints, see the [Service Endpoints](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/using-govcloud-endpoints.html) in the AWS documentation about GovCloud (US). 

Important

Private, disconnected installations are not supported for AWS GovCloud when you install in the `us-gov-east-1` region. 

**Example Route 53 configuration**

```yaml
platform:
  aws:
    region: us-gov-west-1
    serviceEndpoints:
    - name: ec2
      url: https://ec2.us-gov-west-1.amazonaws.com
    - name: elasticloadbalancing
      url: https://elasticloadbalancing.us-gov-west-1.amazonaws.com
    - name: route53
      url: https://route53.us-gov.amazonaws.com
    - name: tagging
      url: https://tagging.us-gov-west-1.amazonaws.com
```


where: 

`<https://route53.us-gov.amazonaws.com>`
     Defaults to `<https://route53.us-gov.amazonaws.com>` for both AWS GovCloud (US) regions. 
`<https://tagging.us-gov-west-1.amazonaws.com>`
     Only the US-West region has endpoints for tagging. Omit this parameter if your cluster is in another region.
