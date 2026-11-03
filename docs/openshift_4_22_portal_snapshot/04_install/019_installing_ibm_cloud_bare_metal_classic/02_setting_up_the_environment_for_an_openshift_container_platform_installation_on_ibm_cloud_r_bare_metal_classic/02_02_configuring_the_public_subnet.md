# 2.2. Configuring the public subnet

To offer DHCP services for OpenShift Container Platform cluster nodes on the public subnet in IBM Cloud® Bare Metal (Classic), you can install and configure `dnsmasq` on the provisioner node. 

All of the OpenShift Container Platform cluster nodes must be on the public subnet. IBM Cloud® Bare Metal (Classic) does not offer a DHCP server on the subnet. Set it up separately on the provisioner node. 

You must reset the BASH variables defined when preparing the provisioner node. Rebooting the provisioner node after preparing it will delete the BASH variables set before. 

**Procedure**

  1. Install `dnsmasq`: 

```shell-session
$ sudo dnf install dnsmasq
```


  2. Open the `dnsmasq` configuration file: 

```shell-session
$ sudo vi /etc/dnsmasq.conf
```


  3. Add the following configuration to the `dnsmasq` configuration file: 

```plaintext
interface=baremetal
except-interface=lo
bind-dynamic
log-dhcp

dhcp-range=<ip_addr>,<ip_addr>,<pub_cidr>
dhcp-option=baremetal,121,0.0.0.0/0,<pub_gateway>,<prvn_priv_ip>,<prvn_pub_ip>

dhcp-hostsfile=/var/lib/dnsmasq/dnsmasq.hostsfile
```


where: 

`dhcp-range`
     Specifies the DHCP range for the `baremetal` network. Replace both instances of `<ip_addr>` with one unused IP address from the public subnet so that the range begins and ends with the same IP address. Replace `<pub_cidr>` with the CIDR of the public subnet. 
`dhcp-option`
    

Specifies the DHCP option for the `baremetal` network. Replace `<pub_gateway>` with the IP address of the gateway for the `baremetal` network. Replace `<prvn_priv_ip>` with the private IP address of the provisioner node on the `provisioning` network. Replace `<prvn_pub_ip>` with the public IP address of the provisioner node on the `baremetal` network. 

     1. To retrieve the value for `<pub_cidr>`, run the following command: 

```shell-session
$ ibmcloud sl subnet detail <publicsubnetid> --output JSON | jq .cidr
```


Replace `<publicsubnetid>` with the ID of the public subnet. 

     2. To retrieve the value for `<pub_gateway>`, run the following command: 

```shell-session
$ ibmcloud sl subnet detail <publicsubnetid> --output JSON | jq .gateway -r
```


Replace `<publicsubnetid>` with the ID of the public subnet. 

     3. To retrieve the value for `<prvn_priv_ip>`, run the following command: 

```shell-session
$ ibmcloud  sl hardware detail <id> --output JSON | \
            jq .primaryBackendIpAddress -r
```


Replace `<id>` with the ID of the provisioner node. 

     4. To retrieve the value for `<prvn_pub_ip>`, run the following command: 

```shell-session
$ ibmcloud sl hardware detail <id> --output JSON | jq .primaryIpAddress -r
```


Replace `<id>` with the ID of the provisioner node. 

  4. Obtain the list of hardware for the cluster: 

```shell-session
$ ibmcloud sl hardware list
```


  5. Obtain the MAC addresses and IP addresses for each node: 

```shell-session
$ ibmcloud sl hardware detail <id> --output JSON | \
  jq '.networkComponents[] | \
  "\(.primaryIpAddress) \(.macAddress)"' | grep -v null
```


Replace `<id>` with the ID of the node. 

**Example output**

```shell-session
"10.196.130.144 00:e0:ed:6a:ca:b4"
"141.125.65.215 00:e0:ed:6a:ca:b5"
```


Make a note of the MAC address and IP address of the public network. Make a separate note of the MAC address of the private network, which you will use later in the `install-config.yaml` file. Repeat this procedure for each node until you have all the public MAC and IP addresses for the public `baremetal` network, and the MAC addresses of the private `provisioning` network. 

  6. Add the MAC and IP address pair of the public `baremetal` network for each node into the `dnsmasq.hostsfile` file: 

```shell-session
$ sudo vim /var/lib/dnsmasq/dnsmasq.hostsfile
```


**Example input**

```plaintext
00:e0:ed:6a:ca:b5,141.125.65.215,master-0
<mac>,<ip>,master-1
<mac>,<ip>,master-2
<mac>,<ip>,worker-0
<mac>,<ip>,worker-1
...
```


Replace `<mac>,<ip>` with the public MAC address and public IP address of the corresponding node name. 

  7. Start `dnsmasq`: 

```shell-session
$ sudo systemctl start dnsmasq
```


  8. Enable `dnsmasq` so that it starts when booting the node: 

```shell-session
$ sudo systemctl enable dnsmasq
```


  9. Verify `dnsmasq` is running: 

```shell-session
$ sudo systemctl status dnsmasq
```


**Example output**

```shell-session
● dnsmasq.service - DNS caching server.
Loaded: loaded (/usr/lib/systemd/system/dnsmasq.service; enabled; vendor preset: disabled)
Active: active (running) since Tue 2021-10-05 05:04:14 CDT; 49s ago
Main PID: 3101 (dnsmasq)
Tasks: 1 (limit: 204038)
Memory: 732.0K
CGroup: /system.slice/dnsmasq.service
└─3101 /usr/sbin/dnsmasq -k
```


  10. Open ports `53` and `67` with UDP protocol: 

```shell-session
$ sudo firewall-cmd --add-port 53/udp --permanent
```


```shell-session
$ sudo firewall-cmd --add-port 67/udp --permanent
```


  11. Add `provisioning` to the external zone with masquerade: 

```shell-session
$ sudo firewall-cmd --change-zone=provisioning --zone=external --permanent
```


This step ensures network address translation for IPMI calls to the management subnet. 

  12. Reload the `firewalld` configuration: 

```shell-session
$ sudo firewall-cmd --reload
```
