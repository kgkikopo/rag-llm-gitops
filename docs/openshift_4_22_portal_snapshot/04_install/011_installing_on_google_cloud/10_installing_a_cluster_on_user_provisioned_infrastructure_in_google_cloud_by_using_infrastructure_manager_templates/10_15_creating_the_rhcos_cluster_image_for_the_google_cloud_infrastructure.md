# 10.15. Creating the RHCOS cluster image for the Google Cloud infrastructure

To deploy OpenShift Container Platform nodes on Google Cloud, you must create a valid Red Hat Enterprise Linux CoreOS (RHCOS) image in your Google Cloud project because RHCOS images are not pre-published on Google Cloud. 

**Prerequisites**

  * You have downloaded the `openshift-install` binary. 



**Procedure**

  1. Obtain the image name by running the following command: 

```shell-session
$ source_image=$(openshift-install coreos print-stream-json | jq -r '.architectures.x86_64.images.gcp.name')
```


  2. Obtain the project name by running the following command: 

```shell-session
$ source_project=$(openshift-install coreos print-stream-json | jq -r '.architectures.x86_64.images.gcp.project')
```


  3. Create the image by running the following command: 

```shell-session
$ gcloud compute images create "${INFRA_ID}-rhcos-image" \
    --source-image="${source_image}" --source-image-project="${source_project}"
```
