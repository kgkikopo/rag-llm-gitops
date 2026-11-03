# 6.3. Deleting a cluster with a configured AWS Local Zone infrastructure

After you install a cluster on Amazon Web Services (AWS) into an existing Virtual Private Cloud (VPC), and you set subnets for each Local Zone location, you can delete the cluster and any AWS resources associated with it. 

The example in the procedure assumes that you created a VPC and its subnets by using a CloudFormation template. 

**Prerequisites**

  * You know the name of the CloudFormation stacks, `<local_zone_stack_name>` and `<vpc_stack_name>`, that were used during the creation of the network. You need the name of the stack to delete the cluster. 
  * You have access rights to the directory that contains the installation files that were created by the installation program. 
  * Your account includes a policy that provides you with permissions to delete the CloudFormation stack. 



**Procedure**

  1. Change to the directory that contains the stored installation program, and delete the cluster by using the `destroy cluster` command: 

```shell-session
$ ./openshift-install destroy cluster --dir <installation_directory> \
   --log-level=debug
```


where: 

`<installation_directory>`
     Specify the directory that stored any files created by the installation program. 
`--log-level=debug`
     To view different log details, specify `error`, `info`, or `warn` instead of `debug`. 

  2. Delete the CloudFormation stack for the Local Zone subnet: 

```shell-session
$ aws cloudformation delete-stack --stack-name <local_zone_stack_name>
```


  3. Delete the stack of resources that represent the VPC: 

```shell-session
$ aws cloudformation delete-stack --stack-name <vpc_stack_name>
```


**Verification**

  * Check that you removed the stack resources by issuing the following commands in the AWS CLI. The AWS CLI outputs that no template component exists. 

```shell-session
$ aws cloudformation describe-stacks --stack-name <local_zone_stack_name>
```


```shell-session
$ aws cloudformation describe-stacks --stack-name <vpc_stack_name>
```
