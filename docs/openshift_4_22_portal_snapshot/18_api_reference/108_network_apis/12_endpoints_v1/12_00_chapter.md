# Chapter 12. Endpoints [v1]

Description
    

Endpoints is a collection of endpoints that implement the actual service. Example: 

```plaintext
 Name: "mysvc",
 Subsets: [
   {
     Addresses: [{"ip": "10.10.1.1"}, {"ip": "10.10.2.2"}],
     Ports: [{"name": "a", "port": 8675}, {"name": "b", "port": 309}]
   },
   {
     Addresses: [{"ip": "10.10.3.3"}],
     Ports: [{"name": "a", "port": 93}, {"name": "b", "port": 76}]
   },
]
```


Endpoints is a legacy API and does not contain information about all Service features. Use discoveryv1.EndpointSlice for complete information about Service endpoints. 

Deprecated: This API is deprecated in v1.33+. Use discoveryv1.EndpointSlice. 

Type
     `object`

- [12.1. Specification](12_01_specification.md)
- [12.2. API endpoints](12_02_api_endpoints.md)
