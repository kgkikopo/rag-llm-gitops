# 9.4. Deploy Ingress Node Firewall Operator

To deploy the Ingress Node Firewall Operator, create a `IngressNodeFirewallConfig` custom resource that will deploy the Operator’s daemon set. You can deploy one or multiple `IngressNodeFirewall` CRDs to nodes by applying firewall rules. 

**Prerequisite**

  * The Ingress Node Firewall Operator is installed. 



**Procedure**

  1. Create the `IngressNodeFirewallConfig` inside the `openshift-ingress-node-firewall` namespace named `ingressnodefirewallconfig`. 
  2. Run the following command to deploy Ingress Node Firewall Operator rules: 

```shell-session
$ oc apply -f rule.yaml
```
