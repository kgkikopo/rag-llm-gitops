# 2.7. Configuring ingress cluster traffic for a service external IP

You can use either a MetalLB implementation or an IP failover deployment to attach an ExternalIP resource to a service so that the service is available to traffic outside your OpenShift Container Platform cluster. 

Hosting an external IP address in this way is only applicable for a cluster installed on bare-metal hardware. 

You must ensure that you correctly configure the external network infrastructure to route traffic to the service. 

Before you begin the procedure, ensure that you meet the following prerequisite: 

  * You configured your cluster with ExternalIPs enabled. For more information, see "Configuring ExternalIPs for services" in the _Additional resources_ section. 



Note

Do not use the same ExternalIP for the egress IP. 

## 2.7.1. Attaching an ExternalIP to a service

You can attach an ExternalIP resource to a service. If you configured your cluster to automatically attach the resource to a service, you might not need to manually attach an ExternalIP to the service. 

The examples in the procedure use a scenario that manually attaches an ExternalIP resource to a service in a cluster with an IP failover configuration. 

**Procedure**

  1. Confirm compatible IP address ranges for the ExternalIP resource by entering the following command in your CLI: 

```shell-session
$ oc get networks.config cluster -o jsonpath='{.spec.externalIP}{"\n"}'
```


Note

If `autoAssignCIDRs` is set and you did not specify a value for `spec.externalIPs` in the ExternalIP resource, OpenShift Container Platform automatically assigns ExternalIP to a new `Service` object. 

  2. Choose one of the following options to attach an ExternalIP resource to the service: 

     1. If you are creating a new service, specify a value in the `spec.externalIPs` parameter and array of one or more valid IP addresses in the `allowedCIDRs` parameter. 

**Example of service YAML configuration file that supports an ExternalIP resource**

```yaml
apiVersion: v1
kind: Service
metadata:
  name: svc-with-externalip
spec:
  externalIPs:
    policy:
      allowedCIDRs:
      - 192.168.123.0/28
# ...
```


     2. If you are attaching an ExternalIP to an existing service, enter the following command. Replace `<name>` with the service name. Replace `<ip_address>` with a valid ExternalIP address. You can provide multiple IP addresses separated by commas. 

```shell-session
$ oc patch svc <name> -p \
  '{
    "spec": {
      "externalIPs": [ "<ip_address>" ]
    }
  }'
```


For example: 

```shell-session
$ oc patch svc mysql-55-rhel7 -p '{"spec":{"externalIPs":["192.174.120.10"]}}'
```


**Example output**

```shell-session
"mysql-55-rhel7" patched
```


  3. To confirm that an ExternalIP address is attached to the service, enter the following command. If you specified an ExternalIP for a new service, you must create the service first. 

```shell-session
$ oc get svc
```


**Example output**

```shell-session
NAME               CLUSTER-IP      EXTERNAL-IP     PORT(S)    AGE
mysql-55-rhel7     172.30.131.89   192.174.120.10  3306/TCP   13m
```


## 2.7.2. Additional resources

[Configuring ExternalIPs for services](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/ingress_and_load_balancing/configuring-ingress-cluster-traffic#configuring-externalip "2.2. Configuring ExternalIPs for services")

  * [About MetalLB and the MetalLB Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/networking_operators/#about-metallb)
  * [Configuring IP failover](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/configuring_network_settings/#configuring-ipfailover)
  * [Configuring ExternalIPs for services](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/ingress_and_load_balancing/configuring-ingress-cluster-traffic#configuring-externalip "2.2. Configuring ExternalIPs for services")
