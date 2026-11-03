# 12.7. Extracting the infrastructure name

To identify your cluster resources in Google Cloud, extract the unique infrastructure name from the Ignition config files. 

The Ignition config files contain a unique cluster identifier that you can use to uniquely identify your cluster in Google Cloud. The infrastructure name is also used to locate the appropriate Google Cloud resources during an OpenShift Container Platform installation. The provided Infrastructure Manager templates contain references to this infrastructure name, so you must extract it. 

Warning

Do not run the `openshift-install create manifests` command again after creating any Google Cloud resources. Running the command again generates a new cluster identifier, which will cause errors in existing resources. If you need to regenerate the manifests because you modified the `install-config.yaml` file, delete any Google Cloud resources you created and re-create them with the new cluster identifier. 

**Prerequisites**

  * You installed the `jq` package. 



**Procedure**

  * To extract and view the infrastructure name from the Ignition config file metadata, run the following command: 

```shell-session
$ jq -r .infraID <installation_directory>/metadata.json
```


where `<installation_directory>` is the path to the directory that you stored the installation files in. 

**Example output**

```shell-session
openshift-vw9j6
```


The output of this command is your cluster name and a random string.
