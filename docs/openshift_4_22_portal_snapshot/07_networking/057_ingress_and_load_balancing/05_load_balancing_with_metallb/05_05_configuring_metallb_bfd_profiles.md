# 5.5. Configuring MetalLB BFD profiles

As a cluster administrator, you can add, modify, and delete Bidirectional Forwarding Detection (BFD) profiles. The MetalLB Operator uses the BFD profile custom resources to identify which BGP sessions use BFD to provide faster path failure detection than BGP alone provides. 

## 5.5.1. About the BFD profile custom resource

As a cluster administrator, you can specify parameters in the BFD profile CR. The MetalLB Operator uses the BFD profile custom resources to identify which BGP sessions use BFD to provide faster path failure detection than BGP alone provides. 

The following table describes parameters for the BFD profile CR: 

Table 5.8. BFD profile custom resourceParameter| Type| Description  
---|---|---  
`metadata.name` |  `string` |  Specifies the name for the BFD profile custom resource.   
`metadata.namespace` |  `string` |  Specifies the namespace for the BFD profile custom resource.   
`spec.detectMultiplier` |  `integer` |  Specifies the detection multiplier to determine packet loss. The remote transmission interval is multiplied by this value to determine the connection loss detection timer.  For example, when the local system has the detect multiplier set to `3` and the remote system has the transmission interval set to `300`, the local system detects failures only after `900` ms without receiving packets. The range is `2` to `255`. The default value is `3`.   
`spec.echoMode` |  `boolean` |  Specifies the echo transmission mode. If you are not using distributed BFD, echo transmission mode works only when the peer is also FRR. The default value is `false` and echo transmission mode is disabled.  When echo transmission mode is enabled, consider increasing the transmission interval of control packets to reduce bandwidth usage. For example, consider increasing the transmit interval to `2000` ms.   
`spec.echoInterval` |  `integer` |  Specifies the minimum transmission interval, less jitter, that this system uses to send and receive echo packets. The range is `10` to `60000`. The default value is `50` ms.   
`spec.minimumTtl` |  `integer` |  Specifies the minimum expected TTL for an incoming control packet. This field applies to multi-hop sessions only.  The purpose of setting a minimum TTL is to make the packet validation requirements more stringent and avoid receiving control packets from other sessions. The default value is `254` and indicates that the system expects only one hop between this system and the peer.   
`spec.passiveMode` |  `boolean` |  Specifies whether a session is marked as active or passive. A passive session does not attempt to start the connection. Instead, a passive session waits for control packets from a peer before it begins to reply.  Marking a session as passive is useful when you have a router that acts as the central node of a star network and you want to avoid sending control packets that you do not need the system to send. The default value is `false` and marks the session as active.   
`spec.receiveInterval` |  `integer` |  Specifies the minimum interval that this system is capable of receiving control packets. The range is `10` to `60000`. The default value is `300` ms.   
`spec.transmitInterval` |  `integer` |  Specifies the minimum transmission interval, less jitter, that this system uses to send control packets. The range is `10` to `60000`. The default value is `300` ms.   
Show more

## 5.5.2. Configure a BFD profile

To achieve faster path failure detection for BGP sessions, configure a MetalLB BFD profile and associate it with a BGP peer. Establishing these profiles ensures that your network routing remains highly available and responsive by identifying connectivity issues more rapidly than standard protocols. 

**Prerequisites**

  * Install the OpenShift CLI (`oc`). 
  * Log in as a user with `cluster-admin` privileges. 



**Procedure**

  1. Create a file, such as `bfdprofile.yaml`, with content like the following example: 

```yaml
apiVersion: metallb.io/v1beta1
kind: BFDProfile
metadata:
  name: doc-example-bfd-profile-full
  namespace: metallb-system
spec:
  receiveInterval: 300
  transmitInterval: 300
  detectMultiplier: 3
  echoMode: false
  passiveMode: true
  minimumTtl: 254
# ...
```


  2. Apply the configuration for the BFD profile: 

```shell-session
$ oc apply -f bfdprofile.yaml
```


## 5.5.3. Additional resources

  * [Configuring MetalLB BGP peers](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/ingress_and_load_balancing/load-balancing-with-metallb#metallb-configure-bgp-peers "5.3. Configuring MetalLB BGP peers")
