# 1.6. NIC partitioning for SR-IOV devices

You can partition a single, high-speed dual port NIC into multiple virtual functions (VFs) and enable SR-IOV to support high availability with Link Aggregation Control Protocol (LACP) bonding. 

This feature supports the use of bonds for high availability with the Link Aggregation Control Protocol (LACP). 

Note

Only one LACP can be declared by physical NIC. 

An OpenShift Container Platform cluster can be deployed on a bond interface with 2 VFs on 2 physical functions (PFs) using the following methods: 

  * Agent-based installer 

Note

The minimum required version of `nmstate` is: 

    * `1.4.2-4` for RHEL 8 versions 
    * `2.2.7` for RHEL 9 versions 

  * Installer-provisioned infrastructure installation 
  * User-provisioned infrastructure installation
