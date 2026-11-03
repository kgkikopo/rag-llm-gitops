# 9.1. Ingress Node Firewall Operator

The Ingress Node Firewall Operator provides ingress firewall rules at a node level that you can specify and manage in the firewall configurations. 

To deploy the daemon set created by the Operator, you create an `IngressNodeFirewallConfig` custom resource (CR). The Operator applies the `IngressNodeFirewallConfig` CR to create ingress node firewall daemon set `daemon`, which run on all nodes that match the `nodeSelector`. 

You configure `rules` of the `IngressNodeFirewall` CR and apply them to clusters using the `nodeSelector` and setting values to "true". 

Important

The Ingress Node Firewall Operator supports only stateless firewall rules. 

Network interface controllers (NICs) that do not support native XDP drivers will run at a lower performance. 

For OpenShift Container Platform 4.14 or later, you must run Ingress Node Firewall Operator on RHEL 9.0 or later.
