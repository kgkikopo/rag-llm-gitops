# Chapter 8. Event [v1]

Description
     Event is a report of an event somewhere in the cluster. Events have a limited retention time and triggers and messages may evolve with time. Event consumers should not rely on the timing of an event with a given Reason reflecting a consistent underlying trigger, or the continued existence of events with that Reason. Events should be treated as informative, best-effort, supplemental data. 
Type
     `object`
Required
    

  * `metadata`
  * `involvedObject`

- [8.1. Specification](08_01_specification.md)
- [8.2. API endpoints](08_02_api_endpoints.md)
