# 13.4. Troubleshooting and maintaining OpenShift Container Platform clusters

## 13.4.1. Troubleshooting and maintaining OpenShift Container Platform clusters

Troubleshooting and maintenance are weekly tasks that can be a challenge if you do not have the tools to reach your goal, whether you want to update a component or investigate an issue. Part of the challenge is knowing where and how to search for tools and answers. 

To maintain and troubleshoot a bare-metal environment with high performance requirements, see the following procedures. 

Important

This troubleshooting information is not a reference for configuring OpenShift Container Platform or developing cloud-native applications. 

For information about developing cloud-native applications on OpenShift Container Platform, see [Red Hat Best Practices for Kubernetes](https://redhat-best-practices-for-k8s.github.io/guide/). 

### 13.4.1.1. Getting Support

If you experience difficulty with a procedure, visit the "Red Hat Customer Portal". 

From the Customer Portal, you can find help in various ways: 

  * Search or browse through the Red Hat Knowledgebase of articles and solutions about Red Hat products. 
  * Submit a support case to Red Hat Support. 
  * Access other product documentation. 



To identify issues with your deployment, you can use the debugging tool or check the health endpoint of your deployment. After you have debugged or obtained health information about your deployment, you can search the Red Hat Knowledgebase for a solution or file a support ticket. 

**Additional resources**

  * [Red Hat Customer Portal](https://access.redhat.com/)



#### 13.4.1.1.1. About the Red Hat Knowledgebase

The Red Hat Knowledgebase helps you get the most from Red Hat products and technologies. 

It includes articles, product documentation, and videos that outline best practices for installing, configuring, and using Red Hat products. You can also search for solutions to known issues. Each solution has a root cause description and steps to fix the problem. 

**Additional resources**

  * [Red Hat Knowledgebase](https://access.redhat.com/knowledgebase)



#### 13.4.1.1.2. Search the Red Hat Knowledgebase

Search the Red Hat Knowledgebase to find solutions to known issues and resolve problems quickly without opening a support case. 

**Prerequisites**

  * You have a Red Hat Customer Portal account. 



**Procedure**

  1. Log in to the [Red Hat Customer Portal](http://access.redhat.com). 
  2. Click **Search**. 
  3. In the search field, input keywords and strings relating to the problem, including: 

     * OpenShift Container Platform components (such as **etcd**) 
     * Related procedure (such as **installation**) 
     * Warnings, error messages, and other outputs related to explicit failures 

  4. Click the **Enter** key. 
  5. Optional: Select the **OpenShift Container Platform** product filter. 
  6. Optional: Select the **Documentation** content type filter. 



#### 13.4.1.1.3. Submitting a support case

If you cannot resolve an OpenShift Container Platform issue by using the Red Hat Knowledgebase, submit a support case to get direct help from Red Hat Support. 

**Prerequisites**

  * You have access to the cluster as a user with the `cluster-admin` role. 
  * You have installed the OpenShift CLI (`oc`). 
  * You have a Red Hat Customer Portal account. 
  * You have a Red Hat Standard or Premium subscription. 



**Procedure**

  1. Log in to [the **Customer Support** page](https://access.redhat.com/support/cases/#/case/list) of the Red Hat Customer Portal. 
  2. Click **Get support**. 
  3. On the **Cases** tab of the **Customer Support** page: 

     1. Optional: Change the pre-filled account and owner details if needed. 
     2. Select the appropriate category for your issue, such as **Bug or Defect** , and click **Continue**. 

  4. Enter the following information: 

     1. In the **Summary** field, enter a concise but descriptive problem summary and further details about the symptoms that you experience and your expectations. 
     2. Select **OpenShift Container Platform** from the **Product** drop-down menu. 
     3. Select **4.22** from the **Version** drop-down. 

  5. Review the list of suggested Red Hat Knowledgebase solutions for a potential match against the problem that you are reporting. If the suggested articles do not address the issue, click **Continue**. 
  6. Review the updated list of suggested Red Hat Knowledgebase solutions for a potential match against the problem that you are reporting. The list updates as you give more information during the case creation process. If the suggested articles do not address the issue, click **Continue**. 
  7. Ensure that the account information presented is as expected, and if not, change it as needed. 
  8. Check that the autofilled OpenShift Container Platform Cluster ID is correct. If it is not, manually obtain your cluster ID. 

     * To manually obtain your cluster ID using the OpenShift Container Platform web console: 

       1. Navigate to **Home** **Overview**. 
       2. Find the value in the **Cluster ID** field of the **Details** section. 

     * Or, open a new support case from the OpenShift Container Platform web console, which automatically fills in your cluster ID. 

       1. From the toolbar, navigate to **(?) Help** **Open Support Case**. 
       2. The **Cluster ID** value automatically fills in. 

     * To obtain your cluster ID using the OpenShift CLI (`oc`), run the following command: 

```shell-session
$ oc get clusterversion -o jsonpath='{.items[].spec.clusterID}{"\n"}'
```


  9. Complete the following questions where prompted and then click **Continue** : 

     * What are you experiencing? What are you expecting to happen? 
     * Define the value or impact to you or the business. 
     * Where are you experiencing this behavior? What environment? 
     * When does this behavior occur? Frequency? Repeatedly? At certain times? 

  10. Upload relevant diagnostic data files and click **Continue**. Red Hat recommends including data gathered by using the `oc adm must-gather` command as a starting point, plus any issue-specific data that the command does not collect. 
  11. Input relevant case management details and click **Continue**. 
  12. Preview the case details and click **Submit**. 



## 13.4.2. General troubleshooting

When you encounter a problem, the first step is to find the specific area where the issue is happening. To narrow down the potential problematic areas, complete one or more of the following tasks: 

  * Query your cluster 
  * Check your pod logs 
  * Debug a pod 
  * Review events 



### 13.4.2.1. Querying your cluster

Get information about your cluster so that you can more accurately find potential problems. 

**Procedure**

  1. Switch into a project by running the following command: 

```shell-session
$ oc project <project_name>
```


  2. Query your cluster version, cluster Operator, and node within that namespace by running the following command: 

```shell-session
$ oc get clusterversion,clusteroperator,node
```


```shell-session
NAME                                         VERSION   AVAILABLE   PROGRESSING   SINCE   STATUS
clusterversion.config.openshift.io/version   4.16.11   True        False         62d     Cluster version is 4.16.11

NAME                                                                           VERSION   AVAILABLE   PROGRESSING   DEGRADED   SINCE   MESSAGE
clusteroperator.config.openshift.io/authentication                             4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/baremetal                                  4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/cloud-controller-manager                   4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/cloud-credential                           4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/cluster-autoscaler                         4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/config-operator                            4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/console                                    4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/control-plane-machine-set                  4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/csi-snapshot-controller                    4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/dns                                        4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/etcd                                       4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/image-registry                             4.16.11   True        False         False      55d
clusteroperator.config.openshift.io/ingress                                    4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/insights                                   4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/kube-apiserver                             4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/kube-controller-manager                    4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/kube-scheduler                             4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/kube-storage-version-migrator              4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/machine-api                                4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/machine-approver                           4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/machine-config                             4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/marketplace                                4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/monitoring                                 4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/network                                    4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/node-tuning                                4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/openshift-apiserver                        4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/openshift-controller-manager               4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/openshift-samples                          4.16.11   True        False         False      35d
clusteroperator.config.openshift.io/operator-lifecycle-manager                 4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/operator-lifecycle-manager-catalog         4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/operator-lifecycle-manager-packageserver   4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/service-ca                                 4.16.11   True        False         False      62d
clusteroperator.config.openshift.io/storage                                    4.16.11   True        False         False      62d

NAME                STATUS   ROLES                         AGE   VERSION
node/ctrl-plane-0   Ready    control-plane,master,worker   62d   v1.29.7
node/ctrl-plane-1   Ready    control-plane,master,worker   62d   v1.29.7
node/ctrl-plane-2   Ready    control-plane,master,worker   62d   v1.29.7
```


For more information, see "oc get" and "Reviewing pod status". 




**Additional resources**

  * [oc get](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/cli_tools/#oc-get)
  * [Reviewing pod status](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/support/#reviewing-pod-status_investigating-pod-issues)



### 13.4.2.2. Checking pod logs

Get logs from the pod so that you can review the logs for issues. 

**Procedure**

  1. List the pods by running the following command: 

```shell-session
$ oc get pod
```


```shell-session
NAME        READY   STATUS    RESTARTS          AGE
busybox-1   1/1     Running   168 (34m ago)     7d
busybox-2   1/1     Running   119 (9m20s ago)   4d23h
busybox-3   1/1     Running   168 (43m ago)     7d
busybox-4   1/1     Running   168 (43m ago)     7d
```


  2. Check pod log files by running the following command: 

```shell-session
$ oc logs -n <namespace> busybox-1
```


For more information, see "oc logs", "Logging", and "Inspecting pod and container logs". 




**Additional resources**

  * [oc logs](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/cli_tools/#oc-logs)
  * [Logging](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/security_and_compliance/#security-monitoring-cluster-logging_security-monitoring)
  * [Inspecting pod and container logs](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/support/#inspecting-pod-and-container-logs_investigating-pod-issues)



### 13.4.2.3. Describing a pod

To troubleshoot pod issues and view detailed information about a pod in OpenShift Container Platform, you can describe a pod using the `oc describe pod` command. The **Events** section in the output provides detailed information about the pod and the containers inside of it. 

**Procedure**

  * Describe a pod by running the following command: 

```shell-session
$ oc describe pod -n <namespace> busybox-1
```


**Example output**

```shell-session
Name:             busybox-1
Namespace:        busy
Priority:         0
Service Account:  default
Node:             worker-3/192.168.0.0
Start Time:       Mon, 27 Nov 2023 14:41:25 -0500
Labels:           app=busybox
                  pod-template-hash=<hash>
Annotations:      k8s.ovn.org/pod-networks:
…
Events:
  Type    Reason   Age                   From     Message
  ----    ------   ----                  ----     -------
  Normal  Pulled   41m (x170 over 7d1h)  kubelet  Container image "quay.io/quay/busybox:latest" already present on machine
  Normal  Created  41m (x170 over 7d1h)  kubelet  Created container busybox
  Normal  Started  41m (x170 over 7d1h)  kubelet  Started container busybox
```


**Additional resources**

  * [oc describe](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/cli_tools/#oc-describe)



### 13.4.2.4. Reviewing events

You can review the events in a given namespace to find potential issues. 

**Procedure**

  1. Check for events in your namespace by running the following command: 

```shell-session
$ oc get events -n <namespace> --sort-by=".metadata.creationTimestamp"
```


The `--sort-by=".metadata.creationTimestamp"` flag places the most recent events at the end of the output. 

  2. Optional: If the events within your specified namespace do not provide enough information, expand your query to all namespaces by running the following command: 

```shell-session
$ oc get events -A --sort-by=".metadata.creationTimestamp"
```


The `--sort-by=".metadata.creationTimestamp"` flag places the most recent events at the end of the output. 

To filter the results of all events from a cluster, you can use the `grep` command. For example, if you are looking for errors, the errors can appear in two different sections of the output: the `TYPE` or `MESSAGE` sections. With the `grep` command, you can search for keywords, such as `error` or `failed`. 

  3. For example, search for a message that contains `warning` or `error` by running the following command: 

```shell-session
$ oc get events -A | grep -Ei "warning|error"
```


```shell-session
NAMESPACE    LAST SEEN   TYPE      REASON          OBJECT              MESSAGE
openshift    59s         Warning   FailedMount     pod/openshift-1     MountVolume.SetUp failed for volume "v4-0-config-user-idp-0-file-data" : references non-existent secret key: test
```


  4. Optional: To clean up the events and see only recurring events, you can delete the events in the relevant namespace by running the following command: 

```shell-session
$ oc delete events -n <namespace> --all
```


For more information, see "Watching cluster events". 




**Additional resources**

  * [Watching cluster events](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/security_and_compliance/#security-monitoring-events_security-monitoring)



### 13.4.2.5. Connecting to a pod

You can directly connect to a currently running pod with the `oc rsh` command, which provides you with a shell on that pod. 

Warning

In pods that run a low-latency application, latency issues can occur when you run the `oc rsh` command. Use the `oc rsh` command only if you cannot connect to the node by using the `oc debug` command. 

**Procedure**

  * Connect to your pod by running the following command: 

```shell-session
$ oc rsh -n <namespace> busybox-1
```


For more information, see "oc rsh" and "Accessing running pods". 




**Additional resources**

  * [oc rsh](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/cli_tools/#oc-rsh)
  * [Accessing running pods](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/support/#accessing-running-pods_investigating-pod-issues)



### 13.4.2.6. Debugging a pod

In certain cases, you do not want to directly interact with your pod that is in production. 

To avoid interfering with running traffic, you can use a secondary pod that is a copy of your original pod. The secondary pod uses the same components as that of the original pod but does not have running traffic. 

**Procedure**

  1. List the pods by running the following command: 

```shell-session
$ oc get pod
```


```shell-session
NAME        READY   STATUS    RESTARTS          AGE
busybox-1   1/1     Running   168 (34m ago)     7d
busybox-2   1/1     Running   119 (9m20s ago)   4d23h
busybox-3   1/1     Running   168 (43m ago)     7d
busybox-4   1/1     Running   168 (43m ago)     7d
```


  2. Debug a pod by running the following command: 

```shell-session
$ oc debug -n <namespace> busybox-1
```


```shell-session
Starting pod/busybox-1-debug, command was: sleep 3600
Pod IP: 10.133.2.11
```


If you do not see a shell prompt, press Enter. 

For more information, see "oc debug" and "Starting debug pods with root access". 




**Additional resources**

  * [oc debug](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/cli_tools/#oc-debug)
  * [Starting debug pods with root access](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/support/#starting-debug-pods-with-root-access_investigating-pod-issues)



### 13.4.2.7. Running a command on a pod

If you want to run a command or set of commands on a pod without directly logging into it, you can use the `oc exec -it` command. 

You can interact with the pod quickly to get process or output information from the pod. A common use case is to run the `oc exec -it` command inside a script to run the same command on multiple pods in a replica set or deployment. 

Warning

In pods that run a low-latency application, the `oc exec` command can cause latency issues. 

**Procedure**

  * To run a command on a pod without logging into it, run the following command: 

```shell-session
$ oc exec -it <pod> -- <command>
```


For more information, see "oc exec" and "Executing remote commands in containers". 




**Additional resources**

  * [oc exec](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/cli_tools/#oc-exec)
  * [Executing remote commands in containers](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#nodes-containers-remote-commands-about_nodes-containers-remote-commands)



## 13.4.3. Cluster maintenance

When deploying OpenShift Container Platform on bare-metal infrastructure, you must pay more attention to certain configurations which can have a significant impact on cluster stability. You can troubleshoot more effectively by completing these tasks: 

  * Monitor for failed or failing hardware components 
  * Periodically check the status of the cluster Operators 



Note

For hardware monitoring, contact your hardware vendor to find the appropriate logging tool for your specific hardware. 

### 13.4.3.1. Checking cluster Operators

Periodically check the status of your cluster Operators to find issues early. 

**Procedure**

  * Check the status of the cluster Operators by running the following command: 

```shell-session
$ oc get co
```


### 13.4.3.2. Watching for failed pods

To reduce troubleshooting time, regularly monitor for failed pods in your cluster. 

**Procedure**

  * To watch for failed pods, run the following command: 

```shell-session
$ oc get po -A | grep -Eiv 'complete|running'
```


## 13.4.4. Security

Implementing a robust cluster security profile is important for building resilient environments. 

### 13.4.4.1. Authentication

Determine which identity providers are in your cluster. For more information about supported identity providers, see "Supported identity providers" in _Authentication and authorization_. 

After you know which providers are configured, you can inspect the `openshift-authentication` namespace to determine if there are potential issues. 

**Procedure**

  1. Check the events in the `openshift-authentication` namespace by running the following command: 

```shell-session
$ oc get events -n openshift-authentication --sort-by='.metadata.creationTimestamp'
```


  2. Check the pods in the `openshift-authentication` namespace by running the following command: 

```shell-session
$ oc get pod -n openshift-authentication
```


  3. Optional: If you need more information, check the logs of one of the running pods by running the following command: 

```shell-session
$ oc logs -n openshift-authentication <pod_name>
```


**Additional resources**

  * [Supported identity providers](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/#supported-identity-providers_understanding-identity-provider)



## 13.4.5. Certificate maintenance

Certificate maintenance is required for continuous cluster authentication. As a cluster administrator, you must manually renew certain certificates, while others are automatically renewed by the cluster. 

Learn about certificates in OpenShift Container Platform and how to maintain them by using the following resources: 

  * [Which OpenShift certificates do rotate automatically and which do not in Openshift 4.x?](https://access.redhat.com/solutions/5018231)
  * [Checking etcd certificate expiry in OpenShift 4](https://access.redhat.com/solutions/7000968)



### 13.4.5.1. Certificates manually managed by the administrator

The following certificates must be renewed by a cluster administrator: 

  * Proxy certificates 
  * User-provisioned certificates for the API server 



#### 13.4.5.1.1. Managing proxy certificates

Proxy certificates allow users to specify one or more custom certificate authority (CA) certificates that are used by platform components when making egress connections. 

Note

Certain CAs set expiration dates and you might need to renew these certificates every two years. 

If you did not originally set the requested certificates, you can determine the certificate expiration in several ways. Most Cloud-native Network Functions (CNFs) use certificates that are not specifically designed for browser-based connectivity. Therefore, you need to pull the certificate from the `ConfigMap` object of your deployment. 

**Procedure**

  * To get the expiration date, run the following command against the certificate file: 

```shell-session
$ openssl x509 -enddate -noout -in <cert_file_name>.pem
```


For more information about determining how and when to renew your proxy certificates, see "Proxy certificates" in _Security and compliance_. 




**Additional resources**

  * [Proxy certificates](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/security_and_compliance/#proxy-certificates)



#### 13.4.5.1.2. User-provisioned API server certificates

The API server is accessible by clients that are external to the cluster at `api.<cluster_name>.<base_domain>`. 

You might want clients to access the API server at a different hostname or without the need to distribute the cluster-managed certificate authority (CA) certificates to the clients. You must set a custom default certificate to be used by the API server when serving content. 

For more information, see "User-provided certificates for the API server" in _Security and compliance_

**Additional resources**

  * [User-provisioned certificates for the API server](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/security_and_compliance/#cert-types-user-provided-certificates-for-the-api-server)



### 13.4.5.2. Certificates managed by the cluster

You only need to check cluster-managed certificates if you detect an issue in the logs. The following certificates are automatically managed by the cluster: 

  * Service CA certificates 
  * Node certificates 
  * Bootstrap certificates 
  * etcd certificates 
  * OLM certificates 
  * Machine Config Operator certificates 
  * Monitoring and cluster logging Operator component certificates 
  * Control plane certificates 
  * Ingress certificates 



**Additional resources**

  * [Service CA certificates](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/security_and_compliance/#cert-types-service-ca-certificates_cert-types-service-ca-certificates)
  * [Node certificates](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/security_and_compliance/#cert-types-node-certificates_cert-types-node-certificates)
  * [Bootstrap certificates](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/security_and_compliance/#cert-types-bootstrap-certificates_cert-types-bootstrap-certificates)
  * [etcd certificates](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/security_and_compliance/#cert-types-etcd-certificates-cert-types-etcd-certificates)
  * [OLM certificates](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/security_and_compliance/#cert-types-olm-certificates_cert-types-olm-certificates)
  * [Machine Config Operator certificates](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/security_and_compliance/#cert-types-machine-config-operator-certificates_cert-types-machine-config-operator-certificates)
  * [Monitoring and cluster logging Operator component certificates](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/security_and_compliance/#cert-types-monitoring-and-cluster-logging-operator-component-certificates_cert-types-monitoring-and-cluster-logging-operator-component-certificates)
  * [Control plane certificates](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/security_and_compliance/#cert-types-control-plane-certificates_cert-types-control-plane-certificates)
  * [Ingress certificates](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/security_and_compliance/#cert-types-ingress-certificates_cert-types-ingress-certificates)



#### 13.4.5.2.1. Certificates managed by etcd

The etcd certificates encrypt communication between etcd member peers and client traffic. Certificates renew automatically if all nodes and services can communicate, so renew them in advance if the cluster might lose communication near the end of the certificate lifetime. 

  * You can manually renew etcd certificates by running the following command: 

```shell-session
$ for each in $(oc get secret -n openshift-etcd | grep "kubernetes.io/tls" | grep -e \
"etcd-peer\|etcd-serving" | awk '{print $1}'); do oc get secret $each -n openshift-etcd -o \
jsonpath="{.data.tls\.crt}" | base64 -d | openssl x509 -noout -enddate; done
```


For more information about updating etcd certificates, see "Checking etcd certificate expiry in OpenShift 4". For more information about etcd certificates, see "etcd certificates" in _Security and compliance_. 

**Additional resources**

  * [Checking etcd certificate expiry in OpenShift 4](https://access.redhat.com/solutions/7000968)
  * [etcd certificates](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/security_and_compliance/#cert-types-etcd-certificates_cert-types-etcd-certificates)



#### 13.4.5.2.2. Node certificates

Node certificates are self-signed certificates, which means that they are signed by the cluster and they originate from an internal certificate authority (CA) that is generated by the bootstrap process. 

After the cluster is installed, the cluster automatically renews the node certificates. 

For more information, see "Node certificates" in _Security and compliance_. 

**Additional resources**

  * [Node certificates](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/security_and_compliance/#cert-types-node-certificates_cert-types-node-certificates)



#### 13.4.5.2.3. Service CA certificates

The `service-ca` is an Operator that creates a self-signed certificate authority (CA) when an OpenShift Container Platform cluster is deployed. This allows user to add certificates to their deployments without manually creating them. Service CA certificates are self-signed certificates. 

For more information, see "Service CA certificates" in _Security and compliance_. 

**Additional resources**

  * [Service CA certificates](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/security_and_compliance/#cert-types-service-ca-certificates_cert-types-service-ca-certificates)



## 13.4.6. Machine Config Operator

The Machine Config Operator provides useful information to cluster administrators and controls what is running directly on the bare-metal host. 

The Machine Config Operator differentiates between groups of nodes in the cluster, allowing control plane nodes and worker nodes to run with different configurations. These groups of nodes run worker or application pods, which are called `MachineConfigPool` (`mcp`) groups. The same machine config is applied to all nodes or only to one MCP in the cluster. 

For more information about the Machine Config Operator, see [Machine Config Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operators/#machine-config-operator_cluster-operators-ref). 

### 13.4.6.1. Purpose of the Machine Config Operator

The Machine Config Operator (MCO) manages and applies configuration and updates of Red Hat Enterprise Linux CoreOS (RHCOS) and container runtime, including everything between the kernel and kubelet. 

Managing RHCOS is important since most telecommunications companies run on bare-metal hardware and use some sort of hardware accelerator or kernel modification. Applying machine configuration to RHCOS manually can cause problems because the MCO monitors each node and what is applied to it. 

You must consider these minor components and how the MCO can help you manage your clusters effectively. 

Important

You must use the MCO to perform all changes on worker or control plane nodes. Do not manually make changes to RHCOS or node files. 

### 13.4.6.2. Applying several machine config files at the same time

When you need to change the machine config for a group of nodes in the cluster, also known as machine config pools (MCPs), sometimes the changes must be applied with several different machine config files. 

The nodes need to restart for the machine config file to be applied. After each machine config file is applied to the cluster, all nodes restart that are affected by the machine config file. 

To prevent the nodes from restarting for each machine config file, you can apply all of the changes at the same time by pausing each MCP that is updated by the new machine config file. 

**Procedure**

  1. Pause the affected MCP by running the following command: 

```shell-session
$ oc patch mcp/<mcp_name> --type merge --patch '{"spec":{"paused":true}}'
```


  2. After you apply all machine config changes to the cluster, run the following command: 

```shell-session
$ oc patch mcp/<mcp_name> --type merge --patch '{"spec":{"paused":false}}'
```


This allows the nodes in your MCP to reboot into the new configurations. 




## 13.4.7. Bare-metal node maintenance

You can connect to a node for general troubleshooting. However, in some cases, you need to perform troubleshooting or maintenance tasks on certain hardware components. This section discusses topics that you need to perform for hardware maintenance. 

### 13.4.7.1. Connecting to a bare-metal node in your cluster

You can connect to bare-metal cluster nodes for general maintenance tasks. 

Note

Configuring the cluster node from the host operating system is not recommended or supported. 

To troubleshoot your nodes, you can do the following tasks: 

  * Retrieve logs from a node 
  * Use debugging 
  * Use SSH to connect to a node 



Important

Use SSH only if you cannot connect to the node with the `oc debug` command. 

**Procedure**

  1. Retrieve the logs from a node by running the following command: 

```shell-session
$ oc adm node-logs <node_name> -u crio
```


  2. Use debugging by running the following command: 

```shell-session
$ oc debug node/<node_name>
```


  3. Set `/host` as the root directory within the debug shell. The debug pod mounts the host’s root file system in `/host` within the pod. By changing the root directory to `/host`, you can run binaries contained in the host’s executable paths: 

```shell-session
# chroot /host
```


You are now logged in as root on the node. 

  4. Optional: Use SSH to connect to the node by running the following command: 

```shell-session
$ ssh core@<node_name>
```


### 13.4.7.2. Moving applications to pods within the cluster

For scheduled hardware maintenance, you need to consider how to move your application pods to other nodes within the cluster without affecting the pod workload. 

**Procedure**

  * Mark the node as unschedulable by running the following command: 

```shell-session
$ oc adm cordon <node_name>
```


When the node is unschedulable, no pods can be scheduled on the node. For more information, see "Working with nodes". 

Note

When moving CNF applications, you might need to verify ahead of time that there are enough additional worker nodes in the cluster due to anti-affinity and pod disruption budget. 




**Additional resources**

  * [Working with nodes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#nodes-nodes-working_nodes-nodes-working)



### 13.4.7.3. DIMM memory replacement

Dual in-line memory module (DIMM) problems sometimes only appear after a server reboots. You can check the log files for these problems. 

When you perform a standard reboot and the server does not start, you can see a message in the console that there is a faulty DIMM memory. In that case, you can acknowledge the faulty DIMM and continue rebooting if the remaining memory is sufficient. Then, you can schedule a maintenance window to replace the faulty DIMM. 

Sometimes, a message in the event logs indicates a bad memory module. In these cases, you can schedule the memory replacement before the server is rebooted. 

### 13.4.7.4. Disk replacement

If you do not have disk redundancy configured on your node through hardware or software redundant array of independent disks (RAID), you need to check the following: 

  * Does the disk contain running pod images? 
  * Does the disk contain persistent data for pods? 



For more information, see "OpenShift Container Platform storage overview" in _Storage_. 

**Additional resources**

  * [OpenShift Container Platform storage overview](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage/#storage-overview_storage-overview)



### 13.4.7.5. Cluster network card replacement

When you replace a network card, the MAC address changes. The MAC address can be part of the DHCP or SR-IOV Operator configuration, router configuration, firewall rules, or cloud-native application configuration. 

Before you bring back a node online after replacing a network card, you must verify that these configurations are up-to-date. 

Important

If you do not have specific procedures for MAC address changes within the network, contact your network administrator or network hardware vendor.
