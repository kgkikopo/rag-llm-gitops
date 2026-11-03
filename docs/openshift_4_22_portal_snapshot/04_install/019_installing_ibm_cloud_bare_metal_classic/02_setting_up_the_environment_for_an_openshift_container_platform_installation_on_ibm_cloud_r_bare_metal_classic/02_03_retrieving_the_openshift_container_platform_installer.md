# 2.3. Retrieving the OpenShift Container Platform installer

Use the `stable-4.x` version of the installation program and your selected architecture to deploy the generally available stable version of OpenShift Container Platform. 

**Procedure**

  * Retrieve the installation program by running one of the following commands: 

```shell-session
$ export VERSION=stable-4.22
```


```shell-session
$ export RELEASE_ARCH=<architecture>
```


```shell-session
$ export RELEASE_IMAGE=$(curl -s https://mirror.openshift.com/pub/openshift-v4/$RELEASE_ARCH/clients/ocp/$VERSION/release.txt | grep 'Pull From: quay.io' | awk -F ' ' '{print $3}')
```
