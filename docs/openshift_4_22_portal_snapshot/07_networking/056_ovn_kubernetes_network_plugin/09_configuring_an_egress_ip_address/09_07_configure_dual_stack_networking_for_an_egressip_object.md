# 9.7. Configure dual-stack networking for an EgressIP object

For a cluster configured for dual-stack networking, you can apply dual-stack networking to a single `EgressIP` object. The `EgressIP` object can then extend dual-stack networking capabilities to a pod. 

Important

Red Hat does not support creating two `EgressIP` objects to represent dual-stack networking capabilities. For example, specifying IPv4 addresses with one object and using another object to specify IPv6 addresses. This configuration limit impacts address-type assignments to pods. 

**Prerequisites**

  * You created two egress nodes so that an `EgressIP` object can allocate IPv4 addresses to one node and IPv6 addresses to the other node. For more information, see "Assignment of egress IP addresses to nodes". 



**Procedure**

  * Create an `EgressIP` object and configure IPv4 and IPv6 addresses for the object. The following example `EgressIP` object uses selectors to identify which pods use the specified egress IP addresses for their outbound traffic: 

```yaml
kind: EgressIP
metadata:
  name: egressip-dual
spec:
  egressIPs:
    - 192.168.118.30
    - 2600:52:7:94::30
  namespaceSelector:
    matchLabels:
      env: qa
  podSelector:
    matchLabels:
      egressip: ds
# ...
```


**Verification**

  1. Create a `Pod` manifest file to test and validate your `EgressIP` object. The pod serves as a client workload that sends outbound traffic to verify that your `EgressIP` policy works as expected. 

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: ubi-egressip-pod
  namespace: test
  labels:
    egressip: ds
spec:
  containers:
  - name: fedora-curl
    image: registry.redhat.io/ubi9/ubi
    command: ["/bin/bash", "-c", "sleep infinity"]
# ...
```


where: 

`<labels>`
     Sets custom identifiers so that the `EgressIP` object can use these labels to apply egress IP address to target pods. 

  2. Run a `curl` request from inside a pod to an external server. This action verifies that outbound traffic correctly uses an address that you specified in the `EgressIP` object. 

```shell-session
$ curl <ipv_address>
```


where: 

`<ipv_address>`
     Depending on the `EgressIP` object, enter an IPv4 or IPv6 address.
