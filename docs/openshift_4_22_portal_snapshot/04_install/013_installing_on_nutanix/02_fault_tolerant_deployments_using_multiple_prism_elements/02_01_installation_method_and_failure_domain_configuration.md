# 2.1. Installation method and failure domain configuration

The OpenShift Container Platform installation method determines how and when you configure failure domains: 

  * If you deploy using installer-provisioned infrastructure, you can configure failure domains in the installation configuration file before deploying the cluster. 

You can also configure failure domains after the cluster is deployed, as described in the following section. 

  * If you deploy using infrastructure that you manage (user-provisioned infrastructure) no additional configuration is required. After the cluster is deployed, you can manually distribute control plane and compute machines across failure domains.
