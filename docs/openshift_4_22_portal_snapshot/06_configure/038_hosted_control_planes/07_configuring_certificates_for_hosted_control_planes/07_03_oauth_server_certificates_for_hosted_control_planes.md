# 7.3. OAuth server certificates for hosted control planes

In hosted control planes, the OAuth server shares its serving certificate configuration with the Kubernetes API server. To configure a custom serving certificate for the OAuth server, you modify the `spec.configuration.apiServer` section in the `HostedCluster` resource. 

Important

This configuration method deviates from the standard OpenShift Container Platform behavior. In OpenShift Container Platform, OAuth certificates are configured separately through the `componentRoute` properties of the Ingress Operator. In hosted control planes, the `namedCertificates` configuration in the API server settings applies to both the Kubernetes API server and the OAuth server. 

In hosted control planes, the Control Plane Operator reads serving certificates through the shared `GetNamedCertificates()` function. Certificates are not configured in an OAuth-specific section of the `HostedCluster` resource. In addition, OAuth server certificates are not provided through an OAuth custom resource definition (CRD) configuration. Instead, hosted control planes automatically injects the selected certificates into the OAuth server deployment. 

Table 7.1. OAuth certificate differences between OpenShift Container Platform and hosted control planesArea| OpenShift Container Platform| hosted control planes  
---|---|---  
Certificate source  |  Ingress Operator generates and maps certificates through component routes  |  OAuth uses `apiServer.servingCerts.namedCertificates` settings   
Certificate selection  |  Based on ingress-managed routes  |  Based on host name match in `namedCertificates` property   
User responsibility  |  No need to manually provide OAuth certificates  |  User must supply certificates if custom behavior is needed   
Code path  |  Ingress Operator manages the OAuth route  |  Control Plane Operator manages the OAuth server container runtime arguments   
Show more
