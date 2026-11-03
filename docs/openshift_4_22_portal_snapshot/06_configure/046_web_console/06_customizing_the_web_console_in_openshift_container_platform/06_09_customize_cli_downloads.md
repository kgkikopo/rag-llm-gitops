# 6.9. Customize CLI downloads

You can configure links for downloading the CLI with custom link text and URLs, which can point directly to file packages or to an external page that provides the packages. 

**Prerequisites**

  * You must have administrator privileges. 



**Procedure**

  1. Navigate to **Administration** **Custom Resource Definitions**. 
  2. Select **ConsoleCLIDownload** from the list of Custom Resource Definitions (CRDs). 
  3. Click the **YAML** tab, and then make your edits: 

```yaml
apiVersion: console.openshift.io/v1
kind: ConsoleCLIDownload
metadata:
  name: example-cli-download-links
spec:
  description: |
    This is an example of download links
  displayName: example
  links:
  - href: 'https://www.example.com/public/example.tar'
    text: example for linux
  - href: 'https://www.example.com/public/example.mac.zip'
    text: example for mac
  - href: 'https://www.example.com/public/example.win.zip'
    text: example for windows
```


  4. Click the **Save** button.
