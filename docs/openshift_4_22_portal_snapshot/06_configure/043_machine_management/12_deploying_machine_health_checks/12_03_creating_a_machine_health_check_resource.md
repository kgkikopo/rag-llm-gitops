# 12.3. Creating a machine health check resource

You can create a `MachineHealthCheck` resource to monitor and automatically remediate unhealthy machines in a machine set. 

Note

You can only apply a machine health check to machines that are managed by compute machine sets or control plane machine sets. 

**Prerequisites**

  * Install the `oc` command-line interface. 



**Procedure**

  1. Create a `healthcheck.yml` file that contains the definition of your machine health check. 
  2. Apply the `healthcheck.yml` file to your cluster: 

```shell-session
$ oc apply -f healthcheck.yml
```
