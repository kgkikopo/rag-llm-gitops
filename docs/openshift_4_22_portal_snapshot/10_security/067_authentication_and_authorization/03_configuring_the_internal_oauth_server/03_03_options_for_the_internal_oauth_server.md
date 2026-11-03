# 3.3. Options for the internal OAuth server

The internal OAuth server provides configuration options for token duration and grant strategies to control authentication behavior. 

## 3.3.1. OAuth token duration options

The internal OAuth server generates two kinds of tokens: 

Token| Description  
---|---  
Access tokens  |  Longer-lived tokens that grant access to the API.   
Authorize codes  |  Short-lived tokens whose only use is to be exchanged for an access token.   
Show more

You can configure the default duration for both types of token. If necessary, you can override the duration of the access token by using an `OAuthClient` object definition. 

## 3.3.2. OAuth grant options

When the OAuth server receives token requests for a client to which the user has not previously granted permission, the action that the OAuth server takes is dependent on the OAuth client’s grant strategy. 

The OAuth client requesting token must provide its own grant strategy. 

You can apply the following default methods: 

Grant option| Description  
---|---  
`auto` |  Auto-approve the grant and retry the request.   
`prompt` |  Prompt the user to approve or deny the grant.   
Show more
