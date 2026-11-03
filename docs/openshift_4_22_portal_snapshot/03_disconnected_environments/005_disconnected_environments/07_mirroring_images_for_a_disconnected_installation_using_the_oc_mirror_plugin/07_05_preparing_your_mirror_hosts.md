# 7.5. Preparing your mirror hosts

Before you can use the oc-mirror plugin to mirror images, you must install the plugin and create a container image registry credentials file to allow the mirroring from Red Hat to your mirror. 

## 7.5.1. Install the oc-mirror OpenShift CLI plugin

You can install the oc-mirror OpenShift CLI plugin to manage image sets in disconnected environments. 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). If you are mirroring image sets in a fully disconnected environment, ensure the following: 

    * You have installed the oc-mirror plugin on the host that has internet access. 
    * The host in the disconnected environment has access to the target mirror registry. 

  * You have set the `umask` parameter to `0022` on the operating system that uses oc-mirror. 
  * You have installed the correct binary for the RHEL version that you are using. 



**Procedure**

  1. Download the oc-mirror CLI plugin: 

     1. Navigate to the [Downloads](https://console.redhat.com/openshift/downloads) page of the Red Hat Hybrid Cloud Console. 
     2. In the **OpenShift disconnected installation tools** section, select the **OS type** and **Architecture type** of the **OpenShift Client (oc) mirror plugin** from the dropdown menus. 
     3. Click **Download** to save the file. 

  2. Extract the archive by running the following command: 

```shell-session
$ tar xvzf oc-mirror.tar.gz
```


  3. If necessary, update the plugin file to be executable by running the following command: 

```shell-session
$ chmod +x oc-mirror
```


Note

Do not rename the `oc-mirror` file. 

  4. Install the oc-mirror CLI plugin by placing the file in your `PATH`, for example `/usr/local/bin`, by running the following command: 

```shell-session
$ sudo mv oc-mirror /usr/local/bin/.
```


**Verification**

  * Verify that the oc-mirror plugin v1 is successfully installed by running the following command: 

```shell-session
$ oc mirror help --v1
```


**Additional resources**

  * [Installing and using CLI plugins](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/cli_tools/#cli-installing-plugins_cli-extend-plugins)



## 7.5.2. Configure credentials that allow images to be mirrored

Create a container image registry credentials file so that you can mirror images from Red Hat to your mirror. Complete the following steps on the installation host. 

Warning

Do not use this image registry credentials file as the pull secret when you install a cluster. If you provide this file when you install cluster, all of the machines in the cluster will have write access to your mirror registry. 

**Prerequisites**

  * You configured a mirror registry to use in your disconnected environment. 
  * You identified an image repository location on your mirror registry to mirror images into. 
  * You provisioned a mirror registry account that allows images to be uploaded to that image repository. 
  * You have write access to the mirror registry. 



**Procedure**

  1. Download your `registry.redhat.io` [pull secret from Red Hat OpenShift Cluster Manager](https://console.redhat.com/openshift/install/pull-secret). 
  2. Make a copy of your pull secret in JSON format by running the following command: 

```shell-session
$ cat ./pull-secret | jq . > <path>/<pull_secret_file_in_json>
```


Specify the path to the directory to store the pull secret in and a name for the JSON file that you create. 

**Example pull secret**

```plaintext
{
  "auths": {
    "cloud.openshift.com": {
      "auth": "b3BlbnNo...",
      "email": "you@example.com"
    },
    "quay.io": {
      "auth": "b3BlbnNo...",
      "email": "you@example.com"
    },
    "registry.connect.redhat.com": {
      "auth": "NTE3Njg5Nj...",
      "email": "you@example.com"
    },
    "registry.redhat.io": {
      "auth": "NTE3Njg5Nj...",
      "email": "you@example.com"
    }
  }
}
```


  3. Save the file as either `~/.docker/config.json` or `$XDG_RUNTIME_DIR/containers/auth.json`: 

     1. If the `.docker` or `$XDG_RUNTIME_DIR/containers` directories do not exist, create one by entering the following command: 

```shell-session
$ mkdir -p <directory_name>
```


Where `<directory_name>` is either `~/.docker` or `$XDG_RUNTIME_DIR/containers`. 

     2. Copy the pull secret to the appropriate directory by entering the following command: 

```shell-session
$ cp <path>/<pull_secret_file_in_json> <directory_name>/<auth_file>
```


The `<directory_name>` is either `~/.docker` or `$XDG_RUNTIME_DIR/containers`, and `<auth_file>` is either `config.json` or `auth.json`

  4. Generate the base64-encoded user name and password or token for your mirror registry by running the following command: 

```shell-session
$ echo -n '<user_name>:<password>' | base64 -w0
```


For `<user_name>` and `<password>`, specify the user name and password that you configured for your registry. 

**Example output**

```shell-session
BGVtbYk3ZHAtqXs=
```


  5. Edit the JSON file and add a section that describes your registry to it: 

```plaintext
  "auths": {
    "<mirror_registry>": {
      "auth": "<credentials>",
      "email": "you@example.com"
    }
  },
```


     * For the `<mirror_registry>` value, specify the registry domain name, and optionally the port, that your mirror registry uses to serve content. For example, `registry.example.com` or `registry.example.com:8443`. 
     * For the `<credentials>` value, specify the base64-encoded user name and password for the mirror registry. 

**Example modified pull secret**

```plaintext
{
  "auths": {
    "registry.example.com": {
      "auth": "BGVtbYk3ZHAtqXs=",
      "email": "you@example.com"
    },
    "cloud.openshift.com": {
      "auth": "b3BlbnNo...",
      "email": "you@example.com"
    },
    "quay.io": {
      "auth": "b3BlbnNo...",
      "email": "you@example.com"
    },
    "registry.connect.redhat.com": {
      "auth": "NTE3Njg5Nj...",
      "email": "you@example.com"
    },
    "registry.redhat.io": {
      "auth": "NTE3Njg5Nj...",
      "email": "you@example.com"
    }
  }
}
```
