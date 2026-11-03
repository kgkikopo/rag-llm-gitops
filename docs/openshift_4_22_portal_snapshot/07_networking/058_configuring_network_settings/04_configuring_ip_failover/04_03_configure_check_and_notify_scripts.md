# 4.3. Configure check and notify scripts

To customize health monitoring for IP failover and receive notifications when VIP state changes in OpenShift Container Platform, you can configure check and notify scripts by using `ConfigMap` objects. 

The check and notify scripts run inside the IP failover pod and use the pod file system rather than the host file system. The host file system is available to the pod under the `/hosts` mount path. When configuring a check or notify script, you must provide the full path to the script. 

Each IP failover pod manages a Keepalived daemon that controls one or more virtual IP (VIP) addresses on the node where the pod is running. Keepalived tracks the state of each VIP on the node, which can be `master`, `backup`, or `fault`. 

The full path names of the check and notify scripts are added to the Keepalived configuration file, `/etc/keepalived/keepalived.conf`, which is loaded each time Keepalived starts. You add the scripts to the pod by using a `ConfigMap` object, as described in the following sections. 

Check script
    

Keepalived monitors application health by periodically running an optional, user-supplied check script. For example, the script can test a web server by issuing a request and verifying the response. If you do not provide a check script, Keepalived runs a default script that tests the TCP connection. This default test is suppressed when the monitor port is set to `0`. 

If the check script returns a non-zero value, the node enters the `backup` state and any VIPs that it holds are reassigned. 

Notify script
    

As a cluster administrator, you can provide an optional notify script that Keepalived calls whenever the VIP state changes. Keepalived passes the following parameters to the notify script: 

  * `$1` — `group` or `instance`
  * `$2` — Name of the `group` or `instance`
  * `$3` — New state: `master`, `backup`, or `fault`



**Prerequisites**

  * You installed the OpenShift CLI (`oc`). 
  * You are logged in to the cluster with a user with `cluster-admin` privileges. 



**Procedure**

  1. Create the desired script and create a `ConfigMap` object to hold it. The script has no input arguments and must return `0` for `OK` and `1` for `fail`. 

The check script, `_mycheckscript.sh_`: 

```bash
#!/bin/bash
    # Whatever tests are needed
    # E.g., send request and verify response
exit 0
```


  2. Create the `ConfigMap` object by running the following command: 

```shell-session
$ oc create configmap mycustomcheck --from-file=mycheckscript.sh
```


  3. Add the script to the pod. The `defaultMode` for the mounted `ConfigMap` object files must able to run by using `oc` commands or by editing the IP failover configuration. 

     1. Add the script to the pod by running the following command. A value of `0755`, `493` decimal, is typical. For example: 

```shell-session
$ oc set env deploy/ipfailover-keepalived \
    OPENSHIFT_HA_CHECK_SCRIPT=/etc/keepalive/mycheckscript.sh
```


```shell-session
$ oc set volume deploy/ipfailover-keepalived --add --overwrite \
    --name=config-volume \
    --mount-path=/etc/keepalive \
    --source='{"configMap": { "name": "mycustomcheck", "defaultMode": 493}}'
```


Note

The `oc set env` command is whitespace sensitive. There must be no whitespace on either side of the `=` sign. 

     2. Alternatively, edit the `ipfailover-keepalived` configuration by running the following command: 

```shell-session
$ oc edit deploy ipfailover-keepalived
```


**Example`ipfailover-keepalived` configuration**

```yaml
    spec:
      containers:
      - env:
        - name: OPENSHIFT_HA_CHECK_SCRIPT
          value: /etc/keepalive/mycheckscript.sh
...
        volumeMounts:
        - mountPath: /etc/keepalive
          name: config-volume
      dnsPolicy: ClusterFirst
...
      volumes:
      - configMap:
          defaultMode: 0755
          name: customrouter
        name: config-volume
...
```


where: 

`spec.container.env.name`
     Specifies the `OPENSHIFT_HA_CHECK_SCRIPT` environment variable to point to the mounted script file. 
`spec.container.volumeMounts`
     Specifies the `spec.container.volumeMounts` field to create the mount point. 
`spec.volumes`
     Specifies a new `spec.volumes` field to mention the config map. 
`spec.volumes.configMap.defaultMode`
     Specifies run permission on the files. When read back, it is displayed in decimal, `493`. 

     3. Save the changes and exit the editor. This restarts the `ipfailover-keepalived` configuration.
