# 18.4. Configure pod security admission for a namespace

You can configure pod security admission modes and profiles at the namespace level to control the security standards that pods must meet in a specific namespace. 

**Procedure**

  * For each pod security admission mode that you want to set on a namespace, run the following command: 

```shell-session
$ oc label namespace <namespace> \
    pod-security.kubernetes.io/<mode>=<profile> \
    --overwrite
```


where: 

`<namespace>`
     Specifies the namespace to configure. 
`<mode>`
     Specifies the pod security admission mode. Valid values are `enforce`, `warn`, or `audit`. 
`<profile>`
     Specifies the pod security profile. Valid values are `restricted`, `baseline`, or `privileged`.
