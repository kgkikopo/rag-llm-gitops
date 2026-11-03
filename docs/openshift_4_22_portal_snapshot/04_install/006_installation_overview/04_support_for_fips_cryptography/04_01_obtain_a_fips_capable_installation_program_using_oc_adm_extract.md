# 4.1. Obtain a FIPS-capable installation program using oc adm extract

To install a OpenShift Container Platform cluster in FIPS mode, extract the FIPS-capable installation binary from the release image by using the OpenShift CLI (`oc`). 

After you extract the binary, proceed with the cluster installation, replacing all instances of the `openshift-install` command with `openshift-install-fips`. 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`) with version 4.16 or newer. 



**Procedure**

  1. Extract the FIPS-capable binary from the installation program by running the following command: 

```shell-session
$ oc adm release extract --registry-config "${pullsecret_file}" --command=openshift-install-fips --to "${extract_dir}" ${RELEASE_IMAGE}
```


where: 

`<pullsecret_file>`
     Specifies the name of a file that contains your pull secret. 
`<extract_dir>`
     Specifies the directory where you want to extract the binary. 
`<RELEASE_IMAGE>`
     Specifies the Quay.io URL of the OpenShift Container Platform release you are using. For more information on finding the release image, see _Extracting the OpenShift Container Platform installation program_. 

  2. Proceed with cluster installation, replacing all instances of the `openshift-install` command with `openshift-install-fips`.
