# 8.9. Configuring the Ingress Controller

## 8.9.1. HAProxy Dynamic Configuration Manager (DCM)

As an administrator, you can use Dynamic Configuration Manager (DCM) as an alternative update mechanism that configures a running HAProxy process through a domain socket. This approach eliminates the need to fork and reload the HAProxy process. 

The router automatically uses DCM for supported operations and falls back to fork-and-reload for operations that DCM cannot handle. 

After a router reload, the default HAProxy process forks a new child process and keeps the old process running until all existing connections close. If HAProxy reloads frequently while handling long-lived connections, old processes accumulate and consume excessive memory on the node. Accumulating processes can cause out-of-memory errors in environments with frequent route or endpoint changes. 

DCM addresses this problem by applying configuration updates directly to the running HAProxy process. 

DCM provides the following benefits over the default fork-and-reload model: 

  * Reduced memory usage: Old HAProxy processes do not accumulate during frequent endpoint updates. The fork-and-reload model can cause each old process to consume hundreds of megabytes or several gigabytes of memory. 
  * Improved metrics accuracy: After a fork-and-reload, the old HAProxy process cannot update metrics for its remaining connections. DCM preserves full metrics continuity because the process is not replaced. 
  * Better load balancing: HAProxy load-balancing algorithms such as `roundrobin`, `random`, and `leastconn` track connection counts per backend server. After a reload, the new process has no data about connections managed by old processes. This lack of data causes uneven traffic distribution. DCM retains this data because the process persists. 



With fork-and-reload, scaling an application to any number of replicas triggers an HAProxy configuration reload. DCM handles the following scaling operations dynamically without triggering an HAProxy reload: 

  * Any scale-out operation 
  * Any scale-in operation 



With DCM, HAProxy still requires a reload for unsupported dynamic operations, including: 

  * Adding, removing, or changes routes 
  * Changing TLS certificates on a route 
  * Changing route annotations 
  * Global router configuration changes 



When DCM encounters an operation that it cannot handle dynamically, the router falls back to the standard fork-and-reload mechanism. This mechanism writes a new `haproxy.config` file and reloads HAProxy, which forks a new process to handle incoming connections. The Ingress Operator includes the `spec.tuningOptions.configurationManagement` API field for selecting between DCM and fork-and-reload to manage HAProxy configuration updates. 

## 8.9.2. Enabling or disabling Dynamic Configuration Manager (DCM)

To reduce HAProxy reloads when endpoints change, you can enable DCM. DCM is disabled by default. 

Warning

Enabling DCM is an experimental feature that is not intended for production use. 

Configure the `spec.tuningOptions.configurationManagement` field on the `IngressController` resource to select either DCM or the standard fork-and-reload mechanism. 

**Prerequisites**

  * You have access to the cluster as a user with the `cluster-admin` role. 
  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  * If you need to enable dynamic updates by using DCM, enter the following command: 

```shell-session
$ oc -n openshift-ingress-operator patch ingresscontrollers/default \
  --type=merge \
  --patch='{"spec":{"tuningOptions":{"configurationManagement":"Dynamic"}}}'
```


  * If you need to disable DCM and revert to the fork-and-reload mechanism, enter the following command: 

```shell-session
$ oc -n openshift-ingress-operator patch ingresscontrollers/default \
  --type=merge \
  --patch='{"spec":{"tuningOptions":{"configurationManagement":"ForkAndReload"}}}'
```


## 8.9.3. Set a custom default certificate

As an administrator, you can configure an Ingress Controller to use a custom certificate by creating a Secret resource and editing the `IngressController` custom resource (CR). 

The following procedure assumes that the custom certificate and key pair are in the `tls.crt` and `tls.key` files in the current working directory. Substitute the actual path names for `tls.crt` and `tls.key`. You also may substitute another name for `custom-certs-default` when creating the Secret resource and referencing it in the IngressController CR. 

Note

The following procedure causes the Ingress Controller to be redeployed, using a rolling deployment strategy. 

**Prerequisites**

  * You must have a certificate/key pair in PEM-encoded files, where the certificate is signed by a trusted certificate authority or by a private trusted certificate authority that you configured in a custom PKI. 
  * Your certificate meets the following requirements: 

    * The certificate is valid for the ingress domain. 
    * The certificate uses the `subjectAltName` extension to specify a wildcard domain, such as `*.apps.ocp4.example.com`. 

  * You must have an `IngressController` CR, which includes just having the `default` `IngressController` CR. You can run the following command to check that you have an `IngressController` CR: 

```shell-session
$ oc --namespace openshift-ingress-operator get ingresscontrollers
```


Note

If you have intermediate certificates, they must be included in the `tls.crt` file of the secret containing a custom default certificate. Order matters when specifying a certificate; list your intermediate certificate(s) after any server certificate(s). 




**Procedure**

  1. Create a Secret resource containing the custom certificate in the `openshift-ingress` namespace using the `tls.crt` and `tls.key` files. 

```shell-session
$ oc --namespace openshift-ingress create secret tls custom-certs-default --cert=tls.crt --key=tls.key
```


  2. Update the IngressController CR to reference the new certificate secret: 

```shell-session
$ oc patch --type=merge --namespace openshift-ingress-operator ingresscontrollers/default \
  --patch '{"spec":{"defaultCertificate":{"name":"custom-certs-default"}}}'
```


  3. Verify the update was effective: 

```shell-session
$ echo Q |\
  openssl s_client -connect console-openshift-console.apps.<domain>:443 -showcerts 2>/dev/null |\
  openssl x509 -noout -subject -issuer -enddate
```


where: 

`<domain>`
     Specifies the base domain name for your cluster. 

**Example output**

```plaintext
subject=C = US, ST = NC, L = Raleigh, O = RH, OU = OCP4, CN = *.apps.example.com
issuer=C = US, ST = NC, L = Raleigh, O = RH, OU = OCP4, CN = example.com
notAfter=May 10 08:32:45 2022 GM
```


Tip

You can alternatively apply the following YAML to set a custom default certificate: 

```yaml
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  name: default
  namespace: openshift-ingress-operator
spec:
  defaultCertificate:
    name: custom-certs-default
```


The certificate secret name should match the value used to update the CR. 

Once the IngressController CR has been modified, the Ingress Operator updates the Ingress Controller’s deployment to use the custom certificate. 




## 8.9.4. Remove a custom default certificate

As an administrator, you can remove a custom certificate that you configured an Ingress Controller to use. 

**Prerequisites**

  * You have access to the cluster as a user with the `cluster-admin` role. 
  * You have installed the OpenShift CLI (`oc`). 
  * You previously configured a custom default certificate for the Ingress Controller. 



**Procedure**

  * To remove the custom certificate and restore the certificate that ships with OpenShift Container Platform, enter the following command: 

```shell-session
$ oc patch -n openshift-ingress-operator ingresscontrollers/default \
  --type json -p $'- op: remove\n  path: /spec/defaultCertificate'
```


There can be a delay while the cluster reconciles the new certificate configuration. 




**Verification**

  * To confirm that the original cluster certificate is restored, enter the following command: 

```shell-session
$ echo Q | \
  openssl s_client -connect console-openshift-console.apps.<domain>:443 -showcerts 2>/dev/null | \
  openssl x509 -noout -subject -issuer -enddate
```


where: 

`<domain>`
     Specifies the base domain name for your cluster. 

**Example output**

```plaintext
subject=CN = *.apps.<domain>
issuer=CN = ingress-operator@1620633373
notAfter=May 10 10:44:36 2023 GMT
```


## 8.9.5. Autoscale an Ingress Controller

You can automatically scale an Ingress Controller to dynamically meet routing performance or availability requirements. For example, the requirement to increase throughput. 

The following procedure provides an example for scaling up the default Ingress Controller. 

**Prerequisites**

  * You have the OpenShift CLI (`oc`) installed. 
  * You have access to an OpenShift Container Platform cluster as a user with the `cluster-admin` role. 
  * On VMware vSphere, bare-metal, and Nutanix installer-provisioned infrastructure, scaling up Ingress Controller pods does not improve external traffic performance. To improve performance, ensure that you complete the following prerequisites: 

    * You manually configured a user-managed load balancer for your cluster. 
    * You ensured that the load balancer was configured for the cluster nodes that handle incoming traffic from the Ingress Controller. 

  * You installed the Custom Metrics Autoscaler Operator and an associated KEDA Controller. 

    * You can install the Operator by using the software catalog on the web console. After you install the Operator, you can create an instance of `KedaController`. 




**Procedure**

  1. Create a service account to authenticate with Thanos by running the following command: 

```shell-session
$ oc create -n openshift-ingress-operator serviceaccount thanos && oc describe -n openshift-ingress-operator serviceaccount thanos
```


**Example output**

```shell-session
Name:                thanos
Namespace:           openshift-ingress-operator
Labels:              <none>
Annotations:         <none>
Image pull secrets:  thanos-dockercfg-kfvf2
Mountable secrets:   thanos-dockercfg-kfvf2
Tokens:              <none>
Events:              <none>
```


  2. Manually create the service account secret token with the following command: 

```shell-session
$ oc apply -f - <<EOF
apiVersion: v1
kind: Secret
metadata:
  name: thanos-token
  namespace: openshift-ingress-operator
  annotations:
    kubernetes.io/service-account.name: thanos
type: kubernetes.io/service-account-token
EOF
```


  3. Define a `TriggerAuthentication` object within the `openshift-ingress-operator` namespace by using the service account’s token. 

     1. Create the `TriggerAuthentication` object and pass the value of the `secret` variable to the `TOKEN` parameter: 

```shell-session
$ oc apply -f - <<EOF
apiVersion: keda.sh/v1alpha1
kind: TriggerAuthentication
metadata:
  name: keda-trigger-auth-prometheus
  namespace: openshift-ingress-operator
spec:
  secretTargetRef:
  - parameter: bearerToken
    name: thanos-token
    key: token
  - parameter: ca
    name: thanos-token
    key: ca.crt
EOF
```


  4. Create and apply a role for reading metrics from Thanos: 

     1. Create a new role, `thanos-metrics-reader.yaml`, that reads metrics from pods and nodes: 

**thanos-metrics-reader.yaml**

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: thanos-metrics-reader
  namespace: openshift-ingress-operator
rules:
- apiGroups:
  - ""
  resources:
  - pods
  - nodes
  verbs:
  - get
- apiGroups:
  - metrics.k8s.io
  resources:
  - pods
  - nodes
  verbs:
  - get
  - list
  - watch
- apiGroups:
  - ""
  resources:
  - namespaces
  verbs:
  - get
```


     2. Apply the new role by running the following command: 

```shell-session
$ oc apply -f thanos-metrics-reader.yaml
```


  5. Add the new role to the service account by entering the following commands: 

```shell-session
$ oc adm policy -n openshift-ingress-operator add-role-to-user thanos-metrics-reader -z thanos --role-namespace=openshift-ingress-operator
```


```shell-session
$ oc adm policy -n openshift-ingress-operator add-cluster-role-to-user cluster-monitoring-view -z thanos
```


Note

The argument `add-cluster-role-to-user` is only required if you use cross-namespace queries. The following step uses a query from the `kube-metrics` namespace which requires this argument. 

  6. Create a new `ScaledObject` YAML file, `ingress-autoscaler.yaml`, that targets the default Ingress Controller deployment: 

**Example`ScaledObject` definition**

```yaml
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: ingress-scaler
  namespace: openshift-ingress-operator
spec:
  scaleTargetRef:
    apiVersion: operator.openshift.io/v1
    kind: IngressController
    name: default
    envSourceContainerName: ingress-operator
  minReplicaCount: 1
  maxReplicaCount: 20
  cooldownPeriod: 1
  pollingInterval: 1
  triggers:
  - type: prometheus
    metricType: AverageValue
    metadata:
      serverAddress: https://thanos-querier.openshift-monitoring.svc.cluster.local:9091
      namespace: openshift-ingress-operator
      metricName: 'kube-node-role'
      threshold: '1'
      query: 'sum(kube_node_role{role="worker",service="kube-state-metrics"})'
      authModes: "bearer"
    authenticationRef:
      name: keda-trigger-auth-prometheus
```


where: 

`spec.scaleTargetRef`
     Specifies the custom resource that you are targeting. In this case, the Ingress Controller. 
`spec.maxReplicaCount`
     Specifies the maximum number of replicas. If you omit this field, the default maximum is set to 100 replicas. This field is optional. 
`spec.triggers.metadata.serverAddress`
     Specifies the Thanos service endpoint in the `openshift-monitoring` namespace. 
`spec.triggers.metadata.namespace`
     The Ingress Operator namespace. 
`spec.triggers.metadata.query`
    

This expression evaluates to however many worker nodes are present in the deployed cluster. 

Important

If you are using cross-namespace queries, you must target port 9091 and not port 9092 in the `serverAddress` field. You also must have elevated privileges to read metrics from this port. 

  7. Apply the custom resource definition by running the following command: 

```shell-session
$ oc apply -f ingress-autoscaler.yaml
```


**Verification**

  * Verify that the default Ingress Controller is scaled out to match the value returned by the `kube-state-metrics` query by running the following commands: 

    * Use the `grep` command to search the Ingress Controller YAML file for the number of replicas: 

```shell-session
$ oc get -n openshift-ingress-operator ingresscontroller/default -o yaml | grep replicas:
```


    * Get the pods in the `openshift-ingress` project: 

```shell-session
$ oc get pods -n openshift-ingress
```


**Example output**

```shell-session
NAME                             READY   STATUS    RESTARTS   AGE
router-default-7b5df44ff-l9pmm   2/2     Running   0          17h
router-default-7b5df44ff-s5sl5   2/2     Running   0          3d22h
router-default-7b5df44ff-wwsth   2/2     Running   0          66s
```


## 8.9.6. Ingress Controller router timeout variables

Reference the router timeout configurations on the Ingress Controller. These settings control how long the router waits for client, server, and tunnel connections during normal traffic. 

Note

Do not modify environment variables directly on the router deployment. Instead, configure timeouts through the `IngressController` custom resource (CR) or through annotations on individual `Route` resources. The Ingress Operator automatically sets the corresponding environment variables on the Ingress Controller deployment. 

A `TimeUnits` value uses a number and a unit: `us` (microseconds), `ms` (milliseconds, default), `s` (seconds), `m` (minutes), `h` (hours), `d` (days). 

The regular expression is: [1-9][0-9]*(`us`|`ms`|`s`|`m`|`h`|`d`). 

The following table lists `IngressController` CR fields and router environment variables: 

Field| Environment variable| Default| Description  
---|---|---|---  
`spec.tuningOptions.backendCheckInterval` |  `ROUTER_BACKEND_CHECK_INTERVAL` |  `5000ms` |  Length of time from one liveness check to the next on backends. The `healthCheckInterval` field can override the `backendCheckInterval` field.   
`spec.tuningOptions.clientFinTimeout` |  `ROUTER_CLIENT_FIN_TIMEOUT` |  `1s` |  Controls the TCP finish (FIN) timeout period for the client connecting to the route. If the FIN sent to close the connection does not answer within the given time, HAProxy closes the connection.   
`spec.tuningOptions.clientTimeout` |  `ROUTER_DEFAULT_CLIENT_TIMEOUT` |  `30s` |  Length of time that a client has to acknowledge or send data.   
`spec.tuningOptions.connectTimeout` |  `ROUTER_DEFAULT_CONNECT_TIMEOUT` |  `5s` |  The maximum connection time allowed to establish a connection to the backend pool.   
`spec.tuningOptions.serverFinTimeout` |  `ROUTER_DEFAULT_SERVER_FIN_TIMEOUT` |  `1s` |  Controls the TCP finish (FIN) timeout from the router to the pod backing the route.   
`spec.tuningOptions.serverTimeout` |  `ROUTER_DEFAULT_SERVER_TIMEOUT` |  `30s` |  Length of time that a server has to acknowledge or send data.   
`spec.tuningOptions.tunnelTimeout` |  `ROUTER_DEFAULT_TUNNEL_TIMEOUT` |  `1h` |  Maximum time that idle TCP or WebSocket tunnel connections can remain open. Router reloads start a new HAProxy process for new connections while the prior process drains existing ones.   
`spec.tuningOptions.headerBufferMaxRewriteBytes` |  `ROUTER_SLOWLORIS_HTTP_KEEPALIVE` |  `300s` |  Sets the maximum time to wait for a new HTTP request on an idle connection. If a timeout occurs, HAProxy closes the connection by sending a TCP finish (FIN) to both the client and server. Standard browsers and applications handle this closure transparently by opening a new connection as needed.   
`spec.tuningOptions.slowlorisTimeout` |  `ROUTER_SLOWLORIS_TIMEOUT` |  `10s` |  Length of time the transmission of an HTTP request can take.   
`spec.tuningOptions.reloadInterval` |  `RELOAD_INTERVAL` |  `5s` |  Minimum frequency for the router to reload and apply configuration changes that require a reload.   
`spec.tuningOptions.healthCheckInterval` |  `ROUTER_METRICS_HAPROXY_TIMEOUT` |  `5s` |  Timeout for the gathering of HAProxy metrics.   
Show more

Note

Different timeout settings govern distinct phases of a connection rather than accumulating together. On SSL passthrough routes, `tcp-request inspect-delay` is the maximum time a new connection has to provide the payload HAProxy requires to select a backend. If a client fails to send this payload within that limit, HAProxy closes the connection immediately. This initial connection limit operates independently from HTTP keep-alive timers controlled by `ROUTER_SLOWLORIS_HTTP_KEEPALIVE` (`timeout http-keep-alive`). 

**Example of a route setting custom timeout**

```yaml
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  annotations:
    haproxy.router.openshift.io/timeout: 5500ms
...
```


Note

Setting a server-side timeout value for passthrough routes too low can cause WebSocket connections to time out often on that route. 

**Additional resources**

  * [Configuring the HAProxy reload interval](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/scalability_and_performance/#configuring-haproxy-interval_routing-optimization)
  * [Installing the custom metrics autoscaler](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#nodes-cma-autoscaling-custom-install_nodes-cma-autoscaling-custom-install)
  * [Enabling monitoring for user-defined projects](https://docs.redhat.com/en/documentation/monitoring_stack_for_red_hat_openshift/latest/html/configuring_user_workload_monitoring/preparing-to-configure-the-monitoring-stack-uwm#enabling-monitoring-for-user-defined-projects-uwm_preparing-to-configure-the-monitoring-stack-uwm)
  * [Understanding custom metrics autoscaler trigger authentications](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#nodes-cma-autoscaling-custom-trigger-auth)
  * [Understanding custom metrics autoscaler triggers](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#nodes-cma-autoscaling-custom-prometheus)
  * [Understanding how to add custom metrics autoscalers](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#nodes-cma-autoscaling-custom-adding)



## 8.9.7. Scale an Ingress Controller

Manually scale an Ingress Controller to meeting routing performance or availability requirements such as the requirement to increase throughput. `oc` commands are used to scale the `IngressController` resource. The following procedure provides an example for scaling up the default `IngressController`. 

Note

Scaling is not an immediate action, as it takes time to create the desired number of replicas. 

**Prerequisites**

  * On VMware vSphere, bare-metal, and Nutanix installer-provisioned infrastructure, scaling up Ingress Controller pods does not improve external traffic performance. To improve performance, ensure that you complete the following prerequisites: 

    * You manually configured a user-managed load balancer for your cluster. 
    * You ensured that the load balancer was configured for the cluster nodes that handle incoming traffic from the Ingress Controller. 




**Procedure**

  1. View the current number of available replicas for the default `IngressController`: 

```shell-session
$ oc get -n openshift-ingress-operator ingresscontrollers/default -o jsonpath='{$.status.availableReplicas}'
```


  2. Scale the default `IngressController` to the desired number of replicas by using the `oc patch` command. The following example scales the default `IngressController` to 3 replicas. 

```shell-session
$ oc patch -n openshift-ingress-operator ingresscontroller/default --patch '{"spec":{"replicas": 3}}' --type=merge
```


  3. Verify that the default `IngressController` scaled to the number of replicas that you specified: 

```shell-session
$ oc get -n openshift-ingress-operator ingresscontrollers/default -o jsonpath='{$.status.availableReplicas}'
```


Tip

You can alternatively apply the following YAML to scale an Ingress Controller to three replicas: 

```yaml
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  name: default
  namespace: openshift-ingress-operator
spec:
  replicas: 3               
```


1

```yaml

```


where: 

`spec.replicas`
     If you need a different amount of replicas, change the `replicas` value. 




## 8.9.8. Configure Ingress access logging

To enable Ingress access logging in OpenShift Container Platform, you can log to a sidecar or forward logs to a custom syslog endpoint and specify the log format. 

Container logging is useful to enable access logs on low-traffic clusters when there is no existing Syslog logging infrastructure, or for short-term use while diagnosing problems with the Ingress Controller. 

Syslog is needed for high-traffic clusters where access logs could exceed the OpenShift Logging stack’s capacity, or for environments where any logging solution needs to integrate with an existing Syslog logging infrastructure. The Syslog use-cases can overlap. 

**Prerequisites**

  * Log in as a user with `cluster-admin` privileges. 



**Procedure**

  * For Ingress access logging to a sidecar, complete the following commands: 

    * To enable Ingress access logging to a sidecar, enter the following command: 

```shell-session
$ oc patch ingresscontroller default -n openshift-ingress-operator --type=merge \
  -p '{"spec":{"logging":{"access":{"destination":{"type":"Container"}}}}}'
```


After you configure the Ingress Controller to log to a sidecar, the Operator creates a container named `logs` inside a router pod that exists in the `openshift-ingress` namespace. 

    * If you need to disable Ingress access logging, enter the following command that does not specify any values for `spec.logging`: 

```shell-session
$ oc patch ingresscontroller default -n openshift-ingress-operator --type=json \
  -p='[{"op": "remove", "path": "/spec/logging"}]'
```


    * To stream the access logs and system events from the OpenShift Container Platform Ingress Controller, enter the following command: 

```shell-session
$ oc -n openshift-ingress logs deployment.apps/router-default -c logs
```


**Example output**

```shell-session
2020-05-11T19:11:50.135710+00:00 router-default-57dfc6cd95-bpmk6 router-default-57dfc6cd95-bpmk6 haproxy[108]: 174.19.21.82:39654 [11/May/2020:19:11:50.133] public be_http:hello-openshift:hello-openshift/pod:hello-openshift:hello-openshift:10.128.2.12:8080 0/0/1/0/1 200 142 - - --NI 1/1/0/0/0 0/0 "GET / HTTP/1.1"
```


  * To enable logging to an external Syslog server, enter the following command. Use this option if you need to forward logs to a centralized logging solution such as Splunk, Rsyslog, or Logstash. 

```shell-session
$ oc patch ingresscontroller default -n openshift-ingress-operator --type=merge \
  -p '{"spec":{"logging":{"access":{"destination":{"type":"Syslog","syslog":{"address":"1.2.3.4","port":514,"maxLenght":1024}}}}}}'
```


    * Replace `1.2.3.4` with the destination IP address of your logging server. Syslog does not support a DNS hostname value. 
    * Replace `514` with the UDP destination port of your logging server. 
    * Replace `1024` with the maximum length of a log message in bytes that you want to set for log messages. 

  * To customize the log format, append an HAProxy-compatible log string to the following command. The string determines what information gets captured in the log format, such as a client IP address. 

```shell-session
$ oc patch ingresscontroller default -n openshift-ingress-operator --type=merge \
  -p '{"spec":{"logging":{"access":{"httpLogFormat":"%ci:%cp [%t] %ft %b/%s %B %bq %HM %HU %HV"}}}}'
```


Note

For a list of HAProxy log variable descriptions, see [Custom log format](https://docs.haproxy.org/2.8/configuration.html#8.2.6) in the upstream HAProxy documentation. 

  * To capture custom HTTP headers or response headers in your logs, enter the following command. Consider this option if you need to track an `X-Forwarded-For` header or custom application IDs in the Ingress and application logs. 

```shell-session
$ oc patch ingresscontroller default -n openshift-ingress-operator --type=merge -p '{"spec":{"logging":{"access":{"httpCaptureHeaders":{"request":[{"name":"User-Agent","maxLength": 1024}],"response":[{"name":"Content-Type","maxLength": 1024}]}}}}}'
```


  * To configure a log empty requests policy, enter the following command and set the `logEmptyRequests` parameter to `Log`. By default, HAProxy might not log empty requests or health checks, so you must manually enable this feature. To disable the feature, set the `logEmptyRequests` parameter to `Ignore`. 

```shell-session
$ oc patch ingresscontroller default -n openshift-ingress-operator --type=merge -p '{"spec":{"logging":{"access":{"logEmptyRequests":"Ignore"}}}}'
```


**Additional resources**

  * [Capturing Original Client IP from the X-Forwarded-For Header in Ingress and Application Logs](https://access.redhat.com/solutions/7096271)



## 8.9.9. Set Ingress Controller thread count

A cluster administrator can set the thread count to increase the amount of incoming connections a cluster can handle. You can patch an existing Ingress Controller to increase the amount of threads. 

**Prerequisites**

  * The following assumes that you already created an Ingress Controller. 



**Procedure**

  * Update the Ingress Controller to increase the number of threads: 

```shell-session
$ oc -n openshift-ingress-operator patch ingresscontroller/default --type=merge -p '{"spec":{"tuningOptions": {"threadCount": 8}}}'
```


Note

If you have a node that is capable of running large amounts of resources, you can configure `spec.nodePlacement.nodeSelector` with labels that match the capacity of the intended node, and configure `spec.tuningOptions.threadCount` to an appropriately high value. 




## 8.9.10. Configure an Ingress Controller to use an internal load balancer

When creating an Ingress Controller on cloud platforms, the Ingress Controller is published by a public cloud load balancer by default. As an administrator, you can create an Ingress Controller that uses an internal cloud load balancer. 

Warning

If your cloud provider is Microsoft Azure, you must have at least one public load balancer that points to your nodes. If you do not, all of your nodes will lose egress connectivity to the internet. 

Important

If you want to change the `scope` for an `IngressController`, you can change the `.spec.endpointPublishingStrategy.loadBalancer.scope` parameter after the custom resource (CR) is created. 

**Figure 8.1. Diagram of LoadBalancer**

![OpenShift Container Platform Ingress LoadBalancerService endpoint publishing strategy](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Networking_Operators-en-US/images/b4b1d1d35869ccf8ab16c88a9c99ea7a/202_OpenShift_Ingress_0222_load_balancer.png) ![OpenShift Container Platform Ingress LoadBalancerService endpoint publishing strategy](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Networking_Operators-en-US/images/b4b1d1d35869ccf8ab16c88a9c99ea7a/202_OpenShift_Ingress_0222_load_balancer.png)

The preceding graphic shows the following concepts pertaining to OpenShift Container Platform Ingress LoadBalancerService endpoint publishing strategy: 

  * You can load balance externally, using the cloud provider load balancer, or internally, using the OpenShift Ingress Controller Load Balancer. 
  * You can use the single IP address of the load balancer and more familiar ports, such as 8080 and 4200 as shown on the cluster depicted in the graphic. 
  * Traffic from the external load balancer is directed at the pods, and managed by the load balancer, as depicted in the instance of a down node. See the [Kubernetes Services documentation](https://kubernetes.io/docs/concepts/services-networking/service/#internal-load-balancer) for implementation details. 



**Prerequisites**

  * Install the OpenShift CLI (`oc`). 
  * Log in as a user with `cluster-admin` privileges. 



**Procedure**

  1. Create an `IngressController` custom resource (CR) in a file named `<name>-ingress-controller.yaml`, such as in the following example: 

```yaml
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  namespace: openshift-ingress-operator
  name: <name>
spec:
  domain: <domain>
  endpointPublishingStrategy:
    type: LoadBalancerService
    loadBalancer:
      scope: Internal
```


where: 

`metadata.name`
     Specifies a name for the `IngressController` object. 
`spec.domain`
     Specifies the `domain` for the application published by the controller. 
`spec.endpointPublishingStrategy.loadBalancer.scope`
     Specifies a value of `Internal` to use an internal load balancer. 

  2. Create the Ingress Controller defined in the previous step by running the following command: 

```shell-session
$ oc create -f <name>-ingress-controller.yaml
```


where: 

`<name>`
     Specifies the name of the `IngressController` object. 

  3. Optional: Confirm that the Ingress Controller was created by running the following command: 

```shell-session
$ oc --all-namespaces=true get ingresscontrollers
```


## 8.9.11. Configure global access for an Ingress Controller on Google Cloud

To allow clients in any region of the same VPC to reach workloads behind an internal load balancer on Google Cloud, you can enable global access on an Ingress Controller in OpenShift Container Platform. 

For more information, see the Google Cloud documentation for [global access](https://cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing#global_access). 

**Prerequisites**

  * You deployed an OpenShift Container Platform cluster on Google Cloud infrastructure. 
  * You configured an Ingress Controller to use an internal load balancer. 
  * You installed the OpenShift CLI (`oc`). 



**Procedure**

  1. Configure the Ingress Controller resource to allow global access. 

Note

You can also create an Ingress Controller and specify the global access option. 

     1. Configure the Ingress Controller resource: 

```shell-session
$ oc -n openshift-ingress-operator edit ingresscontroller/default
```


     2. Edit the YAML file: 

**Sample`clientAccess` configuration set to `Global`**

```yaml
  spec:
    endpointPublishingStrategy:
      loadBalancer:
        providerParameters:
          gcp:
            clientAccess: Global
          type: GCP
        scope: Internal
      type: LoadBalancerService
```


     3. Save the file to apply the changes. 

  2. Run the following command to verify that the service allows global access: 

```shell-session
$ oc -n openshift-ingress edit svc/router-default -o yaml
```


The output shows that global access is enabled for Google Cloud with the annotation, `networking.gke.io/internal-load-balancer-allow-global-access`. 




## 8.9.12. Set the Ingress Controller health check interval

A cluster administrator can set the health check interval to define how long the router waits between two consecutive health checks. This value is applied globally as a default for all routes. The default value is 5 seconds. 

**Prerequisites**

  * The following assumes that you already created an Ingress Controller. 



**Procedure**

  * Update the Ingress Controller to change the interval between back end health checks: 

```shell-session
$ oc -n openshift-ingress-operator patch ingresscontroller/default --type=merge -p '{"spec":{"tuningOptions": {"healthCheckInterval": "8s"}}}'
```


Note

To override the `healthCheckInterval` for a single route, use the route annotation `router.openshift.io/haproxy.health.check.interval`




## 8.9.13. Configure the default Ingress Controller for your cluster to be internal

You can configure the `default` Ingress Controller for your cluster to be internal by deleting and recreating it. 

Warning

If your cloud provider is Microsoft Azure, you must have at least one public load balancer that points to your nodes. If you do not, all of your nodes will lose egress connectivity to the internet. 

Important

If you want to change the `scope` for an `IngressController`, you can change the `.spec.endpointPublishingStrategy.loadBalancer.scope` parameter after the custom resource (CR) is created. 

**Prerequisites**

  * Install the OpenShift CLI (`oc`). 
  * Log in as a user with `cluster-admin` privileges. 



**Procedure**

  1. Configure the `default` Ingress Controller for your cluster to be internal by deleting and recreating it. 

```shell-session
$ oc replace --force --wait --filename - <<EOF
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  namespace: openshift-ingress-operator
  name: default
spec:
  endpointPublishingStrategy:
    type: LoadBalancerService
    loadBalancer:
      scope: Internal
EOF
```


## 8.9.14. Configure the route admission policy

Administrators and application developers can run applications in multiple namespaces with the same domain name. This is for organizations where multiple teams develop microservices that are exposed on the same hostname. 

Warning

Allowing claims across namespaces should only be enabled for clusters with trust between namespaces, otherwise a malicious user could take over a hostname. For this reason, the default admission policy disallows hostname claims across namespaces. 

**Prerequisites**

  * Cluster administrator privileges. 



**Procedure**

  * Edit the `.spec.routeAdmission` field of the `ingresscontroller` resource variable using the following command: 

```shell-session
$ oc -n openshift-ingress-operator patch ingresscontroller/default --patch '{"spec":{"routeAdmission":{"namespaceOwnership":"InterNamespaceAllowed"}}}' --type=merge
```


**Sample Ingress Controller configuration**

```yaml
spec:
  routeAdmission:
    namespaceOwnership: InterNamespaceAllowed
...
```


Tip

You can alternatively apply the following YAML to configure the route admission policy: 

```yaml
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  name: default
  namespace: openshift-ingress-operator
spec:
  routeAdmission:
    namespaceOwnership: InterNamespaceAllowed
```


## 8.9.15. Use wildcard routes

The HAProxy Ingress Controller has support for wildcard routes. The Ingress Operator uses `wildcardPolicy` to configure the `ROUTER_ALLOW_WILDCARD_ROUTES` environment variable of the Ingress Controller. 

The default behavior of the Ingress Controller is to admit routes with a wildcard policy of `None`, which is backwards compatible with existing `IngressController` resources. 

**Procedure**

  1. Configure the wildcard policy. 

     1. Use the following command to edit the `IngressController` resource: 

```shell-session
$ oc edit IngressController
```


     2. Under `spec`, set the `wildcardPolicy` field to `WildcardsDisallowed` or `WildcardsAllowed`: 

```yaml
spec:
  routeAdmission:
    wildcardPolicy: WildcardsDisallowed # or WildcardsAllowed
```


## 8.9.16. HTTP header configuration

To customize request and response headers for your applications, configure the Ingress Controller or apply specific route annotations. Understanding the interaction between these configuration methods ensures you effectively manage global and route-specific header policies. 

You can also set certain headers by using route annotations. The various ways of configuring headers can present challenges when working together. 

Note

You can only set or delete headers within an `IngressController` or `Route` CR, you cannot append them. If an HTTP header is set with a value, that value must be complete and not require appending in the future. In situations where it makes sense to append a header, such as the X-Forwarded-For header, use the `spec.httpHeaders.forwardedHeaderPolicy` field, instead of `spec.httpHeaders.actions`. 

Order of precedence
    

When the same HTTP header is modified both in the Ingress Controller and in a route, HAProxy prioritizes the actions in certain ways depending on whether it is a request or response header. 

  * For HTTP response headers, actions specified in the Ingress Controller are executed after the actions specified in a route. This means that the actions specified in the Ingress Controller take precedence. 
  * For HTTP request headers, actions specified in a route are executed after the actions specified in the Ingress Controller. This means that the actions specified in the route take precedence. 



For example, a cluster administrator sets the X-Frame-Options response header with the value `DENY` in the Ingress Controller using the following configuration: 

**Example`IngressController` spec**

```yaml
apiVersion: operator.openshift.io/v1
kind: IngressController
# ...
spec:
  httpHeaders:
    actions:
      response:
      - name: X-Frame-Options
        action:
          type: Set
          set:
            value: DENY
```


A route owner sets the same response header that the cluster administrator set in the Ingress Controller, but with the value `SAMEORIGIN` using the following configuration: 

**Example`Route` spec**

```yaml
apiVersion: route.openshift.io/v1
kind: Route
# ...
spec:
  httpHeaders:
    actions:
      response:
      - name: X-Frame-Options
        action:
          type: Set
          set:
            value: SAMEORIGIN
```


When both the `IngressController` spec and `Route` spec are configuring the X-Frame-Options response header, then the value set for this header at the global level in the Ingress Controller takes precedence, even if a specific route allows frames. For a request header, the `Route` spec value overrides the `IngressController` spec value. 

This prioritization occurs because the `haproxy.config` file uses the following logic, where the Ingress Controller is considered the front end and individual routes are considered the back end. The header value `DENY` applied to the front end configurations overrides the same header with the value `SAMEORIGIN` that is set in the back end: 

```plaintext
frontend public
  http-response set-header X-Frame-Options 'DENY'

frontend fe_sni
  http-response set-header X-Frame-Options 'DENY'

frontend fe_no_sni
  http-response set-header X-Frame-Options 'DENY'

backend be_secure:openshift-monitoring:alertmanager-main
  http-response set-header X-Frame-Options 'SAMEORIGIN'
```


Additionally, any actions defined in either the Ingress Controller or a route override values set using route annotations. 

Special case headers
     The following headers are either prevented entirely from being set or deleted, or allowed under specific circumstances: 

Table 8.2. Special case header configuration optionsHeader name| Configurable using `IngressController` spec| Configurable using `Route` spec| Reason for disallowment| Configurable using another method  
---|---|---|---|---  
`proxy` |  No  |  No  |  The `proxy` HTTP request header can be used to exploit vulnerable CGI applications by injecting the header value into the `HTTP_PROXY` environment variable. The `proxy` HTTP request header is also non-standard and prone to error during configuration.  |  No   
`host` |  No  |  Yes  |  When the `host` HTTP request header is set using the `IngressController` CR, HAProxy can fail when looking up the correct route.  |  No   
`strict-transport-security` |  No  |  No  |  The `strict-transport-security` HTTP response header is already handled using route annotations and does not need a separate implementation.  |  Yes: the `haproxy.router.openshift.io/hsts_header` route annotation   
`cookie` and `set-cookie` |  No  |  No  |  The cookies that HAProxy sets are used for session tracking to map client connections to particular back-end servers. Allowing these headers to be set could interfere with HAProxy’s session affinity and restrict HAProxy’s ownership of a cookie.  |  Yes: 

  * the `haproxy.router.openshift.io/disable_cookie` route annotation 
  * the `haproxy.router.openshift.io/cookie_name` route annotation 

  
Show more

## 8.9.17. Set or delete HTTP request and response headers in an Ingress Controller

To set or delete HTTP request and response headers on routes in OpenShift Container Platform, you can configure header actions on an Ingress Controller. You can apply the actions to all routes that the controller serves or to specific routes. 

For example, you might want to migrate an application running on your cluster to use mutual TLS, which requires that your application checks for an X-Forwarded-Client-Cert request header, but the OpenShift Container Platform default Ingress Controller provides an X-SSL-Client-Der request header. 

The following procedure modifies the Ingress Controller to set the X-Forwarded-Client-Cert request header, and delete the X-SSL-Client-Der request header. 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 
  * You have access to an OpenShift Container Platform cluster as a user with the `cluster-admin` role. 



**Procedure**

  1. Edit the Ingress Controller resource: 

```shell-session
$ oc -n openshift-ingress-operator edit ingresscontroller/default
```


  2. Replace the X-SSL-Client-Der HTTP request header with the X-Forwarded-Client-Cert HTTP request header: 

```yaml
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  name: default
  namespace: openshift-ingress-operator
spec:
  httpHeaders:
    actions:
      request:
      - name: X-Forwarded-Client-Cert
        action:
          type: Set
          set:
           value: "%{+Q}[ssl_c_der,base64]"
      - name: X-SSL-Client-Der
        action:
          type: Delete
```


where: 

`spec.httpHeaders.actions`
     Specifies the list of actions you want to perform on the HTTP headers. 
`spec.httpHeaders.actions.request`
     Specifies the type of header you want to change. In this case, a request header. 
`spec.httpHeaders.actions.request.name`
     Specifies the name of the header you want to change. For a list of available headers you can set or delete, see _HTTP header configuration_. 
`spec.httpHeaders.actions.request.action.type`
     Specifies the type of action being taken on the header. This field can have the value `Set` or `Delete`. 
`spec.httpHeaders.actions.request.action.set.value`
    

Specifies a `value` when setting HTTP headers. The value can be a string from a list of available directives for that header, for example `DENY`, or it can be a dynamic value that will be interpreted using HAProxy’s dynamic value syntax. In this case, a dynamic value is added. 

Note

For setting dynamic header values for HTTP responses, allowed sample fetchers are `res.hdr` and `ssl_c_der`. For setting dynamic header values for HTTP requests, allowed sample fetchers are `req.hdr` and `ssl_c_der`. Both request and response dynamic values can use the `lower` and `base64` converters. 

  3. Save the file to apply the changes. 



## 8.9.18. Use X-Forwarded headers

To control how the HAProxy Ingress Controller handles `Forwarded` and `X-Forwarded-For` headers in OpenShift Container Platform, you can set the `HTTPHeaders` policy on an Ingress Controller. The Ingress Operator configures the `ROUTER_SET_FORWARDED_HEADERS` environment variable from that field. 

**Procedure**

  1. Configure the `HTTPHeaders` field for the Ingress Controller. 

     1. Use the following command to edit the `IngressController` resource: 

```shell-session
$ oc edit IngressController
```


     2. Under `spec`, set the `HTTPHeaders` policy field to `Append`, `Replace`, `IfNone`, or `Never`: 

```yaml
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  name: default
  namespace: openshift-ingress-operator
spec:
  httpHeaders:
    forwardedHeaderPolicy: Append
```


### 8.9.18.1. Example use cases for X-Forwarded headers

You can use X-Forwarded header policies on an Ingress Controller or route in OpenShift Container Platform to preserve headers from an external proxy or to set headers for internal cluster requests. 

**As a cluster administrator, you can:**

  * Configure an external proxy that injects the `X-Forwarded-For` header into each request before forwarding it to an Ingress Controller. 

To configure the Ingress Controller to pass the header through unmodified, you specify the `never` policy. The Ingress Controller then never sets the headers, and applications receive only the headers that the external proxy provides. 

  * Configure the Ingress Controller to pass the `X-Forwarded-For` header that your external proxy sets on external cluster requests through unmodified. 

To configure the Ingress Controller to set the `X-Forwarded-For` header on internal cluster requests, which do not go through the external proxy, specify the `if-none` policy. If an HTTP request already has the header set through the external proxy, then the Ingress Controller preserves it. If the header is absent because the request did not come through the proxy, then the Ingress Controller adds the header. 




**As an application developer, you can:**

  * Configure an application-specific external proxy that injects the `X-Forwarded-For` header. 

To configure an Ingress Controller to pass the header through unmodified for an application’s Route, without affecting the policy for other Routes, add an annotation `haproxy.router.openshift.io/set-forwarded-headers: if-none` or `haproxy.router.openshift.io/set-forwarded-headers: never` on the Route for the application. 

Note

You can set the `haproxy.router.openshift.io/set-forwarded-headers` annotation on a per route basis, independent from the globally set value for the Ingress Controller. 




## 8.9.19. Enable or disable HTTP/2 on Ingress Controllers

You can enable or disable transparent end-to-end HTTP/2 connectivity in HAProxy. Application owners can use HTTP/2 protocol capabilities, including single connection, header compression, binary streams, and more. 

You can enable or disable HTTP/2 connectivity for an individual Ingress Controller or for the entire cluster. 

Note

If you enable or disable HTTP/2 connectivity for an individual Ingress Controller and for the entire cluster, the HTTP/2 configuration for the Ingress Controller takes precedence over the HTTP/2 configuration for the cluster. 

To enable the use of HTTP/2 for a connection from the client to an HAProxy instance, a route must specify a custom certificate. A route that uses the default certificate cannot use HTTP/2. This restriction is necessary to avoid problems from connection coalescing, where the client re-uses a connection for different routes that use the same certificate. 

Consider the following use cases for an HTTP/2 connection for each route type: 

  * For a re-encrypt route, the connection from HAProxy to the application pod can use HTTP/2 if the application supports using Application-Level Protocol Negotiation (ALPN) to negotiate HTTP/2 with HAProxy. You cannot use HTTP/2 with a re-encrypt route unless the Ingress Controller has HTTP/2 enabled. 
  * For a passthrough route, the connection can use HTTP/2 if the application supports using ALPN to negotiate HTTP/2 with the client. You can use HTTP/2 with a passthrough route if the Ingress Controller has HTTP/2 enabled or disabled. 
  * For an edge-terminated secure route, the connection uses HTTP/2 if the service specifies only `appProtocol: kubernetes.io/h2c`. You can use HTTP/2 with an edge-terminated secure route if the Ingress Controller has HTTP/2 enabled or disabled. 
  * For an insecure route, the connection uses HTTP/2 if the service specifies only `appProtocol: kubernetes.io/h2c`. You can use HTTP/2 with an insecure route if the Ingress Controller has HTTP/2 enabled or disabled. 



Important

For non-passthrough routes, the Ingress Controller negotiates its connection to the application independently of the connection from the client. This means a client might connect to the Ingress Controller and negotiate HTTP/1.1. The Ingress Controller might then connect to the application, negotiate HTTP/2, and forward the request from the client HTTP/1.1 connection by using the HTTP/2 connection to the application. 

This sequence of events causes an issue if the client subsequently tries to upgrade its connection from HTTP/1.1 to the WebSocket protocol. Consider that if you have an application that is intending to accept WebSocket connections, and the application attempts to allow for HTTP/2 protocol negotiation, the client fails any attempt to upgrade to the WebSocket protocol. 

### 8.9.19.1. Enable HTTP/2

To enable HTTP/2 for Ingress Controllers in OpenShift Container Platform, you can annotate a specific Ingress Controller or the cluster Ingress configuration. 

**Procedure**

  * To enable HTTP/2 on a specific Ingress Controller, enter the `oc annotate` command: 

```shell-session
$ oc -n openshift-ingress-operator annotate ingresscontrollers/<ingresscontroller_name> ingress.operator.openshift.io/default-enable-http2=true
```


Replace `<ingresscontroller_name>` with the name of an Ingress Controller to enable HTTP/2. 

  * To enable HTTP/2 for the entire cluster, enter the `oc annotate` command: 

```shell-session
$ oc annotate ingresses.config/cluster ingress.operator.openshift.io/default-enable-http2=true
```


  * Alternatively, apply the following YAML to enable HTTP/2: 

```yaml
apiVersion: config.openshift.io/v1
kind: Ingress
metadata:
  name: cluster
  annotations:
    ingress.operator.openshift.io/default-enable-http2: "true"
```


### 8.9.19.2. Disable HTTP/2

To disable HTTP/2 for Ingress Controllers in OpenShift Container Platform, you can annotate a specific Ingress Controller or the cluster Ingress configuration. 

**Procedure**

  * To disable HTTP/2 on a specific Ingress Controller, enter the `oc annotate` command: 

```shell-session
$ oc -n openshift-ingress-operator annotate ingresscontrollers/<ingresscontroller_name> ingress.operator.openshift.io/default-enable-http2=false
```


Replace `<ingresscontroller_name>` with the name of an Ingress Controller to disable HTTP/2. 

  * To disable HTTP/2 for the entire cluster, enter the `oc annotate` command: 

```shell-session
$ oc annotate ingresses.config/cluster ingress.operator.openshift.io/default-enable-http2=false
```


  * Alternatively, apply the following YAML to disable HTTP/2: 

```yaml
apiVersion: config.openshift.io/v1
kind: Ingress
metadata:
  name: cluster
  annotations:
    ingress.operator.openshift.io/default-enable-http2: "false"
```


## 8.9.20. Configure the PROXY protocol for an Ingress Controller

To preserve original client addresses for connections to an Ingress Controller in OpenShift Container Platform, you can configure the PROXY protocol when you use the HostNetwork, NodePortService, or Private endpoint publishing strategy. 

Warning

The default Ingress Controller with installer-provisioned clusters on non-cloud platforms that use a Keepalived Ingress Virtual IP (VIP) do not support the PROXY protocol. 

The PROXY protocol enables the load balancer to preserve the original client addresses for connections that the Ingress Controller receives. The original client addresses are useful for logging, filtering, and injecting HTTP headers. In the default configuration, the connections that the Ingress Controller receives contain only the source IP address that is associated with the load balancer. 

Important

For a passthrough route configuration, servers in OpenShift Container Platform clusters cannot observe the original client source IP address. If you need to know the original client source IP address, configure Ingress access logging for your Ingress Controller so that you can view the client source IP addresses. 

For re-encrypt and edge routes, the OpenShift Container Platform router sets the `Forwarded` and `X-Forwarded-For` headers so that application workloads check the client source IP address. 

For more information about Ingress access logging, see "Configuring Ingress access logging". 

Configuring the PROXY protocol for an Ingress Controller is not supported when using the `LoadBalancerService` endpoint publishing strategy type. This restriction is because when OpenShift Container Platform runs in a cloud platform, and an Ingress Controller specifies that a service load balancer should be used, the Ingress Operator configures the load balancer service and enables the PROXY protocol based on the platform requirement for preserving source addresses. 

Important

You must configure both OpenShift Container Platform and the external load balancer to use either the PROXY protocol or TCP. 

This feature is not supported in cloud deployments. This restriction is because when OpenShift Container Platform runs in a cloud platform, and an Ingress Controller specifies that a service load balancer should be used, the Ingress Operator configures the load balancer service and enables the PROXY protocol based on the platform requirement for preserving source addresses. 

Important

You must configure both OpenShift Container Platform and the external load balancer to either use the PROXY protocol or to use Transmission Control Protocol (TCP). 

**Prerequisites**

  * You created an Ingress Controller. 



**Procedure**

  1. Edit the Ingress Controller resource by entering the following command in your CLI: 

```shell-session
$ oc -n openshift-ingress-operator edit ingresscontroller/default
```


  2. Set the PROXY configuration: 

     * If your Ingress Controller uses the `HostNetwork` endpoint publishing strategy type, set the `spec.endpointPublishingStrategy.hostNetwork.protocol` subfield to `PROXY`: 

**Sample`hostNetwork` configuration to `PROXY`**

```yaml
# ...
  spec:
    endpointPublishingStrategy:
      hostNetwork:
        protocol: PROXY
      type: HostNetwork
# ...
```


     * If your Ingress Controller uses the `NodePortService` endpoint publishing strategy type, set the `spec.endpointPublishingStrategy.nodePort.protocol` subfield to `PROXY`: 

**Sample`nodePort` configuration to `PROXY`**

```yaml
# ...
  spec:
    endpointPublishingStrategy:
      nodePort:
        protocol: PROXY
      type: NodePortService
# ...
```


     * If your Ingress Controller uses the `Private` endpoint publishing strategy type, set the `spec.endpointPublishingStrategy.private.protocol` subfield to `PROXY`: 

**Sample`private` configuration to `PROXY`**

```yaml
# ...
  spec:
    endpointPublishingStrategy:
      private:
        protocol: PROXY
    type: Private
# ...
```


**Additional resources**

  * [Configuring Ingress access logging](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking_operators/configuring-ingress#nw-configure-ingress-access-logging_configuring-ingress "8.9.8. Configure Ingress access logging")



## 8.9.21. Specify an alternative cluster domain using the appsDomain option

As a cluster administrator, you can specify an alternative to the default cluster domain for user-created routes by configuring the `appsDomain` field. 

The `appsDomain` field is an optional domain for OpenShift Container Platform to use instead of the default, which is specified in the `domain` field. If you specify an alternative domain, it overrides the default cluster domain for the purpose of determining the default host for a new route. 

For example, you can use the DNS domain for your company as the default domain for routes and ingresses for applications running on your cluster. 

**Prerequisites**

  * You deployed an OpenShift Container Platform cluster. 
  * You installed the `oc` command-line interface. 



**Procedure**

  1. Configure the `appsDomain` field by specifying an alternative default domain for user-created routes. 

     1. Edit the ingress `cluster` resource: 

```shell-session
$ oc edit ingresses.config/cluster -o yaml
```


     2. Edit the YAML file: 

**Sample`appsDomain` configuration to `test.example.com`**

```yaml
apiVersion: config.openshift.io/v1
kind: Ingress
metadata:
  name: cluster
spec:
  domain: apps.example.com
  appsDomain: <test.example.com>
```


where: 

`spec.domain`
     Specifies the default domain. You cannot modify the default domain after installation. 
`spec.appsDomain`
     Specifies the domain for OpenShift Container Platform infrastructure to use for application routes. Instead of the default prefix, `apps`, you can use an alternative prefix like `test`. This field is optional. 

  2. Verify that an existing route contains the domain name specified in the `appsDomain` field by exposing the route and verifying the route domain change: 

Note

Wait for the `openshift-apiserver` finish rolling updates before exposing the route. 

     1. Expose the route by entering the following command. The command outputs `route.route.openshift.io/hello-openshift exposed` to designate exposure of the route. 

```shell-session
$ oc expose service hello-openshift
```


     2. Get a list of routes by running the following command: 

```shell-session
$ oc get routes
```


**Example output**

```plaintext
NAME              HOST/PORT                                   PATH   SERVICES          PORT       TERMINATION   WILDCARD
hello-openshift   hello_openshift-<my_project>.test.example.com
hello-openshift   8080-tcp                 None
```


## 8.9.22. Convert HTTP header case

To keep HTTP header name capitalization for applications that require it in OpenShift Container Platform, you can configure header name case adjustments on an Ingress Controller. 

Important

OpenShift Container Platform includes HAProxy 2.8. If you want to update to this version of the web-based load balancer, ensure that you add the `spec.httpHeaders.headerNameCaseAdjustments` section to your cluster’s configuration file. 

As a cluster administrator, you can convert the HTTP header case by entering the `oc patch` command or by setting the `HeaderNameCaseAdjustments` field in the Ingress Controller YAML file. 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 
  * You have access to the cluster as a user with the `cluster-admin` role. 



**Procedure**

  * Capitalize an HTTP header by using the `oc patch` command. 

    1. Change the HTTP header from `host` to `Host` by running the following command: 

```shell-session
$ oc -n openshift-ingress-operator patch ingresscontrollers/default --type=merge --patch='{"spec":{"httpHeaders":{"headerNameCaseAdjustments":["Host"]}}}'
```


    2. Create a `Route` resource YAML file so that the annotation can be applied to the application. 

**Example of a route named`my-application`**

```yaml
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  annotations:
    haproxy.router.openshift.io/h1-adjust-case: true
  name: <application_name>
  namespace: <application_name>
# ...
```


You must set `haproxy.router.openshift.io/h1-adjust-case` to `true` so that the Ingress Controller can adjust the `host` request header as specified. 

  * Specify adjustments by configuring the `HeaderNameCaseAdjustments` field in the Ingress Controller YAML configuration file. 

    1. The following example Ingress Controller YAML file adjusts the `host` header to `Host` for HTTP/1 requests to appropriately annotated routes: 

**Example Ingress Controller YAML**

```yaml
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  name: default
  namespace: openshift-ingress-operator
spec:
  httpHeaders:
    headerNameCaseAdjustments:
    - Host
```


    2. The following example route enables HTTP response header name case adjustments by using the `haproxy.router.openshift.io/h1-adjust-case` annotation: 

**Example route YAML**

```yaml
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  annotations:
    haproxy.router.openshift.io/h1-adjust-case: true
  name: my-application
  namespace: my-application
spec:
  to:
    kind: Service
    name: my-application
```


Set `haproxy.router.openshift.io/h1-adjust-case` to `true`. 




## 8.9.23. Use router compression

You configure the HAProxy Ingress Controller to specify router compression globally for specific MIME types. 

You can use the `mimeTypes` variable to define the formats of MIME types to which compression is applied. The types are: application, image, message, multipart, text, video, or a custom type prefaced by "X-". To see the full notation for MIME types and subtypes, see [RFC1341](https://datatracker.ietf.org/doc/html/rfc1341#page-7). 

Note

Memory allocated for compression can affect the max connections. Additionally, compression of large buffers can cause latency, like heavy regex or long lists of regex. 

Not all MIME types benefit from compression, but HAProxy still uses resources to try to compress if instructed to. Generally, text formats, such as html, css, and js, formats benefit from compression, but formats that are already compressed, such as image, audio, and video, benefit little in exchange for the time and resources spent on compression. 

**Procedure**

  1. Configure the `httpCompression` field for the Ingress Controller. 

     1. Use the following command to edit the `IngressController` resource: 

```shell-session
$ oc edit -n openshift-ingress-operator ingresscontrollers/default
```


     2. Under `spec`, set the `httpCompression` policy field to `mimeTypes` and specify a list of MIME types that should have compression applied: 

```yaml
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  name: default
  namespace: openshift-ingress-operator
spec:
  httpCompression:
    mimeTypes:
    - "text/html"
    - "text/css; charset=utf-8"
    - "application/json"
   ...
```


## 8.9.24. Expose router metrics

You can retrieve Prometheus-format HAProxy ingress router metrics from port `1936` to monitor ingress load and troubleshoot routing behavior. By analyzing these metrics, you can identify capacity bottlenecks and determine when to scale your router deployment. 

**Prerequisites**

  * You have cluster administrator access to the cluster. 
  * You configured your firewall to allow port `1936`. 



Note

The Prometheus `/metrics` endpoint and the HAProxy HTML statistics dashboard are mutually exclusive exposition modes because the HAProxy router process serves one mode at a time. The Ingress Operator configures default Ingress Controller pods for Prometheus scraping (`/metrics` on port `1936`). Browsing `http://<user>:<password>@<pod_IP>:1936/` for interactive HTML statistics is not supported concurrently with Prometheus metrics on deployments that the Ingress Operator configures in this manner. 

**Procedure**

  1. List the router pods in the ingress namespace by entering the following command: 

```shell-session
$ oc get pods -n openshift-ingress
```


**Example output**

```shell-session
NAME                               READY   STATUS    RESTARTS   AGE
router-default-76bfffb66c-46qwp   1/1     Running   0          11h
```


  2. Read the stats user from the router pod under `/var/lib/haproxy/conf/metrics-auth/` by entering the following command: 

```shell-session
$ oc rsh <router_pod_name> cat /var/lib/haproxy/conf/metrics-auth/statsUsername
```


  3. Read the stats password from the router pod under `/var/lib/haproxy/conf/metrics-auth/` by entering the following command: 

```shell-session
$ oc rsh <router_pod_name> cat /var/lib/haproxy/conf/metrics-auth/statsPassword
```


  4. Get pod details, including the IP address for the pod, by entering the following command: 

```shell-session
$ oc describe pod <router_pod>
```


  5. Fetch Prometheus text metrics from the default port `1936` by entering the following command: 

```shell-session
$ curl -u <user>:<password> http://<router_IP>:1936/metrics
```


If the stats endpoint serves TLS-protected Prometheus text, retrieve metrics over HTTPS instead by entering the following command: 

```shell-session
$ curl -u <user>:<password> https://<router_IP>:1936/metrics -k
```


**Example output**

```shell-session
...
# HELP haproxy_max_connections Hard limit on the number of connections (configured or imposed by ulimit -n).
# TYPE haproxy_max_connections gauge
haproxy_max_connections 50000
...
```


  6. Optional: In the OpenShift Container Platform web console, navigate to **Observe** **Metrics** , or query Prometheus directly, to compare ingress load against the HAProxy allowance. 

The `haproxy_max_connections` gauge reflects each scraped router endpoint’s HAProxy allowance from `spec.tuningOptions.maxConnections` on the `IngressController`, bound by operating system limits such as `ulimit -n`. Before relying on ratios, confirm the labeled metric for front-end sessions that your HAProxy Prometheus exporter emits. For example, use `haproxy_frontend_current_sessions` when that series is available for your deployment. 

Expressions similar to `sum(haproxy_frontend_current_sessions) / sum(haproxy_max_connections)` can estimate connection load across scrape targets after you verify those series for your deployment. 

If the ratio approaches `1`, adjust `spec.tuningOptions.maxConnections` on the `IngressController` or scale the router deployment. 




## 8.9.25. Customize HAProxy error code response pages

To customize HAProxy 503 or 404 error pages for the Ingress router in OpenShift Container Platform, you can provide custom pages in a config map and patch the Ingress Controller. 

Custom error code response pages are specified in a config map then patched to the Ingress Controller. The config map keys have two available file names as follows: `error-page-503.http` and `error-page-404.http`. 

Custom HTTP error code response pages must follow the [HAProxy HTTP error page configuration guidelines](https://www.haproxy.com/documentation/hapee/latest/configuration/config-sections/http-errors/). Here is an example of the default OpenShift Container Platform HAProxy router [http 503 error code response page](https://raw.githubusercontent.com/openshift/router/master/images/router/haproxy/conf/error-page-503.http). You can use the default content as a template for creating your own custom page. 

By default, the HAProxy router serves only a 503 error page when the application is not running or when the route is incorrect or non-existent. This default behavior is the same as the behavior on OpenShift Container Platform 4.8 and earlier. If a config map for the customization of an HTTP error code response is not provided, and you are using a custom HTTP error code response page, the router serves a default 404 or 503 error code response page. 

Note

If you use the OpenShift Container Platform default 503 error code page as a template for your customizations, the headers in the file require an editor that can use CRLF line endings. 

**Procedure**

  1. Create a config map named `my-custom-error-code-pages` in the `openshift-config` namespace: 

```shell-session
$ oc -n openshift-config create configmap my-custom-error-code-pages \
  --from-file=error-page-503.http \
  --from-file=error-page-404.http
```


Important

If you do not specify the correct format for the custom error code response page, a router pod outage occurs. To resolve this outage, you must delete or correct the config map and delete the affected router pods so they can be recreated with the correct information. 

  2. Patch the Ingress Controller to reference the `my-custom-error-code-pages` config map by name: 

```shell-session
$ oc patch -n openshift-ingress-operator ingresscontroller/default --patch '{"spec":{"httpErrorCodePages":{"name":"my-custom-error-code-pages"}}}' --type=merge
```


The Ingress Operator copies the `my-custom-error-code-pages` config map from the `openshift-config` namespace to the `openshift-ingress` namespace. The Operator names the config map according to the pattern, `<your_ingresscontroller_name>-errorpages`, in the `openshift-ingress` namespace. 

  3. Display the copy: 

```shell-session
$ oc get cm default-errorpages -n openshift-ingress
```


**Example output**

```plaintext
NAME                       DATA   AGE
default-errorpages         2      25s
```


The example config map name is `default-errorpages` because the `default` Ingress Controller custom resource (CR) was patched. 

  4. Confirm that the config map containing the custom error response page mounts on the router volume where the config map key is the filename that has the custom HTTP error code response: 

     * For 503 custom HTTP custom error code response: 

```shell-session
$ oc -n openshift-ingress rsh <router_pod> cat /var/lib/haproxy/conf/error_code_pages/error-page-503.http
```


     * For 404 custom HTTP custom error code response: 

```shell-session
$ oc -n openshift-ingress rsh <router_pod> cat /var/lib/haproxy/conf/error_code_pages/error-page-404.http
```


**Verification**

Verify your custom error code HTTP response: 

  1. Create a test project and application: 

```shell-session
$ oc new-project test-ingress
```


```shell-session
$ oc new-app django-psql-example
```


  2. For 503 custom http error code response: 

     1. Stop all the pods for the application. 
     2. Run the following curl command or visit the route hostname in the browser: 

```shell-session
$ curl -vk <route_hostname>
```


  3. For 404 custom http error code response: 

     1. Visit a non-existent route or an incorrect route. 
     2. Run the following curl command or visit the route hostname in the browser: 

```shell-session
$ curl -vk <route_hostname>
```


  4. Check if the `errorfile` attribute is properly in the `haproxy.config` file: 

```shell-session
$ oc -n openshift-ingress rsh <router> cat /var/lib/haproxy/conf/haproxy.config | grep errorfile
```


## 8.9.26. Set the Ingress Controller maximum connections

A cluster administrator can set the maximum number of simultaneous connections for OpenShift router deployments. You can patch an existing Ingress Controller to increase the maximum number of connections. 

**Prerequisites**

  * The following assumes that you already created an Ingress Controller 



**Procedure**

  * Update the Ingress Controller to change the maximum number of connections for HAProxy: 

```shell-session
$ oc -n openshift-ingress-operator patch ingresscontroller/default --type=merge -p '{"spec":{"tuningOptions": {"maxConnections": 7500}}}'
```


Warning

If you set the `spec.tuningOptions.maxConnections` value greater than the current operating system limit, the HAProxy process will not start. See the table in the "Ingress Controller configuration parameters" section for more information about this parameter.
