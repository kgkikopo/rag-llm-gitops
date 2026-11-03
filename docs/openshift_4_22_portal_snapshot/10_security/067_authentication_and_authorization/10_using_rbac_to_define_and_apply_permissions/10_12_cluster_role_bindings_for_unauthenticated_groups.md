# 10.12. Cluster role bindings for unauthenticated groups

Unauthenticated groups do not have default access to cluster roles. As a cluster administrator, you can grant limited unauthenticated access when required, while ensuring that the change complies with organizational security standards. 

Note

Before OpenShift Container Platform 4.17, unauthenticated groups were allowed access to some cluster roles. Clusters updated from versions before OpenShift Container Platform 4.17 retain this access for unauthenticated groups. 

For security reasons OpenShift Container Platform 4.22 does not allow unauthenticated groups to have default access to cluster roles. 

There are use cases where it might be necessary to add `system:unauthenticated` to a cluster role. 

Cluster administrators can add unauthenticated users to the following cluster roles: 

  * `system:scope-impersonation`
  * `system:webhook`
  * `system:oauth-token-deleter`
  * `self-access-reviewer`



Important

Always verify compliance with your organization’s security standards when modifying unauthenticated access.
