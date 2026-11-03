# 8.1. Prerequisites for mirroring images with the oc adm command

You must meet several prerequisites before you can mirror images using the `oc adm release mirror` command. 

You must meet the following prerequisites: 

  * You must have a container image registry that supports [Docker v2-2](https://docs.docker.com/registry/spec/manifest-v2-2) in the location that will host the OpenShift Container Platform cluster, such as one of the following registries: 

    * [Red Hat Quay](https://www.redhat.com/en/technologies/cloud-computing/quay)
    * [JFrog Artifactory](https://jfrog.com/artifactory/)
    * [Sonatype Nexus Repository](https://www.sonatype.com/products/repository-oss?topnav=true)
    * [Harbor](https://goharbor.io/)

If you have an entitlement to Red Hat Quay, see the documentation on deploying Red Hat Quay [for proof-of-concept purposes](https://docs.redhat.com/en/documentation/red_hat_quay/3.9/html/deploy_red_hat_quay_for_proof-of-concept_non-production_purposes/index) or [by using the Red Hat Quay Operator](https://access.redhat.com/documentation/en-us/red_hat_quay/3/html/deploying_the_red_hat_quay_operator_on_openshift_container_platform/index). If you need additional assistance selecting and installing a registry, contact your sales representative or Red Hat Support. 

  * If you do not already have an existing solution for a container image registry, subscribers of OpenShift Container Platform are provided a [mirror registry for Red Hat OpenShift](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/disconnected_environments/installing-mirroring-creating-registry "Chapter 4. Creating a mirror registry with mirror registry for Red Hat OpenShift"). The _mirror registry for Red Hat OpenShift_ is included with your subscription and is a small-scale container registry that can be used to mirror the required container images of OpenShift Container Platform in disconnected installations.
