# 6.2. Deleting Amazon Web Services resources with the Cloud Credential Operator utility

After uninstalling an OpenShift Container Platform cluster that uses short-term credentials managed outside the cluster, you can use the Cloud Credential Operator (CCO) utility (`ccoctl`) to remove the Amazon Web Services resources that `ccoctl` created during installation. 

**Prerequisites**

  * Extract and prepare the `ccoctl` binary. 
  * Uninstall an OpenShift Container Platform cluster on AWS that uses short-term credentials. 



**Procedure**

  * Delete the AWS resources that `ccoctl` created by running the following command: 

```shell-session
$ ccoctl aws delete \
  --name=<name> \
  --region=<aws_region>
```


where: 

`<name>`
     Matches the name that was originally used to create and tag the cloud resources. 
`<aws_region>`
    

is the AWS region in which to delete cloud resources. 

**Example output**

```plaintext
2021/04/08 17:50:41 Identity Provider object .well-known/openid-configuration deleted from the bucket <name>-oidc
2021/04/08 17:50:42 Identity Provider object keys.json deleted from the bucket <name>-oidc
2021/04/08 17:50:43 Identity Provider bucket <name>-oidc deleted
2021/04/08 17:51:05 Policy <name>-openshift-cloud-credential-operator-cloud-credential-o associated with IAM Role <name>-openshift-cloud-credential-operator-cloud-credential-o deleted
2021/04/08 17:51:05 IAM Role <name>-openshift-cloud-credential-operator-cloud-credential-o deleted
2021/04/08 17:51:07 Policy <name>-openshift-cluster-csi-drivers-ebs-cloud-credentials associated with IAM Role <name>-openshift-cluster-csi-drivers-ebs-cloud-credentials deleted
2021/04/08 17:51:07 IAM Role <name>-openshift-cluster-csi-drivers-ebs-cloud-credentials deleted
2021/04/08 17:51:08 Policy <name>-openshift-image-registry-installer-cloud-credentials associated with IAM Role <name>-openshift-image-registry-installer-cloud-credentials deleted
2021/04/08 17:51:08 IAM Role <name>-openshift-image-registry-installer-cloud-credentials deleted
2021/04/08 17:51:09 Policy <name>-openshift-ingress-operator-cloud-credentials associated with IAM Role <name>-openshift-ingress-operator-cloud-credentials deleted
2021/04/08 17:51:10 IAM Role <name>-openshift-ingress-operator-cloud-credentials deleted
2021/04/08 17:51:11 Policy <name>-openshift-machine-api-aws-cloud-credentials associated with IAM Role <name>-openshift-machine-api-aws-cloud-credentials deleted
2021/04/08 17:51:11 IAM Role <name>-openshift-machine-api-aws-cloud-credentials deleted
2021/04/08 17:51:39 Identity Provider with ARN arn:aws:iam::<aws_account_id>:oidc-provider/<name>-oidc.s3.<aws_region>.amazonaws.com deleted
```


**Verification**

  * To verify that the resources are deleted, query AWS. For more information, refer to AWS documentation.
