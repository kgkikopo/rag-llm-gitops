# 7.2. FlowCollectorSlice resource for granular flow collection

The `FlowCollectorSlice` is a custom resource definition (CRD) that enables granular, multi-tenant network flow collection. By defining logical slices based on namespaces or subnets, you can selectively collect traffic and apply custom sampling to specific workloads rather than the entire cluster. 

It complements the existing `FlowCollector` custom resource by enabling granular, selective, and multi-tenant-aware flow collection, instead of a single global configuration that applies uniformly to all traffic. 

When slice-based collection is enabled, only traffic that matches at least one `FlowCollectorSlice` is collected, allowing administrators to precisely control which network flows are observed. 

## 7.2.1. Benefits of FlowCollectorSlice

By default, network flow collection applies uniformly to all traffic in the cluster. This can result in excessive data volume and limited flexibility. 

Using `FlowCollectorSlice` provides the following benefits: 

  * Enables selective flow collection for specific namespaces or workloads. 
  * Supports multi-tenant and environment-based observability. 
  * Reduces storage and processing costs by filtering irrelevant traffic. 
  * Preserves backward compatibility through opt-in configuration. 



## 7.2.2. Relationship between FlowCollector and FlowCollectorSlice

While the `FlowCollector` resource defines global flow collection behavior for the cluster, the `FlowCollectorSlice` resource defines which traffic is eligible for collection when slice-based filtering is enabled. 

The `FlowCollector.spec.slicesConfig` field controls how slice definitions are applied. 

## 7.2.3. Collection modes

Slice behavior is governed by the `FlowCollector.spec.slicesConfig.collectionMode` field. Set the field to one of the following collection modes: 

AlwaysCollect
    

  * Collects network flows from all cluster namespaces. 
  * Applies the subnet and sampling configurations defined in `FlowCollectorSlice` resources. 
  * Ignores the namespace selection logic in `FlowCollectorSlice` resources. 
  * Maintains the default collection behavior for backward compatibility. 



AllowList
    

  * Collects only traffic that matches at least one `FlowCollectorSlice` resource. 
  * An optional namespace allow list includes selected namespaces in the collection. 



## 7.2.4. FlowCollectorSlice status

Each `FlowCollectorSlice` resource exposes a `status` subresource that reports: 

  * Validation results. 
  * Reconciliation state. 
  * Whether the slice is successfully applied. 



This status allows administrators to verify that slice definitions are active and functioning as expected.
