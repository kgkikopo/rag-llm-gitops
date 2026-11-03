# 2.2. Troubleshoot DNS connectivity issues in a disconnected environment

If you experience health check probe issues when configuring `nmstate` in a disconnected environment, you can configure the DNS server to resolve the custom domain name instead of the default `root-servers.net` domain. 

Important

Ensure that the DNS server includes a name server (NS) entry for the `root-servers.net` zone. The DNS server does not need to forward a query to an upstream resolver, but the server must return a correct answer for the NS query. 

## 2.2.1. Configuring the bind9 DNS named server

For a cluster configured to query a `bind9` DNS server, you can add the `root-servers.net` zone to a configuration file that contains at least one DNS record. For example you can use the `/var/named/named.localhost` as a zone file that already matches this criteria. 

**Procedure**

  1. Add the `root-servers.net` zone at the end of the `/etc/named.conf` configuration file by running the following command: 

```shell-session
$ cat >> /etc/named.conf <<EOF
zone "root-servers.net" IN {
    	type master;
    	file "named.localhost";
};
EOF
```


  2. Restart the `named` service by running the following command: 

```shell-session
$ systemctl restart named
```


  3. Confirm that the `root-servers.net` zone is present by running the following command: 

```shell-session
$ journalctl -u named|grep root-servers.net
```


**Example output**

```shell-session
Jul 03 15:16:26 rhel-8-10 bash[xxxx]: zone root-servers.net/IN: loaded serial 0
Jul 03 15:16:26 rhel-8-10 named[xxxx]: zone root-servers.net/IN: loaded serial 0
```


  4. Verify that the DNS server can resolve the NS record for the `root-servers.net` domain by running the following command: 

```shell-session
$ host -t NS root-servers.net. 127.0.0.1
```


**Example output**

```shell-session
Using domain server:
Name: 127.0.0.1
Address: 127.0.0.53
Aliases:
root-servers.net name server root-servers.net.
```


## 2.2.2. Configuring the dnsmasq DNS server

If you are using `dnsmasq` as the DNS server, you can delegate resolution of the `root-servers.net` domain to another DNS server, for example, by creating a new configuration file that resolves `root-servers.net` using a DNS server that you specify. 

**Procedure**

  1. Create a configuration file that delegates the domain `root-servers.net` to another DNS server by running the following command: 

```shell-session
$ echo 'server=/root-servers.net/<DNS_server_IP>'> /etc/dnsmasq.d/delegate-root-servers.net.conf
```


  2. Restart the `dnsmasq` service by running the following command: 

```shell-session
$ systemctl restart dnsmasq
```


  3. Confirm that the `root-servers.net` domain is delegated to another DNS server by running the following command: 

```shell-session
$ journalctl -u dnsmasq|grep root-servers.net
```


**Example output**

```shell-session
Jul 03 15:31:25 rhel-8-10 dnsmasq[1342]: using nameserver 192.168.1.1#53 for domain root-servers.net
```


  4. Verify that the DNS server can resolve the NS record for the `root-servers.net` domain by running the following command: 

```shell-session
$ host -t NS root-servers.net. 127.0.0.1
```


**Example output**

```shell-session
Using domain server:
Name: 127.0.0.1
Address: 127.0.0.1#53
Aliases:
root-servers.net name server root-servers.net.
```


## 2.2.3. Creating a custom DNS host name to resolve DNS connectivity issues

In a disconnected environment where the external DNS server cannot be reached, you can resolve Kubernetes NMState Operator health probe issues by specifying a custom DNS host name in the `NMState` custom resource definition (CRD). 

**Procedure**

  1. Add the DNS host name configuration to the `NMState` CRD of your cluster: 

```yaml
apiVersion: nmstate.io/v1
kind: NMState
metadata:
  name: nmstate
spec:
  probeConfiguration:
    dns:
      host: redhat.com
# ...
```


  2. Apply the DNS host name configuration to your cluster network by running the following command. Ensure that you replace `<filename>` with the name of your CRD file. 

```yaml
$ oc apply -f <filename>.yaml
```
