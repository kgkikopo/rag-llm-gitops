# 7.9. Tune the CoreDNS cache

To reduce the load on upstream DNS resolvers, you can tune the CoreDNS cache by adjusting the duration of positive and negative caching. This process involves modifying the time-to-live (TTL) values within the DNS Operator object to control how long query responses are stored. 

For CoreDNS, you can configure the maximum duration of both successful or unsuccessful caching, also known respectively as positive or negative caching. Tuning the cache duration of DNS query responses can reduce the load for any upstream DNS resolvers. 

You can shorten the TTL of the DNS record by setting a lower positive cache. You cannot increase the TTL on the DNS record by setting a higher positive cache. The maximum cache is the lower of the TTL of the DNS record or the positive cache. 

Warning

Setting TTL fields to low values could lead to an increased load on the cluster, any upstream resolvers, or both. 

**Procedure**

  1. Edit the DNS Operator object named `default` by running the following command: 

```shell-session
$ oc edit dns.operator.openshift.io/default
```


  2. Modify the time-to-live (TTL) caching values: 

**Configuring DNS caching**

```yaml
apiVersion: operator.openshift.io/v1
kind: DNS
metadata:
  name: default
spec:
  cache:
    positiveTTL: 1h
    negativeTTL: 0.5h10m
```


where: 

`spec.cache.positiveTTL`
     Specifies a string value that is converted to its respective number of seconds by CoreDNS. If this field is omitted, the value is assumed to be `0s` and the cluster uses the internal default value of `900s` as a fallback. 
`spec.cache.negativeTTL`
     Specifies a string value that is converted to its respective number of seconds by CoreDNS. If this field is omitted, the value is assumed to be `0s` and the cluster uses the internal default value of `30s` as a fallback. 




**Verification**

  1. To review the change, look at the config map again by running the following command: 

```shell-session
$ oc get configmap/dns-default -n openshift-dns -o yaml
```


  2. Verify that you see entries that look like the following example: 

```yaml
       cache 3600 {
            denial 9984 2400
        }
```


**Additional resources**

  * [CoreDNS cache](https://coredns.io/plugins/cache/)



## 7.9.1. Changing the DNS Operator managementState

You can change from the default `Managed` state to `Unmanaged` to stop the DNS Operator from managing its resources in order to apply a workaround or test a configuration change. 

The DNS Operator manages the CoreDNS component to provide a name resolution service for pods and services in the cluster. The `managementState` of the DNS Operator is set to `Managed` by default, which means that the DNS Operator is actively managing its resources. You can change it to `Unmanaged`, which means the DNS Operator is not managing its resources. 

The following are use cases for changing the DNS Operator `managementState`: 

  * You are a developer and want to test a configuration change to see if it fixes an issue in CoreDNS. You can stop the DNS Operator from overwriting the configuration change by setting the `managementState` to `Unmanaged`. 
  * You are a cluster administrator and have reported an issue with CoreDNS, but need to apply a workaround until the issue is fixed. You can set the `managementState` field of the DNS Operator to `Unmanaged` to apply the workaround. 



Note

You cannot upgrade while the `managementState` is set to `Unmanaged`. 

**Procedure**

  1. Change `managementState` to `Unmanaged` in the DNS Operator by running the following command: 

```shell-session
oc patch dns.operator.openshift.io default --type merge --patch '{"spec":{"managementState":"Unmanaged"}}'
```


  2. Review `managementState` of the DNS Operator by using the `jsonpath` command-line JSON parser: 

```shell-session
$ oc get dns.operator.openshift.io default -ojsonpath='{.spec.managementState}'
```


## 7.9.2. Control DNS pod placement

Control where CoreDNS and node-resolver pods run by using taints, tolerations, and selectors. 

The DNS Operator has two daemon sets: one for CoreDNS called `dns-default` and one for managing the `/etc/hosts` file called `node-resolver`. 

You can assign and run CoreDNS pods on specified nodes. For example, if the cluster administrator has configured security policies that prohibit communication between pairs of nodes, you can configure CoreDNS pods to run on a restricted set of nodes. 

DNS service is available to all pods if the following circumstances are true: 

  * DNS pods are running on some nodes in the cluster. 
  * The nodes on which DNS pods are not running have network connectivity to nodes on which DNS pods are running, 



The `node-resolver` daemon set must run on every node host because it adds an entry for the cluster image registry to support pulling images. The `node-resolver` pods have only one job: to look up the `image-registry.openshift-image-registry.svc` service’s cluster IP address and add it to `/etc/hosts` on the node host so that the container runtime can resolve the service name. 

As a cluster administrator, you can use a custom node selector to configure the daemon set for CoreDNS to run or not run on certain nodes. 

**Prerequisites**

  * You installed the `oc` CLI. 
  * You are logged in to the cluster as a user with `cluster-admin` privileges. 
  * Your DNS Operator `managementState` is set to `Managed`. 



**Procedure**

  * To allow the daemon set for CoreDNS to run on certain nodes, configure a taint and toleration: 

    1. Set a taint on the nodes that you want to control DNS pod placement by entering the following command: 

```shell-session
$ oc adm taint nodes <node_name> dns-only=abc:NoExecute
```


       * Replace `<node_name>` with the actual name of the node. 

    2. Modify the DNS Operator object named `default` to include the corresponding toleration by entering the following command: 

```shell-session
$ oc edit dns.operator/default
```


    3. Specify a taint key and a toleration for the taint. The following toleration matches the taint set on the nodes. 

```yaml
apiVersion: operator.openshift.io/v1
kind: DNS
metadata:
  name: default
spec:
  nodePlacement:
    tolerations:
    - effect: NoExecute
      key: "dns-only"
      operator: Equal
      value: abc
      tolerationSeconds: 3600
```


       * If the `key` field is set to `dns-only`, it can be tolerated indefinitely. 
       * The `tolerationSeconds` field is optional. 

    4. Optional: To specify node placement using a node selector, modify the default DNS Operator: 

       1. Edit the DNS Operator object named `default` to include a node selector: 

```yaml
apiVersion: operator.openshift.io/v1
kind: DNS
metadata:
  name: default
spec:
  nodePlacement:
    nodeSelector:
      node-role.kubernetes.io/control-plane: ""
```


          * The `spec.nodePlacement.nodeSelector` field in the example ensures that the CoreDNS pods run only on control plane nodes. 




## 7.9.3. Configure DNS forwarding with TLS

Configure DNS forwarding with TLS to secure queries to upstream resolvers. 

When working in a highly regulated environment, you might need the ability to secure DNS traffic when forwarding requests to upstream resolvers so that you can ensure additional DNS traffic and data privacy. 

Be aware that CoreDNS caches forwarded connections for 10 seconds. CoreDNS will hold a TCP connection open for those 10 seconds if no request is issued. 

Note

With large clusters, ensure that your DNS server is aware that it might get many new connections to hold open because you can initiate a connection per node. Set up your DNS hierarchy accordingly to avoid performance issues. 

**Procedure**

  1. Modify the DNS Operator object named `default`: 

```shell-session
$ oc edit dns.operator/default
```


Cluster administrators can configure transport layer security (TLS) for forwarded DNS queries. 

**Configuring DNS forwarding with TLS**

```yaml
apiVersion: operator.openshift.io/v1
kind: DNS
metadata:
  name: default
spec:
  servers:
  - name: example_server
    zones:
    - example.com
    forwardPlugin:
      transportConfig:
        transport: TLS
        tls:
          caBundle:
            name: mycacert
          serverName: dnstls.example.com
      policy: Random
      upstreams:
      - 1.1.1.1
      - 2.2.2.2:5353
  upstreamResolvers:
    transportConfig:
      transport: TLS
      tls:
        caBundle:
          name: mycacert
        serverName: dnstls.example.com
    upstreams:
    - type: Network
      address: 1.2.3.4
      port: 53
```


where: 

`spec.servers.name`
     Must comply with the `rfc6335` service name syntax. 
`spec.servers.zones`
     Must conform to the `rfc1123` subdomain syntax. The cluster domain, `cluster.local`, is invalid for `zones`. 
`spec.servers.forwardPlugin.transportConfig.transport`
     Must be set to `TLS` when configuring TLS forwarding. 
`spec.servers.forwardPlugin.transportConfig.tls.serverName`
     Must be set to the server name indication (SNI) server name used to validate the upstream TLS certificate. 
`spec.servers.forwardPlugin.policy`
     Specifies the upstream selection policy. Defaults to `Random`; valid values are `RoundRobin` and `Sequential`. 
`spec.servers.forwardPlugin.upstreams`
     Must provide upstream resolvers; maximum 15 entries per `forwardPlugin`. 
`spec.upstreamResolvers.upstreams`
     Specifies an optional field to override the default policy for the default domain. Use the `Network` type only when TLS is enabled and provide an IP address. If omitted, queries use `/etc/resolv.conf`. 
`spec.upstreamResolvers.upstreams.address`
     Must be a valid IPv4 or IPv6 address. 
`spec.upstreamResolvers.upstreams.port`
    

Specifies an optional field to provide a port number. Valid values are between `1` and `65535`; defaults to 853 when omitted. 

Note

If `servers` is undefined or invalid, the config map only contains the default server. 




**Verification**

  1. View the config map: 

```shell-session
$ oc get configmap/dns-default -n openshift-dns -o yaml
```


**Sample DNS ConfigMap based on TLS forwarding example**

```yaml
apiVersion: v1
data:
  Corefile: |
    example.com:5353 {
        forward . 1.1.1.1 2.2.2.2:5353
    }
    bar.com:5353 example.com:5353 {
      forward . 3.3.3.3 4.4.4.4:5454
    }
    .:5353 {
        errors
        health
        kubernetes cluster.local in-addr.arpa ip6.arpa {
            pods insecure
            upstream
            fallthrough in-addr.arpa ip6.arpa
        }
        prometheus :9153
        forward . /etc/resolv.conf 1.2.3.4:53 {
            policy Random
        }
        cache 30
        reload
    }
kind: ConfigMap
metadata:
  labels:
    dns.operator.openshift.io/owning-dns: default
  name: dns-default
  namespace: openshift-dns
```


     * The `data.Corefile` key contains the Corefile configuration for the DNS server. Changes to the `forwardPlugin` triggers a rolling update of the CoreDNS daemon set. 




**Additional resources**

  * [CoreDNS forward documentation](https://coredns.io/plugins/forward/)
