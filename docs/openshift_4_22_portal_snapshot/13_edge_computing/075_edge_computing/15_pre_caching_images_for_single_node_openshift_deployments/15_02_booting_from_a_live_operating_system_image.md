# 15.2. Booting from a live operating system image

You can use the factory-precaching-cli tool to boot servers where only one disk is available and an external disk drive cannot be attached to the server. 

Warning

RHCOS requires the disk to not be in use when the disk is about to be written with an RHCOS image. 

Depending on the server hardware, you can mount the RHCOS live ISO on the blank server using one of the following methods: 

  * Using the Dell RACADM tool on a Dell server. 
  * Using the HPONCFG tool on a HP server. 
  * Using the Redfish BMC API. 



It is recommended to automate the mounting procedure. To automate the procedure, you need to pull the required images and host them on a local HTTP server. 

**Prerequisites**

  * You powered up the host. 
  * You have network connectivity to the host. 



The following example procedure uses the Redfish BMC API to mount the RHCOS live ISO. 

**Procedure**

  1. Mount the RHCOS live ISO: 

     1. Check virtual media status: 

```shell-session
$ curl --globoff -H "Content-Type: application/json" -H \
"Accept: application/json" -k -X GET --user ${username_password} \
https://$BMC_ADDRESS/redfish/v1/Managers/Self/VirtualMedia/1 | python -m json.tool
```


     2. Mount the ISO file as a virtual media: 

```shell-session
$ curl --globoff -L -w "%{http_code} %{url_effective}\\n" -ku ${username_password} -H "Content-Type: application/json" -H "Accept: application/json" -d '{"Image": "http://[$HTTPd_IP]/RHCOS-live.iso"}' -X POST https://$BMC_ADDRESS/redfish/v1/Managers/Self/VirtualMedia/1/Actions/VirtualMedia.InsertMedia
```


     3. Set the boot order to boot from the virtual media once: 

```shell-session
$ curl --globoff  -L -w "%{http_code} %{url_effective}\\n"  -ku ${username_password}  -H "Content-Type: application/json" -H "Accept: application/json" -d '{"Boot":{ "BootSourceOverrideEnabled": "Once", "BootSourceOverrideTarget": "Cd", "BootSourceOverrideMode": "UEFI"}}' -X PATCH https://$BMC_ADDRESS/redfish/v1/Systems/Self
```


  2. Reboot and ensure that the server is booting from virtual media. 



**Additional resources**

  * [About Butane](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_configuration/#installation-special-config-butane-about_installing-customizing)
  * [Creating a custom live RHCOS ISO for remote server access](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_a_single_node/#create-custom-live-rhcos-iso_install-sno-installing-sno-with-the-assisted-installer)
  * [Integrated Dell Remote Access Controller 9 RACADM CLI Guide](https://www.dell.com/support/manuals/en-ie/poweredge-r440/idrac9_6.xx_racadm_pub/supported-racadm-interfaces?guid=guid-a5747353-fc88-4438-b617-c50ca260448e&lang=en-us)
  * [Using HPONCFG](https://support.hpe.com/hpesc/public/docDisplay?docId=emr_na-a00007610en_us)
  * [Booting from an HTTP-hosted ISO image using the Redfish API](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_a_single_node/#install-booting-from-an-iso-over-http-redfish_install-sno-installing-sno-with-the-assisted-installer)
