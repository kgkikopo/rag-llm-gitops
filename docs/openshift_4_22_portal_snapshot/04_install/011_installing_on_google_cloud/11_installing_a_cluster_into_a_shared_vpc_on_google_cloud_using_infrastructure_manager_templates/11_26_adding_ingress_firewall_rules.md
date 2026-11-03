# 11.26. Adding ingress firewall rules

The cluster requires several firewall rules. If you do not use a shared VPC, the Ingress Controller creates these rules by using the Google Cloud cloud provider. When you use a shared VPC, you must create the rules yourself so that traffic can reach the cluster services. 

You can either create cluster-wide firewall rules for all services now or create each rule based on events, when the cluster requests access. By creating each rule when the cluster requests access, you know exactly which firewall rules are required. By creating cluster-wide firewall rules, you can apply the same rule set across multiple clusters. 

If you choose to create each rule based on events, you must create firewall rules after you provision the cluster and during the life of the cluster when the console notifies you that rules are missing. Events that are similar to the following event are displayed, and you must add the firewall rules that are required: 

```shell-session
$ oc get events -n openshift-ingress --field-selector="reason=LoadBalancerManualChange"
```


**Example output**

```shell-session
Firewall change required by security admin: `gcloud compute firewall-rules create k8s-fw-a26e631036a3f46cba28f8df67266d55 --network example-network --description "{\"kubernetes.io/service-name\":\"openshift-ingress/router-default\", \"kubernetes.io/service-ip\":\"35.237.236.234\"}\" --allow tcp:443,tcp:80 --source-ranges 0.0.0.0/0 --target-tags exampl-fqzq7-master,exampl-fqzq7-worker --project example-project`
```


If you encounter issues when creating these rule-based events, you can configure the cluster-wide firewall rules while your cluster is running. 

## 11.26.1. Creating cluster-wide firewall rules for a shared VPC in Google Cloud

You can create cluster-wide firewall rules to allow the access that the OpenShift Container Platform cluster requires. 

Warning

If you do not choose to create firewall rules based on cluster events, you must create cluster-wide firewall rules. 

**Prerequisites**

  * You exported the variables that the Infrastructure Manager templates require to deploy your cluster. 
  * You created the networking and load balancing components in Google Cloud that your cluster requires. 



**Procedure**

  1. Add a single firewall rule to allow the Google Cloud Engine health checks to access all of the services. This rule enables the ingress load balancers to determine the health status of their instances. 

```shell-session
$ gcloud compute firewall-rules create --allow='tcp:30000-32767,udp:30000-32767' --network="${CLUSTER_NETWORK}" --source-ranges='130.211.0.0/22,35.191.0.0/16,209.85.152.0/22,209.85.204.0/22' --target-tags="${INFRA_ID}-master,${INFRA_ID}-worker" ${INFRA_ID}-ingress-hc --account=${HOST_PROJECT_ACCOUNT} --project=${HOST_PROJECT}
```


  2. Add a single firewall rule to allow access to all cluster services: 

     * For an external cluster: 

```shell-session
$ gcloud compute firewall-rules create --allow='tcp:80,tcp:443' --network="${CLUSTER_NETWORK}" --source-ranges="0.0.0.0/0" --target-tags="${INFRA_ID}-master,${INFRA_ID}-worker" ${INFRA_ID}-ingress --account=${HOST_PROJECT_ACCOUNT} --project=${HOST_PROJECT}
```


     * For a private cluster: 

```shell-session
$ gcloud compute firewall-rules create --allow='tcp:80,tcp:443' --network="${CLUSTER_NETWORK}" --source-ranges=${NETWORK_CIDR} --target-tags="${INFRA_ID}-master,${INFRA_ID}-worker" ${INFRA_ID}-ingress --account=${HOST_PROJECT_ACCOUNT} --project=${HOST_PROJECT}
```


Because this rule only allows traffic on TCP ports `80` and `443`, ensure that you add all the ports that your services use.
