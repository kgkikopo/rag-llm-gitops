# 3.2. Configure credentials that allow images to be mirrored

Create a container image registry credentials file so that you can mirror images from Red Hat to your mirror. Complete the following steps on the installation host. 

**Prerequisites**

  * You configured a mirror registry to use in your disconnected environment. 



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


  3. Generate the base64-encoded user name and password or token for your mirror registry by running the following command: 

```shell-session
$ echo -n '<user_name>:<password>' | base64 -w0
```


For `<user_name>` and `<password>`, specify the user name and password that you configured for your registry. 

**Example output**

```shell-session
BGVtbYk3ZHAtqXs=
```


  4. Edit the JSON file and add a section that describes your registry to it: 

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
