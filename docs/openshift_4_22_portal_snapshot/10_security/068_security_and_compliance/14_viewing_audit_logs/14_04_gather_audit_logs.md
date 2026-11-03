# 14.4. Gather audit logs

You can use the must-gather tool to collect the audit logs for debugging your cluster, which you can review or send to Red Hat Support. 

**Procedure**

  1. Run the `oc adm must-gather` command with `-- /usr/bin/gather_audit_logs`: 

```shell-session
$ oc adm must-gather -- /usr/bin/gather_audit_logs
```


  2. Create a compressed file from the `must-gather` directory that was just created in your working directory. For example, on a computer that uses a Linux operating system, run the following command: 

```shell-session
$ tar cvaf must-gather.tar.gz must-gather.local.472290403699006248
```


Replace `must-gather.local.472290403699006248` with the actual directory name. 

  3. Attach the compressed file to your support case on the [the **Customer Support** page](https://access.redhat.com/support/cases/#/case/list) of the Red Hat Customer Portal.
