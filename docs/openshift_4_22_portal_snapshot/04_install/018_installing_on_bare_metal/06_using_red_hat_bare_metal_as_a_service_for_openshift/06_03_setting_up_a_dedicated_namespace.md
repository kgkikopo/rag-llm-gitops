# 6.3. Setting up a dedicated namespace

To prevent accidental interference between Red Hat Bare-Metal-as-a-Service for OpenShift workloads and the OpenShift Container Platform infrastructure, set up a dedicated namespace. Repeat this procedure for every project where you intend to use Red Hat Bare-Metal-as-a-Service for OpenShift. 

**Prerequisites**

  * You have [configured an identify provider](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/index#configuring-identity-providers). 



**Procedure**

  1. Configure a `bmadmin` user in the identity provider and create a secret in OpenShift: 

     1. Create the `bmadmin` user in the identity provider. For example, if using the `htpasswd` identity provider, run the following command: 

```shell-session
$ htpasswd -c -B -b ./users_htpasswd <username> <password>
```


<username>
     The user name for the identity provider. Replace `<username>` with your preferred user name. This example uses `bmadmin`. 
<password>
     The password for the user. Replace `<password>` with a secure password. 

     2. Create a secret in the `openshift-config` namespace to store the identity provider configuration by running the following command: 

```shell-session
$ oc create secret generic <identity_provider_arguments> -n openshift-config
```


For example, when using the `htpasswd` identity provider, run the following command: 

```shell-session
$ oc create secret generic htpass-secret --from-file=htpasswd=users_htpasswd -n openshift-config
```


<identity_provider_arguments>
     The arguments specific to the identity provider secret. Replace `<identity_provider_arguments>` with the appropriate arguments for your identity provider. 

  2. Configure OAuth to use the identity provider: 

     1. Edit the OAuth resource by running the following command: 

```shell-session
$ oc edit oauth cluster
```


The editor opens and displays the Oauth resource. 

     2. Add the identity provider configuration to the `spec.identityProviders` list: 

Table 6.1. Identity provider configuration examplesType| Example  
---|---  
htpasswd  |  `# ... - name: my_bmaas_provider mappingMethod: claim type: htpasswd htpasswd: fileData: name: <secret> # ...`  
LDAP  |  `# ... - name: my_bmaas_provider mappingMethod: claim type: ldap ldap: attributes: id: - dn email: - mail name: - cn preferredUsername: - uid # ...`  
GitHub  |  `# ... - name: my_bmaas_provider mappingMethod: claim type: GitHub github: ca: name: ca-config-map clientID: {...} clientSecret: name: github-secret hostname: ... organizations: - myorganization1 - myorganization2 teams: - myorganization1/team-a - myorganization2/team-b # ...`  
Show more

For more information about identify providers, see [Authentication and authorization](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/index). 

     3. Save and exit the editor. 

  3. Create a `bmadmin` user by running the following command: 

```shell-session
$ oc create user <username>
```


<username>
     The user name. Replace `<username>` with your username. The following examples use `bmadmin` as the username. 

  4. Create a dedicated `bmaas` namespace for Red Hat Bare-Metal-as-a-Service for OpenShift hosts by running the following command: 

```shell-session
$ oc new-project <namespace>
```


`<namespace>`
     Replace <namespace> with the namespace name that you want to use. This example uses `bmaas`. 

  5. Assign the `edit` role to the `bmadmin` user in the `bmaas` namespace by running the following command: 

```shell-session
$ oc adm policy add-role-to-user edit <username> -n bmaas
```


  6. Clone the `baremetal-operator` repository to obtain the role-based access control (RBAC) role definitions by running the following command: 

```shell-session
$ git clone -b release-4.22 https://github.com/openshift/baremetal-operator.git
```


  7. For each role you want to add, apply the appropriate RBAC role YAML file from the repository by running the following command: 

```shell-session
$ oc apply -f baremetal-operator/config/base/rbac/<role_filename>.yaml
```


  8. Assign the custom RBAC roles to the `bmadmin` user in the `bmaas` namespace by running the following command: 

```shell-session
$ oc adm policy add-role-to-user <role_name> bmadmin -n bmaas
```


  9. Login as the `bmadmin` user by running the following command: 

```shell-session
$ oc login <api_server_url>:6443
```


`<api_server_url>`
     The URL to the Kubernetes API.
