# 2.8. Configure the hub cluster with ArgoCD

You can configure the hub cluster with a set of ArgoCD applications that generate the required installation and policy custom resources (CRs) for each site with GitOps Zero Touch Provisioning (ZTP). 

Note

Red Hat Advanced Cluster Management (RHACM) uses `ClusterInstance` CRs to generate the Day 1 managed cluster installation CRs for ArgoCD. Each ArgoCD application can manage a maximum of 1000 `ClusterInstance` CRs. 

**Prerequisites**

  * You have a OpenShift Container Platform hub cluster with Red Hat Advanced Cluster Management (RHACM) and Red Hat OpenShift GitOps installed. 
  * You have extracted the reference deployment from the GitOps ZTP plugin container as described in the "Preparing the GitOps ZTP site configuration repository" section. Extracting the reference deployment creates the `out/argocd/deployment` directory referenced in the following procedure. 



**Procedure**

  1. Prepare the ArgoCD pipeline configuration: 

     1. Create a Git repository with the directory structure similar to the example directory. For more information, see "Preparing the GitOps ZTP site configuration repository". 
     2. Configure access to the repository using the ArgoCD UI. Under **Settings** configure the following: 

        * **Repositories** \- Add the connection information. The URL must end in `.git`, for example, `<https://repo.example.com/repo.git>` and credentials. 
        * **Certificates** \- Add the public certificate for the repository, if needed. 

     3. Modify the two ArgoCD applications, `out/argocd/deployment/clusters-app.yaml` and `out/argocd/deployment/policies-app.yaml`, based on your Git repository: 

        * Update the URL to point to the Git repository. The URL ends with `.git`, for example, `<https://repo.example.com/repo.git>`. 
        * The `targetRevision` indicates which Git repository branch to monitor. 
        * `path` specifies the path to the `ClusterInstance` and `PolicyGenerator` or `PolicyGentemplate` CRs, respectively. 

  2. To install the GitOps ZTP plugin, patch the ArgoCD instance in the hub cluster with the relevant multicluster engine (MCE) subscription image. Customize the patch file that you previously extracted into the `out/argocd/deployment/` directory for your environment. 

     1. Select the `multicluster-operators-subscription` image that matches your RHACM version. 

        * For RHACM 2.8 and 2.9, use the `registry.redhat.io/rhacm2/multicluster-operators-subscription-rhel8:v<rhacm_version>` image. 
        * For RHACM 2.10 and later, use the `registry.redhat.io/rhacm2/multicluster-operators-subscription-rhel9:v<rhacm_version>` image. 

Important

The version of the `multicluster-operators-subscription` image must match the RHACM version. Beginning with the MCE 2.10 release, RHEL 9 is the base image for `multicluster-operators-subscription` images. 

Click `[Expand for Operator list]` in the "Platform Aligned Operators" table in [OpenShift Operator Life Cycles](https://access.redhat.com/support/policy/updates/openshift_operators) to view the complete supported Operators matrix for OpenShift Container Platform. 

     2. Modify the `out/argocd/deployment/argocd-openshift-gitops-patch.json` file with the `multicluster-operators-subscription` image that matches your RHACM version: 

```plaintext
{
  "args": [
    "-c",
    "mkdir -p /.config/kustomize/plugin/policy.open-cluster-management.io/v1/policygenerator && cp /policy-generator/PolicyGenerator-not-fips-compliant /.config/kustomize/plugin/policy.open-cluster-management.io/v1/policygenerator/PolicyGenerator"
  ],
  "command": [
    "/bin/bash"
  ],
  "image": "registry.redhat.io/rhacm2/multicluster-operators-subscription-rhel9:v2.10",
  "name": "policy-generator-install",
  "imagePullPolicy": "Always",
  "volumeMounts": [
    {
      "mountPath": "/.config",
      "name": "kustomize"
    }
  ]
}
```


        * Optional: For RHEL 9 images, in the `args` field, change the executable path from `/policy-generator/PolicyGenerator-not-fips-compliant` to match the required universal executable for your ArgoCD version. 
        * Match the `multicluster-operators-subscription` image to your RHACM version. In disconnected environments, replace the URL with the disconnected registry equivalent for your environment. 

     3. Patch the ArgoCD instance. Run the following command: 

```shell-session
$ oc patch argocd openshift-gitops \
-n openshift-gitops --type=merge \
--patch-file out/argocd/deployment/argocd-openshift-gitops-patch.json
```


  3. In RHACM 2.7 and later, the multicluster engine enables the `cluster-proxy-addon` feature by default. Apply the following patch to disable the `cluster-proxy-addon` feature and remove the relevant hub cluster and managed pods that are responsible for this add-on. Run the following command: 

```shell-session
$ oc patch multiclusterengines.multicluster.openshift.io multiclusterengine --type=merge --patch-file out/argocd/deployment/disable-cluster-proxy-addon.json
```


  4. Apply the pipeline configuration to your hub cluster by running the following command: 

```shell-session
$ oc apply -k out/argocd/deployment
```


  5. Optional: If you have existing ArgoCD applications, verify that the `PrunePropagationPolicy=background` policy is set in the `Application` resource by running the following command: 

```shell-session
$ oc -n openshift-gitops get applications.argoproj.io  \
clusters -o jsonpath='{.spec.syncPolicy.syncOptions}' |jq
```


Example output for an existing policy: 

```shell-session
[
  "CreateNamespace=true",
  "PrunePropagationPolicy=background",
  "RespectIgnoreDifferences=true"
]
```


     1. If the `spec.syncPolicy.syncOption` field does not contain a `PrunePropagationPolicy` parameter or `PrunePropagationPolicy` is set to the `foreground` value, set the policy to `background` in the `Application` resource. See the following example: 

```yaml
kind: Application
spec:
  syncPolicy:
    syncOptions:
    - PrunePropagationPolicy=background
```


Setting the `background` deletion policy ensures that the `ManagedCluster` CR and all its associated resources are deleted.
