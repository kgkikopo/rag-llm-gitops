# 1.4. Completing host discovery and starting cluster installation

After preparing control plane and worker nodes in the Oracle Database Appliance (ODA) environment, complete host discovery and initiate the cluster installation. 

As you create hosts using the provided scripts, the hosts begin to appear in the table of the **Host Discovery** page, where you can configure the hosts as needed. 

**Procedure**

  1. Go to the **Host Discovery** page. 
  2. Assign host roles in the **Host Inventory** table: 

     1. In the **Role** column of the table, expand the **Auto-Assign** arrow for the host. 
     2. Assign the host with either a **Control Plane node** or a **Worker** role. 
     3. Repeat this process for each host in the table. 

  3. Click **Next**. 
  4. On the **Storage** page, verify storage details and configure host storage as needed. 
  5. Click **Next**. 
  6. Configure networking details on the **Networking** page: 

     1. Select **User-Managed Networking** as the **Network Management** type. 
     2. Select **Host SSH Public Key for troubleshooting after installation** to connect to hosts using a public SSH key for troubleshooting after installation. 

  7. Click **Next**. 
  8. Validate cluster details on the **Review and create** page. 
  9. Click **Install cluster** to begin the installation. 
  10. Monitor installation progress and wait for all nodes to reach a `Ready` state.
