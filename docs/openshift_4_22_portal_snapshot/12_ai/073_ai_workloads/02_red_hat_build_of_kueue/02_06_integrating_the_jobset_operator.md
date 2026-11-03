# 2.6. Integrating the JobSet Operator

You can integrate JobSet Operator with Red Hat build of Kueue so you can leverage the scheduling and resource management functionality provided by Red Hat build of Kueue when running the JobSet Operator. 

You can use the JobSet Operator to manage and run large-scale, coordinated workloads like high-performance computing (HPC) and AI training. 

The JobSet Operator models a distributed batch workload as a group of Kubernetes Jobs. This allows you to easily specify different pod templates for different distinct groups of pods, for example, a leader, workers, parameter servers, and so on. 

## 2.6.1. Installing JobSet Operator with Red Hat build of Kueue

You can configure Red Hat build of Kueue to work with the JobSet Operator. 

**Prerequisites**

  * You have installed Red Hat build of Kueue using the Red Hat Build of Kueue Operator in the software catalog. 
  * You have installed JobSet Operator in the software catalog. 
  * You have cluster administrator permissions and the `kueue-batch-admin-role` role. 
  * You have access to the OpenShift Container Platform web console. 
  * You have installed the cert-manager Operator for Red Hat OpenShift for your cluster. 



**Procedure**

  * Add `JobSet` to the `config.integrations.frameworks` section of the Red Hat build of Kueue cluster object, as shown in the following example: 

```yaml
apiVersion: kueue.openshift.io/v1
kind: Kueue
metadata:
  name: cluster
  namespace: openshift-kueue-operator
spec:
  managementState: Managed
  config:
    integrations:
      frameworks:
      - JobSet
```


**Additional resources**

  * [About the JobSet Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/ai_workloads/jobset-operator#js-about_js-about "4.1.1. About the JobSet Operator")
  * [Run A JobSet (Kubernetes documentation)](https://kueue.sigs.k8s.io/docs/tasks/run/jobsets/)
  * [Installing the cert-manager Operator for Red Hat OpenShift by using the web console](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/security_and_compliance/#installing-the-cert-manager-operator-for-red-hat-openshift)



## 2.6.2. Running JobSet Operator with Red Hat build of Kueue

You can add and run JobSet Operator to your existing frameworks. 

**Prerequisites**

  * Red Hat build of Kueue using the Red Hat Build of Kueue Operator is installed. 
  * JobSet Operator is installed. 
  * The cert-manager Operator for Red Hat OpenShift is installed. 
  * The `namespace` where `JobSet` will be created is labeled using `kueue.openshift.io/managed=true`. 
  * Ensure that the following objects have been configured: 

    * `ClusterQueue`
    * `ResourceFlavor`
    * `LocalQueue`
    * `Namespace`




**Procedure**

  1. Create a file named `jobset.yaml`. 

**Example of a`JobSet`**

```yaml
apiVersion: jobset.x-k8s.io/v1alpha2
kind: JobSet
metadata:
  name: jobset
  namespace: my-namespace
spec:
  replicatedJobs:
    - name: workers
      replicas: 1
      template:
        spec:
          parallelism: 3
          completions: 3
          backoffLimit: 1
          template:
            spec:
              containers:
                - name: sleep
                  image: busybox
                  resources:
                    requests:
                      cpu: 200m
                      memory: "200Mi"
                  command:
                    - sleep
                  args:
                    - 220s
    - name: driver
      template:
        spec:
          parallelism: 1
          completions: 1
          backoffLimit: 0
          template:
            spec:
              containers:
                - name: sleep
                  image: busybox
                  resources:
                    requests:
                      cpu: 200m
                      memory: "200Mi"
                  command:
                    - sleep
                  args:
                    - 220s
```


  2. Specify the target local queue in the `metadata.labels` section of the `JobSet` configuration. 

```yaml
metadata:
  labels:
    kueue.x-k8s.io/queue-name: <local-queue-name>
```


  3. Apply the JobSet configuration by running the following command: 

```shell-session
$ oc apply -f jobset.yaml
```


**Additional resources**

  * [Configuring a cluster queue](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/ai_workloads/red-hat-build-of-kueue#configuring-clusterqueues_configuring-quotas "2.9.1. Configuring a cluster queue")
  * [Configuring a resource flavor](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/ai_workloads/red-hat-build-of-kueue#configuring-resourceflavors_configuring-quotas "2.9.2. Configuring a resource flavor")
  * [Configuring a local queue](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/ai_workloads/red-hat-build-of-kueue#configuring-localqueues_configuring-quotas "2.9.3. Configuring a local queue")
