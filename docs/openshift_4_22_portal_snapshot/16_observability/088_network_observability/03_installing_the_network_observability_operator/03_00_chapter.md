# Chapter 3. Installing the Network Observability Operator

Installing the Loki Operator is recommended before using the Network Observability Operator. You can use network observability without Loki, but special considerations apply if you only need metrics or external exporters. 

The Loki Operator integrates a gateway that implements multi-tenancy and authentication with Loki for data flow storage. The `LokiStack` resource manages Loki, which is a scalable, highly-available, multi-tenant log aggregation system, and a web proxy with OpenShift Container Platform authentication. The `LokiStack` proxy uses OpenShift Container Platform authentication to enforce multi-tenancy and facilitate the saving and indexing of data in Loki log stores.

- [3.1. Network observability without Loki](03_01_network_observability_without_loki.md)
- [3.2. Install the Loki Operator](03_02_install_the_loki_operator.md)
- [3.3. Install the Network Observability Operator](03_03_install_the_network_observability_operator.md)
- [3.4. Enable multi-tenancy in network observability](03_04_enable_multi_tenancy_in_network_observability.md)
- [3.5. Uninstall the Network Observability Operator](03_05_uninstall_the_network_observability_operator.md)
