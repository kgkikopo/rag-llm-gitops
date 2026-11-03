# 1.6. Running the Terraform script via the C3 region

Run the `terraform.tfvars` Terraform script to create all infrastructure resources on Oracle® Edge Cloud. These resources include the OpenShift Container Platform VCN, public and private subnets, load balancers, internet GW, NAT GW, and DNS server. 

This procedure deploys a cluster consisting of three control plane (master) and three compute (worker) nodes. After deployment, you must rename and reboot the nodes. This process temporarily duplicates nodes, requiring manual cleanup in the next procedure. 

**Procedure**

  1. Connect to the bastion server via SSH. 
  2. Set the C3 Certificate location and export the certificate. 
  3. Run the `terraform.tfvars` script to create three control plane nodes and three compute nodes. 
  4. Update the labels for the control plane and compute nodes. 
  5. Stop and restart the instances one by one on the Oracle® Edge Cloud portal. 

For the full procedure, see the "Terraform Script Execution - Part 2" section in the [Oracle documentation](https://www.oracle.com/a/otn/docs/compute_cloud_at_customer_assisted_installer.pdf?source=:em:nl:mt::::PCATP).
