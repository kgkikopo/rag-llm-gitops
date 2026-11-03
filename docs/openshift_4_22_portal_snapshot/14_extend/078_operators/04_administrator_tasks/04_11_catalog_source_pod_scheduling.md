# 4.11. Catalog source pod scheduling

When a `grpc` type catalog source defines the `spec.image` field, the Catalog Operator creates a pod to serve that image. 

By default, the pod specification configures the following default settings: 

  * Node selector: `kubernetes.io/os=linux`
  * Priority class name: `system-cluster-critical`
  * Tolerations: None 



As an administrator, you can override these defaults by configuring fields in the optional `spec.grpcPodConfig` section of the `CatalogSource` object. 

Important

The Marketplace Operator, `openshift-marketplace`, manages the default `OperatorHub` custom resource’s (CR). This CR manages `CatalogSource` objects. If you attempt to modify fields in the `CatalogSource` object’s `spec.grpcPodConfig` section, the Marketplace Operator automatically reverts these modifications. By default, if you modify fields in the `spec.grpcPodConfig` section of the `CatalogSource` object, the Marketplace Operator automatically reverts these changes. 

To apply persistent changes to `CatalogSource` object, you must first disable a default `CatalogSource` object. 

**Additional resources**

  * [OLM concepts and resources  Catalog source](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/understanding-operators#olm-catalogsource_olm-understanding-olm "2.4.1.2.2. Catalog source")



## 4.11.1. Disabling default CatalogSource objects at a local level

You can make persistent local changes to a `CatalogSource` object by disabling the default `CatalogSource` object. Otherwise, the Marketplace Operator automatically reverts any manual modifications to fields in the `spec.grpcPodConfig` section. 

The Marketplace Operator, `openshift-marketplace`, manages the default custom resources (CRs) of the `OperatorHub`. The `OperatorHub` manages `CatalogSource` objects. 

To apply persistent changes to `CatalogSource` object, you must first disable a default `CatalogSource` object. 

**Procedure**

  * To disable all the default `CatalogSource` objects at a local level, enter the following command: 

```shell-session
$ oc patch operatorhub cluster -p '{"spec": {"disableAllDefaultSources": true}}' --type=merge
```


Note

You can also configure the default `OperatorHub` CR to either disable all `CatalogSource` objects or disable a specific object. 




**Additional resources**

  * [OperatorHub custom resource](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/understanding-operators#olm-software-catalog-arch-operatorhub-crd_olm-understanding-software-catalog "2.5.2.1. OperatorHub custom resource")
  * [Disabling the default OperatorHub catalog sources](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/disconnected_environments/#olm-restricted-networks-operatorhub_olm-restricted-networks)



## 4.11.2. Overriding the node selector for catalog source pods

To control which nodes run catalog source pods, you can override the default node selector in the `spec.grpcPodConfig` section of the `CatalogSource` object. 

**Prerequisites**

  * A `CatalogSource` object of source type `grpc` with `spec.image` is defined. 



**Procedure**

  * Edit the `CatalogSource` object and add or modify the `spec.grpcPodConfig` section to include the following: 

```yaml
  grpcPodConfig:
    nodeSelector:
      custom_label: <label>
```


where `<label>` is the label for the node selector that you want catalog source pods to use for scheduling. 




**Additional resources**

  * [Placing pods on specific nodes using node selectors](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#nodes-scheduler-node-selectors)



## 4.11.3. Overriding the priority class name for catalog source pods

To control the scheduling priority of catalog source pods, you can override the default priority class name in the `spec.grpcPodConfig` section of the `CatalogSource` object. 

**Prerequisites**

  * A `CatalogSource` object of source type `grpc` with a defined `spec.image`. 



**Procedure**

  * Edit the `CatalogSource` object and configure the `spec.grpcPodConfig` section, similar to the following example: 

```yaml
  grpcPodConfig:
    priorityClassName: <priority_class>
```


where: 

`<priority_class>`
    

Specifies one of the following priority classes: 

    * A default Kubernetes priority class, such as `system-cluster-critical` or `system-node-critical`
    * An empty string (`""`) to assign the default priority 
    * A custom, pre-existing priority class name 

Note

Previously, the only pod scheduling parameter that could be overriden was `priorityClassName`. This was done by adding the `operatorframework.io/priorityclass` annotation to the `CatalogSource` object. For example: 

```yaml
apiVersion: operators.coreos.com/v1alpha1
kind: CatalogSource
metadata:
  name: example-catalog
  namespace: openshift-marketplace
  annotations:
    operatorframework.io/priorityclass: system-cluster-critical
```


If a `CatalogSource` object defines both the annotation and `spec.grpcPodConfig.priorityClassName`, the annotation takes precedence over the configuration parameter. 




**Additional resources**

  * [Pod priority classes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#admin-guide-priority-preemption-priority-class_nodes-pods-priority)



## 4.11.4. Overriding tolerations for catalog source pods

To allow catalog source pods to schedule onto nodes with matching taints, you can override the default tolerations in the `spec.grpcPodConfig` section of the `CatalogSource` object. 

**Prerequisites**

  * A `CatalogSource` object of source type `grpc` with `spec.image` is defined. 



**Procedure**

  * Edit the `CatalogSource` object and add or modify the `spec.grpcPodConfig` section to include the following: 

```yaml
  grpcPodConfig:
    tolerations:
      - key: "<key_name>"
        operator: "<operator_type>"
        value: "<value>"
        effect: "<effect>"
```


**Additional resources**

  * [Understanding taints and tolerations](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#nodes-scheduler-taints-tolerations-about_nodes-scheduler-taints-tolerations)
