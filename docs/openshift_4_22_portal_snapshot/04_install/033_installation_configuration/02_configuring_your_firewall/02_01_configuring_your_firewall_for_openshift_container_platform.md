# 2.1. Configuring your firewall for OpenShift Container Platform

Before you install OpenShift Container Platform, you must configure your firewall to grant access to the sites that OpenShift Container Platform requires. 

There are no special configuration considerations for services running on only controller nodes compared to compute nodes. 

Note

If your environment has a dedicated load balancer in front of your OpenShift Container Platform cluster, review the allowlists between your firewall and load balancer to prevent unwanted network restrictions to your cluster. 

**Procedure**

  1. Allowlist the following container registry URLs for cluster installation and upgrades: 

URL| Port| Function  
---|---|---  
`registry.redhat.io` |  443  |  Provides core container images   
`access.redhat.com` |  443  |  Hosts a signature store that a container client requires for verifying images pulled from `registry.access.redhat.com`. In a firewall environment, ensure that this resource is on the allowlist.   
`registry.access.redhat.com` |  443  |  Hosts all the container images that are stored on the Red Hat Ecosystem Catalog, including core container images.   
`quay.io` |  443  |  Provides core container images   
`cdn.quay.io` |  443  |  Provides core container images   
`cdn01.quay.io` |  443  |  Provides core container images   
`cdn02.quay.io` |  443  |  Provides core container images   
`cdn03.quay.io` |  443  |  Provides core container images   
`cdn04.quay.io` |  443  |  Provides core container images   
`cdn05.quay.io` |  443  |  Provides core container images   
`cdn06.quay.io` |  443  |  Provides core container images   
`icr.io` |  443  |  Provides IBM Cloud Pak container images. This domain is only required if you use IBM Cloud Paks.   
`cp.icr.io` |  443  |  Provides IBM Cloud Pak container images. This domain is only required if you use IBM Cloud Paks.   
Show more

     * You can use the wildcard `*.quay.io` instead of `cdn.quay.io` and `cdn0[1-6].quay.io` in your allowlist. 
     * You can use the wildcard `*.access.redhat.com` to simplify the configuration and ensure that all subdomains, including `registry.access.redhat.com`, are allowed. 
     * When adding a site such as `quay.io` to your allowlist, do not add a wildcard entry such as `*.quay.io` to your denylist. In most cases, image registries use a content delivery network (CDN) to serve images. If a firewall blocks access, image downloads are denied when the initial download request redirects to a hostname such as `cdn01.quay.io`. 

  2. Allowlist the following URLs to enable cluster access, authentication, and updates: 

URL| Port| Function  
---|---|---  
`*.apps.<cluster_name>.<base_domain>` |  443  |  Allowlist these URLs to enable cluster access, authentication, and updates.   
`api.openshift.com` |  443  |  API endpoint for cluster tokens and update checks.   
`console.redhat.com` |  443  |  Authentication service for cluster tokens.   
`sso.redhat.com` |  443  |  The `<https://console.redhat.com>` site uses authentication from `sso.redhat.com`  
Show more

For egress traffic, Operators require route access to perform health checks to establish a connection for reaching endpoints. The authentication and web console Operators connect to two routes to verify functionality. Cluster administrators who do not want to allow `*.apps.<cluster_name>.<base_domain>`, must allow the following routes: 

     * `oauth-openshift.apps.<cluster_name>.<base_domain>`
     * `canary-openshift-ingress-canary.apps.<cluster_name>.<base_domain>`
     * `console-openshift-console.apps.<cluster_name>.<base_domain>`, or the hostname that is specified in the `spec.route.hostname` field of the `consoles.operator/cluster` object if the field is not empty. 

  3. Allowlist the following registry URLs that host related artifacts for cluster installation and upgrades, such as installation content, release images, and client tools: 

URL| Port| Function  
---|---|---  
`mirror.openshift.com` |  443  |  Required to access mirrored installation content and images. This site is also a source of release image signatures, although the Cluster Version Operator needs only a single functioning source.   
`quayio-production-s3.s3.amazonaws.com` |  443  |  Required to access Quay image content in AWS.   
`rhcos.mirror.openshift.com` |  443  |  Required to download Red Hat Enterprise Linux CoreOS (RHCOS) images.   
`storage.googleapis.com/openshift-release` |  443  |  A source of release image signatures, although the Cluster Version Operator needs only a single functioning source.   
Show more

  4. Set your firewall’s allowlist to include any site that provides resources for a language or framework that your builds require. 
  5. If you do not disable Telemetry, you must grant access to the following URLs to access Telemetry and Red Hat Lightspeed: 

URL| Port| Function  
---|---|---  
`cert-api.access.redhat.com` |  443  |  Required for Telemetry   
`api.access.redhat.com` |  443  |  Required for Telemetry   
`infogw.api.openshift.com` |  443  |  Required for Telemetry   
`console.redhat.com` |  443  |  Required for Telemetry and for `insights-operator`  
Show more

  6. If you use Alibaba Cloud, Amazon Web Services (AWS), Microsoft Azure, or Google Cloud to host your cluster, you must grant access to the URLs that offer the cloud provider API and DNS for that cloud: 

Cloud| URL| Port| Function  
---|---|---|---  
Alibaba  |  `*.aliyuncs.com` |  443  |  Required to access Alibaba Cloud services and resources. Review the [Alibaba endpoints_config.go file](https://github.com/aliyun/alibaba-cloud-sdk-go/blob/master/sdk/endpoints/endpoints_config.go?spm=a2c4g.11186623.0.0.47875873ciGnC8&file=endpoints_config.go) to find the exact endpoints to allow for the regions that you use.   
AWS  |  `aws.amazon.com` |  443  |  Used to install and manage clusters in an AWS environment.   
`*.amazonaws.com` Alternatively, if you choose to not use a wildcard for AWS APIs, you must include the following URLs in your allowlist:  |  443  |  Required to access AWS services and resources. Review the [AWS Service Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html) in the AWS documentation to find the exact endpoints to allow for the regions that you use.   
`ec2.amazonaws.com` |  443  |  Used to install and manage clusters in an AWS environment.   
`ec2.us-east-1.amazonaws.com` |  443  |  Used to get the list of available regions when interactively generating the `install-config.yaml` file.   
`events.amazonaws.com` |  443  |  Used to install and manage clusters in an AWS environment.   
`iam.amazonaws.com` |  443  |  Used to install and manage clusters in an AWS environment.   
`route53.amazonaws.com` |  443  |  Used to install and manage clusters in an AWS environment.   
`*.s3.amazonaws.com` |  443  |  Used to install and manage clusters in an AWS environment.   
`*.s3.<aws_region>.amazonaws.com` |  443  |  Used to install and manage clusters in an AWS environment.   
`*.s3.dualstack.<aws_region>.amazonaws.com` |  443  |  Used to install and manage clusters in an AWS environment.   
`sts.amazonaws.com` |  443  |  Used to install and manage clusters in an AWS environment.   
`sts.<aws_region>.amazonaws.com` |  443  |  Used to install and manage clusters in an AWS environment.   
`tagging.us-east-1.amazonaws.com` |  443  |  Used to install and manage clusters in an AWS environment. This endpoint is always `us-east-1`, regardless of the region the cluster is deployed in.   
`ec2.<aws_region>.amazonaws.com` |  443  |  Used to install and manage clusters in an AWS environment.   
`elasticloadbalancing.<aws_region>.amazonaws.com` |  443  |  Used to install and manage clusters in an AWS environment.   
`servicequotas.<aws_region>.amazonaws.com` |  443  |  Required. Used to confirm quotas for deploying the service.   
`tagging.<aws_region>.amazonaws.com` |  443  |  Allows the assignment of metadata about AWS resources in the form of tags.   
`*.cloudfront.net` |  443  |  Used to provide access to CloudFront. If you use the AWS Security Token Service (STS) and the private S3 bucket, you must provide access to CloudFront.  |  GCP   
`*.googleapis.com` |  443  |  Required to access Google Cloud services and resources. Review [Cloud Endpoints](https://cloud.google.com/endpoints/) in the Google Cloud documentation to find the endpoints to allow for your APIs.   
`accounts.google.com` |  443  |  Required to access your Google Cloud account.  |  Microsoft Azure   
`management.azure.com` |  443  |  Required to access Microsoft Azure services and resources. Review the [Microsoft Azure REST API reference](https://docs.microsoft.com/en-us/rest/api/azure/) in the Microsoft Azure documentation to find the endpoints to allow for your APIs.   
`*.blob.core.windows.net` |  443  |  Required to download Ignition files.   
Show more

  7. Allowlist the following URL for optional third-party content: 

URL| Port| Function  
---|---|---  
`registry.connect.redhat.com` |  443  |  Required for all third-party images and certified operators.   
Show more

  8. If you use a default Red Hat Network Time Protocol (NTP) server, allow the following URLs. NTP operates on User Datagram Protocol (UDP) port 123, so this port must be opened on the firewall. 

URL| Port| Function  
---|---|---  
`1.rhel.pool.ntp.org` |  123  |  Provides NTP services for time synchronization.   
`2.rhel.pool.ntp.org` |  123  |  Provides NTP services for time synchronization.   
`3.rhel.pool.ntp.org` |  123  |  Provides NTP services for time synchronization.   
Show more

Note

If you do not use a default Red Hat NTP server, verify the NTP server for your platform and allow it in your firewall. 




**Additional resources**

  * [OpenID Connect requirements for AWS STS](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/#cco-short-term-creds-auth-flow-aws-oidc_cco-short-term-creds)
