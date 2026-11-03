# 4.8. Remove IP failover

To remove IP failover from your OpenShift Container Platform cluster and clean up iptables rules and virtual IP addresses, you can delete the deployment and service account, then run a cleanup job on each configured node. 

When IP failover is initially configured, the worker nodes in the cluster are modified with an `iptables` rule that explicitly allows multicast packets on `224.0.0.18` for Keepalived. Because of the change to the nodes, removing IP failover requires running a job to remove the `iptables` rule and removing the virtual IP addresses used by Keepalived. 

**Procedure**

  1. Optional: Identify and delete any check and notify scripts that are stored as config maps: 

     1. Identify whether any pods for IP failover use a config map as a volume: 

```shell-session
$ oc get pod -l ipfailover \
  -o jsonpath="\
{range .items[?(@.spec.volumes[*].configMap)]}
{'Namespace: '}{.metadata.namespace}
{'Pod:       '}{.metadata.name}
{'Volumes that use config maps:'}
{range .spec.volumes[?(@.configMap)]}  {'volume:    '}{.name}
  {'configMap: '}{.configMap.name}{'\n'}{end}
{end}"
```


**Example output**

```plaintext
Namespace: default
Pod:       keepalived-worker-59df45db9c-2x9mn
Volumes that use config maps:
  volume:    config-volume
  configMap: mycustomcheck
```


     2. If the preceding step provided the names of config maps that are used as volumes, delete the config maps: 

```shell-session
$ oc delete configmap <configmap_name>
```


  2. Identify an existing deployment for IP failover: 

```shell-session
$ oc get deployment -l ipfailover
```


**Example output**

```shell-session
NAMESPACE   NAME         READY   UP-TO-DATE   AVAILABLE   AGE
default     ipfailover   2/2     2            2           105d
```


  3. Delete the deployment: 

```shell-session
$ oc delete deployment <ipfailover_deployment_name>
```


  4. Remove the `ipfailover` service account: 

```shell-session
$ oc delete sa ipfailover
```


  5. Run a job that removes the IP tables rule that was added when IP failover was initially configured: 

     1. Create a file such as `remove-ipfailover-job.yaml` with contents that are similar to the following example: 

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  generateName: remove-ipfailover-
  labels:
    app: remove-ipfailover
spec:
  template:
    metadata:
      name: remove-ipfailover
    spec:
      containers:
      - name: remove-ipfailover
        image: registry.redhat.io/openshift4/ose-keepalived-ipfailover-rhel9:v4.22
        command: ["/var/lib/ipfailover/keepalived/remove-failover.sh"]
      nodeSelector:
        kubernetes.io/hostname: <host_name>
      restartPolicy: Never
```


        * The `nodeSelector` is likely the same as the selector used in the old IP failover deployment. 
        * Run the job for each node in your cluster that was configured for IP failover and replace the hostname each time. 

     2. Run the job: 

```shell-session
$ oc create -f remove-ipfailover-job.yaml
```


**Example output**

```plaintext
job.batch/remove-ipfailover-2h8dm created
```


**Verification**

  * Confirm that the job removed the initial configuration for IP failover. 

```shell-session
$ oc logs job/remove-ipfailover-2h8dm
```


**Example output**

```shell-session
remove-failover.sh: OpenShift IP Failover service terminating.
  - Removing ip_vs module ...
  - Cleaning up ...
  - Releasing VIPs  (interface eth0) ...
```
