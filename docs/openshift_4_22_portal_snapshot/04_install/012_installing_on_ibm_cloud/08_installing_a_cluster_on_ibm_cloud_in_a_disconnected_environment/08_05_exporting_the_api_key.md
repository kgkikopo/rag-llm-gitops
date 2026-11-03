# 8.5. Exporting the API key

You must set the API key you created as a global variable; the installation program ingests the variable during startup to set the API key. 

**Prerequisites**

  * You have created either a user API key or service ID API key for your IBM Cloud® account. 



**Procedure**

  * Export your API key for your account as a global variable: 

```shell-session
$ export IC_API_KEY=<api_key>
```


Important

You must set the variable name exactly as specified; the installation program expects the variable name to be present during startup.
