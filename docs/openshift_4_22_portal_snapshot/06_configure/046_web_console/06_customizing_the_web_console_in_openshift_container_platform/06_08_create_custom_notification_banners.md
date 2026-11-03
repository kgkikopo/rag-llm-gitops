# 6.8. Create custom notification banners

You can create a `ConsoleNotification` custom resource to display a banner at the top or bottom of every page in the web console. 

**Prerequisites**

  * You must have administrator privileges. 



**Procedure**

  1. From **Administration** **Custom Resource Definitions** , click **ConsoleNotification**. 
  2. Select the **Instances** tab. 
  3. Click **Create Console Notification** and edit the file: 

```yaml
apiVersion: console.openshift.io/v1
kind: ConsoleNotification
metadata:
  name: example
spec:
  text: This is an example notification message with an optional link.
  location: BannerTop
  link:
    href: 'https://www.example.com'
    text: Optional link text
  color: '#fff'
  backgroundColor: '#0088ce'
```


The `location` field accepts `BannerTop`, `BannerBottom`, or `BannerTopBottom`. 

  4. Click **Create** to apply your changes.
