# 1.4. Create containers by using images from third-party registries

Some container image registries require access authorization. You can use Podman to authenticate your credentials, pull registry images, and store local images in a local file system. 

OpenShift Container Platform can communicate with registries to access private image repositories by using credentials supplied by the user. This allows OpenShift Container Platform to push and pull images to and from private repositories. 

OpenShift Container Platform can create containers by using images from third-party registries, but these registries unlikely offer the same image notification support as the integrated OpenShift image registry.In this situation, OpenShift Container Platform fetches tags from the remote registry upon image stream creation. To refresh the fetched tags, run `oc import-image <stream>`. When new images are detected, the previously described build and deployment reactions occur. 

**Procedure**

  1. Use the [Red Hat Ecosystem Catalog](https://catalog.redhat.com/software/containers/explore) to search for specific container images from the Red Hat Repository and select the required image. 
  2. Click **Get this image** to find the command for your container image. 
  3. Log in by running the following command and entering your username and password to authenticate. Example output is shown for demonstrative purposes. 

```shell-session
$ podman login registry.redhat.io
```


```shell-session
 Username:<your_registry_account_username>
 Password:<your_registry_account_password>
```


  4. Download the image and save it locally by running the following command: 

```shell-session
$ podman pull registry.redhat.io/<repository_name>
```
