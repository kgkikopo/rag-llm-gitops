# 9.5. Understand EgressIP failover control

The `reachabilityTotalTimeoutSeconds` parameter controls how quickly the system detects a failing `egressIP` node and initiates a failover. This parameter directly determines the maximum time the platform waits before declaring a node unreachable. 

Important

When you configure `egressIP` with multiple egress nodes, the complete failover time from node failure to recovery on a new node is expected to be on the order of seconds or longer. This is because the new IP assignment can only begin after the `reachabilityTotalTimeoutSeconds` period has fully elapsed without a successful check. 

To ensure traffic uses the correct external path, `egressIP` traffic on a node will always egress through the network interface on which the `egressIP` address has been assigned. 

## 9.5.1. Configure the EgressIP failover time limit

You can configure the `reachabilityTotalTimeoutSeconds` parameter to control how quickly the system detects a failing `egressIP` node and initiates a failover. 

**Prerequisites**

  * You installed the OpenShift CLI (`oc`). 
  * You logged in to the cluster as a cluster administrator. 



**Procedure**

  1. Edit the `Network` custom resource by running the following command: 

```bash
$ oc edit network.operator cluster
```


  2. Navigate to the `egressIPConfig: {}` section under `spec:defaultNetwork:ovnKubernetesConfig:`
  3. Modify the block to include the `reachabilityTotalTimeoutSeconds` parameter with your chosen value, 5 seconds for example. Make sure to use the correct indentation: 

```yaml
  defaultNetwork:
    ovnKubernetesConfig:
      egressIPConfig:
        reachabilityTotalTimeoutSeconds: 5
```


Note

The value must be an integer between 0 and 60. For details on possible values, see the "EgressIP failover settings" section. 

  4. Save and exit the editor. The operator automatically applies the changes. 



**Verification**

  1. Verify that the system correctly accepted the `reachabilityTotalTimeoutSeconds` parameter by running the following command: 

```shell-session
$ oc get network.operator cluster -o yaml
```


  2. Inspect the output and confirm that the `reachabilityTotalTimeoutSeconds` parameter is correctly nested under `spec:defaultNetwork:ovnKubernetesConfig:egressIPConfig:` with your intended value: 

```yaml
 # ...
  spec:
    # ...
    defaultNetwork:
      ovnKubernetesConfig:
        egressIPConfig:
          reachabilityTotalTimeoutSeconds: 5
        gatewayConfig:
  # ...
```


## 9.5.2. EgressIP failover settings

The `reachabilityTotalTimeoutSeconds` parameter defines the total time limit in seconds for the platform health check process before a node is declared down. 

The following table summarizes the acceptable values and their implications: 

Parameter Value (Seconds)| Effect on reachability check| Failover impact and use case  
---|---|---  
`0` |  Disables the reachability check.  |  No automatic failover: Use only if an external system handles node health monitoring and failover. The platform will not automatically react to node failures.   
`1 - 60` |  Sets the total time limit for reachability probing.  |  Directly controls detection time: This value defines the lower limit for your overall failover time. A smaller value leads to faster failover but might increase network traffic. Default: 1 second. The maximum accepted integer value is 60.   
Show more
