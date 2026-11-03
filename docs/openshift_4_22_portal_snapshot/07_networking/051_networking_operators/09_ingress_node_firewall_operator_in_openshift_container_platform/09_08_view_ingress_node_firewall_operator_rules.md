# 9.8. View Ingress Node Firewall Operator rules

Inspect existing rules and configs to confirm the firewall is applied as intended. 

**Procedure**

  1. Run the following command to view all current rules : 

```shell-session
$ oc get ingressnodefirewall
```


  2. Choose one of the returned `<resource>` names and run the following command to view the rules or configs: 

```shell-session
$ oc get <resource> <name> -o yaml
```
