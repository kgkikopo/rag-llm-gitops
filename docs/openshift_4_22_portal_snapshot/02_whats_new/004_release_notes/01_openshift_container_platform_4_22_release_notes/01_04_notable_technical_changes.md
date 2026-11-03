# 1.4. Notable technical changes

You can review the list of technical changes for OpenShift Container Platform 4.22 to see if any of the changes affect your clusters or environments. 

Platform components and Operators now use dedicated service accounts
    

Most OpenShift Container Platform platform components and Operators have been updated to use dedicated service accounts instead of the `default` service account. This change follows the principle of least privilege, simplifies security audits, and reduces the risk of accidental permission elevation by ensuring that platform identities are isolated from user workloads. 

The following dynamic tools continue to use the `default` service account to ensure operational efficiency: 

  * `oc debug`: Uses the `default` service account to avoid the performance overhead of creating and removing unique service accounts for short-lived troubleshooting sessions. 
  * `oc adm must-gather`: Uses the `default` service account to collect diagnostic data across the cluster without requiring extensive manual RBAC modifications. 



For more information, see [Default project service accounts and roles](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/#default-service-accounts-and-roles_using-service-accounts). 

Unused Cluster API Operator image removed from release image
     With this update, the OpenShift Container Platform release image no longer includes the `cluster-api-operator` image. As a result, you can no longer pull this image from the release image manually. If you mirror the release image, you can delete this image from your mirror. ([OCPBUGS-61949](https://redhat.atlassian.net/browse/OCPBUGS-61949))
