# 3.1. Overview of the GitOps ZTP update process

You can update GitOps Zero Touch Provisioning (ZTP) for a fully operational hub cluster running an earlier version of the GitOps ZTP infrastructure. The update process avoids impact on managed clusters. 

Note

Any changes to policy settings, including adding recommended content, results in updated policies that must be rolled out to the managed clusters and reconciled. 

At a high level, the strategy for updating the GitOps ZTP infrastructure is as follows: 

  1. Label all existing clusters with the `ztp-done` label. 
  2. Stop the ArgoCD applications. 
  3. Install the new GitOps ZTP tools. 
  4. Update required content and optional changes in the Git repository. 
  5. Enable pulling the ISO images for the desired OpenShift Container Platform version. 
  6. Update and restart the application configuration.
