# 5.2. The machine lifecycle

Understanding the machine lifecycle can help you troubleshoot machine issues. The lifecycle begins with the request to provision a machine and continues until the machine no longer exists. 

The machine lifecycle proceeds in the following order. Interruptions due to errors or lifecycle hooks are not included in this overview. 

  1. There is a request to provision a new machine for one of the following reasons: 

     * A cluster administrator scales a machine set such that it requires additional machines. 
     * An autoscaling policy scales machine set such that it requires additional machines. 
     * A machine that is managed by a machine set fails or is deleted and the machine set creates a replacement to maintain the required number of machines. 

  2. The machine enters the `Provisioning` phase. 
  3. The infrastructure provider creates an instance for the machine. 
  4. The machine has a provider ID or address and enters the `Provisioned` phase. 
  5. The Ignition configuration file is processed. 
  6. The kubelet issues a certificate signing request (CSR). 
  7. The cluster machine approver approves the CSR. 
  8. The machine becomes a node and enters the `Running` phase. 
  9. An existing machine is slated for deletion for one of the following reasons: 

     * A user with `cluster-admin` permissions uses the `oc delete machine` command. 
     * The machine gets a `machine.openshift.io/delete-machine` annotation. 
     * The machine set that manages the machine marks it for deletion to reduce the replica count as part of reconciliation. 
     * The cluster autoscaler identifies a node that is unnecessary to meet the deployment needs of the cluster. 
     * A machine health check is configured to replace an unhealthy machine. 

  10. The machine enters the `Deleting` phase, in which it is marked for deletion but is still present in the API. 
  11. The machine controller removes the instance from the infrastructure provider. 
  12. The machine controller deletes the `Node` object.
