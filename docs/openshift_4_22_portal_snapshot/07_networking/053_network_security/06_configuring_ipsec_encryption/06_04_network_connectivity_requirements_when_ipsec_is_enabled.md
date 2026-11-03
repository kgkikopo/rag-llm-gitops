# 6.4. Network connectivity requirements when IPsec is enabled

When IPsec is enabled in OpenShift Container Platform, you must configure the network connectivity between machines to allow cluster components to communicate. Each machine must be able to resolve the hostnames of all other machines in the cluster. 

Table 6.2. Ports used for all-machine to all-machine communicationsProtocol| Port| Description  
---|---|---  
UDP  |  `500` |  IPsec IKE packets   
`4500` |  IPsec NAT-T packets   
ESP  |  N/A  |  IPsec Encapsulating Security Payload (ESP)   
Show more
