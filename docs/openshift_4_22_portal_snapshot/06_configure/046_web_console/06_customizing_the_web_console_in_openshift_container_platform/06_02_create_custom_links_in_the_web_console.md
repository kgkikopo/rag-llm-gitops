# 6.2. Create custom links in the web console

You can create a `ConsoleLink` custom resource to add a link to the help menu, user menu, application menu, or namespace dashboard in the web console. 

**Prerequisites**

  * You must have administrator privileges. 



**Procedure**

  1. From **Administration** **Custom Resource Definitions** , click **ConsoleLink**. 
  2. Select the **Instances** tab. 
  3. Click **Create Console Link** and edit the file: 

```yaml
apiVersion: console.openshift.io/v1
kind: ConsoleLink
metadata:
  name: example
spec:
  href: 'https://www.example.com'
  location: HelpMenu
  text: Link 1
```


The `location` field accepts `HelpMenu`, `UserMenu`, `ApplicationMenu`, or `NamespaceDashboard`. 

To make the custom link appear in all namespaces, follow this example: 

```yaml
apiVersion: console.openshift.io/v1
kind: ConsoleLink
metadata:
  name: namespaced-dashboard-link-for-all-namespaces
spec:
  href: 'https://www.example.com'
  location: NamespaceDashboard
  text: This appears in all namespaces
```


To make the custom link appear in only some namespaces, follow this example: 

```yaml
apiVersion: console.openshift.io/v1
kind: ConsoleLink
metadata:
  name: namespaced-dashboard-for-some-namespaces
spec:
  href: 'https://www.example.com'
  location: NamespaceDashboard
  # This text will appear in a box called "Launcher" under "namespace" or "project" in the web console
  text: Custom Link Text
  namespaceDashboard:
    namespaces:
    # for these specific namespaces
    - my-namespace
    - your-namespace
    - other-namespace
```


To make the custom link appear in the application menu, follow this example: 

```yaml
apiVersion: console.openshift.io/v1
kind: ConsoleLink
metadata:
  name: application-menu-link-1
spec:
  href: 'https://www.example.com'
  location: ApplicationMenu
  text: Link 1
  applicationMenu:
    section: My New Section
    # image that is 24x24 in size
    imageURL: https://via.placeholder.com/24
```


  4. Click **Save** to apply your changes.
