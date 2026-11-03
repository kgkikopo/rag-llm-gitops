# Chapter 10. Detach volumes after non-graceful node shutdown

Automatic volume detachment after non-graceful node shutdowns prevents volumes from remaining attached to failed nodes, enabling faster workload recovery by allowing pods to reschedule and reattach volumes on healthy nodes without manual intervention.

- [10.1. Overview](10_01_overview.md)
- [10.2. Adding an out-of-service taint manually for automatic volume detachment](10_02_adding_an_out_of_service_taint_manually_for_automatic_volume_detachment.md)
