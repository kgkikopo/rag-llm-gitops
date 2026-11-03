# 12.23. Adding the ingress DNS records

If you removed the DNS zone configuration when creating Kubernetes manifests and generating Ignition configs, you must manually create DNS records that point at the ingress load balancer so that external clients can reach the applications that run on your cluster. 

You can create either a wildcard `*.apps.{baseDomain}.` or specific records. You can use A, CNAME, and other records per your requirements. 

**Prerequisites**

  * Ensure you defined the variables in the _Exporting common variables_ section. 
  * Remove the DNS Zone configuration when creating Kubernetes manifests and generating Ignition configs. 
  * Ensure the bootstrap process completed successfully. 



**Procedure**

  1. Wait for the Ingress router to create a load balancer and populate the `EXTERNAL-IP` field: 

```shell-session
$ oc -n openshift-ingress get service router-default
```


**Example output**

```shell-session
NAME             TYPE           CLUSTER-IP      EXTERNAL-IP      PORT(S)                      AGE
router-default   LoadBalancer   172.30.18.154   35.233.157.184   80:32288/TCP,443:31215/TCP   98
```


  2. Add the A record to your zones: 

     * To use A records: 

       1. Export the variable for the router IP address: 

```shell-session
$ export ROUTER_IP=`oc -n openshift-ingress get service router-default --no-headers | awk '{print $4}'`
```


       2. Add the A record to the private zones: 

```shell-session
$ if [ -f transaction.yaml ]; then rm transaction.yaml; fi
```


```shell-session
$ gcloud dns record-sets transaction start --zone ${INFRA_ID}-private-zone
```


```shell-session
$ gcloud dns record-sets transaction add ${ROUTER_IP} --name \*.apps.${CLUSTER_NAME}.${BASE_DOMAIN}. --ttl 300 --type A --zone ${INFRA_ID}-private-zone
```


```shell-session
$ gcloud dns record-sets transaction execute --zone ${INFRA_ID}-private-zone
```


       3. For an external cluster, also add the A record to the public zones: 

```shell-session
$ if [ -f transaction.yaml ]; then rm transaction.yaml; fi
```


```shell-session
$ gcloud dns record-sets transaction start --zone ${BASE_DOMAIN_ZONE_NAME}
```


```shell-session
$ gcloud dns record-sets transaction add ${ROUTER_IP} --name \*.apps.${CLUSTER_NAME}.${BASE_DOMAIN}. --ttl 300 --type A --zone ${BASE_DOMAIN_ZONE_NAME}
```


```shell-session
$ gcloud dns record-sets transaction execute --zone ${BASE_DOMAIN_ZONE_NAME}
```


     * To add explicit domains instead of using a wildcard, create entries for each of the cluster’s current routes: 

```shell-session
$ oc get --all-namespaces -o jsonpath='{range .items[*]}{range .status.ingress[*]}{.host}{"\n"}{end}{end}' routes
```


**Example output**

```shell-session
oauth-openshift.apps.your.cluster.domain.example.com
console-openshift-console.apps.your.cluster.domain.example.com
downloads-openshift-console.apps.your.cluster.domain.example.com
alertmanager-main-openshift-monitoring.apps.your.cluster.domain.example.com
prometheus-k8s-openshift-monitoring.apps.your.cluster.domain.example.com
```
