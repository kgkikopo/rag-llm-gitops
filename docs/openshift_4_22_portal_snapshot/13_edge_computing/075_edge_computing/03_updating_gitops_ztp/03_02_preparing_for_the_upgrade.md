# 3.2. Preparing for the upgrade

Use the following procedure to prepare your site for the GitOps Zero Touch Provisioning (ZTP) upgrade. 

**Procedure**

  1. Get the latest version of the GitOps ZTP container that has the custom resources (CRs) used to configure Red Hat OpenShift GitOps for use with GitOps ZTP. 
  2. Extract the `argocd/deployment` directory by using the following commands: 

```shell-session
$ mkdir -p ./update
```


```shell-session
$ podman run --log-driver=none --rm registry.redhat.io/openshift4/ztp-site-generate-rhel8:v4.22 extract /home/ztp --tar | tar x -C ./update
```


The `/update` directory contains the following subdirectories: 

     * `update/extra-manifest`: contains the source CR files that you package into a `ConfigMap` and reference in the `ClusterInstance` CR using the `extraManifestsRefs` field. 
     * `update/source-crs`: contains the source CR files that the `PolicyGenerator` or `PolicyGentemplate` CR uses to generate the Red Hat Advanced Cluster Management (RHACM) policies. 
     * `update/argocd/deployment`: contains patches and YAML files to apply on the hub cluster for use in the next step of this procedure. 
     * `update/argocd/example`: contains example `ClusterInstance` and `PolicyGenerator` or `PolicyGentemplate` files that represent the recommended configuration. 

  3. Update the `clusters-app.yaml` and `policies-app.yaml` files to reflect the name of your applications and the URL, branch, and path for your Git repository. 

If the upgrade includes changes that results in obsolete policies, the obsolete policies should be removed prior to performing the upgrade. 

  4. Diff the changes between the configuration and deployment source CRs in the `/update` folder and Git repo where you manage your fleet site CRs. Apply and push the required changes to your site repository. 

Important

When you update GitOps ZTP to the latest version, you must apply the changes from the `update/argocd/deployment` directory to your site repository. Do not use older versions of the `argocd/deployment/` files.
