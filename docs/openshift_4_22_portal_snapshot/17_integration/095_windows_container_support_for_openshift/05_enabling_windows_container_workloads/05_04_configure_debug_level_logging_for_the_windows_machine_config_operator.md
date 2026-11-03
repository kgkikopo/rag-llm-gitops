# 5.4. Configure debug-level logging for the Windows Machine Config Operator

You can edit the WMCO `Subscription` object to change the Windows Machine Config Operator (WMCO) log level to `debug`, if you need more verbose output. 

By default, the WMCO is configured to use the `info` log level. 

**Procedure**

  1. Edit the `windows-machine-config-operator` subscription in the `windows-machine-config-operator` namespace by using the following command: 

```shell-session
$ oc edit subscription windows-machine-config-operator -n openshift-windows-machine-config-operator
```


  2. Add the follwing parameters to the `.spec.config.env` stanza: 

```yaml
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
# ...
  name: windows-machine-config-operator
  namespace: openshift-windows-machine-config-operator
# ...
spec:
# ...
  config:
    env:
    - name: ARGS
      value: --debugLogging
```


where: 

`spec.config.env.name`
     Specifies a list of environment variables that must exist in all containers in the pod. 
`spec.config.env.value`
     Specifies the `debug` level of verbosity for log messages. 

You can revert to the default `info` log level by removing the `name` and `value` parameters that you added.
