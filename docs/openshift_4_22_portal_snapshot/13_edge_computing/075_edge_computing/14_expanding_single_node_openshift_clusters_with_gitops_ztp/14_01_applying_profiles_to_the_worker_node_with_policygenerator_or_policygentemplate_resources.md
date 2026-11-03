# 14.1. Applying profiles to the worker node with PolicyGenerator or PolicyGenTemplate resources

You can configure the additional worker node with a DU profile. 

You can apply a RAN distributed unit (DU) profile to the worker node cluster using the GitOps Zero Touch Provisioning (ZTP) common, group, and site-specific `PolicyGenerator` or `PolicyGenTemplate` resources. The GitOps ZTP pipeline that is linked to the ArgoCD `policies` application includes the following CRs that you can find in the relevant `out/argocd/example` folder when you extract the `ztp-site-generate` container: 

/acmpolicygenerator resources
    

  * `acm-common-ranGen.yaml`
  * `acm-group-du-sno-ranGen.yaml`
  * `acm-example-sno-site.yaml`
  * `ns.yaml`
  * `kustomization.yaml`



/policygentemplates resources
    

  * `common-ranGen.yaml`
  * `group-du-sno-ranGen.yaml`
  * `example-sno-site.yaml`
  * `ns.yaml`
  * `kustomization.yaml`



Configuring the DU profile on the worker node is considered an upgrade. To initiate the upgrade flow, you must update the existing policies or create additional ones. Then, you must create a `ClusterGroupUpgrade` CR to reconcile the policies in the group of clusters.
