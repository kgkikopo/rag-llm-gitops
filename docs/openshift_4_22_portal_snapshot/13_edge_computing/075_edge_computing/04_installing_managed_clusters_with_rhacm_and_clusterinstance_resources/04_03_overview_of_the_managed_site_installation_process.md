# 4.3. Overview of the managed site installation process

After you apply the managed site custom resources (CRs) on the hub cluster, the following actions happen automatically: 

  1. A Discovery image ISO file is generated and booted on the target host. 
  2. When the ISO file successfully boots on the target host it reports the host hardware information to RHACM. 
  3. After all hosts are discovered, OpenShift Container Platform is installed. 
  4. When OpenShift Container Platform finishes installing, the hub installs the `klusterlet` service on the target cluster. 
  5. The requested add-on services are installed on the target cluster. 



The Discovery image ISO process is complete when the `Agent` CR for the managed cluster is created on the hub cluster. 

Important

The target bare-metal host must meet the networking, firmware. For more information, see "Recommended single-node OpenShift cluster configuration for vDU application workloads".
