# 9.4. PTP events REST API v2 reference

Use the following REST API v2 endpoints to subscribe the `cloud-event-consumer` application to Precision Time Protocol (PTP) events posted at `http://ptp-event-publisher-service-NODE_NAME.openshift-ptp.svc.cluster.local:9043/api/ocloudNotifications/v2` in the PTP events producer pod. 

  * [`api/ocloudNotifications/v2/subscriptions`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/advanced_networking/using-ptp-hardware#api-ocloud-notifications-v2-subscriptions_using-ptp-hardware-fast-events-framework-v2 "9.4.1.1. api/ocloudNotifications/v2/subscriptions")

    * `POST`: Creates a new subscription 
    * `GET`: Retrieves a list of subscriptions 
    * `DELETE`: Deletes all subscriptions 

  * [`api/ocloudNotifications/v2/subscriptions/{subscription_id}`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/advanced_networking/using-ptp-hardware#api-ocloud-notifications-v2-subscriptions-subscription_id_using-ptp-hardware-fast-events-framework-v2 "9.4.1.8. api/ocloudNotifications/v2/subscriptions/{subscription_id}")

    * `GET`: Returns details for the specified subscription ID 
    * `DELETE`: Deletes the subscription associated with the specified subscription ID 

  * [`api/ocloudNotifications/v2/health`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/advanced_networking/using-ptp-hardware#api-ocloudnotifications-v2-health_using-ptp-hardware-fast-events-framework-v2 "9.4.1.13. api/ocloudNotifications/v2/health")

    * `GET`: Returns the health status of `ocloudNotifications` API 

  * [`api/ocloudNotifications/v2/publishers`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/advanced_networking/using-ptp-hardware#api-ocloudnotifications-v2-publishers_using-ptp-hardware-fast-events-framework-v2 "9.4.1.16. api/ocloudNotifications/v2/publishers")

    * `GET`: Returns a list of PTP event publishers for the cluster node 

  * [`api/ocloudnotifications/v2/{resource_address}/CurrentState`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/advanced_networking/using-ptp-hardware#resource-address-current-state-v2_using-ptp-hardware-fast-events-framework-v2 "9.4.1.19. api/ocloudNotifications/v2/{resource_address}/CurrentState")

    * `GET`: Returns the current state of the event type specified by the `{resouce_address}`. 




## 9.4.1. PTP events REST API v2 endpoints

Use the PTP events REST API v2 endpoints to create and manage event subscriptions and to poll the current state of PTP events on cluster nodes. 

### 9.4.1.1. api/ocloudNotifications/v2/subscriptions

### 9.4.1.2. HTTP method

`GET api/ocloudNotifications/v2/subscriptions`

### 9.4.1.3. Description

Returns a list of subscriptions. If subscriptions exist, a `200 OK` status code is returned along with the list of subscriptions. 

**Example API response**

```plaintext
[
 {
  "ResourceAddress": "/cluster/node/compute-1.example.com/sync/sync-status/os-clock-sync-state",
  "EndpointUri": "http://consumer-events-subscription-service.cloud-events.svc.cluster.local:9043/event",
  "SubscriptionId": "ccedbf08-3f96-4839-a0b6-2eb0401855ed",
  "UriLocation": "http://ptp-event-publisher-service-compute-1.openshift-ptp.svc.cluster.local:9043/api/ocloudNotifications/v2/subscriptions/ccedbf08-3f96-4839-a0b6-2eb0401855ed"
 },
 {
  "ResourceAddress": "/cluster/node/compute-1.example.com/sync/ptp-status/clock-class",
  "EndpointUri": "http://consumer-events-subscription-service.cloud-events.svc.cluster.local:9043/event",
  "SubscriptionId": "a939a656-1b7d-4071-8cf1-f99af6e931f2",
  "UriLocation": "http://ptp-event-publisher-service-compute-1.openshift-ptp.svc.cluster.local:9043/api/ocloudNotifications/v2/subscriptions/a939a656-1b7d-4071-8cf1-f99af6e931f2"
 },
 {
  "ResourceAddress": "/cluster/node/compute-1.example.com/sync/ptp-status/lock-state",
  "EndpointUri": "http://consumer-events-subscription-service.cloud-events.svc.cluster.local:9043/event",
  "SubscriptionId": "ba4564a3-4d9e-46c5-b118-591d3105473c",
  "UriLocation": "http://ptp-event-publisher-service-compute-1.openshift-ptp.svc.cluster.local:9043/api/ocloudNotifications/v2/subscriptions/ba4564a3-4d9e-46c5-b118-591d3105473c"
 },
 {
  "ResourceAddress": "/cluster/node/compute-1.example.com/sync/gnss-status/gnss-sync-status",
  "EndpointUri": "http://consumer-events-subscription-service.cloud-events.svc.cluster.local:9043/event",
  "SubscriptionId": "ea0d772e-f00a-4889-98be-51635559b4fb",
  "UriLocation": "http://ptp-event-publisher-service-compute-1.openshift-ptp.svc.cluster.local:9043/api/ocloudNotifications/v2/subscriptions/ea0d772e-f00a-4889-98be-51635559b4fb"
 },
 {
  "ResourceAddress": "/cluster/node/compute-1.example.com/sync/sync-status/sync-state",
  "EndpointUri": "http://consumer-events-subscription-service.cloud-events.svc.cluster.local:9043/event",
  "SubscriptionId": "762999bf-b4a0-4bad-abe8-66e646b65754",
  "UriLocation": "http://ptp-event-publisher-service-compute-1.openshift-ptp.svc.cluster.local:9043/api/ocloudNotifications/v2/subscriptions/762999bf-b4a0-4bad-abe8-66e646b65754"
 }
]
```


### 9.4.1.4. HTTP method

`POST api/ocloudNotifications/v2/subscriptions`

### 9.4.1.5. Description

Creates a new subscription for the required event by passing the appropriate payload. 

You can subscribe to the following PTP events: 

  * `sync-state` events 
  * `lock-state` events 
  * `gnss-sync-status events` events 
  * `os-clock-sync-state` events 
  * `clock-class` events 



Table 9.13. Query parametersParameter| Type  
---|---  
subscription  |  data   
Show more

**Example sync-state subscription payload**

```plaintext
{
"EndpointUri": "http://consumer-events-subscription-service.cloud-events.svc.cluster.local:9043/event",
"ResourceAddress": "/cluster/node/{node_name}/sync/sync-status/sync-state"
}
```


**Example PTP lock-state events subscription payload**

```plaintext
{
"EndpointUri": "http://consumer-events-subscription-service.cloud-events.svc.cluster.local:9043/event",
"ResourceAddress": "/cluster/node/{node_name}/sync/ptp-status/lock-state"
}
```


**Example PTP gnss-sync-status events subscription payload**

```plaintext
{
"EndpointUri": "http://consumer-events-subscription-service.cloud-events.svc.cluster.local:9043/event",
"ResourceAddress": "/cluster/node/{node_name}/sync/gnss-status/gnss-sync-status"
}
```


**Example PTP os-clock-sync-state events subscription payload**

```plaintext
{
"EndpointUri": "http://consumer-events-subscription-service.cloud-events.svc.cluster.local:9043/event",
"ResourceAddress": "/cluster/node/{node_name}/sync/sync-status/os-clock-sync-state"
}
```


**Example PTP clock-class events subscription payload**

```plaintext
{
"EndpointUri": "http://consumer-events-subscription-service.cloud-events.svc.cluster.local:9043/event",
"ResourceAddress": "/cluster/node/{node_name}/sync/ptp-status/clock-class"
}
```


**Example API response**

```plaintext
{
    "ResourceAddress": "/cluster/node/compute-1.example.com/sync/ptp-status/lock-state",
    "EndpointUri": "http://consumer-events-subscription-service.cloud-events.svc.cluster.local:9043/event",
    "SubscriptionId": "620283f3-26cd-4a6d-b80a-bdc4b614a96a",
    "UriLocation": "http://ptp-event-publisher-service-compute-1.openshift-ptp.svc.cluster.local:9043/api/ocloudNotifications/v2/subscriptions/620283f3-26cd-4a6d-b80a-bdc4b614a96a"
}
```


The following subscription status events are possible: 

Table 9.14. PTP events REST API v2 subscription status codesStatus code| Description  
---|---  
`201 Created` |  Indicates that the subscription is created   
`400 Bad Request` |  Indicates that the server could not process the request because it was malformed or invalid   
`404 Not Found` |  Indicates that the subscription resource is not available   
`409 Conflict` |  Indicates that the subscription already exists   
Show more

### 9.4.1.6. HTTP method

`DELETE api/ocloudNotifications/v2/subscriptions`

### 9.4.1.7. Description

Deletes all subscriptions. 

**Example API response**

```plaintext
{
"status": "deleted all subscriptions"
}
```


### 9.4.1.8. api/ocloudNotifications/v2/subscriptions/{subscription_id}

### 9.4.1.9. HTTP method

`GET api/ocloudNotifications/v2/subscriptions/{subscription_id}`

### 9.4.1.10. Description

Returns details for the subscription with ID `subscription_id`. 

Table 9.15. Global path parametersParameter| Type  
---|---  
`subscription_id` |  string   
Show more

**Example API response**

```plaintext
{
    "ResourceAddress": "/cluster/node/compute-1.example.com/sync/ptp-status/lock-state",
    "EndpointUri": "http://consumer-events-subscription-service.cloud-events.svc.cluster.local:9043/event",
    "SubscriptionId": "620283f3-26cd-4a6d-b80a-bdc4b614a96a",
    "UriLocation": "http://ptp-event-publisher-service-compute-1.openshift-ptp.svc.cluster.local:9043/api/ocloudNotifications/v2/subscriptions/620283f3-26cd-4a6d-b80a-bdc4b614a96a"
}
```


### 9.4.1.11. HTTP method

`DELETE api/ocloudNotifications/v2/subscriptions/{subscription_id}`

### 9.4.1.12. Description

Deletes the subscription with ID `subscription_id`. 

Table 9.16. Global path parametersParameter| Type  
---|---  
`subscription_id` |  string   
Show more

Table 9.17. HTTP response codesHTTP response| Description  
---|---  
204 No Content  |  Success   
Show more

### 9.4.1.13. api/ocloudNotifications/v2/health

### 9.4.1.14. HTTP method

`GET api/ocloudNotifications/v2/health/`

### 9.4.1.15. Description

Returns the health status for the `ocloudNotifications` REST API. 

Table 9.18. HTTP response codesHTTP response| Description  
---|---  
200 OK  |  Success   
Show more

### 9.4.1.16. api/ocloudNotifications/v2/publishers

### 9.4.1.17. HTTP method

`GET api/ocloudNotifications/v2/publishers`

### 9.4.1.18. Description

Returns a list of publisher details for the cluster node. The system generates notifications when the relevant equipment state changes. 

You can use equipment synchronization status subscriptions together to deliver a detailed view of the overall synchronization health of the system. 

**Example API response**

```plaintext
[
  {
    "ResourceAddress": "/cluster/node/compute-1.example.com/sync/sync-status/sync-state",
    "EndpointUri": "http://localhost:9043/api/ocloudNotifications/v2/dummy",
    "SubscriptionId": "4ea72bfa-185c-4703-9694-cdd0434cd570",
    "UriLocation": "http://localhost:9043/api/ocloudNotifications/v2/publishers/4ea72bfa-185c-4703-9694-cdd0434cd570"
  },
  {
    "ResourceAddress": "/cluster/node/compute-1.example.com/sync/sync-status/os-clock-sync-state",
    "EndpointUri": "http://localhost:9043/api/ocloudNotifications/v2/dummy",
    "SubscriptionId": "71fbb38e-a65d-41fc-823b-d76407901087",
    "UriLocation": "http://localhost:9043/api/ocloudNotifications/v2/publishers/71fbb38e-a65d-41fc-823b-d76407901087"
  },
  {
    "ResourceAddress": "/cluster/node/compute-1.example.com/sync/ptp-status/clock-class",
    "EndpointUri": "http://localhost:9043/api/ocloudNotifications/v2/dummy",
    "SubscriptionId": "7bc27cad-03f4-44a9-8060-a029566e7926",
    "UriLocation": "http://localhost:9043/api/ocloudNotifications/v2/publishers/7bc27cad-03f4-44a9-8060-a029566e7926"
  },
  {
    "ResourceAddress": "/cluster/node/compute-1.example.com/sync/ptp-status/lock-state",
    "EndpointUri": "http://localhost:9043/api/ocloudNotifications/v2/dummy",
    "SubscriptionId": "6e7b6736-f359-46b9-991c-fbaed25eb554",
    "UriLocation": "http://localhost:9043/api/ocloudNotifications/v2/publishers/6e7b6736-f359-46b9-991c-fbaed25eb554"
  },
  {
    "ResourceAddress": "/cluster/node/compute-1.example.com/sync/gnss-status/gnss-sync-status",
    "EndpointUri": "http://localhost:9043/api/ocloudNotifications/v2/dummy",
    "SubscriptionId": "31bb0a45-7892-45d4-91dd-13035b13ed18",
    "UriLocation": "http://localhost:9043/api/ocloudNotifications/v2/publishers/31bb0a45-7892-45d4-91dd-13035b13ed18"
  }
]
```


Table 9.19. HTTP response codesHTTP response| Description  
---|---  
200 OK  |  Success   
Show more

### 9.4.1.19. api/ocloudNotifications/v2/{resource_address}/CurrentState

### 9.4.1.20. HTTP method

`GET api/ocloudNotifications/v2/cluster/node/{node_name}/sync/ptp-status/lock-state/CurrentState`

`GET api/ocloudNotifications/v2/cluster/node/{node_name}/sync/sync-status/os-clock-sync-state/CurrentState`

`GET api/ocloudNotifications/v2/cluster/node/{node_name}/sync/ptp-status/clock-class/CurrentState`

`GET api/ocloudNotifications/v2/cluster/node/{node_name}/sync/sync-status/sync-state/CurrentState`

`GET api/ocloudNotifications/v2/cluster/node/{node_name}/sync/gnss-status/gnss-sync-state/CurrentState`

### 9.4.1.21. Description

Returns the current state of the `os-clock-sync-state`, `clock-class`, `lock-state`, `gnss-sync-status`, or `sync-state` events for the cluster node. 

  * `os-clock-sync-state` notifications describe the host operating system clock synchronization state. Can be in `LOCKED` or `FREERUN` state. 
  * `clock-class` notifications describe the current state of the PTP clock class. 
  * `lock-state` notifications describe the current status of the PTP equipment lock state. Can be in `LOCKED`, `HOLDOVER` or `FREERUN` state. 
  * `sync-state` notifications describe the current status of the least synchronized of the PTP clock `lock-state` and `os-clock-sync-state` states. 
  * `gnss-sync-status` notifications describe the GNSS clock synchronization state. 



Table 9.20. Global path parametersParameter| Type  
---|---  
`resource_address` |  string   
Show more

**Example lock-state API response**

```plaintext
{
  "id": "c1ac3aa5-1195-4786-84f8-da0ea4462921",
  "type": "event.sync.ptp-status.ptp-state-change",
  "source": "/cluster/node/compute-1.example.com/sync/ptp-status/lock-state",
  "dataContentType": "application/json",
  "time": "2023-01-10T02:41:57.094981478Z",
  "data": {
    "version": "1.0",
    "values": [
      {
        "ResourceAddress": "/cluster/node/compute-1.example.com/ens5fx/master",
        "data_type": "notification",
        "value_type": "enumeration",
        "value": "LOCKED"
      },
      {
        "ResourceAddress": "/cluster/node/compute-1.example.com/ens5fx/master",
        "data_type": "metric",
        "value_type": "decimal64.3",
        "value": "29"
      }
    ]
  }
}
```


**Example os-clock-sync-state API response**

```plaintext
{
  "specversion": "0.3",
  "id": "4f51fe99-feaa-4e66-9112-66c5c9b9afcb",
  "source": "/cluster/node/compute-1.example.com/sync/sync-status/os-clock-sync-state",
  "type": "event.sync.sync-status.os-clock-sync-state-change",
  "subject": "/cluster/node/compute-1.example.com/sync/sync-status/os-clock-sync-state",
  "datacontenttype": "application/json",
  "time": "2022-11-29T17:44:22.202Z",
  "data": {
    "version": "1.0",
    "values": [
      {
        "ResourceAddress": "/cluster/node/compute-1.example.com/CLOCK_REALTIME",
        "data_type": "notification",
        "value_type": "enumeration",
        "value": "LOCKED"
      },
      {
        "ResourceAddress": "/cluster/node/compute-1.example.com/CLOCK_REALTIME",
        "data_type": "metric",
        "value_type": "decimal64.3",
        "value": "27"
      }
    ]
  }
}
```


**Example clock-class API response**

```plaintext
{
  "id": "064c9e67-5ad4-4afb-98ff-189c6aa9c205",
  "type": "event.sync.ptp-status.ptp-clock-class-change",
  "source": "/cluster/node/compute-1.example.com/sync/ptp-status/clock-class",
  "dataContentType": "application/json",
  "time": "2023-01-10T02:41:56.785673989Z",
  "data": {
    "version": "1.0",
    "values": [
      {
        "ResourceAddress": "/cluster/node/compute-1.example.com/ens5fx/master",
        "data_type": "metric",
        "value_type": "decimal64.3",
        "value": "165"
      }
    ]
  }
}
```


**Example sync-state API response**

```plaintext
{
    "specversion": "0.3",
    "id": "8c9d6ecb-ae9f-4106-82c4-0a778a79838d",
    "source": "/sync/sync-status/sync-state",
    "type": "event.sync.sync-status.synchronization-state-change",
    "subject": "/cluster/node/compute-1.example.com/sync/sync-status/sync-state",
    "datacontenttype": "application/json",
    "time": "2024-08-28T14:50:57.327585316Z",
    "data":
    {
        "version": "1.0",
        "values": [
        {
            "ResourceAddress": "/cluster/node/compute-1.example.com/sync/sync-status/sync-state",
            "data_type": "notification",
            "value_type": "enumeration",
            "value": "LOCKED"
        }]
    }
}
```


**Example gnss-sync-state API response**

```plaintext
{
  "id": "435e1f2a-6854-4555-8520-767325c087d7",
  "type": "event.sync.gnss-status.gnss-state-change",
  "source": "/cluster/node/compute-1.example.com/sync/gnss-status/gnss-sync-status",
  "dataContentType": "application/json",
  "time": "2023-09-27T19:35:33.42347206Z",
  "data": {
    "version": "1.0",
    "values": [
      {
        "ResourceAddress": "/cluster/node/compute-1.example.com/ens2fx/master",
        "data_type": "notification",
        "value_type": "enumeration",
        "value": "SYNCHRONIZED"
      },
      {
        "ResourceAddress": "/cluster/node/compute-1.example.com/ens2fx/master",
        "data_type": "metric",
        "value_type": "decimal64.3",
        "value": "5"
      }
    ]
  }
}
```
