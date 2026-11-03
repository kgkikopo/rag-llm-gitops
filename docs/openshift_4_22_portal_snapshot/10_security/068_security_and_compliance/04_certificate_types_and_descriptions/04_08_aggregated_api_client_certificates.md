# 4.8. Aggregated API client certificates

Review aggregated API client certificate validity and automatic rotation in OpenShift Container Platform to plan maintenance for extension API server authentication. 

## 4.8.1. Purpose

Aggregated API client certificates are used to authenticate the `KubeAPIServer` when connecting to the aggregated API servers. 

## 4.8.2. Management

These certificates are managed by the system and not the user. 

## 4.8.3. Expiration

This certificate authority (CA) is valid for 30 days. 

The managed client certificates are valid for 30 days. 

CA and client certificates are rotated automatically through the use of controllers. 

## 4.8.4. Customization

You cannot customize the aggregated API server certificates.
