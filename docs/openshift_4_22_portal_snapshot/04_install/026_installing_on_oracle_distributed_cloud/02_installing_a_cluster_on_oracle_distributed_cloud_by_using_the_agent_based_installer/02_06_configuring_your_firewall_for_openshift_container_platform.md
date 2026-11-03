# 2.6. Configuring your firewall for OpenShift Container Platform

Before you install OpenShift Container Platform, you must configure your firewall to grant access to the sites that OpenShift Container Platform requires. 

For a disconnected environment, you must mirror content from both Red Hat and Oracle. This environment requires that you create firewall rules to expose your firewall to specific ports and registries. 

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

  6. Set your firewall’s allowlist to include the following registry URLs: 

URL| Port| Function  
---|---|---  
`api.openshift.com` |  443  |  Required both for your cluster token and to check if updates are available for the cluster.   
`rhcos.mirror.openshift.com` |  443  |  Required to download Red Hat Enterprise Linux CoreOS (RHCOS) images.   
Show more

  7. Set your firewall’s allowlist to include the following external URLs. Each repository URL hosts OCI containers. Consider mirroring images to as few repositories as possible to reduce any performance issues. 

URL| Port| Function  
---|---|---  
`k8s.gcr.io` |  port  |  A Kubernetes registry that hosts container images for a community-based image registry. This image registry is hosted on a custom Google Container Registry (GCR) domain.   
`ghcr.io` |  port  |  A GitHub image registry where you can store and manage Open Container Initiative images. Requires an access token to publish, install, and delete private, internal, and public packages.   
`storage.googleapis.com` |  443  |  A source of release image signatures, although the Cluster Version Operator needs only a single functioning source.   
`registry.k8s.io` |  port  |  Replaces the `k8s.gcr.io` image registry because the `k8s.gcr.io` image registry does not support other platforms and vendors.   
Show more
