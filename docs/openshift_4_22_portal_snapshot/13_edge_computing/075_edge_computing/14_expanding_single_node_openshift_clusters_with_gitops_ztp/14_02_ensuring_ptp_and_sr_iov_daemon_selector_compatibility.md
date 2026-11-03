# 14.2. Ensuring PTP and SR-IOV daemon selector compatibility

If the DU profile was deployed using the GitOps Zero Touch Provisioning (ZTP) plugin version 4.11 or earlier, the PTP and SR-IOV Operators might be configured to place the daemons only on nodes labeled as `master`. 

This configuration prevents the PTP and SR-IOV daemons from operating on the worker node. If the PTP and SR-IOV daemon node selectors are incorrectly configured on your system, you must change the daemons before proceeding with the worker DU profile configuration. 

**Procedure**

  1. Check the daemon node selector settings of the PTP Operator on one of the spoke clusters: 

```shell-session
$ oc get ptpoperatorconfig/default -n openshift-ptp -ojsonpath='{.spec}' | jq
```


The following is example output for the PTP Operator: 

```plaintext
{"daemonNodeSelector":{"node-role.kubernetes.io/master":""}}
```


     * If the node selector is set to `master`, the spoke was deployed with the version of the GitOps ZTP plugin that requires changes. 

  2. Check the daemon node selector settings of the SR-IOV Operator on one of the spoke clusters: 

```shell-session
$  oc get sriovoperatorconfig/default -n \
openshift-sriov-network-operator -ojsonpath='{.spec}' | jq
```


The following is example output for the SR-IOV Operator: 

```plaintext
{"configDaemonNodeSelector":{"node-role.kubernetes.io/worker":""},"disableDrain":false,"enableInjector":true,"enableOperatorWebhook":true}
```


     * If the node selector is set to `master`, the spoke was deployed with the version of the GitOps ZTP plugin that requires changes. 

  3. In the group policy, add the following `complianceType` and `spec` entries: 

```yaml
spec:
    - fileName: PtpOperatorConfig.yaml
      policyName: "config-policy"
      complianceType: mustonlyhave
      spec:
        daemonNodeSelector:
          node-role.kubernetes.io/worker: ""
    - fileName: SriovOperatorConfig.yaml
      policyName: "config-policy"
      complianceType: mustonlyhave
      spec:
        configDaemonNodeSelector:
          node-role.kubernetes.io/worker: ""
```


Important

Changing the `daemonNodeSelector` field causes temporary PTP synchronization loss and SR-IOV connectivity loss. 

  4. Commit the changes in Git, and then push to the Git repository being monitored by the GitOps ZTP ArgoCD application.
