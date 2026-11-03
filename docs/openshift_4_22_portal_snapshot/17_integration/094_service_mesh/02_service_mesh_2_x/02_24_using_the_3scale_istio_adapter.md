# 2.24. Using the 3scale Istio adapter

The 3scale Istio Adapter is an optional adapter that allows you to label a service running within the Red Hat OpenShift Service Mesh and integrate that service with the 3scale API Management solution. It is not required for Red Hat OpenShift Service Mesh. 

Important

You can only use the 3scale Istio adapter with Red Hat OpenShift Service Mesh versions 2.0 and below. The Mixer component was deprecated in release 2.0 and removed in release 2.1. For Red Hat OpenShift Service Mesh versions 2.1.0 and later you should use the [3scale WebAssembly module](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/service_mesh/service-mesh-2-x#ossm-threescale-webassembly-module "2.23. Using the 3scale WebAssembly module"). 

If you want to enable 3scale backend cache with the 3scale Istio adapter, you must also enable Mixer policy and Mixer telemetry. See [Deploying the Red Hat OpenShift Service Mesh control plane](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/service_mesh/service-mesh-2-x#ossm-create-smcp "2.9. Creating the ServiceMeshControlPlane"). 

## 2.24.1. Integrate the 3scale adapter with Red Hat OpenShift Service Mesh

You can use these examples to configure requests to your services using the 3scale Istio Adapter. 

**Prerequisites**

  * Red Hat OpenShift Service Mesh version 2.x 
  * A working 3scale account ([SaaS](https://www.3scale.net/signup/) or [3scale 2.9 On-Premises](https://access.redhat.com/documentation/en-us/red_hat_3scale_api_management/2.9/html/installing_3scale/install-threescale-on-openshift-guide)) 
  * Enabling backend cache requires 3scale 2.9 or greater 
  * Red Hat OpenShift Service Mesh prerequisites 
  * Ensure Mixer policy enforcement is enabled. Update Mixer policy enforcement section provides instructions to check the current Mixer policy enforcement status and enable policy enforcement. 
  * Mixer policy and telemetry must be enabled if you are using a mixer plugin. 

    * You will need to properly configure the Service Mesh Control Plane (SMCP) when upgrading. 




Note

To configure the 3scale Istio Adapter, refer to Red Hat OpenShift Service Mesh custom resources for instructions on adding adapter parameters to the custom resource file. 

Note

Pay particular attention to the `kind: handler` resource. You must update this with your 3scale account credentials. You can optionally add a `service_id` to a handler, but this is kept for backwards compatibility only, since it would render the handler only useful for one service in your 3scale account. If you add `service_id` to a handler, enabling 3scale for other services requires you to create more handlers with different `service_ids`. 

Use a single handler per 3scale account by following the steps below: 

**Procedure**

  1. Create a handler for your 3scale account and specify your account credentials. Omit any service identifier. 

```yaml
  apiVersion: "config.istio.io/v1alpha2"
  kind: handler
  metadata:
   name: threescale
  spec:
   adapter: threescale
   params:
     system_url: "https://<organization>-admin.3scale.net/"
     access_token: "<ACCESS_TOKEN>"
   connection:
     address: "threescale-istio-adapter:3333"
```


Optionally, you can provide a `backend_url` field within the _params_ section to override the URL provided by the 3scale configuration. This may be useful if the adapter runs on the same cluster as the 3scale on-premise instance, and you wish to leverage the internal cluster DNS. 

  2. Edit or patch the Deployment resource of any services belonging to your 3scale account as follows: 

     1. Add the `"service-mesh.3scale.net/service-id"` label with a value corresponding to a valid `service_id`. 
     2. Add the `"service-mesh.3scale.net/credentials"` label with its value being the _name of the handler resource_ from step 1. 

  3. Do step 2 to link it to your 3scale account credentials and to its service identifier, whenever you intend to add more services. 
  4. Modify the rule configuration with your 3scale configuration to dispatch the rule to the threescale handler. 

**Rule configuration example**

```yaml
  apiVersion: "config.istio.io/v1alpha2"
  kind: rule
  metadata:
    name: threescale
  spec:
    match: destination.labels["service-mesh.3scale.net"] == "true"
    actions:
      - handler: threescale.handler
        instances:
          - threescale-authorization.instance
```


### 2.24.1.1. Generating 3scale custom resources

The adapter includes a tool that allows you to generate the `handler`, `instance`, and `rule` custom resources. 

Table 2.29. UsageOption| Description| Required| Default value  
---|---|---|---  
`-h, --help` |  Produces help output for available options  |  No  |   
`--name` |  Unique name for this URL, token pair  |  Yes  |   
`-n, --namespace` |  Namespace to generate templates  |  No  |  istio-system   
`-t, --token` |  3scale access token  |  Yes  |   
`-u, --url` |  3scale Admin Portal URL  |  Yes  |   
`--backend-url` |  3scale backend URL. If set, it overrides the value that is read from system configuration  |  No  |   
`-s, --service` |  3scale API/Service ID  |  No  |   
`--auth` |  3scale authentication pattern to specify (1=API Key, 2=App Id/App Key, 3=OIDC)  |  No  |  Hybrid   
`-o, --output` |  File to save produced manifests to  |  No  |  Standard output   
`--version` |  Outputs the CLI version and exits immediately  |  No  |   
Show more

#### 2.24.1.1.1. Generate templates from URL examples

Note

  * Run the following commands via `oc exec` from the 3scale adapter container image in [Generating manifests from a deployed adapter](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/service_mesh/service-mesh-2-x#ossm-threescale-manifests_threescale-adapter "2.24.1.2. Generating manifests from a deployed adapter"). 
  * Use the `3scale-config-gen` command to help avoid YAML syntax and indentation errors. 
  * You can omit the `--service` if you use the annotations. 
  * This command must be invoked from within the container image via `oc exec`. 



**Procedure**

  * Use the `3scale-config-gen` command to autogenerate templates files allowing the token, URL pair to be shared by multiple services as a single handler: 

```plaintext
$ 3scale-config-gen --name=admin-credentials --url="https://<organization>-admin.3scale.net:443" --token="[redacted]"
```


  * The following example generates the templates with the service ID embedded in the handler: 

```plaintext
$ 3scale-config-gen --url="https://<organization>-admin.3scale.net" --name="my-unique-id" --service="123456789" --token="[redacted]"
```


**Additional resources**

  * [Tokens](https://access.redhat.com/documentation/en-us/red_hat_3scale_api_management/2.10/html-single/admin_portal_guide/index#tokens). 



### 2.24.1.2. Generating manifests from a deployed adapter

Note

  * `NAME` is an identifier you use to identify with the service you are managing with 3scale. 
  * The `CREDENTIALS_NAME` reference is an identifier that corresponds to the `match` section in the rule configuration. This is automatically set to the `NAME` identifier if you are using the CLI tool. 
  * Its value does not need to be anything specific: the label value should just match the contents of the rule. See [Routing service traffic through the adapter](https://github.com/3scale/3scale-istio-adapter/blob/v2.X/README.md#routing-service-traffic-through-the-adapter) for more information. 



  1. Run this command to generate manifests from a deployed adapter in the `istio-system` namespace: 

```plaintext
$ export NS="istio-system" URL="https://replaceme-admin.3scale.net:443" NAME="name" TOKEN="token"
oc exec -n ${NS} $(oc get po -n ${NS} -o jsonpath='{.items[?(@.metadata.labels.app=="3scale-istio-adapter")].metadata.name}') \
-it -- ./3scale-config-gen \
--url ${URL} --name ${NAME} --token ${TOKEN} -n ${NS}
```


  2. This will produce sample output to the terminal. Edit these samples if required and create the objects using the `oc create` command. 
  3. When the request reaches the adapter, the adapter needs to know how the service maps to an API on 3scale. You can provide this information in two ways: 

     1. Label the workload (recommended) 
     2. Hard code the handler as `service_id`

  4. Update the workload with the required annotations: 

Note

You only need to update the service ID provided in this example if it is not already embedded in the handler. **The setting in the handler takes precedence**. 

```plaintext
$ export CREDENTIALS_NAME="replace-me"
export SERVICE_ID="replace-me"
export DEPLOYMENT="replace-me"
patch="$(oc get deployment "${DEPLOYMENT}"
patch="$(oc get deployment "${DEPLOYMENT}" --template='{"spec":{"template":{"metadata":{"labels":{ {{ range $k,$v := .spec.template.metadata.labels }}"{{ $k }}":"{{ $v }}",{{ end }}"service-mesh.3scale.net/service-id":"'"${SERVICE_ID}"'","service-mesh.3scale.net/credentials":"'"${CREDENTIALS_NAME}"'"}}}}}' )"
oc patch deployment "${DEPLOYMENT}" --patch ''"${patch}"''
```


### 2.24.1.3. Routing service traffic through the adapter

Follow these steps to drive traffic for your service through the 3scale adapter. 

**Prerequisites**

  * Credentials and service ID from your 3scale administrator. 



**Procedure**

  1. Match the rule `destination.labels["service-mesh.3scale.net/credentials"] == "threescale"` that you previously created in the configuration, in the `kind: rule` resource. 
  2. Add the above label to `PodTemplateSpec` on the Deployment of the target workload to integrate a service. the value, `threescale`, refers to the name of the generated handler. This handler stores the access token required to call 3scale. 
  3. Add the `destination.labels["service-mesh.3scale.net/service-id"] == "replace-me"` label to the workload to pass the service ID to the adapter via the instance at request time. 



## 2.24.2. Configure the integration settings in 3scale

Follow this procedure to configure the 3scale integration settings. 

Note

For 3scale SaaS customers, Red Hat OpenShift Service Mesh is enabled as part of the Early Access program. 

**Procedure**

  1. Navigate to **[your_API_name]** **Integration**
  2. Click **Settings**. 
  3. Select the **Istio** option under _Deployment_. 

     * The **API Key (user_key)** option under _Authentication_ is selected by default. 

  4. Click **Update Product** to save your selection. 
  5. Click **Configuration**. 
  6. Click **Update Configuration**. 



## 2.24.3. Caching behavior

Responses from 3scale System APIs are cached by default within the adapter. Entries will be purged from the cache when they become older than the `cacheTTLSeconds` value. Also by default, automatic refreshing of cached entries will be attempted seconds before they expire, based on the `cacheRefreshSeconds` value. You can disable automatic refreshing by setting this value higher than the `cacheTTLSeconds` value. 

Caching can be disabled entirely by setting `cacheEntriesMax` to a non-positive value. 

By using the refreshing process, cached values whose hosts become unreachable will be retried before eventually being purged when past their expiry. 

## 2.24.4. Authenticating requests

This release supports the following authentication methods: 

  * **Standard API Keys** : single randomized strings or hashes acting as an identifier and a secret token. 
  * **Application identifier and key pairs** : immutable identifier and mutable secret key strings. 
  * **OpenID authentication method** : client ID string parsed from the JSON Web Token. 



### 2.24.4.1. Applying authentication patterns

Modify the `instance` custom resource, as illustrated in the following authentication method examples, to configure authentication behavior. You can accept the authentication credentials from: 

  * Request headers 
  * Request parameters 
  * Both request headers and query parameters 



Note

When specifying values from headers, they must be lower case. For example, if you want to send a header as `User-Key`, this must be referenced in the configuration as `request.headers["user-key"]`. 

#### 2.24.4.1.1. API key authentication method

Service Mesh looks for the API key in query parameters and request headers as specified in the `user` option in the `subject` custom resource parameter. It checks the values in the order given in the custom resource file. You can restrict the search for the API key to either query parameters or request headers by omitting the unwanted option. 

In this example, Service Mesh looks for the API key in the `user_key` query parameter. If the API key is not in the query parameter, Service Mesh then checks the `user-key` header. 

**API key authentication method example**

```yaml
apiVersion: "config.istio.io/v1alpha2"
kind: instance
metadata:
  name: threescale-authorization
  namespace: istio-system
spec:
  template: authorization
  params:
    subject:
      user: request.query_params["user_key"] | request.headers["user-key"] | ""
    action:
      path: request.url_path
      method: request.method | "get"
```


If you want the adapter to examine a different query parameter or request header, change the name as appropriate. For example, to check for the API key in a query parameter named “key”, change `request.query_params["user_key"]` to `request.query_params["key"]`. 

#### 2.24.4.1.2. Application ID and application key pair authentication method

Service Mesh looks for the application ID and application key in query parameters and request headers, as specified in the `properties` option in the `subject` custom resource parameter. The application key is optional. It checks the values in the order given in the custom resource file. You can restrict the search for the credentials to either query parameters or request headers by not including the unwanted option. 

In this example, Service Mesh looks for the application ID and application key in the query parameters first, moving on to the request headers if needed. 

**Application ID and application key pair authentication method example**

```yaml
apiVersion: "config.istio.io/v1alpha2"
kind: instance
metadata:
  name: threescale-authorization
  namespace: istio-system
spec:
  template: authorization
  params:
    subject:
        app_id: request.query_params["app_id"] | request.headers["app-id"] | ""
        app_key: request.query_params["app_key"] | request.headers["app-key"] | ""
    action:
      path: request.url_path
      method: request.method | "get"
```


If you want the adapter to examine a different query parameter or request header, change the name as appropriate. For example, to check for the application ID in a query parameter named `identification`, change `request.query_params["app_id"]` to `request.query_params["identification"]`. 

#### 2.24.4.1.3. OpenID authentication method

To use the _OpenID Connect (OIDC) authentication method_ , use the `properties` value on the `subject` field to set `client_id`, and optionally `app_key`. 

You can manipulate this object using the methods described previously. In the example configuration shown below, the client identifier (application ID) is parsed from the JSON Web Token (JWT) under the label _azp_. You can modify this as needed. 

**OpenID authentication method example**

```yaml
apiVersion: "config.istio.io/v1alpha2"
kind: instance
metadata:
  name: threescale-authorization
spec:
  template: threescale-authorization
  params:
    subject:
      properties:
        app_key: request.query_params["app_key"] | request.headers["app-key"] | ""
        client_id: request.auth.claims["azp"] | ""
      action:
        path: request.url_path
        method: request.method | "get"
        service: destination.labels["service-mesh.3scale.net/service-id"] | ""
```


For this integration to work correctly, OIDC must still be done in 3scale for the client to be created in the identity provider (IdP). You should create a [Request authorization](https://istio.io/latest/docs/tasks/security/authorization/authz-jwt/) for the service you want to protect in the same namespace as that service. The JWT is passed in the `Authorization` header of the request. 

In the sample `RequestAuthentication` defined below, replace `issuer`, `jwksUri`, and `selector` as appropriate. 

**OpenID Policy example**

```yaml
apiVersion: security.istio.io/v1beta1
kind: RequestAuthentication
metadata:
  name: jwt-example
  namespace: bookinfo
spec:
  selector:
    matchLabels:
      app: productpage
  jwtRules:
  - issuer: >-
      http://keycloak-keycloak.34.242.107.254.nip.io/auth/realms/3scale-keycloak
    jwksUri: >-
      http://keycloak-keycloak.34.242.107.254.nip.io/auth/realms/3scale-keycloak/protocol/openid-connect/certs
```


#### 2.24.4.1.4. Hybrid authentication method

You can choose to not enforce a particular authentication method and accept any valid credentials for either method. If both an API key and an application ID/application key pair are provided, Service Mesh uses the API key. 

In this example, Service Mesh checks for an API key in the query parameters, then the request headers. If there is no API key, it then checks for an application ID and key in the query parameters, then the request headers. 

**Hybrid authentication method example**

```yaml
apiVersion: "config.istio.io/v1alpha2"
kind: instance
metadata:
  name: threescale-authorization
spec:
  template: authorization
  params:
    subject:
      user: request.query_params["user_key"] | request.headers["user-key"] |
      properties:
        app_id: request.query_params["app_id"] | request.headers["app-id"] | ""
        app_key: request.query_params["app_key"] | request.headers["app-key"] | ""
        client_id: request.auth.claims["azp"] | ""
    action:
      path: request.url_path
      method: request.method | "get"
      service: destination.labels["service-mesh.3scale.net/service-id"] | ""
```


## 2.24.5. 3scale Adapter metrics

The adapter, by default reports various Prometheus metrics that are exposed on port `8080` at the `/metrics` endpoint. These metrics provide insight into how the interactions between the adapter and 3scale are performing. The service is labeled to be automatically discovered and scraped by Prometheus. 

Note

There are incompatible changes in the 3scale Istio Adapter metrics since the previous releases in Service Mesh 1.x. 

In Prometheus, metrics have been renamed with one addition for the backend cache, so that the following metrics exist as of Service Mesh 2.0: 

Table 2.30. Prometheus metricsMetric| Type| Description  
---|---|---  
`threescale_latency` |  Histogram  |  Request latency between adapter and 3scale.   
`threescale_http_total` |  Counter  |  HTTP Status response codes for requests to 3scale backend.   
`threescale_system_cache_hits` |  Counter  |  Total number of requests to the 3scale system fetched from the configuration cache.   
`threescale_backend_cache_hits` |  Counter  |  Total number of requests to 3scale backend fetched from the backend cache.   
Show more

## 2.24.6. 3scale backend cache

The 3scale backend cache provides an authorization and reporting cache for clients of the 3scale Service Management API. This cache is embedded in the adapter to enable lower latencies in responses in certain situations assuming the administrator is willing to accept the trade-offs. 

Note

3scale backend cache is disabled by default. 3scale backend cache functionality trades inaccuracy in rate limiting and potential loss of hits since the last flush was performed for low latency and higher consumption of resources in the processor and memory. 

### 2.24.6.1. Advantages of enabling backend cache

The following are advantages to enabling the backend cache: 

  * Enable the backend cache when you find latencies are high while accessing services managed by the 3scale Istio Adapter. 
  * Enabling the backend cache will stop the adapter from continually checking with the 3scale API manager for request authorizations, which will lower the latency. 

    * This creates an in-memory cache of 3scale authorizations for the 3scale Istio Adapter to store and reuse before attempting to contact the 3scale API manager for authorizations. Authorizations will then take much less time to be granted or denied. 

  * Backend caching is useful in cases when you are hosting the 3scale API manager in another geographical location from the service mesh running the 3scale Istio Adapter. 

    * This is generally the case with the 3scale Hosted (SaaS) platform, but also if a user hosts their 3scale API manager in another cluster located in a different geographical location, in a different availability zone, or in any case where the network overhead to reach the 3scale API manager is noticeable. 




### 2.24.6.2. Trade-offs for having lower latencies

The following are trade-offs for having lower latencies: 

  * Each 3scale adapter’s authorization state updates every time a flush happens. 

    * This means two or more instances of the adapter will introduce more inaccuracy between flushing periods. 
    * There is a greater chance of too many requests being granted that exceed limits and introduce erratic behavior, which leads to some requests going through and some not, depending on which adapter processes each request. 

  * An adapter cache that cannot flush its data and update its authorization information risks shut down or crashing without reporting its information to the API manager. 
  * A fail open or fail closed policy will be applied when an adapter cache cannot determine whether a request must be granted or denied, possibly due to network connectivity issues in contacting the API manager. 
  * When cache misses occur, typically right after booting the adapter or after a long period of no connectivity, latencies will grow in order to query the API manager. 
  * An adapter cache must do much more work on computing authorizations than it would without an enabled cache, which will tax processor resources. 
  * Memory requirements will grow proportionally to the combination of the amount of limits, applications, and services managed by the cache. 



### 2.24.6.3. Backend cache configuration settings

The following points explain the backend cache configuration settings: 

  * Find the settings to configure the backend cache in the 3scale configuration options. 
  * The last 3 settings control enabling of backend cache: 

    * `PARAM_USE_CACHE_BACKEND` \- set to true to enable backend cache. 
    * `PARAM_BACKEND_CACHE_FLUSH_INTERVAL_SECONDS` \- sets time in seconds between consecutive attempts to flush cache data to the API manager. 
    * `PARAM_BACKEND_CACHE_POLICY_FAIL_CLOSED` \- set whether or not to allow/open or deny/close requests to the services when there is not enough cached data and the 3scale API manager cannot be reached. 




## 2.24.7. 3scale Istio Adapter APIcast emulation

The 3scale Istio Adapter performs as APIcast would when the following conditions occur: 

  * When a request cannot match any mapping rule defined, the returned HTTP code is 404 Not Found. This was previously 403 Forbidden. 
  * When a request is denied because it goes over limits, the returned HTTP code is 429 Too Many Requests. This was previously 403 Forbidden. 
  * When generating default templates via the CLI, it will use underscores rather than dashes for the headers, for example: `user_key` rather than `user-key`. 



## 2.24.8. 3scale Istio adapter verification

You might want to check whether the 3scale Istio adapter is working as expected. If your adapter is not working, use the following steps to help troubleshoot the problem. 

**Procedure**

  1. Ensure the _3scale-adapter_ pod is running in the Service Mesh control plane namespace: 

```shell-session
$ oc get pods -n istio-system
```


  2. Check that the _3scale-adapter_ pod has printed out information about itself booting up, such as its version: 

```shell-session
$ oc logs istio-system
```


  3. When performing requests to the services protected by the 3scale adapter integration, always try requests that lack the right credentials and ensure they fail. Check the 3scale adapter logs to gather additional information. 



**Additional resources**

  * [Inspecting pod and container logs](https://docs.openshift.com/container-platform/4.7/support/troubleshooting/investigating-pod-issues.html#inspecting-pod-and-container-logs_investigating-pod-issues). 



## 2.24.9. 3scale Istio adapter troubleshooting checklist

As the administrator installing the 3scale Istio adapter, there are a number of scenarios that might be causing your integration to not function properly. Use the following list to troubleshoot your installation: 

  * Incorrect YAML indentation. 
  * Missing YAML sections. 
  * Forgot to apply the changes in the YAML to the cluster. 
  * Forgot to label the service workloads with the `service-mesh.3scale.net/credentials` key. 
  * Forgot to label the service workloads with `service-mesh.3scale.net/service-id` when using handlers that do not contain a `service_id` so they are reusable per account. 
  * The _Rule_ custom resource points to the wrong handler or instance custom resources, or the references lack the corresponding namespace suffix. 
  * The _Rule_ custom resource `match` section cannot possibly match the service you are configuring, or it points to a destination workload that is not currently running or does not exist. 
  * Wrong access token or URL for the 3scale Admin Portal in the handler. 
  * The _Instance_ custom resource’s `params/subject/properties` section fails to list the right parameters for `app_id`, `app_key`, or `client_id`, either because they specify the wrong location such as the query parameters, headers, and authorization claims, or the parameter names do not match the requests used for testing. 
  * Failing to use the configuration generator without realizing that it actually lives in the adapter container image and needs `oc exec` to invoke it.
