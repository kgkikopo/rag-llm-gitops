# 8.5. Configuring and managing Tang servers using the NBDE Tang Server Operator

With the NBDE Tang Server Operator, you can deploy and quickly configure Tang servers. On the deployed Tang servers, you can list existing keys and rotate them. 

## 8.5.1. Deploy a Tang server using the NBDE Tang Server Operator

You can deploy and quickly configure one or more Tang servers using the NBDE Tang Server Operator in the web console. 

**Prerequisites**

  * You must have `cluster-admin` privileges on an OpenShift Container Platform cluster. 
  * You have installed the NBDE Tang Server Operator on your OCP cluster. 



**Procedure**

  1. In the OpenShift Container Platform web console, navigate to **Ecosystem** **Software Catalog**. 
  2. Select **Project** , and click **Create Project** : 

![Create Project in the web console](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Security_and_compliance-en-US/images/5c18fe4af4c5278bc84520eac6149577/nbde-tang-server-operator-07-create-project.png) ![Create Project in the web console](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Security_and_compliance-en-US/images/5c18fe4af4c5278bc84520eac6149577/nbde-tang-server-operator-07-create-project.png)

  3. On the `Create Project` page, fill in the required information, for example: 

![Example values on the Create Project page](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Security_and_compliance-en-US/images/a6a880d64a79dbb996b12c5ce2ae8dcd/nbde-tang-server-operator-09-project-values.png) ![Example values on the Create Project page](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Security_and_compliance-en-US/images/a6a880d64a79dbb996b12c5ce2ae8dcd/nbde-tang-server-operator-09-project-values.png)

  4. Click **Create**. 
  5. NBDE Tang Server replicas require a Persistent Volume Claim (PVC) for storing encryption keys. In the web console, navigate to **Storage** **PersistentVolumeClaims** : 

![PersistentVolumeClaims in the Storage menu](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Security_and_compliance-en-US/images/eb00c8f14a19d006efe6eb61428cd9de/nbde-tang-server-operator-11-pvc.png) ![PersistentVolumeClaims in the Storage menu](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Security_and_compliance-en-US/images/eb00c8f14a19d006efe6eb61428cd9de/nbde-tang-server-operator-11-pvc.png)

  6. On the following `PersistentVolumeClaims` screen, click **Create PersistentVolumeClaim**. 
  7. On the `Create PersistentVolumeClaim` page, select a storage that fits your deployment scenario. Consider how often you want to rotate the encryption keys. Name your PVC and choose the claimed storage capacity, for example: 

![Create PersistentVolumeClaims page](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Security_and_compliance-en-US/images/e544d77f4bdf708ec1f341a795ae555c/nbde-tang-server-operator-13-create-pvc.png) ![Create PersistentVolumeClaims page](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Security_and_compliance-en-US/images/e544d77f4bdf708ec1f341a795ae555c/nbde-tang-server-operator-13-create-pvc.png)

  8. Navigate to **Ecosystem** **Installed Operators** , and click **NBDE Tang Server**. 
  9. Click **Create instance**. 

![Create NBDE Tang Server instance](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Security_and_compliance-en-US/images/6960212ac71f6abf259abab7278d8802/nbde-tang-server-operator-15-create-instance.png) ![Create NBDE Tang Server instance](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Security_and_compliance-en-US/images/6960212ac71f6abf259abab7278d8802/nbde-tang-server-operator-15-create-instance.png)

  10. On the `Create TangServer` page, choose the name of the Tang Server instance, amount of replicas, and specify the name of the previously created Persistent Volume Claim, for example: 

![Create TangServer page](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Security_and_compliance-en-US/images/f106d49f37570ba038a7875195f8752d/nbde-tang-server-operator-17-create-tangserver.png) ![Create TangServer page](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Security_and_compliance-en-US/images/f106d49f37570ba038a7875195f8752d/nbde-tang-server-operator-17-create-tangserver.png)

  11. After you enter the required values a change settings that differ from the default values in your scenario, click **Create**. 



## 8.5.2. Rotate keys using the NBDE Tang Server Operator

With the NBDE Tang Server Operator, you also can rotate your Tang server keys. The precise interval at which you should rotate them depends on your application, key sizes, and institutional policy. 

**Prerequisites**

  * You must have `cluster-admin` privileges on an OpenShift Container Platform cluster. 
  * You deployed a Tang server using the NBDE Tang Server Operator on your OpenShift cluster. 
  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  1. List the existing keys on your Tang server, for example: 

```shell-session
$ oc -n nbde describe tangserver
```


**Example output**

```shell-session
…
Status:
  Active Keys:
	File Name:  	QS82aXnPKA4XpfHr3umbA0r2iTbRcpWQ0VI2Qdhi6xg
	Generated:  	2022-02-08 15:44:17.030090484 +0000
	sha1:       	PvYQKtrTuYsMV2AomUeHrUWkCGg
	sha256:     	QS82aXnPKA4XpfHr3umbA0r2iTbRcpWQ0VI2Qdhi6xg
…
```


  2. Create a YAML file for moving your active keys to hidden keys, for example, `minimal-keyretrieve-rotate-tangserver.yaml`. Specify the SHA-1 thumbprint of your active key in the `hiddenKeys` entry: 

**Example key-rotation YAML for tang-operator**

```yaml
apiVersion: daemons.redhat.com/v1alpha1
kind: TangServer
metadata:
  name: tangserver
  namespace: nbde
  finalizers:
    - finalizer.daemons.tangserver.redhat.com
spec:
  replicas: 1
  hiddenKeys:
    - sha1: "PvYQKtrTuYsMV2AomUeHrUWkCGg"
```


  3. Apply the YAML file: 

```shell-session
$ oc apply -f minimal-keyretrieve-rotate-tangserver.yaml
```


**Verification**

  1. After a certain amount of time depending on your configuration, check that the previous `activeKey` value is the new `hiddenKey` value and the `activeKey` key file is newly generated, for example: 

```shell-session
$ oc -n nbde describe tangserver
```


**Example output**

```shell-session
…
Spec:
  Hidden Keys:
    sha1:    PvYQKtrTuYsMV2AomUeHrUWkCGg
  Replicas:  1
Status:
  Active Keys:
    File Name:  T-0wx1HusMeWx4WMOk4eK97Q5u4dY5tamdDs7_ughnY.jwk
    Generated:  2023-10-25 15:38:18.134939752 +0000
    sha1:       vVxkNCNq7gygeeA9zrHrbc3_NZ4
    sha256:     T-0wx1HusMeWx4WMOk4eK97Q5u4dY5tamdDs7_ughnY
  Hidden Keys:
    File Name:           .QS82aXnPKA4XpfHr3umbA0r2iTbRcpWQ0VI2Qdhi6xg.jwk
    Generated:           2023-10-25 15:37:29.126928965 +0000
    Hidden:              2023-10-25 15:38:13.515467436 +0000
    sha1:                PvYQKtrTuYsMV2AomUeHrUWkCGg
    sha256:              QS82aXnPKA4XpfHr3umbA0r2iTbRcpWQ0VI2Qdhi6xg
…
```


## 8.5.3. Delete hidden keys with the NBDE Tang Server Operator

After you rotate your Tang server keys, the previously active keys become hidden and are no longer advertised by the Tang instance. You can use the NBDE Tang Server Operator to remove encryption keys no longer used. 

WARNING
     Do not remove any hidden keys unless you are sure that all bound Clevis clients already use new keys. 

**Prerequisites**

  * You must have `cluster-admin` privileges on an OpenShift Container Platform cluster. 
  * You deployed a Tang server using the NBDE Tang Server Operator on your OpenShift cluster. 
  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  1. List the existing keys on your Tang server, for example: 

```shell-session
$ oc -n nbde describe tangserver
```


**Example output**

```shell-session
…
Status:
  Active Keys:
	File Name:  	PvYQKtrTuYsMV2AomUeHrUWkCGg.jwk
	Generated:  	2022-02-08 15:44:17.030090484 +0000
	sha1:	    	PvYQKtrTuYsMV2AomUeHrUWkCGg
	sha256:	    	QS82aXnPKA4XpfHr3umbA0r2iTbRcpWQ0VI2Qdhi6xg
…
```


  2. Create a YAML file for removing all hidden keys, for example, `hidden-keys-deletion-tangserver.yaml`. Set the `hiddenKeys` entry to an empty array to preserve no hidden keys on your Tang server: 

**Example hidden-keys-deletion YAML for tang-operator**

```yaml
apiVersion: daemons.redhat.com/v1alpha1
kind: TangServer
metadata:
  name: tangserver
  namespace: nbde
  finalizers:
    - finalizer.daemons.tangserver.redhat.com
spec:
  replicas: 1
  hiddenKeys: []
```


  3. Apply the YAML file: 

```shell-session
$ oc apply -f hidden-keys-deletion-tangserver.yaml
```


**Verification**

  1. After a certain amount of time depending on your configuration, check that the previous active key still exists, but no hidden key is available, for example: 

```shell-session
$ oc -n nbde describe tangserver
```


**Example output**

```shell-session
…
Spec:
  Hidden Keys:
    sha1:    PvYQKtrTuYsMV2AomUeHrUWkCGg
  Replicas:  1
Status:
  Active Keys:
    File Name:  T-0wx1HusMeWx4WMOk4eK97Q5u4dY5tamdDs7_ughnY.jwk
    Generated:  2023-10-25 15:38:18.134939752 +0000
    sha1:       vVxkNCNq7gygeeA9zrHrbc3_NZ4
    sha256:     T-0wx1HusMeWx4WMOk4eK97Q5u4dY5tamdDs7_ughnY
Status:
  Ready:                 1
  Running:               1
  Service External URL:  http://35.222.247.84:7500/adv
  Tang Server Error:     No
Events:
…
```
