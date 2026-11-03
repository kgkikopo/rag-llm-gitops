# 19.1. Install the Red Hat Quay Container Security Operator

You can install the Red Hat Quay Container Security Operator from the OpenShift Container Platform web console OperatorHub, or by using the CLI. 

**Prerequisites**

  * You have installed the `oc` CLI. 
  * You have access to the web console as a user with `cluster-admin` privileges. 
  * You have containers that come from a Red Hat Quay or Quay.io registry running on your cluster. 



**Procedure**

  1. You can install the Red Hat Quay Container Security Operator by using the OpenShift Container Platform web console: 

     1. On the web console, navigate to **Ecosystem** **Software Catalog** and select **Security**. 
     2. Select the **Red Hat Quay Container Security Operator** Operator, and then select **Install**. 
     3. On the **Red Hat Quay Container Security Operator** page, select **Install**. **Update channel** , **Installation mode** , and **Update approval** are selected automatically. The **Installed Namespace** field defaults to `openshift-operators`. You can adjust these settings as needed. 
     4. Select **Install**. The **Red Hat Quay Container Security Operator** is displayed after a few moments on the **Installed Operators** page. 
     5. Optional: You can add custom certificates to the Red Hat Quay Container Security Operator. For example, create a certificate named `quay.crt` in the current directory. Then, run the following command to add the custom certificate to the Red Hat Quay Container Security Operator: 

```shell-session
$ oc create secret generic container-security-operator-extra-certs --from-file=quay.crt -n openshift-operators
```


     6. Optional: If you added a custom certificate, restart the Red Hat Quay Container Security Operator pod for the new certificates to take effect. 

  2. Alternatively, you can install the Red Hat Quay Container Security Operator by using the CLI: 

     1. Retrieve the latest version of the Container Security Operator and its channel by entering the following command: 

```shell-session
$ oc get packagemanifests container-security-operator \
  -o jsonpath='{range .status.channels[*]}{@.currentCSV} {@.name}{"\n"}{end}' \
  | awk '{print "STARTING_CSV=" $1 " CHANNEL=" $2 }' \
  | sort -Vr \
  | head -1
```


**Example output**

```shell-session
STARTING_CSV=container-security-operator.v3.8.9 CHANNEL=stable-3.8
```


     2. Using the output from the previous command, create a `Subscription` custom resource for the Red Hat Quay Container Security Operator and save it as `container-security-operator.yaml`. For example: 

```yaml
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: container-security-operator
  namespace: openshift-operators
spec:
  channel: ${CHANNEL}
  installPlanApproval: Automatic
  name: container-security-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace
  startingCSV: ${STARTING_CSV}
```


where: 

`spec.channel`
     Specifies the values you obtained in the previous step for the `spec.channel`. 
`spec.startingCSV`
     Specifies the value you obtained in the previous step for the `spec.startingCSV` parameter. 

     3. Enter the following command to apply the configuration: 

```shell-session
$ oc apply -f container-security-operator.yaml
```


**Example output**

```shell-session
subscription.operators.coreos.com/container-security-operator created
```
