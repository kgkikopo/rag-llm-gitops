# 3.6. Adding Nutanix root CA certificates to your system trust

Because the installation program requires access to the Prism Central API, you must add your Nutanix trusted root CA certificates to your system trust before you install an OpenShift Container Platform cluster. 

**Procedure**

  1. From the Prism Central web console, download the Nutanix root CA certificates. 
  2. Extract the compressed file that contains the Nutanix root CA certificates. 
  3. Add the files for your operating system to the system trust. For example, on a Fedora operating system, run the following command: 

```shell-session
# cp certs/lin/* /etc/pki/ca-trust/source/anchors
```


  4. Update your system trust. For example, on a Fedora operating system, run the following command: 

```shell-session
# update-ca-trust extract
```
