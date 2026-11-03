# 5.11. Project-level limits

To help control overcommit, you can set per-project resource limit ranges, specifying memory and CPU limits and defaults for a project that overcommit cannot exceed. 

For information on project-level resource limits, see the _Additional resources_ section. 

Alternatively, you can disable overcommitment for specific projects. 

## 5.11.1. Disable overcommitment for a project

If overcommitment is enabled on a project, you can disable overcommitment for that project. This allows infrastructure components to be configured independently of overcommitment. 

**Procedure**

  1. Create or edit the namespace object file. 
  2. Add the following annotation: 

```yaml
apiVersion: v1
kind: Namespace
metadata:
  annotations:
    quota.openshift.io/cluster-resource-override-enabled: "false"
# ...
```


where: 

`metadata.annotations.quota.openshift.io/cluster-resource-override-enabled.false`
     Specifies that overcommit is disabled for this namespace.
