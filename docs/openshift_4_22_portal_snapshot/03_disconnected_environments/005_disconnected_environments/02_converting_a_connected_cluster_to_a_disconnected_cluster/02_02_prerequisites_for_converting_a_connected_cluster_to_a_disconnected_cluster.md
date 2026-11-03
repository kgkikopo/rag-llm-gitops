# 2.2. Prerequisites for converting a connected cluster to a disconnected cluster

You must meet several prerequisites before converting a connected cluster to a disconnected cluster. 

The following prerequisites must be met: 

  * The `oc` client is installed. 
  * A running cluster. 
  * An installed mirror registry, which is a container image registry that supports Docker v2-2 in the location that will host the OpenShift Container Platform cluster, such as one of the following registries: 

    * Red Hat Quay 
    * JFrog Artifactory 
    * Sonatype Nexus Repository 
    * Harbor 

If you have a subscription to Red Hat Quay, see the documentation on "Deploying Red Hat Quay for proof-of-concept purposes" or "Deploying Red Hat Quay by using the Quay Operator". 

  * The mirror repository must be configured to share images. For example, a Red Hat Quay repository requires organizations to share images. For more information, see the "Red Hat Quay documentation on organizations". 
  * Access to the internet to obtain the necessary container images. 



**Additional resources**

  * [Red Hat Quay](https://www.redhat.com/en/technologies/cloud-computing/quay)
  * [JFrog Artifactory](https://jfrog.com/artifactory/)
  * [Sonatype Nexus Repository](https://www.sonatype.com/products/repository-oss?topnav=true)
  * [Harbor](https://goharbor.io/)
  * [Deploying Red Hat Quay for proof-of-concept purposes](https://docs.redhat.com/en/documentation/red_hat_quay/3/html/proof_of_concept_-_deploying_red_hat_quay)
  * [Deploying Red Hat Quay by using the Quay Operator](https://access.redhat.com/documentation/en-us/red_hat_quay/3/html/deploying_the_red_hat_quay_operator_on_openshift_container_platform/index)
  * [Red Hat Quay documentation on organizations](https://access.redhat.com/documentation/en-us/red_hat_quay/3/html-single/use_red_hat_quay/index#user-org-intro_use-quay)
