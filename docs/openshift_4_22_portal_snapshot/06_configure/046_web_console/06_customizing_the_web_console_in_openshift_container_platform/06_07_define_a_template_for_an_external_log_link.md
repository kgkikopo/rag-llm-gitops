# 6.7. Define a template for an external log link

If you are connected to a service that helps you browse your logs, but you need to generate URLs in a particular way, then you can define a template for your link. 

**Prerequisites**

  * You must have administrator privileges. 



**Procedure**

  1. From **Administration** **Custom Resource Definitions** , click **ConsoleExternalLogLink**. 
  2. Select the **Instances** tab. 
  3. Click **Create Console External Log Link** and edit the file: 

```yaml
apiVersion: console.openshift.io/v1
kind: ConsoleExternalLogLink
metadata:
  name: example
spec:
  hrefTemplate: >-
    https://example.com/logs?resourceName=${resourceName}&containerName=${containerName}&resourceNamespace=${resourceNamespace}&podLabels=${podLabels}
  text: Example Logs
```
