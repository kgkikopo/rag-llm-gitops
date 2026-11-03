# 1.4. Getting cluster version, status, and update details

You can view the cluster version and status by running the `oc get clusterversion` command. If the status shows that the installation is still progressing, you can review the status of the Operators for more information. 

You can also list the current update channel and review the available cluster updates. 

**Prerequisites**

  * You have access to the cluster as a user with the `cluster-admin` role. 
  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  1. Obtain the cluster version and overall status: 

```shell-session
$ oc get clusterversion
```


**Example output**

```shell-session
NAME      VERSION   AVAILABLE   PROGRESSING   SINCE   STATUS
version   4.6.4     True        False         6m25s   Cluster version is 4.6.4
```


The example output indicates that the cluster has been installed successfully. 

  2. If the cluster status indicates that the installation is still progressing, you can obtain more detailed progress information by checking the status of the Operators: 

```shell-session
$ oc get clusteroperators.config.openshift.io
```


  3. View a detailed summary of cluster specifications, update availability, and update history: 

```shell-session
$ oc describe clusterversion
```


  4. List the current update channel: 

```shell-session
$ oc get clusterversion -o jsonpath='{.items[0].spec}{"\n"}'
```


**Example output**

```shell-session
{"channel":"stable-4.6","clusterID":"245539c1-72a3-41aa-9cec-72ed8cf25c5c"}
```


  5. Review the available cluster updates: 

```shell-session
$ oc adm upgrade
```


**Example output**

```shell-session
Cluster version is 4.6.4

Updates:

VERSION IMAGE
4.6.6   quay.io/openshift-release-dev/ocp-release@sha256:c7e8f18e8116356701bd23ae3a23fb9892dd5ea66c8300662ef30563d7104f39
```


**Additional resources**

  * [Querying Operator status after installation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/support/#querying-operator-status-after-installation_troubleshooting-installations)
  * [Troubleshooting Operator issues](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/support/#troubleshooting-operator-issues)
  * [Updating a cluster using the web console](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/updating_clusters/#updating-cluster-web-console)
  * [Understanding update channels and releases](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/updating_clusters/#understanding-update-channels-releases)
