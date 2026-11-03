# 7.4. Check DNS Operator status

You can inspect the status and view the details of the DNS Operator by using the `oc describe` command. 

**Procedure**

  * View the status of the DNS Operator: 

```shell-session
$ oc describe clusteroperators/dns
```


Though the messages and spelling might vary in a specific release, the expected status output looks like: 

```shell-session
Status:
  Conditions:
    Last Transition Time:  <date>
    Message:               DNS "default" is available.
    Reason:                AsExpected
    Status:                True
    Type:                  Available
    Last Transition Time:  <date>
    Message:               Desired and current number of DNSes are equal
    Reason:                AsExpected
    Status:                False
    Type:                  Progressing
    Last Transition Time:  <date>
    Reason:                DNSNotDegraded
    Status:                False
    Type:                  Degraded
    Last Transition Time:  <date>
    Message:               DNS default is upgradeable: DNS Operator can be upgraded
    Reason:                DNSUpgradeable
    Status:                True
    Type:                  Upgradeable
```
