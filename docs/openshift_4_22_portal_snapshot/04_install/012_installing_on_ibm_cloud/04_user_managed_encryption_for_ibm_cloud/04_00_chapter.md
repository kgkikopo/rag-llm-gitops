# Chapter 4. User-managed encryption for IBM Cloud

By default, OpenShift Container Platform uses provider-managed encryption to secure the root volumes and persistent data volumes of a cluster. You can override this by specifying an IBM® Key Protect root key by using the `encryptionKey` parameter in the `install-config.yaml` file. 

You can specify that: 

  * The same root key applies to all cluster machines by specifying the key as part of the cluster’s default machine configuration. All managed storage classes are updated with this key, so data volumes provisioned after installation are also encrypted by using this key. 
  * Separate root keys apply to the control plane and compute machine pools. 



When you bring your own root key, you change the `install-config.yaml` file to specify the Cloud Resource Name (CRN) of the root key by using the `encryptionKey` parameter. 

Note

Make sure you have integrated Key Protect with your IBM Cloud Block Storage service. For more information, see "Key Protect documentation".

- [4.1. Additional resources](04_01_additional_resources.md)
