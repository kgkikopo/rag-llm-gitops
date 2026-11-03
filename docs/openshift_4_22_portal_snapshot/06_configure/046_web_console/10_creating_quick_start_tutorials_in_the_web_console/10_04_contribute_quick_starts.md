# 10.4. Contribute quick starts

OpenShift Container Platform introduces the quick start custom resource, which is defined by a `ConsoleQuickStart` object. Operators and administrators can use this resource to contribute quick starts to the cluster. 

**Prerequisites**

  * You must have cluster administrator privileges. 



**Procedure**

  1. To create a new quick start, run: 

```yaml
$ oc get -o yaml consolequickstart spring-with-s2i > my-quick-start.yaml
```


  2. Run: 

```yaml
$ oc create -f my-quick-start.yaml
```


  3. Update the YAML file using the guidance outlined in this documentation. 
  4. Save your edits. 



## 10.4.1. View the quick start API documentation

You can view the API documentation for the `ConsoleQuickStart` resource by using the `oc explain` command. 

**Procedure**

  * To see the quick start API documentation, run: 

```shell-session
$ oc explain consolequickstarts
```


Run `oc explain -h` for more information about `oc explain` usage. 




## 10.4.2. Map the elements in the quick start to the quick start CR

These mappings show where each part of the quick start custom resource (CR) is displayed in the quick start within the web console. 

### 10.4.2.1. Conclusion element

**Viewing the conclusion element in the YAML file**

```yaml
...
summary:
  failed: Try the steps again.
  success: Your Spring application is running.
title: Run the Spring application
conclusion: >-
  Your Spring application is deployed and ready.
```


The `conclusion` field defines the conclusion text. 

In the web console, the conclusion is displayed in the last section of the quick start. 

![quick start conclusion in the web console](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Web_console-en-US/images/14b1853045f55716968f590d570f761c/quick-start-conclusion.png) ![quick start conclusion in the web console](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Web_console-en-US/images/14b1853045f55716968f590d570f761c/quick-start-conclusion.png)

### 10.4.2.2. Description element

**Viewing the description element in the YAML file**

```yaml
apiVersion: console.openshift.io/v1
kind: ConsoleQuickStart
metadata:
  name: spring-with-s2i
spec:
  description: 'Import a Spring Application from git, build, and deploy it onto OpenShift.'
...
```


The `description` field defines the description text. 

In the web console, the description is displayed on the introductory tile of the quick start on the **Quick Starts** page. 

![quick start description in the web console](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Web_console-en-US/images/8c42497a050b11a695ce290ab035e31a/quick-start-description.png) ![quick start description in the web console](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Web_console-en-US/images/8c42497a050b11a695ce290ab035e31a/quick-start-description.png)

### 10.4.2.3. The displayName element

**Viewing the`displayName` element in the YAML file**

```yaml
apiVersion: console.openshift.io/v1
kind: ConsoleQuickStart
metadata:
  name: spring-with-s2i
spec:
  description: 'Import a Spring Application from git, build, and deploy it onto OpenShift.'
  displayName: Get started with Spring
  durationMinutes: 10
```


The `displayName` field defines the display name text. 

In the web console, the display name is displayed on the introductory tile of the quick start on the **Quick Starts** page. 

![quick start display name in the web console](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Web_console-en-US/images/530e6950f1fad49a87dd721f8656457b/quick-start-display-name.png) ![quick start display name in the web console](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Web_console-en-US/images/530e6950f1fad49a87dd721f8656457b/quick-start-display-name.png)

### 10.4.2.4. The durationMinutes element

**Viewing the`durationMinutes` element in the YAML file**

```yaml
apiVersion: console.openshift.io/v1
kind: ConsoleQuickStart
metadata:
  name: spring-with-s2i
spec:
  description: 'Import a Spring Application from git, build, and deploy it onto OpenShift.'
  displayName: Get started with Spring
  durationMinutes: 10
```


The `durationMinutes` field defines, in minutes, how long the quick start should take to complete. 

In the web console, the duration minutes element is displayed on the introductory tile of the quick start on the **Quick Starts** page. 

![quick start durationMinutes element in the web console](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Web_console-en-US/images/18cd61484b9c004a0cd15cb41bfea8a0/quick-start-duration.png) ![quick start durationMinutes element in the web console](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Web_console-en-US/images/18cd61484b9c004a0cd15cb41bfea8a0/quick-start-duration.png)

### 10.4.2.5. Icon element

**Viewing the icon element in the YAML file**

```yaml
...
spec:
  description: 'Import a Spring Application from git, build, and deploy it onto OpenShift.'
  displayName: Get started with Spring
  durationMinutes: 10
  icon: >-
    data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGlkPSJMYXllcl8xIiBkYXRhLW5hbWU9IkxheWVyIDEiIHZpZXdCb3g9IjAgMCAxMDI0IDEwMjQiPjxkZWZzPjxzdHlsZT4uY2xzLTF7ZmlsbDojMTUzZDNjO30uY2xzLTJ7ZmlsbDojZDhkYTlkO30uY2xzLTN7ZmlsbDojNThjMGE4O30uY2xzLTR7ZmlsbDojZmZmO30uY2xzLTV7ZmlsbDojM2Q5MTkxO308L3N0eWxlPjwvZGVmcz48dGl0bGU+c25vd2Ryb3BfaWNvbl9yZ2JfZGVmYXVsdDwvdGl0bGU+PHBhdGggY2xhc3M9ImNscy0xIiBkPSJNMTAxMi42OSw1OTNjLTExLjEyLTM4LjA3LTMxLTczLTU5LjIxLTEwMy44LTkuNS0xMS4zLTIzLjIxLTI4LjI5LTM5LjA2LTQ3Ljk0QzgzMy41MywzNDEsNzQ1LjM3LDIzNC4xOCw2NzQsMTY4Ljk0Yy01LTUuMjYtMTAuMjYtMTAuMzEtMTUuNjUtMTUuMDdhMjQ2LjQ5LDI0Ni40OSwwLDAsMC0zNi41NS0yNi44LDE4Mi41LDE4Mi41LDAsMCwwLTIwLjMtMTEuNzcsMjAxLjUzLDIwMS41MywwLDAsMC00My4xOS0xNUExNTUuMjQsMTU1LjI0LDAsMCwwLDUyOCw5NS4yYy02Ljc2LS42OC0xMS43NC0uODEtMTQuMzktLjgxaDBsLTEuNjIsMC0xLjYyLDBhMTc3LjMsMTc3LjMsMCwwLDAtMzEuNzcsMy4zNSwyMDguMjMsMjA4LjIzLDAsMCwwLTU2LjEyLDE3LjU2LDE4MSwxODEsMCwwLDAtMjAuMjcsMTEuNzUsMjQ3LjQzLDI0Ny40MywwLDAsMC0zNi41NywyNi44MUMzNjAuMjUsMTU4LjYyLDM1NSwxNjMuNjgsMzUwLDE2OWMtNzEuMzUsNjUuMjUtMTU5LjUsMTcyLTI0MC4zOSwyNzIuMjhDOTMuNzMsNDYwLjg4LDgwLDQ3Ny44Nyw3MC41Miw0ODkuMTcsNDIuMzUsNTIwLDIyLjQzLDU1NC45LDExLjMxLDU5MywuNzIsNjI5LjIyLTEuNzMsNjY3LjY5LDQsNzA3LjMxLDE1LDc4Mi40OSw1NS43OCw4NTkuMTIsMTE4LjkzLDkyMy4wOWEyMiwyMiwwLDAsMCwxNS41OSw2LjUyaDEuODNsMS44Ny0uMzJjODEuMDYtMTMuOTEsMTEwLTc5LjU3LDE0My40OC0xNTUuNiwzLjkxLTguODgsNy45NS0xOC4wNSwxMi4yLTI3LjQzcTUuNDIsOC41NCwxMS4zOSwxNi4yM2MzMS44NSw0MC45MSw3NS4xMiw2NC42NywxMzIuMzIsNzIuNjNsMTguOCwyLjYyLDQuOTUtMTguMzNjMTMuMjYtNDkuMDcsMzUuMy05MC44NSw1MC42NC0xMTYuMTksMTUuMzQsMjUuMzQsMzcuMzgsNjcuMTIsNTAuNjQsMTE2LjE5bDUsMTguMzMsMTguOC0yLjYyYzU3LjItOCwxMDAuNDctMzEuNzIsMTMyLjMyLTcyLjYzcTYtNy42OCwxMS4zOS0xNi4yM2M0LjI1LDkuMzgsOC4yOSwxOC41NSwxMi4yLDI3LjQzLDMzLjQ5LDc2LDYyLjQyLDE0MS42OSwxNDMuNDgsMTU1LjZsMS44MS4zMWgxLjg5YTIyLDIyLDAsMCwwLDE1LjU5LTYuNTJjNjMuMTUtNjQsMTAzLjk1LTE0MC42LDExNC44OS0yMTUuNzhDMTAyNS43Myw2NjcuNjksMTAyMy4yOCw2MjkuMjIsMTAxMi42OSw1OTNaIi8+PHBhdGggY2xhc3M9ImNscy0yIiBkPSJNMzY0LjE1LDE4NS4yM2MxNy44OS0xNi40LDM0LjctMzAuMTUsNDkuNzctNDAuMTFhMjEyLDIxMiwwLDAsMSw2NS45My0yNS43M0ExOTgsMTk4LDAsMCwxLDUxMiwxMTYuMjdhMTk2LjExLDE5Ni4xMSwwLDAsMSwzMiwzLjFjNC41LjkxLDkuMzYsMi4wNiwxNC41MywzLjUyLDYwLjQxLDIwLjQ4LDg0LjkyLDkxLjA1LTQ3LjQ0LDI0OC4wNi0yOC43NSwzNC4xMi0xNDAuNywxOTQuODQtMTg0LjY2LDI2OC40MmE2MzAuODYsNjMwLjg2LDAsMCwwLTMzLjIyLDU4LjMyQzI3Niw2NTUuMzQsMjY1LjQsNTk4LDI2NS40LDUyMC4yOSwyNjUuNCwzNDAuNjEsMzExLjY5LDI0MC43NCwzNjQuMTUsMTg1LjIzWiIvPjxwYXRoIGNsYXNzPSJjbHMtMyIgZD0iTTUyNy41NCwzODQuODNjODQuMDYtOTkuNywxMTYuMDYtMTc3LjI4LDk1LjIyLTIzMC43NCwxMS42Miw4LjY5LDI0LDE5LjIsMzcuMDYsMzEuMTMsNTIuNDgsNTUuNSw5OC43OCwxNTUuMzgsOTguNzgsMzM1LjA3LDAsNzcuNzEtMTAuNiwxMzUuMDUtMjcuNzcsMTc3LjRhNjI4LjczLDYyOC43MywwLDAsMC0zMy4yMy01OC4zMmMtMzktNjUuMjYtMTMxLjQ1LTE5OS0xNzEuOTMtMjUyLjI3QzUyNi4zMywzODYuMjksNTI3LDM4NS41Miw1MjcuNTQsMzg0LjgzWiIvPjxwYXRoIGNsYXNzPSJjbHMtNCIgZD0iTTEzNC41OCw5MDguMDdoLS4wNmEuMzkuMzksMCwwLDEtLjI3LS4xMWMtMTE5LjUyLTEyMS4wNy0xNTUtMjg3LjQtNDcuNTQtNDA0LjU4LDM0LjYzLTQxLjE0LDEyMC0xNTEuNiwyMDIuNzUtMjQyLjE5LTMuMTMsNy02LjEyLDE0LjI1LTguOTIsMjEuNjktMjQuMzQsNjQuNDUtMzYuNjcsMTQ0LjMyLTM2LjY3LDIzNy40MSwwLDU2LjUzLDUuNTgsMTA2LDE2LjU5LDE0Ny4xNEEzMDcuNDksMzA3LjQ5LDAsMCwwLDI4MC45MSw3MjNDMjM3LDgxNi44OCwyMTYuOTMsODkzLjkzLDEzNC41OCw5MDguMDdaIi8+PHBhdGggY2xhc3M9ImNscy01IiBkPSJNNTgzLjQzLDgxMy43OUM1NjAuMTgsNzI3LjcyLDUxMiw2NjQuMTUsNTEyLDY2NC4xNXMtNDguMTcsNjMuNTctNzEuNDMsMTQ5LjY0Yy00OC40NS02Ljc0LTEwMC45MS0yNy41Mi0xMzUuNjYtOTEuMThhNjQ1LjY4LDY0NS42OCwwLDAsMSwzOS41Ny03MS41NGwuMjEtLjMyLjE5LS4zM2MzOC02My42MywxMjYuNC0xOTEuMzcsMTY3LjEyLTI0NS42Niw0MC43MSw1NC4yOCwxMjkuMSwxODIsMTY3LjEyLDI0NS42NmwuMTkuMzMuMjEuMzJhNjQ1LjY4LDY0NS42OCwwLDAsMSwzOS41Nyw3MS41NEM2ODQuMzQsNzg2LjI3LDYzMS44OCw4MDcuMDUsNTgzLjQzLDgxMy43OVoiLz48cGF0aCBjbGFzcz0iY2xzLTQiIGQ9Ik04ODkuNzUsOTA4YS4zOS4zOSwwLDAsMS0uMjcuMTFoLS4wNkM4MDcuMDcsODkzLjkzLDc4Nyw4MTYuODgsNzQzLjA5LDcyM2EzMDcuNDksMzA3LjQ5LDAsMCwwLDIwLjQ1LTU1LjU0YzExLTQxLjExLDE2LjU5LTkwLjYxLDE2LjU5LTE0Ny4xNCwwLTkzLjA4LTEyLjMzLTE3My0zNi42Ni0yMzcuNHEtNC4yMi0xMS4xNi04LjkzLTIxLjdjODIuNzUsOTAuNTksMTY4LjEyLDIwMS4wNSwyMDIuNzUsMjQyLjE5QzEwNDQuNzksNjIwLjU2LDEwMDkuMjcsNzg2Ljg5LDg4OS43NSw5MDhaIi8+PC9zdmc+Cg==
...
```


The `icon` field defines the icon as a base64 value. 

In the web console, the icon is displayed on the introductory tile of the quick start on the **Quick Starts** page. 

![quick start icon element in the web console](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Web_console-en-US/images/4331b5eb1c15bacda48ab67e66d797c2/quick-start-icon.png) ![quick start icon element in the web console](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Web_console-en-US/images/4331b5eb1c15bacda48ab67e66d797c2/quick-start-icon.png)

### 10.4.2.6. Introduction element

**Viewing the introduction element in the YAML file**

```yaml
...
  introduction: >-
    **Spring** is a Java framework for building applications based on a distributed microservices architecture.

    - Spring enables easy packaging and configuration of Spring applications into a self-contained executable application which can be easily deployed as a container to OpenShift.

    - Spring applications can integrate OpenShift capabilities to provide a natural "Spring on OpenShift" developer experience for both existing and net-new Spring applications. For example:

    - Externalized configuration using Kubernetes ConfigMaps and integration with Spring Cloud Kubernetes

    - Service discovery using Kubernetes Services

    - Load balancing with Replication Controllers

    - Kubernetes health probes and integration with Spring Actuator

    - Metrics: Prometheus, Grafana, and integration with Spring Cloud Sleuth

    - Distributed tracing with Istio

    - Developer tooling through Red Hat OpenShift and Red Hat CodeReady developer tooling to quickly scaffold new Spring projects, gain access to familiar Spring APIs in your favorite IDE, and deploy to Red Hat OpenShift
...
```


The `introduction` field introduces the quick start and lists the tasks within it. 

In the web console, after you click a quick start card, a side panel slides in that introduces the quick start and lists the tasks within it. 

![quick start introduction element in the web console](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Web_console-en-US/images/cdc65cf85d34b09431f96036bb3b65ac/quick-start-introduction.png) ![quick start introduction element in the web console](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Web_console-en-US/images/cdc65cf85d34b09431f96036bb3b65ac/quick-start-introduction.png)

## 10.4.3. Add a custom icon to a quick start

A default icon is provided for all quick starts. You can provide your own custom icon. 

**Procedure**

  1. Find the `.svg` file that you want to use as your custom icon. 
  2. Use an [online tool to convert the text to base64](https://cryptii.com/pipes/text-to-base64). 
  3. In the YAML file, add `icon: >-`, then on the next line include `data:image/svg+xml;base64` followed by the output from the base64 conversion. For example: 

```yaml
icon: >-
   data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgdmlld.
```


## 10.4.4. Limit access to a quick start

Not all quick starts should be available for everyone. The `accessReviewResources` section of the YAML file provides the ability to limit access to the quick start. 

To only allow the user to access the quick start if they have the ability to create `HelmChartRepository` resources, use the following configuration: 

```yaml
accessReviewResources:
  - group: helm.openshift.io
    resource: helmchartrepositories
    verb: create
```


To only allow the user to access the quick start if they have the ability to list Operator groups and package manifests, thus ability to install Operators, use the following configuration: 

```yaml
accessReviewResources:
  - group: operators.coreos.com
    resource: operatorgroups
    verb: list
  - group: packages.operators.coreos.com
    resource: packagemanifests
    verb: list
```


## 10.4.5. Link to other quick starts

You can link a quick start to another quick start by setting the `nextQuickStart` field. 

In the `nextQuickStart` section of the YAML file, enter the `name`, not the `displayName`, of the quick start to which you want to link. For example: 

```yaml
nextQuickStart:
  - add-healthchecks
```


## 10.4.6. Supported tags for quick starts

Write your quick start content in markdown using these tags. The markdown is converted to HTML. 

Tag| Description  
---|---  
`'b',` |  Defines bold text.   
`'img',` |  Embeds an image.   
`'i',` |  Defines italic text.   
`'strike',` |  Defines strike-through text.   
`'s',` |  Defines smaller text   
`'del',` |  Defines smaller text.   
`'em',` |  Defines emphasized text.   
`'strong',` |  Defines important text.   
`'a',` |  Defines an anchor tag.   
`'p',` |  Defines paragraph text.   
`'h1',` |  Defines a level 1 heading.   
`'h2',` |  Defines a level 2 heading.   
`'h3',` |  Defines a level 3 heading.   
`'h4',` |  Defines a level 4 heading.   
`'ul',` |  Defines an unordered list.   
`'ol',` |  Defines an ordered list.   
`'li',` |  Defines a list item.   
`'code',` |  Defines a text as code.   
`'pre',` |  Defines a block of preformatted text.   
`'button',` |  Defines a button in text.   
Show more

## 10.4.7. Quick start highlighting markdown reference

You can use highlighting, or hints, in a quick start to add a link that highlights and animates a component of the web console. 

The markdown syntax contains: 

  * Bracketed link text 
  * The `highlight` keyword, followed by the ID of the element that you want to animate 



### 10.4.7.1. Perspective switcher

```plaintext
[Perspective switcher]{{highlight qs-perspective-switcher}}
```


### 10.4.7.2. Administrator perspective navigation links

```plaintext
[Home]{{highlight qs-nav-home}}
[Operators]{{highlight qs-nav-operators}}
[Workloads]{{highlight qs-nav-workloads}}
[Serverless]{{highlight qs-nav-serverless}}
[Networking]{{highlight qs-nav-networking}}
[Storage]{{highlight qs-nav-storage}}
[Service catalog]{{highlight qs-nav-servicecatalog}}
[Compute]{{highlight qs-nav-compute}}
[User management]{{highlight qs-nav-usermanagement}}
[Administration]{{highlight qs-nav-administration}}
```


### 10.4.7.3. Developer perspective navigation links

```plaintext
[Add]{{highlight qs-nav-add}}
[Topology]{{highlight qs-nav-topology}}
[Search]{{highlight qs-nav-search}}
[Project]{{highlight qs-nav-project}}
[Helm]{{highlight qs-nav-helm}}
```


### 10.4.7.4. Common navigation links

```plaintext
[Builds]{{highlight qs-nav-builds}}
[Pipelines]{{highlight qs-nav-pipelines}}
[Monitoring]{{highlight qs-nav-monitoring}}
```


### 10.4.7.5. Masthead links

```plaintext
[CloudShell]{{highlight qs-masthead-cloudshell}}
[Utility Menu]{{highlight qs-masthead-utilitymenu}}
[User Menu]{{highlight qs-masthead-usermenu}}
[Applications]{{highlight qs-masthead-applications}}
[Import]{{highlight qs-masthead-import}}
[Help]{{highlight qs-masthead-help}}
[Notifications]{{highlight qs-masthead-notifications}}
```


## 10.4.8. Code snippet markdown reference

Embed executable and copyable CLI code snippets in a quick start using this markdown syntax. Executing a snippet requires the Web Terminal Operator; copying works with or without it installed. 

### 10.4.8.1. Syntax for inline code snippets

```plaintext
`code block`{{copy}}
`code block`{{execute}}
```


Note

If the `execute` syntax is used, the **Copy to clipboard** action is present whether you have the Web Terminal Operator installed or not. 

### 10.4.8.2. Syntax for multi-line code snippets

````plaintext
```
multi line code block
```{{copy}}

```
multi line code block
```{{execute}}
````
