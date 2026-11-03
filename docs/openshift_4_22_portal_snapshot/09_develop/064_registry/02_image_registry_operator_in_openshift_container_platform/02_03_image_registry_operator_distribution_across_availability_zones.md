# 2.3. Image Registry Operator distribution across availability zones

The Image Registry Operator spreads image registry pods across topology zones by default to prevent delayed recovery times during a complete zone failure. 

The following example YAML shows the default topology constraint parameter values: 

```yaml
  topologySpreadConstraints:
  - labelSelector:
      matchLabels:
        docker-registry: default
    maxSkew: 1
    topologyKey: kubernetes.io/hostname
    whenUnsatisfiable: DoNotSchedule
  - labelSelector:
      matchLabels:
        docker-registry: default
    maxSkew: 1
    topologyKey: node-role.kubernetes.io/worker
    whenUnsatisfiable: DoNotSchedule
  - labelSelector:
      matchLabels:
        docker-registry: default
    maxSkew: 1
    topologyKey: topology.kubernetes.io/zone
    whenUnsatisfiable: DoNotSchedule
```


Reference the following YAML to understand the default parameter value that the Image Registry Operator uses when the Operator deploys with a zone-related topology constraint, which applies to bare metal and vSphere instances: 

```yaml
 topologySpreadConstraints:
  - labelSelector:
      matchLabels:
        docker-registry: default
    maxSkew: 1
    topologyKey: kubernetes.io/hostname
    whenUnsatisfiable: DoNotSchedule
  - labelSelector:
      matchLabels:
        docker-registry: default
    maxSkew: 1
    topologyKey: node-role.kubernetes.io/worker
    whenUnsatisfiable: DoNotSchedule
```


As a cluster administrator. you can override the default `topologySpreadConstraints` section values by configuring the `configs.imageregistry.operator.openshift.io/cluster` spec file.
