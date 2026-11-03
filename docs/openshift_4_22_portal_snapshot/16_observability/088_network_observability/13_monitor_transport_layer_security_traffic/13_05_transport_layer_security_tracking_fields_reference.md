# 13.5. Transport Layer Security tracking fields reference

Transport Layer Security (TLS) metadata fields track and define encryption protocols, protocol versions, and cipher suite data to help you analyze secure network flows. 

Table 13.1. TLS tracking fieldsField| Description| Possible values| Availability  
---|---|---|---  
**TLS Version** |  Negotiated TLS protocol version.  | 

  * `1.0`: Deprecated 
  * `1.1`: Deprecated 
  * `1.2`: Secure 
  * `1.3`: Current standard 

|  `ClientHello`, `ServerHello` `ClientHello` displays the version requested by the client. `ServerHello` displays the negotiated version selected by the server.   
**TLS Cipher Suite** |  Cryptographic algorithm suite negotiated between the client and server.  |  Examples: 

  * `TLS_AES_256_GCM_SHA384`
  * `TLS_CHACHA20_POLY1305_SHA256`

|  `ServerHello` only  Displays as `n/a` in `ClientHello` messages.   
**TLS Group** |  Elliptic curve used for key exchange.  |  Examples: 

  * `X25519`: Recommended for TLS 1.3 
  * `secp256r1` (P-256) 

|  `ServerHello` (TLS 1.3 only)  Displays as `n/a` in `ClientHello` messages and TLS 1.2 connections.   
**TLS Types** |  Type of TLS handshake message captured.  | 

  * `ClientHello`: Initial client request 
  * `ServerHello`: Server response 

|  All TLS flows   
Show more
