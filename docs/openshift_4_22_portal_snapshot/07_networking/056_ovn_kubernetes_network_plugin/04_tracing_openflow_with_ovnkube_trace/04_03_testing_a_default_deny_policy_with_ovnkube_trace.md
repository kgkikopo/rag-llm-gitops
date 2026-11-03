# 4.3. Testing a default deny policy with ovnkube-trace

To verify that an ingress default deny network policy blocks traffic in OpenShift Container Platform, you can run `ovnkube-trace` with a higher log level and read the ACL debug output. You can add an allow policy for labeled namespaces and confirm that traffic succeeds. 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 
  * You are logged in to the cluster with a user with `cluster-admin` privileges. 
  * You have installed the `ovnkube-trace` binary on your local host. 



**Procedure**

  1. Create the following YAML that defines a `deny-by-default` policy to deny ingress from all pods in all namespaces. Save the YAML in the `deny-by-default.yaml` file: 

```yaml
kind: NetworkPolicy
apiVersion: networking.k8s.io/v1
metadata:
  name: deny-by-default
  namespace: default
spec:
  podSelector: {}
  ingress: []
```


  2. Apply the policy by entering the following command: 

```shell-session
$ oc apply -f deny-by-default.yaml
```


**Example output**

```shell-session
networkpolicy.networking.k8s.io/deny-by-default created
```


  3. Start a web service in the `default` namespace by entering the following command: 

```shell-session
$ oc run web --namespace=default --image=quay.io/openshifttest/nginx --labels="app=web" --expose --port=80
```


  4. Run the following command to create the `prod` namespace: 

```shell-session
$ oc create namespace prod
```


  5. Run the following command to label the `prod` namespace: 

```shell-session
$ oc label namespace/prod purpose=production
```


  6. To deploy an `alpine` image in the `prod` namespace and start a shell, run the following command: 

```shell-session
$ oc run test-6459 --namespace=prod --rm -i -t --image=alpine -- sh
```


  7. Open another terminal session. 
  8. In this new terminal session run `ovn-trace` to verify the failure in communication between the source pod `test-6459` running in namespace `prod` and destination pod running in the `default` namespace: 

```shell-session
$ ./ovnkube-trace \
 -src-namespace prod \
 -src test-6459 \
 -dst-namespace default \
 -dst web \
 -tcp -dst-port 80 \
 -loglevel 0
```


**Example output**

```shell-session
ovn-trace source pod to destination pod indicates failure from test-6459 to web
```


  9. Increase the log level to 2 to expose the reason for the failure by running the following command: 

```shell-session
$ ./ovnkube-trace \
 -src-namespace prod \
 -src test-6459 \
 -dst-namespace default \
 -dst web \
 -tcp -dst-port 80 \
 -loglevel 2
```


**Example output**

```shell-session
...
------------------------------------------------
 3. ls_out_acl_hint (northd.c:7454): !ct.new && ct.est && !ct.rpl && ct_mark.blocked == 0, priority 4, uuid 12efc456
    reg0[8] = 1;
    reg0[10] = 1;
    next;
 5. ls_out_acl_action (northd.c:7835): reg8[30..31] == 0, priority 500, uuid 69372c5d
    reg8[30..31] = 1;
    next(4);
 5. ls_out_acl_action (northd.c:7835): reg8[30..31] == 1, priority 500, uuid 2fa0af89
    reg8[30..31] = 2;
    next(4);
 4. ls_out_acl_eval (northd.c:7691): reg8[30..31] == 2 && reg0[10] == 1 && (outport == @a16982411286042166782_ingressDefaultDeny), priority 2000, uuid 447d0dab
    reg8[17] = 1;
    ct_commit { ct_mark.blocked = 1; };
    next;
...
```


where: `ct_commit { ct_mark.blocked = 1; };`:: Specifies that ingress traffic is blocked due to the default deny policy being in place. 

  10. Create a policy that allows traffic from all pods in a particular namespaces with a label `purpose=production`. Save the YAML in the `web-allow-prod.yaml` file: 

```yaml
kind: NetworkPolicy
apiVersion: networking.k8s.io/v1
metadata:
  name: web-allow-prod
  namespace: default
spec:
  podSelector:
    matchLabels:
      app: web
  policyTypes:
  - Ingress
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          purpose: production
```


  11. Apply the policy by entering the following command: 

```shell-session
$ oc apply -f web-allow-prod.yaml
```


  12. Run `ovnkube-trace` to verify that traffic is now allowed by entering the following command: 

```shell-session
$ ./ovnkube-trace \
 -src-namespace prod \
 -src test-6459 \
 -dst-namespace default \
 -dst web \
 -tcp -dst-port 80 \
 -loglevel 0
```


**Example output**

```shell-session
ovn-trace source pod to destination pod indicates success from test-6459 to web
ovn-trace destination pod to source pod indicates success from web to test-6459
ovs-appctl ofproto/trace source pod to destination pod indicates success from test-6459 to web
ovs-appctl ofproto/trace destination pod to source pod indicates success from web to test-6459
ovn-detrace source pod to destination pod indicates success from test-6459 to web
ovn-detrace destination pod to source pod indicates success from web to test-6459
```


  13. Run the following command in the shell that was opened in step six to connect nginx to the web-server: 

```shell-session
$ wget -qO- --timeout=2 http://web.default
```


**Example output**

```shell-session
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
  body {
    width: 35em;
    margin: 0 auto;
    font-family: Tahoma, Verdana, Arial, sans-serif;
  }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
```
