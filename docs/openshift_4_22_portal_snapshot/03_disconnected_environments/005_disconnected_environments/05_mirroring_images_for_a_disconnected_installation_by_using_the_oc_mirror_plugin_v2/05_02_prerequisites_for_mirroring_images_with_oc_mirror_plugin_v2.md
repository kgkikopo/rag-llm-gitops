# 5.2. Prerequisites for mirroring images with oc-mirror plugin v2

Before you can mirror images with the oc-mirror plugin v2, you must meet several prerequisites. 

The following prerequisites must be met: 

  * You must have a container image registry that supports [Docker V2-2](https://docs.docker.com/registry/spec/manifest-v2-2) in the location that hosts the OpenShift Container Platform cluster, such as Red Hat Quay. 

Note

    * If you use Red Hat Quay, use version 3.6 or later with the oc-mirror plugin. See [Deploying the Red Hat Quay Operator on OpenShift Container Platform (Red Hat Quay documentation)](https://access.redhat.com/documentation/en-us/red_hat_quay/3/html/deploying_the_red_hat_quay_operator_on_openshift_container_platform/index). If you need additional assistance selecting and installing a registry, contact your sales representative or Red Hat Support. 
    * If you do not have an existing solution for a container image registry, OpenShift Container Platform subscribers receive a mirror registry for Red Hat OpenShift. This mirror registry is included with your subscription and serves as a small-scale container registry. You can use this registry to mirror the necessary container images of OpenShift Container Platform for disconnected installations. 

  * Every machine in the provisioned clusters must have access to the mirror registry. If the registry is unreachable, tasks like installation, updating, or routine operations such as workload relocation, might fail. Mirror registries must be operated in a highly available manner, ensuring their availability aligns with the production availability of your OpenShift Container Platform clusters.
