# 8.2. The OpenStack Cloud Controller Manager (CCM) config map

An RHOSP CCM config map defines how your cluster interacts with your RHOSP cloud. By default, the configuration is stored under the `cloud.conf` key in the `cloud-conf` config map in the `openshift-cloud-controller-manager` namespace. 

Important

The `cloud-conf` config map is generated from the `cloud-provider-config` config map in the `openshift-config` namespace. 

To change the settings that are described by the `cloud-conf` config map, modify the `cloud-provider-config` config map. 

As part of this synchronization, the CCM Operator overrides some options. For more information, see "The RHOSP Cloud Controller Manager". 

For example: 

**An example`cloud-conf` config map**

```yaml
apiVersion: v1
data:
  cloud.conf: |
    [Global]
    secret-name = openstack-credentials
    secret-namespace = kube-system
    region = regionOne
    [LoadBalancer]
    enabled = True
kind: ConfigMap
metadata:
  creationTimestamp: "2022-12-20T17:01:08Z"
  name: cloud-conf
  namespace: openshift-cloud-controller-manager
  resourceVersion: "2519"
  uid: cbbeedaf-41ed-41c2-9f37-4885732d3677
```


`apiVersion.data.cloud.conf`: Specifies global options by using a `clouds.yaml` file rather than modifying the config map. 

The following options are present in the config map. Except when indicated otherwise, they are mandatory for clusters that run on RHOSP. 

## 8.2.1. Load balancer options

You can configure load balancer options to control how the Cloud Controller Manager (CCM) creates and manages RHOSP Octavia load balancers for services in your cluster. 

Note

Neutron-LBaaS support is deprecated. 

Option| Description  
---|---  
`enabled` |  Enables the `LoadBalancer` service type integration. The default value is `true`.   
`floating-network-id` |  Optional. The external network used to create floating IP addresses for load balancer virtual IP addresses (VIPs). If there are multiple external networks in the cloud, you must set this option or specify the `loadbalancer.openstack.org/floating-network-id` label in the service annotation.   
`floating-subnet-id` |  Optional. The external network subnet used to create floating IP addresses for the load balancer VIP. Can be overridden by the service annotation `loadbalancer.openstack.org/floating-subnet-id`.   
`floating-subnet` |  Optional. A name pattern (glob or regular expression if starting with `~`) for the external network subnet used to create floating IP addresses for the load balancer VIP. Can be overridden by the service annotation `loadbalancer.openstack.org/floating-subnet`. If multiple subnets match the pattern, the first one with available IP addresses is used.   
`floating-subnet-tags` |  Optional. Tags for the external network subnet used to create floating IP addresses for the load balancer VIP. Can be overridden by the service annotation `loadbalancer.openstack.org/floating-subnet-tags`. If multiple subnets match these tags, the first one with available IP addresses is used.  If the RHOSP network is configured with sharing disabled, for example, with the `--no-share` flag used during creation, this option is unsupported. Set the network to share to use this option.   
`lb-method` |  The load balancing algorithm used to create the load balancer pool. For the Amphora provider the value can be `ROUND_ROBIN`, `LEAST_CONNECTIONS`, or `SOURCE_IP`. The default value is `ROUND_ROBIN`.  For the OVN provider, only the `SOURCE_IP_PORT` algorithm is supported.  For the Amphora provider, if using the `LEAST_CONNECTIONS` or `SOURCE_IP` methods, configure the `create-monitor` option as `true` in the `cloud-provider-config` config map on the `openshift-config` namespace and `ETP:Local` on the load-balancer type service to allow balancing algorithm enforcement in the client to service endpoint connections.   
`lb-provider` |  Optional. Used to specify the provider of the load balancer, for example, `amphora` or `octavia`. Only the Amphora and Octavia providers are supported.   
`lb-version` |  Optional. The load balancer API version. Only `"v2"` is supported.   
`subnet-id` |  The ID of the Networking service subnet on which load balancer VIPs are created. For dual stack deployments, leave this option unset. The OpenStack cloud provider automatically selects which subnet to use for a load balancer.   
`network-id` |  The ID of the Networking service network on which load balancer VIPs are created. Unnecessary if `subnet-id` is set. If this property is not set, the network is automatically selected based on the network that cluster nodes use.   
`create-monitor` |  Creates a health monitor for the service load balancer. A health monitor is required for services that declare `externalTrafficPolicy: Local`. The default value is `false`.  This option is unsupported if you use RHOSP earlier than version 17 with the `ovn` provider.   
`monitor-delay` |  The interval in seconds by which probes are sent to members of the load balancer. The default value is `5`.   
`monitor-max-retries` |  The number of successful checks that are required to change the operating status of a load balancer member to `ONLINE`. The valid range is `1` to `10`, and the default value is `1`.   
`monitor-timeout` |  The time in seconds that a monitor waits to connect to the back end before it times out. The default value is `3`.   
`internal-lb` |  Whether or not to create an internal load balancer without floating IP addresses. The default value is `false`.   
`LoadBalancerClass "ClassName"` |  This is a config section that comprises a set of options: 

  * `floating-network-id`
  * `floating-subnet-id`
  * `floating-subnet`
  * `floating-subnet-tags`
  * `network-id`
  * `subnet-id`

The behavior of these options is the same as that of the identically named options in the load balancer section of the CCM config file.  You can set the `ClassName` value by specifying the service annotation `loadbalancer.openstack.org/class`.   
`max-shared-lb` |  The maximum number of services that can share a load balancer. The default value is `2`.   
Show more

## 8.2.2. Options that the Operator overrides

The CCM Operator overrides specific options, which you might recognize from configuring RHOSP. Do not configure these options. The options are for informational purposes only. 

Table 8.1. Options overridden by the CCM OperatorOption| Description  
---|---  
`auth-url` |  The RHOSP Identity service URL. For example, `<http://128.110.154.166/identity>`.   
`os-endpoint-type` |  The type of endpoint to use from the service catalog.   
`username` |  The Identity service user name.   
`password` |  The Identity service user password.   
`domain-id` |  The Identity service user domain ID.   
`domain-name` |  The Identity service user domain name.   
`tenant-id` |  The Identity service project ID. Leave this option unset if you are using Identity service application credentials.  In version 3 of the Identity API, which changed the identifier `tenant` to `project`, the value of `tenant-id` is automatically mapped to the project construct in the API.   
`tenant-name` |  The Identity service project name.   
`tenant-domain-id` |  The Identity service project domain ID.   
`tenant-domain-name` |  The Identity service project domain name.   
`user-domain-id` |  The Identity service user domain ID.   
`user-domain-name` |  The Identity service user domain name.   
`use-clouds` |  Whether to fetch authorization credentials from a `clouds.yaml` file. Options set in this section are prioritized over values read from the `clouds.yaml` file.  The CCM Operator searches for the file in the following places: 

  1. The value of the `clouds-file` option. 
  2. A file path stored in the environment variable `OS_CLIENT_CONFIG_FILE`. 
  3. The directory `pkg/openstack`. 
  4. The directory `~/.config/openstack`. 
  5. The directory `/etc/openstack`. 

  
`clouds-file` |  The file path of a `clouds.yaml` file. It is used if the `use-clouds` option is set to `true`.   
`cloud` |  The named cloud in the `clouds.yaml` file that you want to use. It is used if the `use-clouds` option is set to `true`.   
Show more
