# 2.5. Integrating the Leader Worker Set Operator

You can integrate the Leader Worker Set Operator with Red Hat build of Kueue so you can leverage the scheduling and resource management functionality when running LeaderWorkerSets. 

The Leader Worker Set Operator allows you to manage multi-node AI/ML inference deployments efficiently. Red Hat build of Kueue provides scheduling and resource management capabilities for these deployments. You can configure Leader Worker Set Operator to leverage these capabilities when running the `LeaderWorkerSet` API for deploying a group of pods as a unit of replication. 

## 2.5.1. Installing Leader Worker Set Operator with Red Hat build of Kueue

You can configure Red Hat build of Kueue to work with the Leader Worker Set Operator. 

**Prerequisites**

  * You have installed Red Hat build of Kueue using the Red Hat Build of Kueue Operator in the software catalog. 
  * You have installed Leader Worker Set Operator and Operand in the software catalog. 
  * You have cluster administrator permissions and the `kueue-batch-admin-role` role. 
  * You have access to the OpenShift Container Platform web console. 
  * You have installed the cert-manager Operator for Red Hat OpenShift for your cluster. 



**Procedure**

  * Add `LeaderWorkerSet` to the `config.integrations.framework` section of the Red Hat build of Kueue cluster object, as shown in the following example: 

```yaml
apiVersion: kueue.openshift.io/v1
kind: Kueue
metadata:
  labels:
    app.kubernetes.io/name: kueue-operator
    app.kubernetes.io/managed-by: kustomize
  name: cluster
  namespace: openshift-kueue-operator
spec:
  managementState: Managed
  config:
    integrations:
      frameworks:
      - BatchJob
      - LeaderWorkerSet
```


**Additional resources**

  * [About the Leader Worker Set Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/ai_workloads/leader-worker-set-operator#lws-about_lws-about "3.1.1. About the Leader Worker Set Operator")
  * [LeaderWorkerSet API (Kubernetes documentation)](https://lws.sigs.k8s.io/docs/reference/leaderworkerset.v1/)
  * [Installing the cert-manager Operator for Red Hat OpenShift by using the web console](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/security_and_compliance/#installing-the-cert-manager-operator-for-red-hat-openshift)



## 2.5.2. Running Leader Worker Set Operator with Red Hat build of Kueue

You can add and run the Leader Worker Set Operator to your existing frameworks. 

**Prerequisites**

  * Red Hat build of Kueue using the Red Hat Build of Kueue Operator is installed. 
  * Leader Worker Set Operator and Operand are installed. 
  * The cert-manager Operator for Red Hat OpenShift is installed. 
  * The `namespace` where `LeaderWorkerSet` will be created is labeled using `kueue.openshift.io/managed=true`. 
  * Ensure that the following objects have been configured: 

    * `ClusterQueue`
    * `ResourceFlavor`
    * `LocalQueue`
    * `Namespace`




**Procedure**

  1. Create a file named `leaderworkerset.yaml`. 

**Example of a`LeaderWorkerSet`**

```yaml
apiVersion: leaderworkerset.x-k8s.io/v1
kind: LeaderWorkerSet
metadata:
  generation: 1
  name: my-lws
  namespace: my-namespace
spec:
  leaderWorkerTemplate:
    leaderTemplate:
      metadata: {}
      spec:
        containers:
        - image: nginxinc/nginx-unprivileged:1.27
          name: leader
          resources: {}
    restartPolicy: RecreateGroupOnPodRestart
    size: 3
    workerTemplate:
      metadata: {}
      spec:
        containers:
        - image: nginxinc/nginx-unprivileged:1.27
          name: worker
          ports:
          - containerPort: 8080
            protocol: TCP
          resources: {}
  networkConfig:
    subdomainPolicy: Shared
  replicas: 2
  rolloutStrategy:
    rollingUpdateConfiguration:
      maxSurge: 1
      maxUnavailable: 1
    type: RollingUpdate
  startupPolicy: LeaderCreated
```


  2. Specify the target local queue in the `metadata.labels` section of the `LeaderWorkerSet` configuration. 

```yaml
metadata:
  labels:
    kueue.x-k8s.io/queue-name: user-queue
```


  3. Apply the leader worker set configuration by running the following command: 

```shell-session
$ oc apply -f leaderworkerset.yaml
```


**Additional resources**

  * [Configuring a cluster queue](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/ai_workloads/red-hat-build-of-kueue#configuring-clusterqueues_configuring-quotas "2.9.1. Configuring a cluster queue")
  * [Configuring a resource flavor](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/ai_workloads/red-hat-build-of-kueue#configuring-resourceflavors_configuring-quotas "2.9.2. Configuring a resource flavor")
  * [Configuring a local queue](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/ai_workloads/red-hat-build-of-kueue#configuring-localqueues_configuring-quotas "2.9.3. Configuring a local queue")
