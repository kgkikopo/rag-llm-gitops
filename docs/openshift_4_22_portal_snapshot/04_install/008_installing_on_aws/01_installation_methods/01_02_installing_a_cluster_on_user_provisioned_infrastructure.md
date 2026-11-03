# 1.2. Installing a cluster on user-provisioned infrastructure

You can install a cluster on AWS in one of two ways: on infrastructure that you provide or infrastructure that you provide by using an internal mirror of the installation release content. 

To install OpenShift Container Platform on AWS infrastructure that you provide, you can use the provided CloudFormation templates to create stacks of AWS resources that represent each of the components required for an OpenShift Container Platform installation. 

To install a cluster that does not require an active internet connection to obtain the software components, install OpenShift Container Platform on AWS infrastructure that you provide by using an internal mirror of the installation release content. You can also use this installation method to ensure that your clusters only use container images that satisfy your organizational controls on external content. While you can install OpenShift Container Platform by using the mirrored content, your cluster still requires internet access to use the AWS APIs.
