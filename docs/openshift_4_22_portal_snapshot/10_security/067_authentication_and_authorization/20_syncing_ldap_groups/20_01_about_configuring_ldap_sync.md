# 20.1. About configuring LDAP sync

Review how LDAP group sync works and what the sync configuration file contains so you can configure group sync for your LDAP schema. 

Before you can run LDAP sync, you need a sync configuration file. This file contains the following LDAP client configuration details: 

  * Configuration for connecting to your LDAP server. 
  * Sync configuration options that are dependent on the schema used in your LDAP server. 
  * An administrator-defined list of name mappings that maps OpenShift Container Platform group names to groups in your LDAP server. 



The format of the configuration file depends upon the schema you are using: 

  * RFC 2307 
  * Active Directory 
  * augmented Active Directory. 



## 20.1.1. LDAP client configuration

The LDAP client configuration section of the configuration defines the connections to your LDAP server. The following example shows the LDAP client configuration fields: 

```yaml
url: ldap://10.0.0.0:389
bindDN: cn=admin,dc=example,dc=com
bindPassword: <password>
insecure: false
ca: my-ldap-ca-bundle.crt
```


  * The `url` field shows the connection protocol, IP address of the LDAP server hosting your database, and the port to connect to, formatted as `scheme://host:port`. 
  * The `bindDN` field shows an optional distinguished name (DN) to use as the Bind DN. OpenShift Container Platform uses this if elevated privilege is required to retrieve entries for the sync operation. 
  * The `bindPassword` field shows an optional password to use to bind. OpenShift Container Platform uses this if elevated privilege is necessary to retrieve entries for the sync operation. This value may also be provided in an environment variable, external file, or encrypted file. 
  * The `insecure` field controls whether the LDAP connection uses TLS. When set to `false`, `ldaps://` URLs connect to the server using TLS, and `ldap://` URLs are upgraded to TLS. When set to `true`, no TLS connection is made to the server, and you cannot use `ldaps://` URL schemes. 
  * The `ca` field shows the certificate bundle to use for validating server certificates for the configured URL. If empty, OpenShift Container Platform uses system-trusted roots. This only applies if `insecure` is set to `false`. 



## 20.1.2. LDAP query definition

Sync configurations consist of LDAP query definitions for the entries that are required for synchronization. The specific definition of an LDAP query depends on the schema used to store membership information in the LDAP server. The following example shows the LDAP query definition fields: 

```yaml
baseDN: ou=users,dc=example,dc=com
scope: sub
derefAliases: never
timeout: 0
filter: (objectClass=person)
pageSize: 0
```


  * The `baseDN` field contains the distinguished name (DN) of the branch of the directory where all searches start from. It is required that you specify the top of your directory tree, but you can also specify a subtree in the directory. 
  * The `scope` field shows the search scope. Valid values are `base`, `one`, and `sub`. If you omit this field, the default is `sub`. For descriptions of each value, see Table 1, _LDAP search scope options_. 
  * The `derefAliases` field shows the behavior of the search with respect to aliases in the LDAP tree. Valid values are `never`, `search`, `base`, or `always`. If this is left undefined, then the default is to `always` dereference aliases. Descriptions of the dereferencing behaviors are in Table 2, _LDAP dereferencing behaviors_. 
  * The `timeout` field shows the time limit allowed for the search by the client, in seconds. A value of `0` imposes no client-side limit. 
  * The `filter` field contains a valid LDAP search filter. If this is left undefined, then the default is `(objectClass=*)`. 
  * The `pageSize` field shows the maximum number of LDAP entries the server returns per page. If set to `0`, no page size limit applies. Set this field when a query returns more entries than the client or server allow by default. 



LDAP search scope| Description  
---|---  
`base` |  Only consider the object specified by the base DN given for the query.   
`one` |  Consider all of the objects on the same level in the tree as the base DN for the query.   
`sub` |  Consider the entire subtree rooted at the base DN given for the query.   
Show more

Dereferencing behavior| Description  
---|---  
`never` |  Never dereference any aliases found in the LDAP tree.   
`search` |  Only dereference aliases found while searching.   
`base` |  Only dereference aliases while finding the base object.   
`always` |  Always dereference all aliases found in the LDAP tree.   
Show more

## 20.1.3. User-defined name mapping

A user-defined name mapping explicitly maps the names of OpenShift Container Platform groups to unique identifiers that find groups on your LDAP server. The mapping uses normal YAML syntax. A user-defined mapping can contain an entry for every group in your LDAP server or only a subset of those groups. If there are groups on the LDAP server that do not have a user-defined name mapping, the default behavior during sync is to use the attribute specified as the name of the OpenShift Container Platform group. 

The following example shows a user-defined name mapping: 

```yaml
groupUIDNameMapping:
  "cn=group1,ou=groups,dc=example,dc=com": firstgroup
  "cn=group2,ou=groups,dc=example,dc=com": secondgroup
  "cn=group3,ou=groups,dc=example,dc=com": thirdgroup
```


## 20.1.4. About the RFC 2307 configuration file

Review the RFC 2307 LDAP sync configuration file so you can define user and group queries and the attributes used in OpenShift Container Platform group records. 

The RFC 2307 schema requires you to provide an LDAP query definition for both user and group entries, as well as the attributes with which to represent them in the internal OpenShift Container Platform records. 

For clarity, the group you create in OpenShift Container Platform should use attributes other than the distinguished name whenever possible for user-facing or administrator-facing fields. For example, identify the users of an OpenShift Container Platform group by their e-mail, and use the name of the group as the common name. The following configuration file creates these relationships: 

Note

If using user-defined name mappings, your configuration file differs. 

```yaml
kind: LDAPSyncConfig
apiVersion: v1
url: ldap://LDAP_SERVICE_IP:389
insecure: false
bindDN: cn=admin,dc=example,dc=com
bindPassword:
  file: "/etc/secrets/bindPassword"
rfc2307:
    groupsQuery:
        baseDN: "ou=groups,dc=example,dc=com"
        scope: sub
        derefAliases: never
        pageSize: 0
    groupUIDAttribute: dn
    groupNameAttributes: [ cn ]
    groupMembershipAttributes: [ member ]
    usersQuery:
        baseDN: "ou=users,dc=example,dc=com"
        scope: sub
        derefAliases: never
        pageSize: 0
    userUIDAttribute: dn
    userNameAttributes: [ mail ]
    tolerateMemberNotFoundErrors: false
    tolerateMemberOutOfScopeErrors: false
```


where: 

`url`
     Specifies the IP address and host of the LDAP server where the record of the group is stored. 
`insecure`
     Specifies whether the LDAP connection uses TLS. When set to `false`, `ldaps://` URLs connect to the server using TLS, and `ldap://` URLs are upgraded to TLS. When set to `true`, no TLS connection is made to the server, and you cannot use `ldaps://` URL schemes. 
`rfc2307.groupUIDAttribute`
     Specifies the attribute that uniquely identifies a group on the LDAP server. You cannot specify `groupsQuery` filters when using DN for `groupUIDAttribute`. For fine-grained filtering, use an allowlist file, a denylist file, or both. 
`rfc2307.groupNameAttributes`
     Specifies the attribute to use as the name of the group. 
`rfc2307.groupMembershipAttributes`
     Specifies the attribute on the group that stores the membership information. 
`rfc2307.userUIDAttribute`
     Specifies the attribute that uniquely identifies a user on the LDAP server. You cannot specify `usersQuery` filters when using DN for userUIDAttribute. For fine-grained filtering, use an allowlist file, a denylist file, or both. 
`rfc2307.userNameAttributes`
     Specifies the attribute to use as the name of the user in the OpenShift Container Platform group record. 

## 20.1.5. About the Active Directory configuration file

Review the Active Directory LDAP sync configuration file so you can define user queries and the attributes used in OpenShift Container Platform group records. 

The Active Directory schema requires you to provide an LDAP query definition for user entries, as well as the attributes to represent them with in the internal OpenShift Container Platform group records. 

For clarity, the group you create in OpenShift Container Platform should use attributes other than the distinguished name whenever possible for user-facing or administrator-facing fields. For example, identify the users of an OpenShift Container Platform group by their e-mail, but define the name of the group by the name of the group on the LDAP server. The following configuration file creates these relationships: 

```yaml
kind: LDAPSyncConfig
apiVersion: v1
url: ldap://LDAP_SERVICE_IP:389
activeDirectory:
    usersQuery:
        baseDN: "ou=users,dc=example,dc=com"
        scope: sub
        derefAliases: never
        filter: (objectclass=person)
        pageSize: 0
    userNameAttributes: [ mail ]
    groupMembershipAttributes: [ memberOf ]
```


where: 

`activeDirectory.userNameAttributes`
     Specifies the attribute to use as the name of the user in the OpenShift Container Platform group record. 
`activeDirectory.groupMembershiptAttributes`
     Specifies the attribute on the user that stores the membership information. 

## 20.1.6. About the augmented Active Directory configuration file

Review the augmented Active Directory LDAP sync configuration file so you can define user and group queries and the attributes used in OpenShift Container Platform group records. 

The augmented Active Directory schema requires you to provide an LDAP query definition for both user entries and group entries, as well as the attributes with which to represent them in the internal OpenShift Container Platform group records. 

For clarity, the group you create in OpenShift Container Platform should use attributes other than the distinguished name whenever possible for user-facing or administrator-facing fields. For example, identify the users of an OpenShift Container Platform group by their e-mail, and use the name of the group as the common name. The following configuration file creates these relationships. 

```yaml
kind: LDAPSyncConfig
apiVersion: v1
url: ldap://LDAP_SERVICE_IP:389
augmentedActiveDirectory:
    groupsQuery:
        baseDN: "ou=groups,dc=example,dc=com"
        scope: sub
        derefAliases: never
        pageSize: 0
    groupUIDAttribute: dn
    groupNameAttributes: [ cn ]
    usersQuery:
        baseDN: "ou=users,dc=example,dc=com"
        scope: sub
        derefAliases: never
        filter: (objectclass=person)
        pageSize: 0
    userNameAttributes: [ mail ]
    groupMembershipAttributes: [ memberOf ]
```


where: 

`augmentedActiveDirectory.groupUIDAttribute`
     Specifies the attribute that uniquely identifies a group on the LDAP server. You cannot specify `groupsQuery` filters when using DN for groupUIDAttribute. For fine-grained filtering, use an allowlist file, a denylist file, or both. 
`augmentedActiveDirectory.groupNameAttributes`
     Specifies the attribute to use as the name of the group. 
`augmentedActiveDirectory.userNameAttributes`
     Specifies the attribute to use as the name of the user in the OpenShift Container Platform group record. 
`augmentedActiveDirectory.groupMembershipAttributes`
     Specifies the attribute on the user that stores the membership information.
