# Chapter 7. Event [events.k8s.io/v1]

Description
     Event is a report of an event somewhere in the cluster. It generally denotes some state change in the system. Events have a limited retention time and triggers and messages may evolve with time. Event consumers should not rely on the timing of an event with a given Reason reflecting a consistent underlying trigger, or the continued existence of events with that Reason. Events should be treated as informative, best-effort, supplemental data. 
Type
     `object`
Required
    

  * `eventTime`

- [7.1. Specification](07_01_specification.md)
- [7.2. API endpoints](07_02_api_endpoints.md)
