# 3.4. Git source

When specified, source code is fetched from the supplied location. 

If you supply an inline Dockerfile, it overwrites the Dockerfile in the `contextDir` of the Git repository. 

The source definition is part of the `spec` section in the `BuildConfig`: 

```yaml
source:
  git: 
```


1

```yaml
    uri: "https://github.com/openshift/ruby-hello-world"
    ref: "master"
  contextDir: "app/dir" 
```


2

```yaml
  dockerfile: "FROM openshift/ruby-22-centos7\nUSER example" 
```


3

```yaml

```


[1](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/creating-build-inputs#CO4-1)
    

The `git` field contains the Uniform Resource Identifier (URI) to the remote Git repository of the source code. You must specify the value of the `ref` field to check out a specific Git reference. A valid `ref` can be a SHA1 tag or a branch name. The default value of the `ref` field is `master`. 

[2](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/creating-build-inputs#CO4-2)
    

The `contextDir` field allows you to override the default location inside the source code repository where the build looks for the application source code. If your application exists inside a sub-directory, you can override the default location (the root folder) using this field. 

[3](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/creating-build-inputs#CO4-3)
    

If the optional `dockerfile` field is provided, it should be a string containing a Dockerfile that overwrites any Dockerfile that may exist in the source repository. 

If the `ref` field denotes a pull request, the system uses a `git fetch` operation and then checkout `FETCH_HEAD`. 

When no `ref` value is provided, OpenShift Container Platform performs a shallow clone (`--depth=1`). In this case, only the files associated with the most recent commit on the default branch (typically `master`) are downloaded. This results in repositories downloading faster, but without the full commit history. To perform a full `git clone` of the default branch of a specified repository, set `ref` to the name of the default branch (for example `main`). 

Warning

Git clone operations that go through a proxy that is performing man in the middle (MITM) TLS hijacking or reencrypting of the proxied connection do not work. 

## 3.4.1. Using a proxy

If your Git repository can only be accessed using a proxy, you can define the proxy to use in the `source` section of the build configuration. You can configure both an HTTP and HTTPS proxy to use. Both fields are optional. Domains for which no proxying should be performed can also be specified in the `NoProxy` field. 

Note

Your source URI must use the HTTP or HTTPS protocol for this to work. 

```yaml
source:
  git:
    uri: "https://github.com/openshift/ruby-hello-world"
    ref: "master"
    httpProxy: http://proxy.example.com
    httpsProxy: https://proxy.example.com
    noProxy: somedomain.com, otherdomain.com
```


Note

For Pipeline strategy builds, given the current restrictions with the Git plugin for Jenkins, any Git operations through the Git plugin do not leverage the HTTP or HTTPS proxy defined in the `BuildConfig`. The Git plugin only uses the proxy configured in the Jenkins UI at the Plugin Manager panel. This proxy is then used for all git interactions within Jenkins, across all jobs. 

**Additional resources**

  * You can find instructions on how to configure proxies through the Jenkins UI at [JenkinsBehindProxy](https://wiki.jenkins-ci.org/display/JENKINS/JenkinsBehindProxy). 



## 3.4.2. Source clone secrets

Builder pods require access to any Git repositories defined as source for a build. Source clone secrets are used to provide the builder pod with access it would not normally have access to, such as private repositories or repositories with self-signed or untrusted SSL certificates. 

The following source clone secret configurations are supported: 

  * A `.gitconfig` file 
  * Basic authentication 
  * SSH key authentication 
  * Trusted certificate authorities 



Note

You can also use combinations of these configurations to meet your specific needs. 

### 3.4.2.1. Automatically adding a source clone secret to a build configuration

When a `BuildConfig` is created, OpenShift Container Platform can automatically populate its source clone secret reference. This behavior allows the resulting builds to automatically use the credentials stored in the referenced secret to authenticate to a remote Git repository, without requiring further configuration. 

To use this functionality, a secret containing the Git repository credentials must exist in the namespace in which the `BuildConfig` is later created. This secrets must include one or more annotations prefixed with `build.openshift.io/source-secret-match-uri-`. The value of each of these annotations is a Uniform Resource Identifier (URI) pattern, which is defined as follows. When a `BuildConfig` is created without a source clone secret reference and its Git source URI matches a URI pattern in a secret annotation, OpenShift Container Platform automatically inserts a reference to that secret in the `BuildConfig`. 

**Prerequisites**

A URI pattern must consist of: 

  * A valid scheme: `*://`, `git://`, `http://`, `https://` or `ssh://`
  * A host: *` or a valid hostname or IP address optionally preceded by `*.`
  * A path: `/*` or `/` followed by any characters optionally including `*` characters 



In all of the above, a `*` character is interpreted as a wildcard. 

Important

URI patterns must match Git source URIs which are conformant to [RFC3986](https://www.ietf.org/rfc/rfc3986.txt). Do not include a username (or password) component in a URI pattern. 

For example, if you use `ssh://git@bitbucket.atlassian.com:7999/ATLASSIAN jira.git` for a git repository URL, the source secret must be specified as `ssh://bitbucket.atlassian.com:7999/*` (and not `ssh://git@bitbucket.atlassian.com:7999/*`). 

```shell-session
$ oc annotate secret mysecret \
    'build.openshift.io/source-secret-match-uri-1=ssh://bitbucket.atlassian.com:7999/*'
```


**Procedure**

If multiple secrets match the Git URI of a particular `BuildConfig`, OpenShift Container Platform selects the secret with the longest match. This allows for basic overriding, as in the following example. 

The following fragment shows two partial source clone secrets, the first matching any server in the domain `mycorp.com` accessed by HTTPS, and the second overriding access to servers `mydev1.mycorp.com` and `mydev2.mycorp.com`: 

```yaml
kind: Secret
apiVersion: v1
metadata:
  name: matches-all-corporate-servers-https-only
  annotations:
    build.openshift.io/source-secret-match-uri-1: https://*.mycorp.com/*
data:
  ...
---
kind: Secret
apiVersion: v1
metadata:
  name: override-for-my-dev-servers-https-only
  annotations:
    build.openshift.io/source-secret-match-uri-1: https://mydev1.mycorp.com/*
    build.openshift.io/source-secret-match-uri-2: https://mydev2.mycorp.com/*
data:
  ...
```


  * Add a `build.openshift.io/source-secret-match-uri-` annotation to a pre-existing secret using: 

```shell-session
$ oc annotate secret mysecret \
    'build.openshift.io/source-secret-match-uri-1=https://*.mycorp.com/*'
```


### 3.4.2.2. Manually adding a source clone secret

Source clone secrets can be added manually to a build configuration by adding a `sourceSecret` field to the `source` section inside the `BuildConfig` and setting it to the name of the secret that you created. In this example, it is the `basicsecret`. 

```yaml
apiVersion: "build.openshift.io/v1"
kind: "BuildConfig"
metadata:
  name: "sample-build"
spec:
  output:
    to:
      kind: "ImageStreamTag"
      name: "sample-image:latest"
  source:
    git:
      uri: "https://github.com/user/app.git"
    sourceSecret:
      name: "basicsecret"
  strategy:
    sourceStrategy:
      from:
        kind: "ImageStreamTag"
        name: "python-33-centos7:latest"
```


**Procedure**

You can also use the `oc set build-secret` command to set the source clone secret on an existing build configuration. 

  * To set the source clone secret on an existing build configuration, enter the following command: 

```shell-session
$ oc set build-secret --source bc/sample-build basicsecret
```


### 3.4.2.3. Creating a secret from a .gitconfig file

If the cloning of your application is dependent on a `.gitconfig` file, then you can create a secret that contains it. Add it to the builder service account and then your `BuildConfig`. 

**Procedure**

  * To create a secret from a `.gitconfig` file: 



```shell-session
$ oc create secret generic <secret_name> --from-file=<path/to/.gitconfig>
```


Note

SSL verification can be turned off if `sslVerify=false` is set for the `http` section in your `.gitconfig` file: 

```plaintext
[http]
        sslVerify=false
```


### 3.4.2.4. Creating a secret from a .gitconfig file for secured Git

If your Git server is secured with two-way SSL and user name with password, you must add the certificate files to your source build and add references to the certificate files in the `.gitconfig` file. 

**Prerequisites**

  * You must have Git credentials. 



**Procedure**

Add the certificate files to your source build and add references to the certificate files in the `.gitconfig` file. 

  1. Add the `client.crt`, `cacert.crt`, and `client.key` files to the `/var/run/secrets/openshift.io/source/` folder in the application source code. 
  2. In the `.gitconfig` file for the server, add the `[http]` section shown in the following example: 

```shell-session
# cat .gitconfig
```


**Example output**

```shell-session
[user]
        name = <name>
        email = <email>
[http]
        sslVerify = false
        sslCert = /var/run/secrets/openshift.io/source/client.crt
        sslKey = /var/run/secrets/openshift.io/source/client.key
        sslCaInfo = /var/run/secrets/openshift.io/source/cacert.crt
```


  3. Create the secret: 

```shell-session
$ oc create secret generic <secret_name> \
--from-literal=username=<user_name> \
```


1

```shell-session
--from-literal=password=<password> \
```


2

```shell-session
--from-file=.gitconfig=.gitconfig \
--from-file=client.crt=/var/run/secrets/openshift.io/source/client.crt \
--from-file=cacert.crt=/var/run/secrets/openshift.io/source/cacert.crt \
--from-file=client.key=/var/run/secrets/openshift.io/source/client.key
```


[1](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/creating-build-inputs#CO5-1)
    

The user’s Git user name. 

[2](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/creating-build-inputs#CO5-2)
    

The password for this user. 




Important

To avoid having to enter your password again, be sure to specify the source-to-image (S2I) image in your builds. However, if you cannot clone the repository, you must still specify your user name and password to promote the build. 

**Additional resources**

  * `/var/run/secrets/openshift.io/source/` folder in the application source code. 



### 3.4.2.5. Creating a secret from source code basic authentication

Basic authentication requires either a combination of `--username` and `--password`, or a token to authenticate against the software configuration management (SCM) server. 

**Prerequisites**

  * User name and password to access the private repository. 



**Procedure**

  1. Create the secret first before using the `--username` and `--password` to access the private repository: 

```shell-session
$ oc create secret generic <secret_name> \
    --from-literal=username=<user_name> \
    --from-literal=password=<password> \
    --type=kubernetes.io/basic-auth
```


  2. Create a basic authentication secret with a token: 

```shell-session
$ oc create secret generic <secret_name> \
    --from-literal=password=<token> \
    --type=kubernetes.io/basic-auth
```


### 3.4.2.6. Creating a secret from source code SSH key authentication

SSH key based authentication requires a private SSH key. 

The repository keys are usually located in the `$HOME/.ssh/` directory, and are named `id_dsa.pub`, `id_ecdsa.pub`, `id_ed25519.pub`, or `id_rsa.pub` by default. 

**Procedure**

  1. Generate SSH key credentials: 

```shell-session
$ ssh-keygen -t ed25519 -C "your_email@example.com"
```


Note

Creating a passphrase for the SSH key prevents OpenShift Container Platform from building. When prompted for a passphrase, leave it blank. 

Two files are created: the public key and a corresponding private key (one of `id_dsa`, `id_ecdsa`, `id_ed25519`, or `id_rsa`). With both of these in place, consult your source control management (SCM) system’s manual on how to upload the public key. The private key is used to access your private repository. 

  2. Before using the SSH key to access the private repository, create the secret: 

```shell-session
$ oc create secret generic <secret_name> \
    --from-file=ssh-privatekey=<path/to/ssh/private/key> \
    --from-file=<path/to/known_hosts> \
```


1

```shell-session
    --type=kubernetes.io/ssh-auth
```


[1](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/creating-build-inputs#CO6-1)
    

Optional: Adding this field enables strict server host key check. 

Warning

Skipping the `known_hosts` file while creating the secret makes the build vulnerable to a potential man-in-the-middle (MITM) attack. 

Note

Ensure that the `known_hosts` file includes an entry for the host of your source code. 




### 3.4.2.7. Creating a secret from source code trusted certificate authorities

The set of Transport Layer Security (TLS) certificate authorities (CA) that are trusted during a Git clone operation are built into the OpenShift Container Platform infrastructure images. If your Git server uses a self-signed certificate or one signed by an authority not trusted by the image, you can create a secret that contains the certificate or disable TLS verification. 

If you create a secret for the CA certificate, OpenShift Container Platform uses it to access your Git server during the Git clone operation. Using this method is significantly more secure than disabling Git SSL verification, which accepts any TLS certificate that is presented. 

**Procedure**

Create a secret with a CA certificate file. 

  1. If your CA uses Intermediate Certificate Authorities, combine the certificates for all CAs in a `ca.crt` file. Enter the following command: 

```shell-session
$ cat intermediateCA.crt intermediateCA.crt rootCA.crt > ca.crt
```


  2. Create the secret by entering the following command: 

```shell-session
$ oc create secret generic mycert --from-file=ca.crt=</path/to/file> 
```


1

```shell-session

```


[1](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/creating-build-inputs#CO7-1)
    

You must use the key name `ca.crt`. 




### 3.4.2.8. Source secret combinations

You can combine the different methods for creating source clone secrets for your specific needs. 

#### 3.4.2.8.1. Creating a SSH-based authentication secret with a .gitconfig file

You can combine the different methods for creating source clone secrets for your specific needs, such as a SSH-based authentication secret with a `.gitconfig` file. 

**Prerequisites**

  * SSH authentication 
  * A `.gitconfig` file 



**Procedure**

  * To create a SSH-based authentication secret with a `.gitconfig` file, enter the following command: 

```shell-session
$ oc create secret generic <secret_name> \
    --from-file=ssh-privatekey=<path/to/ssh/private/key> \
    --from-file=<path/to/.gitconfig> \
    --type=kubernetes.io/ssh-auth
```


#### 3.4.2.8.2. Creating a secret that combines a .gitconfig file and CA certificate

You can combine the different methods for creating source clone secrets for your specific needs, such as a secret that combines a `.gitconfig` file and certificate authority (CA) certificate. 

**Prerequisites**

  * A `.gitconfig` file 
  * CA certificate 



**Procedure**

  * To create a secret that combines a `.gitconfig` file and CA certificate, enter the following command: 

```shell-session
$ oc create secret generic <secret_name> \
    --from-file=ca.crt=<path/to/certificate> \
    --from-file=<path/to/.gitconfig>
```


#### 3.4.2.8.3. Creating a basic authentication secret with a CA certificate

You can combine the different methods for creating source clone secrets for your specific needs, such as a secret that combines a basic authentication and certificate authority (CA) certificate. 

**Prerequisites**

  * Basic authentication credentials 
  * CA certificate 



**Procedure**

  * To create a basic authentication secret with a CA certificate, enter the following command: 

```shell-session
$ oc create secret generic <secret_name> \
    --from-literal=username=<user_name> \
    --from-literal=password=<password> \
    --from-file=ca-cert=</path/to/file> \
    --type=kubernetes.io/basic-auth
```


#### 3.4.2.8.4. Creating a basic authentication secret with a Git configuration file

You can combine the different methods for creating source clone secrets for your specific needs, such as a secret that combines a basic authentication and a `.gitconfig` file. 

**Prerequisites**

  * Basic authentication credentials 
  * A `.gitconfig` file 



**Procedure**

  * To create a basic authentication secret with a `.gitconfig` file, enter the following command: 

```shell-session
$ oc create secret generic <secret_name> \
    --from-literal=username=<user_name> \
    --from-literal=password=<password> \
    --from-file=</path/to/.gitconfig> \
    --type=kubernetes.io/basic-auth
```


#### 3.4.2.8.5. Creating a basic authentication secret with a .gitconfig file and CA certificate

You can combine the different methods for creating source clone secrets for your specific needs, such as a secret that combines a basic authentication, `.gitconfig` file, and certificate authority (CA) certificate. 

**Prerequisites**

  * Basic authentication credentials 
  * A `.gitconfig` file 
  * CA certificate 



**Procedure**

  * To create a basic authentication secret with a `.gitconfig` file and CA certificate, enter the following command: 

```shell-session
$ oc create secret generic <secret_name> \
    --from-literal=username=<user_name> \
    --from-literal=password=<password> \
    --from-file=</path/to/.gitconfig> \
    --from-file=ca-cert=</path/to/file> \
    --type=kubernetes.io/basic-auth
```
