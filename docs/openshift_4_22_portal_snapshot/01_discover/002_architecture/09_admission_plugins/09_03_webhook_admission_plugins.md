# 9.3. Webhook admission plugins

In addition to OpenShift Container Platform default admission plugins, you can implement dynamic admission through webhook admission plugins that call webhook servers. This approach extends the functionality of the admission chain. 

Webhook servers are called over HTTP at defined endpoints. 

There are two types of webhook admission plugins in OpenShift Container Platform: 

  * During the admission process, the _mutating admission plugin_ can perform tasks, such as injecting affinity labels. 



  * At the end of the admission process, the _validating admission plugin_ validates that an object is configured properly, for example ensuring affinity labels are as expected. If the validation passes, OpenShift Container Platform schedules the object as configured. 



When an API request comes in, mutating or validating admission plugins use the list of external webhooks in the configuration and call them in parallel: 

  * If all of the webhooks approve the request, the admission chain continues. 
  * If any of the webhooks deny the request, the admission request is denied and the reason for doing so is based on the first denial. 
  * If more than one webhook denies the admission request, only the first denial reason is returned to the user. 
  * If an error is encountered when calling a webhook, the request is either denied or the webhook is ignored depending on the error policy set. If the error policy is set to `Ignore`, the request is unconditionally accepted in the event of a failure. If the policy is set to `Fail`, failed requests are denied. Using `Ignore` can result in unpredictable behavior for all clients. 



Communication between the webhook admission plugin and the webhook server must use TLS. Generate a CA certificate and use the certificate to sign the server certificate that is used by your webhook admission server. The PEM-encoded CA certificate is supplied to the webhook admission plugin using a mechanism, such as service serving certificate secrets. 

The following diagram illustrates the sequential admission chain process within which multiple webhook servers are called. 

**Figure 9.1. API admission chain with mutating and validating admission plugins**

![API admission stage](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Architecture-en-US/images/e2115419a4f5ded9dcc282b79e84a8b2/api-admission-chain.png) ![API admission stage](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Architecture-en-US/images/e2115419a4f5ded9dcc282b79e84a8b2/api-admission-chain.png)

An example webhook admission plugin use case is where all pods must have a common set of labels. In this example, the mutating admission plugin can inject labels and the validating admission plugin can check that labels are as expected. OpenShift Container Platform would subsequently schedule pods that include required labels and reject those that do not. 

Some common webhook admission plugin use cases include: 

  * Namespace reservation. 
  * Limiting custom network resources managed by the SR-IOV network device plugin. 
  * Defining tolerations that enable taints to qualify which pods should be scheduled on a node. 
  * Pod priority class validation. 



Note

The maximum default webhook timeout value in OpenShift Container Platform is 13 seconds, and it cannot be changed.
