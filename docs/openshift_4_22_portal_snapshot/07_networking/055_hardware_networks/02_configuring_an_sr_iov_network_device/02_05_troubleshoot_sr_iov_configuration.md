# 2.5. Troubleshoot SR-IOV configuration

After following the procedure to configure an SR-IOV network device, the following sections address some error conditions. 

**Procedure**

  * To display the state of nodes, run the following command: 

```shell-session
$ oc get sriovnetworknodestates -n openshift-sriov-network-operator <node_name>
```


`<node_name>` specifies the name of a node with an SR-IOV network device. 

If the output from the command indicates "cannot allocate memory", check the following items: 

    * Confirm that global SR-IOV settings are enabled in the BIOS for the node. 
    * Confirm that VT-d is enabled in the BIOS for the node. 




**Additional resources**

  * [Using CPU Manager](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/scalability_and_performance/#using-cpu-manager)



**Additional resources**

  * [Configuring an SR-IOV network attachment](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hardware_networks/configuring-sriov-net-attach "Chapter 3. Configuring an SR-IOV Ethernet network attachment")
