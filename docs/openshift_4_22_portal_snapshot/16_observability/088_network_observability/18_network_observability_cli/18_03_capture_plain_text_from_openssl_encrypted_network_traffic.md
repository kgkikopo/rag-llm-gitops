# 18.3. Capture plain text from OpenSSL encrypted network traffic

Use the Network Observability CLI to capture and view plain text content from OpenSSL-encrypted network packets. This CLI-only feature uses eBPF probes to intercept and display unencrypted data without requiring TLS certificates or Operator configuration. 

## 18.3.1. Plain text packet capture for OpenSSL encrypted traffic

The Network Observability CLI packet capture feature can intercept and display the unencrypted content of OpenSSL-encrypted network traffic. 

This feature helps you debug encrypted connections when you need to inspect payload data that would otherwise be unreadable. 

The CLI uses eBPF probes to intercept OpenSSL library functions before encryption and after decryption, capturing the plain text content without requiring TLS certificates or keys. 

This is a CLI-only feature that requires no Operator or agent configuration. 

This capability is particularly valuable for the following tasks: 

  * Debugging application-level protocol issues in OpenSSL-encrypted traffic. 
  * Verifying API request and response payloads between services. 
  * Analyzing encrypted traffic content without disabling TLS. 
  * Troubleshooting encrypted connections where you lack access to certificates. 



Note

Plain text capture currently supports OpenSSL encrypted traffic only. The feature works with the `oc netobserv packets` subcommand for packet-level capture, not with flow-level capture. 

### 18.3.1.1. How plain text capture works

When you enable plain text capture during packet capture, the following actions occur: 

  1. The CLI attaches eBPF probes to OpenSSL library functions in the target process. 
  2. The probes intercept data before encryption (for outgoing traffic) and after decryption (for incoming traffic). 
  3. Plain text content is captured and displayed alongside standard packet information. 
  4. You can filter captures by pod IP, port, or other criteria to focus on specific traffic. 



### 18.3.1.2. Key considerations

When using plain text capture, consider the following conditions: 

Privileged access
     The CLI requires sufficient permissions to attach eBPF probes to running processes. You must have cluster-admin privileges or equivalent access. 
OpenSSL only
     The feature captures plain text from applications that use dynamically linked `OpenSSL` or `libssl` only. Applications that use static `OpenSSL` or other TLS libraries are not supported. 
Packet capture only
     Plain text capture works with `oc netobserv packets` for packet-level data, not with `oc netobserv flows` for flow-level aggregation. 
Performance impact
     eBPF probes have minimal performance impact, but capturing large volumes of plain text data can consume additional resources. Use filters to limit capture scope in production environments. 
Security and compliance
     Captured plain text data can contain sensitive information such as passwords, API keys, or personal data. Ensure appropriate access controls and retention policies are in place. 

## 18.3.2. Prepare for plain text packet capture

Verify that your environment meets the requirements for capturing plain text from OpenSSL-encrypted network traffic. 

**Prerequisites**

  * The OpenShift CLI (`oc`) is installed. 
  * The Network Observability CLI (`oc netobserv`) plugin is installed. 
  * You have `cluster-admin` privileges or equivalent access to run privileged operations. 



**Procedure**

  1. Verify the Network Observability CLI plugin is installed by running the following command: 

```shell-session
$ oc netobserv version
```


**Example output**

```shell-session
NetObserv CLI version 1.12.0
```


  2. Identify the target application for packet capture by running the following command: 

```shell-session
$ oc get pods -n <namespace>
```


     * Replace `<namespace>` with the name of the namespace where your pods are deployed. 
     * Note the pod name and namespace of the application that uses OpenSSL for TLS encryption. 

  3. Get the pod IP address by running the following command: 

```shell-session
$ oc get pod <pod_name> -n <namespace> -o jsonpath='{.status.podIP}'
```


  4. Identify the port the application listens on by running the following command: 

```shell-session
$ oc get pod <pod_name> -n <namespace> -o jsonpath='{.spec.containers[*].ports[*].containerPort}'
```


**Verification**

  * Verify that you have the information needed for packet capture by using the following examples: 

    * Pod IP address, such as `10.131.0.15`
    * Port number, such as `8443`
    * Pod uses OpenSSL for TLS encryption 




You can now proceed to capture packets with OpenSSL plain text. 

## 18.3.3. Capture packets that contain OpenSSL plain text

Capture network packets and view the unencrypted plain text content from OpenSSL-encrypted connections by using the Network Observability CLI. 

**Prerequisites**

  * The OpenShift CLI (`oc`) is installed. 
  * The Network Observability CLI (`oc netobserv`) plugin is installed. 
  * You have `cluster-admin` privileges. 
  * You have identified the pod IP address and port of the target application that uses OpenSSL. 



Warning

Plain text packet capture reveals unencrypted content from TLS connections, which can contain sensitive information such as passwords, API keys, or personal data. Ensure that appropriate access controls and retention policies are in place. Delete capture files securely when no longer needed. 

**Procedure**

  1. Start a packet capture with OpenSSL plain text enabled, filtering by the target pod IP and port: 

```shell-session
$ oc netobserv packets --peer_ip=<pod_ip> --port=<pod_port> --enable_openssl
```


Replace `<pod_ip>` with the pod IP address and `<pod_port>` with the port number. 

**Example**

```shell-session
$ oc netobserv packets --peer_ip=10.131.0.15 --port=8443 --enable_openssl
```


The CLI displays a live table of captured packets with plain text data from OpenSSL-encrypted connections. 

  2. Pause the capture by pressing `Ctrl`+`Space`. 
  3. Navigate the packet capture output: 

     * Use the arrow keys (`↑` `↓`) to select a packet. 
     * When the capture is paused, the selected packet’s payload is displayed in the detail panel. 
     * Press `Tab` to cycle focus between the filter input, packet table, and detail panel. 
     * Press `Esc` to resume the capture. 
     * You can also use the mouse to select packets and move focus between panels. 

  4. Optional: Apply additional filters to narrow the capture scope: 

```shell-session
$ oc netobserv packets --peer_ip=<pod_ip> --port=<pod_port> --query='SrcK8S_Namespace="<namespace>" or DstK8S_Namespace="<namespace>"' --protocol=TCP --enable_openssl
```


You can combine filters such as `--protocol`, `--query`, or other options to focus on specific traffic. Use `--query` to filter by namespace, as `--namespace` changes where the CLI components are deployed. 

  5. Optional: Capture packets to a file for later analysis: 

```shell-session
$ oc netobserv packets --peer_ip=<pod_ip> --port=<pod_port> --enable_openssl --copy
```


The CLI writes captured packet data, including plain text content, to the `./output/pcap` directory. 

  6. Stop the packet capture: 

Press `Ctrl`+`C` to stop capturing packets and return to the shell prompt. 




**Verification**

  1. If you captured packets to a file, verify the output: 

```shell-session
$ ls ./output/pcap/
```


The directory contains timestamped `.pcapng` capture files. Open a capture file with Wireshark for packet-level analysis. 

  2. Verify the captured plain text: 

```shell-session
$ ls ./output/plaintext/
```


The directory contains timestamped `.jsonl` files with decoded plain text records. 

  3. Examine a plain text capture: 

```shell-session
$ less ./output/plaintext/<timestamp>.jsonl
```


## 18.3.4. Additional resources

  * [Capture network packets with the CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_observability/network-observability-cli#network-observability-cli-capturing-packets_netobserv-cli-using "18.2.2. Capture packets")
  * [Network Observability CLI reference](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_observability/network-observability-cli#network-observability-netobserv-cli-reference_netobserv-cli-reference "18.4.1. Network Observability CLI usage")
