# 7.5. Creating the installation files

Generate the ISO image and create an iPXE script to upload to your iSCSI target. 

**Procedure**

  1. Create the agent image by running the following command: 

```shell-session
$ openshift-install --dir <install_directory> agent create image
```


  2. Create an iPXE script by running the following command: 

```shell-session
$ cat << EOF > agent.ipxe
!ipxe
set initiator-iqn <iscsi_initiator_base>:\${hostname}
sanboot --keep iscsi:<iscsi_network_subnet>.1::::<iscsi_target_base>:\${hostname}
EOF
```


where: 

`<iscsi_initiator_base>`
     Specifies the iSCSI initiator name on the host that is booting the ISO. This name can also be used by the iSCSI target. 
`<iscsi_network_subnet>`
     Specifies the IP address of the iSCSI target. 
`<iscsi_target_base>`
     Specifies the iSCSI target name. This name can be the same as the initiator name. 

**Example Command**

```shell-session
$ cat << EOF > agent.ipxe
!ipxe
set initiator-iqn iqn.2023-01.com.example:\${hostname}
sanboot --keep iscsi:192.168.45.1::::iqn.2023-01.com.example:\${hostname}
EOF
```
