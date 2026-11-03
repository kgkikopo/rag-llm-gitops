# 2.4. Extracting the OpenShift Container Platform installer

Extract the OpenShift Container Platform installer after retrieving it to prepare for the installation of the cluster. 

**Procedure**

  1. Set the environment variables: 

```shell-session
$ export cmd=openshift-baremetal-install
```


```shell-session
$ export pullsecret_file=~/pull-secret.txt
```


```shell-session
$ export extract_dir=$(pwd)
```


  2. Get the `oc` binary: 

```shell-session
$ curl -s https://mirror.openshift.com/pub/openshift-v4/clients/ocp/$VERSION/openshift-client-linux.tar.gz | tar zxvf - oc
```


  3. Extract the installer: 

```shell-session
$ sudo cp oc /usr/local/bin
```


```shell-session
$ oc adm release extract --registry-config "${pullsecret_file}" --command=$cmd --to "${extract_dir}" ${RELEASE_IMAGE}
```


```shell-session
$ sudo cp openshift-baremetal-install /usr/local/bin
```
