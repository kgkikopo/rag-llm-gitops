# 4.5. Access registry metrics

The OpenShift Container Registry provides an endpoint for Prometheus metrics at the **_/extensions/v2/metrics_** path. You can access these metrics by running a metrics query that includes a cluster role. 

**Procedure**

  1. Create a cluster role if you do not already have one to access the metrics: 

```shell-session
$ cat <<EOF | oc create -f -
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: prometheus-scraper
rules:
- apiGroups:
  - image.openshift.io
  resources:
  - registry/metrics
  verbs:
  - get
EOF
```


  2. Add the cluster role to a user account by entering the following command: 

```shell-session
$ oc adm policy add-cluster-role-to-user prometheus-scraper <username>
```


  3. For the metrics query, get the user token. 

```shell-session
openshift:
$ oc whoami -t
```


  4. Run a metrics query in node or inside a pod. The following example command and output demonstrate this task. 

```shell-session
$ curl --insecure -s -u <user>:<secret> \ 
```


1

```shell-session
    https://image-registry.openshift-image-registry.svc:5000/extensions/v2/metrics | grep imageregistry | head -n 20
```


     * `<user>:<secret>`: The `<user>` object can be arbitrary, but `<secret>` tag must use the user token. 

```shell-session
# HELP imageregistry_build_info A metric with a constant '1' value labeled by major, minor, git commit & git version from which the image registry was built.
# TYPE imageregistry_build_info gauge
imageregistry_build_info{gitCommit="9f72191",gitVersion="v3.11.0+9f72191-135-dirty",major="3",minor="11+"} 1
# HELP imageregistry_digest_cache_requests_total Total number of requests without scope to the digest cache.
# TYPE imageregistry_digest_cache_requests_total counter
imageregistry_digest_cache_requests_total{type="Hit"} 5
imageregistry_digest_cache_requests_total{type="Miss"} 24
# HELP imageregistry_digest_cache_scoped_requests_total Total number of scoped requests to the digest cache.
# TYPE imageregistry_digest_cache_scoped_requests_total counter
imageregistry_digest_cache_scoped_requests_total{type="Hit"} 33
imageregistry_digest_cache_scoped_requests_total{type="Miss"} 44
# HELP imageregistry_http_in_flight_requests A gauge of requests currently being served by the registry.
# TYPE imageregistry_http_in_flight_requests gauge
imageregistry_http_in_flight_requests 1
# HELP imageregistry_http_request_duration_seconds A histogram of latencies for requests to the registry.
# TYPE imageregistry_http_request_duration_seconds summary
imageregistry_http_request_duration_seconds{method="get",quantile="0.5"} 0.01296087
imageregistry_http_request_duration_seconds{method="get",quantile="0.9"} 0.014847248
imageregistry_http_request_duration_seconds{method="get",quantile="0.99"} 0.015981195
imageregistry_http_request_duration_seconds_sum{method="get"} 12.260727916000022
```
