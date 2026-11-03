# 1.1. Configuration and customization

You can manage Jenkins authentication in two ways: 

  * OpenShift Container Platform OAuth authentication provided by the OpenShift Container Platform Login plugin. 
  * Standard authentication provided by Jenkins. 



## 1.1.1. OpenShift Container Platform OAuth authentication

OAuth authentication is activated by configuring options on the **Configure Global Security** panel in the Jenkins UI, or by setting the `OPENSHIFT_ENABLE_OAUTH` environment variable on the Jenkins **Deployment configuration** to anything other than `false`. This activates the OpenShift Container Platform Login plugin, which retrieves the configuration information from pod data or by interacting with the OpenShift Container Platform API server. 

Valid credentials are controlled by the OpenShift Container Platform identity provider. 

Jenkins supports both browser and non-browser access. 

Valid users are automatically added to the Jenkins authorization matrix at log in, where OpenShift Container Platform roles dictate the specific Jenkins permissions that users have. The roles used by default are the predefined `admin`, `edit`, and `view`. The login plugin executes self-SAR requests against those roles in the project or namespace that Jenkins is running in. 

Users with the `admin` role have the traditional Jenkins administrative user permissions. Users with the `edit` or `view` role have progressively fewer permissions. 

The default OpenShift Container Platform `admin`, `edit`, and `view` roles and the Jenkins permissions those roles are assigned in the Jenkins instance are configurable. 

When running Jenkins in an OpenShift Container Platform pod, the login plugin looks for a config map named `openshift-jenkins-login-plugin-config` in the namespace that Jenkins is running in. 

If this plugin finds and can read in that config map, you can define the role to Jenkins Permission mappings. Specifically: 

  * The login plugin treats the key and value pairs in the config map as Jenkins permission to OpenShift Container Platform role mappings. 
  * The key is the Jenkins permission group short ID and the Jenkins permission short ID, with those two separated by a hyphen character. 
  * If you want to add the `Overall Jenkins Administer` permission to an OpenShift Container Platform role, the key should be `Overall-Administer`. 
  * To get a sense of which permission groups and permissions IDs are available, go to the matrix authorization page in the Jenkins console and IDs for the groups and individual permissions in the table they provide. 
  * The value of the key and value pair is the list of OpenShift Container Platform roles the permission should apply to, with each role separated by a comma. 
  * If you want to add the `Overall Jenkins Administer` permission to both the default `admin` and `edit` roles, as well as a new Jenkins role you have created, the value for the key `Overall-Administer` would be `admin,edit,jenkins`. 



Note

The `admin` user that is pre-populated in the OpenShift Container Platform Jenkins image with administrative privileges is not given those privileges when OpenShift Container Platform OAuth is used. To grant these permissions the OpenShift Container Platform cluster administrator must explicitly define that user in the OpenShift Container Platform identity provider and assign the `admin` role to the user. 

Jenkins users' permissions that are stored can be changed after the users are initially established. The OpenShift Container Platform Login plugin polls the OpenShift Container Platform API server for permissions and updates the permissions stored in Jenkins for each user with the permissions retrieved from OpenShift Container Platform. If the Jenkins UI is used to update permissions for a Jenkins user, the permission changes are overwritten the next time the plugin polls OpenShift Container Platform. 

You can control how often the polling occurs with the `OPENSHIFT_PERMISSIONS_POLL_INTERVAL` environment variable. The default polling interval is five minutes. 

The easiest way to create a new Jenkins service using OAuth authentication is to use a template. 

## 1.1.2. Jenkins authentication

Jenkins authentication is used by default if the image is run directly, without using a template. 

The first time Jenkins starts, the configuration is created along with the administrator user and password. The default user credentials are `admin` and `password`. Configure the default password by setting the `JENKINS_PASSWORD` environment variable when using, and only when using, standard Jenkins authentication. 

**Procedure**

  * Create a Jenkins application that uses standard Jenkins authentication by entering the following command: 

```shell-session
$ oc new-app -e \
    JENKINS_PASSWORD=<password> \
    ocp-tools-4/jenkins-rhel8
```
