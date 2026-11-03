# 2.3. Configuring ingress cluster traffic by using an Ingress Controller

You can use the Ingress Controller to control how external users communicate with services that run inside the cluster. 

Before you begin any of the procedures that are listed in the Configuring ingress cluster traffic by using an Ingress Controller document, ensure that you meet the following prerequisites. A cluster administrator performs these prerequisites: 

  * Set up the external port to the cluster networking environment so that requests can reach the cluster. 
  * Make sure there is at least one user with cluster admin role. To add this role to a user, run the following command: 

```shell-session
$ oc adm policy add-cluster-role-to-user cluster-admin username
```


  * You have an OpenShift Container Platform cluster with at least one master and at least one node and a system outside the cluster that has network access to the cluster. This procedure assumes that the external system is on the same subnet as the cluster. The additional networking required for external systems on a different subnet is out-of-scope for this topic. 



## 2.3.1. Use Ingress Controllers and routes

You can use the Ingress Controller to allow external access to an OpenShift Container Platform cluster. The Ingress Operator manages Ingress Controllers and wildcard DNS. 

An Ingress Controller is configured to accept external requests and proxy them based on the configured routes. This is limited to HTTP, HTTPS using SNI, and TLS using SNI, which is sufficient for web applications and services that work over TLS with SNI. 

Work with your administrator to configure an Ingress Controller to accept external requests and proxy them based on the configured routes. 

The administrator can create a wildcard DNS entry and then set up an Ingress Controller. Then, you can work with the edge Ingress Controller without having to contact the administrators. 

By default, every Ingress Controller in the cluster can admit any route created in any project in the cluster. The Ingress Controller has the following characteristics: 

  * Has two replicas by default, which means it should be running on two compute nodes. 
  * Can be scaled up to have more replicas on more nodes. 



## 2.3.2. Creating a project and service

If the project and service that you want to expose does not exist, create the project and then create the service. 

If the project and service already exists, skip to the procedure on exposing the service to create a route. 

**Prerequisites**

  * Install the OpenShift CLI (`oc`) and log in as a cluster administrator. 



**Procedure**

  1. Create a new project for your service by running the `oc new-project` command: 

```shell-session
$ oc new-project <project_name>
```


  2. Use the `oc new-app` command to create your service: 

```shell-session
$ oc new-app nodejs:12~https://github.com/sclorg/nodejs-ex.git
```


  3. To verify that the service was created, run the following command: 

```shell-session
$ oc get svc -n <project_name>
```


**Example output**

```shell-session
NAME        TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
nodejs-ex   ClusterIP   172.30.197.157   <none>        8080/TCP   70s
```


Note

By default, the new service does not have an external IP address. 




## 2.3.3. Exposing the service by creating a route

To enable external access to your application that runs on OpenShift Container Platform, you can expose the service as a route by using the `oc expose` command. 

**Prerequisites**

  * You logged into OpenShift Container Platform. 



**Procedure**

  1. Log in to the project where the service you want to expose is located: 

```shell-session
$ oc project <project_name>
```


  2. Run the `oc expose service` command to expose the route: 

```shell-session
$ oc expose service nodejs-ex
```


**Example output**

```shell-session
route.route.openshift.io/nodejs-ex exposed
```


  3. To verify that the service is exposed, you can use a tool, such as `curl` to check that the service is accessible from outside the cluster. 

     1. To find the hostname of the route, enter the following command: 

```shell-session
$ oc get route
```


**Example output**

```shell-session
NAME        HOST/PORT                        PATH   SERVICES    PORT       TERMINATION   WILDCARD
nodejs-ex   nodejs-ex-myproject.example.com         nodejs-ex   8080-tcp                 None
```


     2. To check that the host responds to a GET request, enter the following command: 

**Example`curl` command**

```shell-session
$ curl --head nodejs-ex-myproject.example.com
```


**Example output**

```shell-session
HTTP/1.1 200 OK
...
```


## 2.3.4. Ingress sharding in OpenShift Container Platform

To optimise routing performance in OpenShift Container Platform, create shards so that you can load balance incoming traffic across multiple Ingress Controllers. 

In OpenShift Container Platform, an Ingress Controller can serve all routes, or it can serve a subset of routes. By default, the Ingress Controller serves any route created in any namespace of the cluster. You can add additional Ingress Controllers to your cluster to optimize routing by creating shards, which are subsets of routes based on selected characteristics. To mark a route as a member of a shard, use labels in the route or namespace `metadata` field. The Ingress Controller uses _selectors_ , also known as a _selection expression_ , to select a subset of routes from the entire pool of routes to serve. 

You can also use Ingress sharding when you want to isolate traffic so that the traffic can route to a specific Ingress Controller. 

By default, each route uses the default domain of the cluster. However, routes can be configured to use the domain of the router instead. 

## 2.3.5. Ingress Controller sharding

You can use Ingress sharding, also known as _router sharding_ , to distribute a set of routes across multiple routers by adding labels to routes, namespaces, or both. 

The Ingress Controller uses a corresponding set of selectors to admit only the routes that have a specified label. Each Ingress shard comprises the routes that are filtered by using a given selection expression. 

As the primary mechanism for traffic to enter the cluster, the demands on the Ingress Controller can be significant. As a cluster administrator, you can shard the routes to the following components: 

  * Balance Ingress Controllers, or routers, with several routes to accelerate responses to changes. 
  * Assign certain routes to have different reliability guarantees than other routes. 
  * Allow certain Ingress Controllers to have different policies defined. 
  * Allow only specific routes to use additional features. 
  * Expose different routes on different addresses so that internal and external users can see different routes, for example. 
  * Transfer traffic from one version of an application to another during a blue-green deployment. 



When Ingress Controllers are sharded, a given route is admitted to zero or more Ingress Controllers in the group. The status of a route describes whether an Ingress Controller has admitted the route. An Ingress Controller only admits a route if the route is unique to a shard. 

With sharding, you can distribute subsets of routes over multiple Ingress Controllers. These subsets can be nonoverlapping, also called _traditional_ sharding, or overlapping, otherwise known as _overlapped_ sharding. 

The following table outlines three sharding methods: 

Sharding method| Description  
---|---  
Namespace selector  |  After you add a namespace selector to the Ingress Controller, all routes in a namespace that have matching labels for the namespace selector are included in the Ingress shard. Consider this method when an Ingress Controller serves all routes created in a namespace.   
Route selector  |  After you add a route selector to the Ingress Controller, all routes with labels that match the route selector are included in the Ingress shard. Consider this method when you want an Ingress Controller to serve only a subset of routes or a specific route in a namespace.   
Namespace and route selectors  |  Provides your Ingress Controller scope for both namespace selector and route selector methods. Consider this method when you want the flexibility of both the namespace selector and the route selector methods.   
Show more

### 2.3.5.1. Traditional sharding example

To understand traditional sharding, you can review the example of a configured Ingress Controller `finops-router` that has the label selector `spec.namespaceSelector.matchExpressions` with key values set to `finance` and `ops`. 

**Example YAML definition for`finops-router`**

```yaml
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  name: finops-router
  namespace: openshift-ingress-operator
spec:
  namespaceSelector:
    matchExpressions:
    - key: name
      operator: In
      values:
      - finance
      - ops
```


An example of a configured Ingress Controller `dev-router` that has the label selector `spec.namespaceSelector.matchLabels.name` with the key value set to `dev`: 

**Example YAML definition for`dev-router`**

```yaml
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  name: dev-router
  namespace: openshift-ingress-operator
spec:
  namespaceSelector:
    matchLabels:
      name: dev
```


If all application routes are in separate namespaces, such as each labeled with `name:finance`, `name:ops`, and `name:dev`, the configuration effectively distributes your routes between the two Ingress Controllers. OpenShift Container Platform routes for console, authentication, and other purposes should not be handled. 

In the previous scenario, sharding becomes a special case of partitioning, with no overlapping subsets. Routes are divided between router shards. 

Warning

The `default` Ingress Controller continues to serve all routes unless the `namespaceSelector` or `routeSelector` fields contain routes that are meant for exclusion. See this [Red Hat Knowledgebase solution](https://access.redhat.com/solutions/5097511) and the section "Sharding the default Ingress Controller" for more information on how to exclude routes from the default Ingress Controller. 

### 2.3.5.2. Overlapped sharding example

An overlapped sharding example shows how an Ingress Controller in OpenShift Container Platform can serve overlapping namespace label selectors so that more than one controller can admit the same routes. 

**Example YAML definition for`devops-router`**

```yaml
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  name: devops-router
  namespace: openshift-ingress-operator
spec:
  namespaceSelector:
    matchExpressions:
    - key: name
      operator: In
      values:
      - dev
      - ops
```


The routes in the namespaces labeled `name:dev` and `name:ops` are now serviced by two different Ingress Controllers. With this configuration, you have overlapping subsets of routes. 

With overlapping subsets of routes you can create more complex routing rules. For example, you can divert higher priority traffic to the dedicated `finops-router` while sending lower priority traffic to `devops-router`. 

### 2.3.5.3. Sharding the default Ingress Controller

You can restrict an Ingress Controller from servicing routes with specific labels by using either namespace selectors or route selectors. 

After creating a new Ingress shard, there might be routes that are admitted to your new Ingress shard that are also admitted by the default Ingress Controller. This is because the default Ingress Controller has no selectors and admits all routes by default. 

The following procedure restricts the default Ingress Controller from servicing your newly sharded `finance`, `ops`, and `dev`, routes by using a namespace selector. This adds further isolation to Ingress shards. 

Important

You must keep all of OpenShift Container Platform’s administration routes on the same Ingress Controller. Therefore, avoid adding additional selectors to the default Ingress Controller that exclude these essential routes. 

**Prerequisites**

  * You installed the OpenShift CLI (`oc`). 
  * You are logged in as a project administrator. 



**Procedure**

  1. Modify the default Ingress Controller by running the following command: 

```shell-session
$ oc edit ingresscontroller -n openshift-ingress-operator default
```


  2. Edit the Ingress Controller to contain a `namespaceSelector` that excludes the routes with any of the `finance`, `ops`, and `dev` labels: 

```yaml
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  name: default
  namespace: openshift-ingress-operator
spec:
  namespaceSelector:
    matchExpressions:
      - key: name
        operator: NotIn
        values:
          - finance
          - ops
          - dev
```


The default Ingress Controller no longer serves the namespaces labeled with `name:finance`, `name:ops`, and `name:dev`. 




### 2.3.5.4. Ingress sharding and DNS

As a cluster administrator, ensure that you add a separate DNS entry for each router in a project. A router will not forward unknown routes to another router. 

Consider the following example: 

  * Router A lives on host 192.168.0.5 and has routes with `*.foo.com`. 
  * Router B lives on host 192.168.1.9 and has routes with `*.example.com`. 



Separate DNS entries must resolve `*.foo.com` to the node hosting Router A and `*.example.com` to the node hosting Router B: 

  * `*.foo.com A IN 192.168.0.5`
  * `*.example.com A IN 192.168.1.9`



### 2.3.5.5. Configure Ingress Controller sharding by using route labels

You can use route labels to configure Ingress Controller sharding so that the Ingress Controller serves any route in any namespace that is selected by the route selector. 

**Figure 2.1. Ingress sharding by using route labels**

![A diagram showing multiple Ingress Controllers with different route selectors serving any route containing a label that matches a given route selector regardless of the namespace a route belongs to](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Ingress_and_load_balancing-en-US/images/88e02b6d127bf165fed27d7c18366e6a/nw-sharding-route-labels.png) ![A diagram showing multiple Ingress Controllers with different route selectors serving any route containing a label that matches a given route selector regardless of the namespace a route belongs to](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Ingress_and_load_balancing-en-US/images/88e02b6d127bf165fed27d7c18366e6a/nw-sharding-route-labels.png)

Ingress Controller sharding is useful when balancing incoming traffic load among a set of Ingress Controllers and when isolating traffic to a specific Ingress Controller. For example, company A goes to one Ingress Controller and company B to another. 

**Procedure**

  1. Edit the `router-internal.yaml` file: 

```yaml
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  name: sharded
  namespace: openshift-ingress-operator
spec:
  domain: <apps-sharded.basedomain.example.net>
  nodePlacement:
    nodeSelector:
      matchLabels:
        node-role.kubernetes.io/worker: ""
  routeSelector:
    matchLabels:
      type: sharded
```


     * `<apps-sharded.basedomain.example.net>`: Specify a domain to be used by the Ingress Controller. This domain must be different from the default Ingress Controller domain. 

  2. Apply the Ingress Controller `router-internal.yaml` file: 

```shell-session
# oc apply -f router-internal.yaml
```


The Ingress Controller selects routes in any namespace that have the label `type: sharded`. 

  3. Create a new route by using the domain configured in the `router-internal.yaml`: 

```shell-session
$ oc expose svc <service-name> --hostname <route-name>.apps-sharded.basedomain.example.net
```


### 2.3.5.6. Configure Ingress Controller sharding by using namespace labels

You can use namespace labels to configure Ingress Controller sharding so that the Ingress Controller serves any route in any namespace that is selected by the namespace selector. 

**Figure 2.2. Ingress sharding by using namespace labels**

![A diagram showing multiple Ingress Controllers with different namespace selectors serving routes that belong to the namespace containing a label that matches a given namespace selector](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Ingress_and_load_balancing-en-US/images/afe594e8499d327fa587b8ca4f61a2cd/nw-sharding-namespace-labels.png) ![A diagram showing multiple Ingress Controllers with different namespace selectors serving routes that belong to the namespace containing a label that matches a given namespace selector](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Ingress_and_load_balancing-en-US/images/afe594e8499d327fa587b8ca4f61a2cd/nw-sharding-namespace-labels.png)

Ingress Controller sharding is useful when balancing incoming traffic load among a set of Ingress Controllers and when isolating traffic to a specific Ingress Controller. For example, company A goes to one Ingress Controller and company B to another. 

**Procedure**

  1. Edit the `router-internal.yaml` file: 

```shell-session
$ cat router-internal.yaml
```


**Example output**

```yaml
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  name: sharded
  namespace: openshift-ingress-operator
spec:
  domain: <apps-sharded.basedomain.example.net>
  nodePlacement:
    nodeSelector:
      matchLabels:
        node-role.kubernetes.io/worker: ""
  namespaceSelector:
    matchLabels:
      type: sharded
```


     * `<apps-sharded.basedomain.example.net>`: Specify a domain to be used by the Ingress Controller. This domain must be different from the default Ingress Controller domain. 

  2. Apply the Ingress Controller `router-internal.yaml` file: 

```shell-session
$ oc apply -f router-internal.yaml
```


The Ingress Controller selects routes in any namespace that is selected by the namespace selector that have the label `type: sharded`. 

  3. Create a new route by using the domain configured in the `router-internal.yaml`: 

```shell-session
$ oc expose svc <service-name> --hostname <route-name>.apps-sharded.basedomain.example.net
```


### 2.3.5.7. Creating a route for Ingress Controller sharding

Ingress Controller sharding balances incoming traffic among a set of Ingress Controllers and can isolate traffic to a specific Ingress Controller. You create a route to direct traffic to the appropriate shard. 

**Prerequisites**

  * You installed the OpenShift CLI (`oc`). 
  * You are logged in as a project administrator. 
  * You have a web application that exposes a port and an HTTP or TLS endpoint listening for traffic on the port. 
  * You have configured the Ingress Controller for sharding. 



**Procedure**

  1. Create a project called `hello-openshift` by running the following command: 

```shell-session
$ oc new-project hello-openshift
```


  2. Create a pod in the project by running the following command: 

```shell-session
$ oc create -f https://raw.githubusercontent.com/openshift/origin/master/examples/hello-openshift/hello-pod.json
```


  3. Create a service called `hello-openshift` by running the following command: 

```shell-session
$ oc expose pod/hello-openshift
```


  4. Create a route definition called `hello-openshift-route.yaml`: 

**YAML definition of the created route for sharding**

```yaml
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  labels:
    type: sharded
  name: hello-openshift-edge
  namespace: hello-openshift
spec:
  subdomain: hello-openshift
  tls:
    termination: edge
  to:
    kind: Service
    name: hello-openshift
```


where: 

`type`
     Specifies both the label key and its corresponding label value must match the ones specified in the Ingress Controller. In this example, the Ingress Controller has the label key and value `type: sharded`. 
`subdomain`
     Specifies the route gets exposed by using the value of the `subdomain` field. When you specify the `subdomain` field, you must leave the hostname unset. If you specify both the `host` and `subdomain` fields, then the route uses the value of the `host` field, and ignore the `subdomain` field. 

  5. Use `hello-openshift-route.yaml` to create a route to the `hello-openshift` application by running the following command: 

```shell-session
$ oc -n hello-openshift create -f hello-openshift-route.yaml
```


**Verification**

  * Get the status of the route with the following command: 

```shell-session
$ oc -n hello-openshift get routes/hello-openshift-edge -o yaml
```


The resulting `Route` resource should look similar to the following: 

**Example output**

```yaml
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  labels:
    type: sharded
  name: hello-openshift-edge
  namespace: hello-openshift
spec:
  subdomain: hello-openshift
  tls:
    termination: edge
  to:
    kind: Service
    name: hello-openshift
status:
  ingress:
  - host: hello-openshift.<apps-sharded.basedomain.example.net>
    routerCanonicalHostname: router-sharded.<apps-sharded.basedomain.example.net>
    routerName: sharded
```


where: 

`host`
     Specifies the hostname the Ingress Controller, or router, uses to expose the route. The value of the `host` field is automatically determined by the Ingress Controller, and uses its domain. In this example, the domain of the Ingress Controller is `<apps-sharded.basedomain.example.net>`. 
`<apps-sharded.basedomain.example.net>`
     Specifies the hostname of the Ingress Controller. If the hostname is not set, the route can use a subdomain instead. When you specify a subdomain, you automatically use the domain of the Ingress Controller that exposes the route. When a route is exposed by multiple Ingress Controllers, the route is hosted at multiple URLs. 
`routerName`
     Specifies the name of the Ingress Controller. In this example, the Ingress Controller has the name `sharded`. 




### 2.3.5.8. Additional resources

  * [Baseline Ingress Controller (router) performance](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/scalability_and_performance/#baseline-router-performance_routing-optimization)
  * [Configuring the Ingress Controller](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/networking_operators/#configuring-ingress-controller)
  * [Installing a cluster on bare metal](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_bare_metal/#installing-bare-metal)
  * [Installing a cluster on vSphere](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_vmware_vsphere/#installing-vsphere)
  * [About network policy](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_security/#about-network-policy)
