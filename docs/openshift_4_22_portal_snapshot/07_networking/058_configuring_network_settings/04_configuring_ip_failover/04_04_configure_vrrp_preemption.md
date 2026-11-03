# 4.4. Configure VRRP preemption

To control VIP preemption behavior when nodes recover in OpenShift Container Platform, you can configure the `OPENSHIFT_HA_PREEMPTION` variable to set a delay before higher priority VIPs take over or disable preemption entirely. 

When a virtual IP (VIP) on a node recovers from the `fault` state, it enters the `backup` state if it has a lower priority than the VIP currently in the `master` state. 

There are two options for the `OPENSHIFT_HA_PREEMPTION` variable: 

  * `nopreempt`: When set, the `master` role does not move from a lower-priority VIP to a higher-priority VIP. 
  * `preempt_delay 300`: When set, Keepalived waits 300 seconds before moving the `master` role to the higher-priority VIP. 



In the following example, the `OPENSHIFT_HA_PREEMPTION` value is set to `preempt_delay 300`. 

**Procedure**

  * To specify preemption enter `oc edit deploy ipfailover-keepalived` to edit the router deployment configuration: 

```shell-session
$ oc edit deploy ipfailover-keepalived
```


```yaml
# ...
    spec:
      containers:
      - env:
        - name: OPENSHIFT_HA_PREEMPTION
          value: preempt_delay 300
#...
```
