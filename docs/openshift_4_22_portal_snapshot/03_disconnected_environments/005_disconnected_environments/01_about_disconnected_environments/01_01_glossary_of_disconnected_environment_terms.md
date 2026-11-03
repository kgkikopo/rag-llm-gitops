# 1.1. Glossary of disconnected environment terms

Although it is used throughout the OpenShift Container Platform documentation, _disconnected environment_ is a broad term that can refer to environments with various levels of internet connectivity. 

Other terms are sometimes used to refer to a specific level of internet connectivity, and these environments might require additional unique configurations. 

The following table describes the different terms used to refer to environments without a full internet connection: 

Table 1.1. Disconnected environment termsTerm| Description  
---|---  
Air-gapped network  |  An environment or network that is completely isolated from an external network.  This isolation depends on a physical separation, or an "air gap", between machines on the internal network and any other part of an external network. Air-gapped environments are often used in industries with strict security or regulatory requirements.   
Disconnected environment  |  An environment or network that has some level of isolation from an external network.  This isolation could be enabled by physical or logical separation between machines on the internal network and an external network. Regardless of the level of isolation from the external network, a cluster in a disconnected environment does not have access to public services hosted by Red Hat and requires additional setup to maintain full cluster functionality.   
Restricted Network  |  An environment or network with limited connection to an external network.  A physical connection may exist between machines on the internal network and an external network, but network traffic is limited by additional configurations, such as with firewalls and proxies.   
Show more
