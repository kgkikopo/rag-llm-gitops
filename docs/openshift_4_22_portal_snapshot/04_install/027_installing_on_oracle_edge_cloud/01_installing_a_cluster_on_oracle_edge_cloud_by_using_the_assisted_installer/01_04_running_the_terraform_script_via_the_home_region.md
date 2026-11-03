# 1.4. Running the Terraform script via the Home region

Copy the Terraform scripts `createInfraResources.tf` and `terraform.tfvars` onto the bastion server. Then run the `createInfraResources.tf` script to create the Dynamic Group Identity resources on your Oracle Cloud Infrastructure (OCI) Home Region. 

These resources include dynamic groups, policies, and tags. 

**Prerequisites**

  * You have tenancy privileges to create Dynamic Groups and Policies. If not, you can manually provision them during this procedure. 



**Procedure**

  1. Connect to the bastion server via SSH. 
  2. Create `OpenShift\createResourceOnHomeRegion` folders. 
  3. Copy the `createInfraResources.tf` and `terraform.tfvars` files from the C3_PCA GitHub repository into the `createResourceOnHomeRegion` folder. 
  4. Ensure that you have access to the source environment, and that your C3 certificate has been exported. 
  5. Run the `createInfraResources.tf` Terraform script. 

For the full procedure, see the "Terraform Script Execution Part-1 (Run Script via Home Region)" section in the [Oracle documentation](https://www.oracle.com/a/otn/docs/compute_cloud_at_customer_assisted_installer.pdf?source=:em:nl:mt::::PCATP).
