# 19.4. Uninstall the Red Hat Quay Container Security Operator

To uninstall the Container Security Operator, you must uninstall the Operator and delete the `imagemanifestvulns.secscan.quay.redhat.com` custom resource definition (CRD). 

**Procedure**

  1. On the OpenShift Container Platform web console, click **Ecosystem** **Installed Operators**. 
  2. Click the Options menu ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Security_and_compliance-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) of the Container Security Operator. 
  3. Click **Uninstall Operator**. 
  4. Confirm your decision by clicking **Uninstall** in the popup window. 
  5. Use the CLI to delete the `imagemanifestvulns.secscan.quay.redhat.com` CRD. 

     1. Remove the `imagemanifestvulns.secscan.quay.redhat.com` custom resource definition by entering the following command: 

```shell-session
$ oc delete customresourcedefinition imagemanifestvulns.secscan.quay.redhat.com
```


**Example output**

```shell-session
customresourcedefinition.apiextensions.k8s.io "imagemanifestvulns.secscan.quay.redhat.com" deleted
```
