# 13.2. Default service accounts

OpenShift Container Platform automatically creates default service accounts for cluster management and in each project for build, deployment, and pod operations. 

## 13.2.1. Default cluster service accounts

Several infrastructure controllers run using service account credentials. The following service accounts are created in the OpenShift Container Platform infrastructure project (`openshift-infra`) at server start, and given the following roles cluster-wide: 

Service account| Description  
---|---  
`replication-controller` |  Assigned the `system:replication-controller` role   
`deployment-controller` |  Assigned the `system:deployment-controller` role   
`build-controller` |  Assigned the `system:build-controller` role. Additionally, the `build-controller` service account is included in the privileged security context constraint to create privileged build pods.   
Show more

## 13.2.2. Default project service accounts and roles

Three service accounts are automatically created in each project: 

Service account| Usage  
---|---  
`builder` |  Used by build pods. It is given the `system:image-builder` role, which allows pushing images to any imagestream in the project using the internal Docker registry.  Note The `builder` service account is not created if the `Build` cluster capability is not enabled.   
`deployer` |  Used by deployment pods and given the `system:deployer` role, which allows viewing and modifying replication controllers and pods in the project.  Note The `deployer` service account is not created if the `DeploymentConfig` cluster capability is not enabled.   
`default` |  Used to run all other pods unless they specify a different service account.  Important Access rights and security privileges tied to the `default` service account apply to every pod in the project that does not specify a different service account. To implement the principle of least privilege and improve auditability, create dedicated service accounts for your workloads instead of using the `default` service account.  While most OpenShift Container Platform platform components and Operators use dedicated service accounts, the following dynamic tools continue to use the `default` service account to ensure operational efficiency: 

  * `oc debug`: Uses the `default` service account to avoid the performance overhead of creating and removing unique service accounts for short-lived troubleshooting sessions. 
  * `oc adm must-gather`: Uses the `default` service account to collect diagnostic data across the cluster without requiring extensive manual RBAC modifications. 

  
Show more

All service accounts in a project are given the `system:image-puller` role, which allows pulling images from any image stream in the project using the internal container image registry. 

## 13.2.3. Automatically generated image pull secrets

OpenShift Container Platform automatically creates image pull secrets for each service account to integrate the internal image registry with user authentication. 

Note

Prior to OpenShift Container Platform 4.16, a long-lived service account API token secret was also generated for each service account that was created. Starting with OpenShift Container Platform 4.16, this service account API token secret is no longer created. 

After upgrading to 4.22, any existing long-lived service account API token secrets are not deleted and will continue to function. For information about detecting long-lived API tokens that are in use in your cluster or deleting them if they are not needed, see "Long-lived service account API tokens in OpenShift Container Platform (Red Hat Knowledgebase)". 

This image pull secret is necessary to integrate the OpenShift image registry into the cluster’s user authentication and authorization system. 

However, if you do not enable the `ImageRegistry` capability or if you disable the integrated OpenShift image registry in the Cluster Image Registry Operator’s configuration, an image pull secret is not generated for each service account. 

When the integrated OpenShift image registry is disabled on a cluster that previously had it enabled, the previously generated image pull secrets are deleted automatically.
