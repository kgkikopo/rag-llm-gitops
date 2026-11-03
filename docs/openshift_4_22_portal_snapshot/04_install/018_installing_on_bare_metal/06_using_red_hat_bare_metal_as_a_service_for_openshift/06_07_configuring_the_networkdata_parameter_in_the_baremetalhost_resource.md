# 6.7. Configuring the networkData parameter in the BareMetalHost resource

The `networkData` field in the `BareMetalHost` custom resource (CR) allows you to control the network configuration of the bare-metal host at creation time. 

For most operating systems, this is achieved using a configuration file encapsulated in a Kubernetes secret. Then, the `cloud-init` service uses it to customize services. 

**Procedure**

  1. Create a file named `network-data.yaml` with the following content: 

```yaml
links:
  - id: <interface_id>
    type: phy
    ethernet_mac_address: <mac_address>
networks:
  - id: <interface_id>
    link: <interface_id>
    type: ipv4_dhcp
services:
  - type: dns
    address: <dns_server>
```


`<interface_id>`
     The ID of the network interface, such as `enp2s0`. 
`<mac_address>`
     The MAC address of the network interface. 
`<dns_server>`
     The IP address of the DNS server. 

  2. Create a secret from the `networkData` file by running the following command: 

```shell-session
$ oc create secret generic <hostname>-network-data \
  --from-file=networkData=network-data.yaml -n bmaas
```


`<hostname>`
     The hostname of the bare-metal host. 

  3. Configure the `BareMetalHost` to use the `networkData` file by running the following command: 

```shell-session
$ oc patch baremetalhost <hostname> -n bmaas \
  --type merge -p '{"spec":{"networkData":{"name":"<hostname>-network-data"}}}'
```
