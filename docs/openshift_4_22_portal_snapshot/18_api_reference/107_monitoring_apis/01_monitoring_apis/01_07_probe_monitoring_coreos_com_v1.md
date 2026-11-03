# 1.7. Probe [monitoring.coreos.com/v1]

Description
    

The `Probe` custom resource definition (CRD) defines how to scrape metrics from prober exporters such as the [blackbox exporter](<https://github.com/prometheus/blackbox_exporter>). 

The `Probe` resource needs 2 pieces of information: * The list of probed addresses which can be defined statically or by discovering Kubernetes Ingress objects. * The prober which exposes the availability of probed endpoints (over various protocols such HTTP, TCP, ICMP, …​) as Prometheus metrics. 

`Prometheus` and `PrometheusAgent` objects select `Probe` objects using label and namespace selectors. 

Type
     `object`
