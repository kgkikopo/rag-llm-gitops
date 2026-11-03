# 13.8. Pruning cron jobs

Clean up completed and failed Kubernetes jobs manually to prevent resource exhaustion. You can restrict cron job access to authorized users and configure resource quotas to control job and pod creation. 

Cron jobs can perform pruning of successful jobs, but might not properly handle failed jobs. Therefore, the cluster administrator should perform regular cleanup of jobs manually. They should also restrict the access to cron jobs to a small group of trusted users and set appropriate quota to prevent the cron job from creating too many jobs and pods. 

**Additional resources**

  * [Running tasks in pods using jobs](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#nodes-nodes-jobs)
  * [Resource quotas across multiple projects](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/building_applications/quotas#setting-quotas-across-multiple-projects "8.2. Resource quotas across multiple projects")
  * [Using RBAC to define and apply permissions](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/#using-rbac)
