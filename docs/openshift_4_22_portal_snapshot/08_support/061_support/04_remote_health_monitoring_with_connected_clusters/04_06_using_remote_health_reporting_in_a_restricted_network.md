# 4.6. Using remote health reporting in a restricted network

You can manually gather and upload Insights Operator archives to diagnose issues from a restricted network. 

To use the Insights Operator in a restricted network, you must complete the following tasks: 

  * Create a copy of your Insights Operator archive. 
  * Upload the Insights Operator archive to the Red Hat Hybrid Cloud Console. 



Additionally, you can select to obfuscate the Insights Operator data before data upload. 

**Additional resources**

  * [Red Hat Hybrid Cloud Console](https://console.redhat.com)
  * [Enabling Insights Operator data obfuscation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/support/remote-health-monitoring-with-connected-clusters#insights-operator-enable-obfuscation_remote-health-reporting-from-restricted-network "4.6.3. Enabling Insights Operator data obfuscation")



## 4.6.1. Running an Insights Operator gather operation

You must run a gather operation to create an Insights Operator archive. 

**Prerequisites**

  * You are logged in to OpenShift Container Platform as `cluster-admin`. 



**Procedure**

  1. Create a file named `gather-job.yaml` using this template: 

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: insights-operator-job
  annotations:
    config.openshift.io/inject-proxy: insights-operator
spec:
  backoffLimit: 6
  ttlSecondsAfterFinished: 600
  template:
    spec:
      restartPolicy: OnFailure
      serviceAccountName: operator
      nodeSelector:
        beta.kubernetes.io/os: linux
        node-role.kubernetes.io/master: ""
      tolerations:
      - effect: NoSchedule
        key: node-role.kubernetes.io/master
        operator: Exists
      - effect: NoExecute
        key: node.kubernetes.io/unreachable
        operator: Exists
        tolerationSeconds: 900
      - effect: NoExecute
        key: node.kubernetes.io/not-ready
        operator: Exists
        tolerationSeconds: 900
      volumes:
      - name: snapshots
        emptyDir: {}
      - name: service-ca-bundle
        configMap:
          name: service-ca-bundle
          optional: true
      initContainers:
      - name: insights-operator
        image: quay.io/openshift/origin-insights-operator:latest
        terminationMessagePolicy: FallbackToLogsOnError
        volumeMounts:
        - name: snapshots
          mountPath: /var/lib/insights-operator
        - name: service-ca-bundle
          mountPath: /var/run/configmaps/service-ca-bundle
          readOnly: true
        ports:
        - containerPort: 8443
          name: https
        resources:
          requests:
            cpu: 10m
            memory: 70Mi
        args:
        - gather
        - -v=4
        - --config=/etc/insights-operator/server.yaml
      containers:
        - name: sleepy
          image: quay.io/openshift/origin-base:latest
          args:
            - /bin/sh
            - -c
            - sleep 10m
          volumeMounts: [{name: snapshots, mountPath: /var/lib/insights-operator}]
```


  2. Copy your `insights-operator` image version: 

```shell-session
$ oc get -n openshift-insights deployment insights-operator -o yaml
```


**Example output**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: insights-operator
  namespace: openshift-insights
# ...
spec:
  template:
# ...
    spec:
      containers:
      - args:
# ...
        image: registry.ci.openshift.org/ocp/4.15-2023-10-12-212500@sha256:a0aa581400805ad0...
# ...
```


The `spec.template.spec.containers.image` field specifies your `insights-operator` image version. 

  3. Paste your image version in `gather-job.yaml`: 

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: insights-operator-job
# ...
spec:
# ...
  template:
    spec:
    initContainers:
    - name: insights-operator
      image: image: registry.ci.openshift.org/ocp/4.15-2023-10-12-212500@sha256:a0aa581400805ad0...
      terminationMessagePolicy: FallbackToLogsOnError
      volumeMounts:
```


Replace the value of `spec.template.initContainers.image` with your `insights-operator` image version. 

  4. Create the gather job: 

```shell-session
$ oc apply -n openshift-insights -f gather-job.yaml
```


  5. Find the name of the job pod: 

```shell-session
$ oc describe -n openshift-insights job/insights-operator-job
```


**Example output**

```shell-session
Name:             insights-operator-job
Namespace:        openshift-insights
# ...
Events:
  Type    Reason            Age    From            Message
  ----    ------            ----   ----            -------
  Normal  SuccessfulCreate  7m18s  job-controller  Created pod: insights-operator-job-<your_job>
```


Replace `insights-operator-job-<your_job>` with the name of the pod. 

  6. Verify that the operation has finished: 

```shell-session
$ oc logs -n openshift-insights insights-operator-job-<your_job> insights-operator
```


**Example output**

```shell-session
I0407 11:55:38.192084       1 diskrecorder.go:34] Wrote 108 records to disk in 33ms
```


  7. Save the created archive: 

```shell-session
$ oc cp openshift-insights/insights-operator-job-<your_job>:/var/lib/insights-operator ./insights-data
```


  8. Clean up the job: 

```shell-session
$ oc delete -n openshift-insights job insights-operator-job
```


## 4.6.2. Uploading an Insights Operator archive

You can manually upload an Insights Operator archive to [console.redhat.com](https://console.redhat.com) to diagnose potential issues. 

**Prerequisites**

  * You are logged in to OpenShift Container Platform as `cluster-admin`. 
  * You have a workstation with unrestricted internet access. 
  * You have created a copy of the Insights Operator archive. 



**Procedure**

  1. Download the `dockerconfig.json` file: 

```shell-session
$ oc extract secret/pull-secret -n openshift-config --to=.
```


  2. Copy your `"cloud.openshift.com"` `"auth"` token from the `dockerconfig.json` file: 

```plaintext
{
  "auths": {
    "cloud.openshift.com": {
      "auth": "<your_token>",
      "email": "asd@redhat.com"
    }
}
```


  3. Upload the archive to [console.redhat.com](https://console.redhat.com): 

```shell-session
$ curl -v -H "User-Agent: insights-operator/one10time200gather184a34f6a168926d93c330 cluster/<cluster_id>" -H "Authorization: Bearer <your_token>" -F "upload=@<path_to_archive>; type=application/vnd.redhat.openshift.periodic+tar" https://console.redhat.com/api/ingress/v1/upload
```


where: 

`<cluster_id>`
     Specifies the cluster ID. 
`<your_token>`
     Specifies the token from your pull secret. 
`<path_to_archive>`
    

Specifies the path to the Insights Operator archive. 

If the operation is successful, the command returns a `"request_id"` and `"account_number"`: 

**Example output**

```shell-session
* Connection #0 to host console.redhat.com left intact
{"request_id":"393a7cf1093e434ea8dd4ab3eb28884c","upload":{"account_number":"6274079"}}%
```


**Verification**

  1. Log in to <https://console.redhat.com/openshift>. 
  2. Click the **Cluster List** menu in the left pane. 
  3. To display the details of the cluster, click the cluster name. 
  4. Open the **Red Hat Lightspeed Advisor** tab of the cluster. 

If the upload was successful, the tab displays one of the following: 

     * **Your cluster passed all recommendations** , if the Red Hat Lightspeed advisor service did not identify any issues. 
     * A list of issues that the Red Hat Lightspeed advisor service has detected, prioritized by risk (low, moderate, important, and critical). 




## 4.6.3. Enabling Insights Operator data obfuscation

You can enable obfuscation to mask sensitive and identifiable IPv4 addresses and cluster base domains that the Insights Operator sends to [console.redhat.com](https://console.redhat.com). 

Warning

Although this feature is available, Red Hat recommends keeping obfuscation disabled for a more effective support experience. 

Obfuscation assigns non-identifying values to cluster IPv4 addresses, and uses a translation table that is retained in memory to change IP addresses to their obfuscated versions throughout the Insights Operator archive before uploading the data to [console.redhat.com](https://console.redhat.com). 

For cluster base domains, obfuscation changes the base domain to a hardcoded substring. For example, `cluster-api.openshift.example.com` becomes `cluster-api.<CLUSTER_BASE_DOMAIN>`. 

The following procedure enables obfuscation using the `support` secret in the `openshift-config` namespace. 

**Prerequisites**

  * You are logged in to the OpenShift Container Platform web console as `cluster-admin`. 



**Procedure**

  1. Navigate to **Workloads** **Secrets**. 
  2. Select the **openshift-config** project. 
  3. Search for the **support** secret using the **Search by name** field. If it does not exist, click **Create** **Key/value secret** to create it. 
  4. Click the Options menu ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Support-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) , and then click **Edit Secret**. 
  5. Click **Add Key/Value**. 
  6. Create a key named `enableGlobalObfuscation` with a value of `true`, and click **Save**. 
  7. Navigate to **Workloads** **Pods**
  8. Select the `openshift-insights` project. 
  9. Find the `insights-operator` pod. 
  10. To restart the `insights-operator` pod, click the Options menu ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Support-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) , and then click **Delete Pod**. 



**Verification**

  1. Navigate to **Workloads** **Secrets**. 
  2. Select the **openshift-insights** project. 
  3. Search for the **obfuscation-translation-table** secret using the **Search by name** field. 

If the `obfuscation-translation-table` secret exists, then obfuscation is enabled and working. 

Alternatively, you can inspect `/insights-operator/gathers.json` in your Insights Operator archive for the value `"is_global_obfuscation_enabled": true`. 




**Additional resources**

  * [Showing data collected by the Insights Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/support/remote-health-monitoring-with-connected-clusters#insights-operator-showing-data-collected-from-the-cluster_showing-data-collected-by-remote-health-monitoring "4.2.2. Showing data collected by the Insights Operator")
