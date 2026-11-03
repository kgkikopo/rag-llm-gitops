# 20.5. LDAP group sync examples

Review LDAP group sync examples so you can configure synchronization for RFC 2307, Active Directory, or augmented Active Directory schemas. 

Note

These examples cover only direct group membership. Each user is a direct member of a group, and groups do not contain other groups as members. For information, see "LDAP nested membership sync". 

## 20.5.1. Sync groups using the RFC 2307 schema

Sync LDAP groups by using the RFC 2307 schema so you can mirror direct group membership from your LDAP server in OpenShift Container Platform. 

For the RFC 2307 schema, the following examples synchronize a group named `admins` that has two members: `Jane` and `Jim`. The examples explain: 

  * How the group and users are added to the LDAP server. 
  * What the resulting group record in OpenShift Container Platform is after synchronization. 



Note

These examples assume that all users are direct members of their respective groups. Specifically, no groups have other groups as members. For information on how to sync nested groups, see "LDAP nested membership sync". 

In the RFC 2307 schema, users and groups exist on the LDAP server as first-class entries, and group membership is stored in attributes on the group. The following snippet of `ldif` defines the users and group for this schema: 

```plaintext
  dn: ou=users,dc=example,dc=com
  objectClass: organizationalUnit
  ou: users
  dn: cn=Jane,ou=users,dc=example,dc=com
  objectClass: person
  objectClass: organizationalPerson
  objectClass: inetOrgPerson
  cn: Jane
  sn: Smith
  displayName: Jane Smith
  mail: jane.smith@example.com
  dn: cn=Jim,ou=users,dc=example,dc=com
  objectClass: person
  objectClass: organizationalPerson
  objectClass: inetOrgPerson
  cn: Jim
  sn: Adams
  displayName: Jim Adams
  mail: jim.adams@example.com
  dn: ou=groups,dc=example,dc=com
  objectClass: organizationalUnit
  ou: groups
  dn: cn=admins,ou=groups,dc=example,dc=com
  objectClass: groupOfNames
  cn: admins
  owner: cn=admin,dc=example,dc=com
  description: System Administrators
  member: cn=Jane,ou=users,dc=example,dc=com
  member: cn=Jim,ou=users,dc=example,dc=com
```


where: 

`dn: cn=admins,ou=groups,dc=example,dc=com`
     Specifies that this group is a first-class entry in the LDAP server. 
`member: cn=Jane,ou=users,dc=example,dc=com`
     Specifies that the members of a group are listed with an identifying reference as attributes on the group. 

**Prerequisites**

  * An LDAP sync configuration file exists. This procedure uses an example file named `rfc2307_config.yaml`. 
  * You have access to the cluster as a user with the `cluster-admin` role. 



**Procedure**

  * Sync with the `rfc2307_config.yaml` file by running the following command: 

```shell-session
$ oc adm groups sync --sync-config=rfc2307_config.yaml --confirm
```


After you run the sync command, the following group record is created in OpenShift Container Platform: 

```yaml
apiVersion: user.openshift.io/v1
kind: Group
metadata:
  annotations:
    openshift.io/ldap.sync-time: 2015-10-13T10:08:38-0400
    openshift.io/ldap.uid: cn=admins,ou=groups,dc=example,dc=com
    openshift.io/ldap.url: LDAP_SERVER_IP:389
  creationTimestamp:
  name: admins
users:
- jane.smith@example.com
- jim.adams@example.com
```


where: 

`metadata.annotations.openshift.io/ldap.sync-time`
     Specifies the last time this OpenShift Container Platform group was synchronized with the LDAP server, in ISO 8601 format. 
`metadata.annotations.openshift.io/ldap.uid`
     Specifies the unique identifier for the group on the LDAP server. 
`metadata.annotations.openshift.io/ldap.url`
     Specifies the IP address and host of the LDAP server where the record of the group is stored. 
`metadata.name`
     Specifies the name of the group as specified by the sync file. 
`users`
     Specifies the users that are members of the group, named as specified by the sync file. 




## 20.5.2. Sync groups by using the RFC 2307 schema with user-defined name mappings

Sync LDAP groups using the RFC 2307 schema with user-defined name mappings so you can map LDAP group identifiers to OpenShift Container Platform group names. 

When you sync groups with user-defined name mappings, include the mappings in the configuration file, as shown in the following `rfc2307_config_user_defined.yaml` example: 

```yaml
kind: LDAPSyncConfig
apiVersion: v1
groupUIDNameMapping:
  "cn=admins,ou=groups,dc=example,dc=com": Administrators
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

`groupUIDNameMapping`
     Specifies the user-defined name mapping. 
`rfc2307.groupUIDAttribute`
     Specifies the unique identifier attribute that is used for the keys in the user-defined name mapping. You cannot specify `groupsQuery` filters when using DN for groupUIDAttribute. For fine-grained filtering, use an allowlist file, a denylist file, or both. 
`rfc2307.groupNameAttributes`
     Specifies the attribute to name OpenShift Container Platform groups with if their unique identifier is not in the user-defined name mapping. 
`rfc2307.userUIDAttribute`
     Specifies the attribute that uniquely identifies a user on the LDAP server. You cannot specify `usersQuery` filters when using DN for the `userUIDAttribute` parameter. For fine-grained filtering, use an allowlist file, a denylist file, or both. 

**Prerequisites**

  * An LDAP sync configuration file exists. This procedure uses an example file named `rfc2307_config_user_defined.yaml`. 
  * You have access to the cluster as a user with the `cluster-admin` role. 



**Procedure**

  * Sync groups using the `rfc2307_config_user_defined.yaml` file by running the following command: 

```shell-session
$ oc adm groups sync --sync-config=rfc2307_config_user_defined.yaml --confirm
```


After you run the sync command, the following group record is created in OpenShift Container Platform: 

```yaml
apiVersion: user.openshift.io/v1
kind: Group
metadata:
  annotations:
    openshift.io/ldap.sync-time: 2015-10-13T10:08:38-0400
    openshift.io/ldap.uid: cn=admins,ou=groups,dc=example,dc=com
    openshift.io/ldap.url: LDAP_SERVER_IP:389
  creationTimestamp:
  name: Administrators
users:
- jane.smith@example.com
- jim.adams@example.com
```


where: 

`metadata.name`
     Specifies the name of the group as specified by the user-defined name mapping. 




## 20.5.3. Sync groups by using RFC 2307 with user-defined error tolerances

Sync LDAP groups using the RFC 2307 schema with error tolerances so you can complete group synchronization when some members are missing or out of scope. 

By default, if the groups being synced contain members whose entries are outside of the scope defined in the member query, the group sync fails with an error: 

```plaintext
Error determining LDAP group membership for "<group>": membership lookup for user "<user>" in group "<group>" failed because of "search for entry with dn="<user-dn>" would search outside of the base dn specified (dn="<base-dn>")".
```


This often indicates a misconfigured `baseDN` in the `usersQuery` field. However, in cases where the `baseDN` intentionally does not contain some of the members of the group, setting `tolerateMemberOutOfScopeErrors: true` allows the group sync to continue. Out of scope members are ignored. 

Similarly, when the group sync process fails to locate a member for a group, it fails with errors: 

```plaintext
Error determining LDAP group membership for "<group>": membership lookup for user "<user>" in group "<group>" failed because of "search for entry with base dn="<user-dn>" refers to a non-existent entry".
Error determining LDAP group membership for "<group>": membership lookup for user "<user>" in group "<group>" failed because of "search for entry with base dn="<user-dn>" and filter "<filter>" did not return any results".
```


This often indicates a misconfigured `usersQuery` field. However, in cases where the group contains member entries that are known to be missing, setting `tolerateMemberNotFoundErrors: true` allows the group sync to continue. Missing members are ignored. 

Warning

Enabling error tolerances for the LDAP group sync causes the sync process to ignore member entries that cause errors. If the LDAP group sync is not configured correctly, this could result in synced OpenShift Container Platform groups missing members. 

The following example shows LDAP entries that use RFC 2307 schema with invalid group membership: `rfc2307_problematic_users.ldif`

```plaintext
  dn: ou=users,dc=example,dc=com
  objectClass: organizationalUnit
  ou: users
  dn: cn=Jane,ou=users,dc=example,dc=com
  objectClass: person
  objectClass: organizationalPerson
  objectClass: inetOrgPerson
  cn: Jane
  sn: Smith
  displayName: Jane Smith
  mail: jane.smith@example.com
  dn: cn=Jim,ou=users,dc=example,dc=com
  objectClass: person
  objectClass: organizationalPerson
  objectClass: inetOrgPerson
  cn: Jim
  sn: Adams
  displayName: Jim Adams
  mail: jim.adams@example.com
  dn: ou=groups,dc=example,dc=com
  objectClass: organizationalUnit
  ou: groups
  dn: cn=admins,ou=groups,dc=example,dc=com
  objectClass: groupOfNames
  cn: admins
  owner: cn=admin,dc=example,dc=com
  description: System Administrators
  member: cn=Jane,ou=users,dc=example,dc=com
  member: cn=Jim,ou=users,dc=example,dc=com
  member: cn=INVALID,ou=users,dc=example,dc=com
  member: cn=Jim,ou=OUTOFSCOPE,dc=example,dc=com
```


where: 

`member: cn=INVALID,ou=users,dc=example,dc=com`
     Specifies a member that does not exist on the LDAP server. 
`member: cn=Jim,ou=OUTOFSCOPE,dc=example,dc=com`
     Specifies a member that may exist, but is not under the `baseDN` in the user query for the sync job. 

To tolerate the errors in the above example, the following additions to your sync configuration file must be made: 

```yaml
kind: LDAPSyncConfig
apiVersion: v1
url: ldap://LDAP_SERVICE_IP:389
rfc2307:
    groupsQuery:
        baseDN: "ou=groups,dc=example,dc=com"
        scope: sub
        derefAliases: never
    groupUIDAttribute: dn
    groupNameAttributes: [ cn ]
    groupMembershipAttributes: [ member ]
    usersQuery:
        baseDN: "ou=users,dc=example,dc=com"
        scope: sub
        derefAliases: never
    userUIDAttribute: dn
    userNameAttributes: [ mail ]
    tolerateMemberNotFoundErrors: true
    tolerateMemberOutOfScopeErrors: true
```


where: 

`rfc2307.userUIDAttribute`
     Specifies the attribute that uniquely identifies a user on the LDAP server. You cannot specify `usersQuery` filters when using DN for userUIDAttribute. For fine-grained filtering, use an allowlist file, a denylist file, or both. 
`rfc2307.tolerateMemberNotFoundErrors`
     Specifies whether the sync job tolerates groups for which some members were not found. When set to `true`, members whose LDAP entries are not found are ignored. The default behavior for the sync job is to fail if a member of a group is not found. 
`rfc2307.tolerateMemberOutOfScopeErrors`
     Specifies whether the sync job tolerates groups for which some members are outside the user scope given in the `usersQuery` `baseDN`. When set to `true`, members outside the member query scope are ignored. The default behavior for the sync job is to fail if a member of a group is out of scope. 

**Prerequisites**

  * An LDAP sync configuration file exists. This procedure uses an example file named `rfc2307_config_tolerating.yaml`. 
  * You have access to the cluster as a user with the `cluster-admin` role. 



**Procedure**

  * Sync with the `rfc2307_config_tolerating.yaml` file by running the following command: 

```shell-session
$ oc adm groups sync --sync-config=rfc2307_config_tolerating.yaml --confirm
```


OpenShift Container Platform creates the following group record as a result of the previous sync operation: 

```yaml
apiVersion: user.openshift.io/v1
kind: Group
metadata:
  annotations:
    openshift.io/ldap.sync-time: 2015-10-13T10:08:38-0400
    openshift.io/ldap.uid: cn=admins,ou=groups,dc=example,dc=com
    openshift.io/ldap.url: LDAP_SERVER_IP:389
  creationTimestamp:
  name: admins
users:
- jane.smith@example.com
- jim.adams@example.com
```


where: 

`users`
     Specifies the users that are members of the group, as specified by the sync file. Members for which lookup encountered tolerated errors are absent. 




## 20.5.4. Sync groups using the Active Directory schema

You can sync LDAP groups for your OpenShift Container Platform cluster using the Active Directory schema by running `oc adm groups sync` with an LDAP sync configuration file. In this schema, group membership is stored in attributes on user entries, such as `memberOf`. 

In the Active Directory schema, users exist on the LDAP server as first-class entries, and group membership is stored in attributes on the user. The following snippet of `ldif` defines the users and group for this schema: 

```plaintext
dn: ou=users,dc=example,dc=com
objectClass: organizationalUnit
ou: users

dn: cn=Jane,ou=users,dc=example,dc=com
objectClass: person
objectClass: organizationalPerson
objectClass: inetOrgPerson
objectClass: testPerson
cn: Jane
sn: Smith
displayName: Jane Smith
mail: jane.smith@example.com
memberOf: admins 
```


1

```plaintext
dn: cn=Jim,ou=users,dc=example,dc=com
objectClass: person
objectClass: organizationalPerson
objectClass: inetOrgPerson
objectClass: testPerson
cn: Jim
sn: Adams
displayName: Jim Adams
mail: jim.adams@example.com
memberOf: admins
```


where: 

`memberOf`
     Specifies that the group memberships of the user are listed as attributes on the user, and the group does not exist as an entry on the server. The `memberOf` attribute does not have to be a literal attribute on the user; in some LDAP servers, the attribute is created during search and returned to the client, but not committed to the database. 

**Prerequisites**

  * An LDAP sync configuration file exists. This procedure uses an example file named `active_directory_config.yaml`. 
  * You have access to the cluster as a user with the `cluster-admin` role. 



**Procedure**

  * Sync with the `active_directory_config.yaml` file by running the following command: 

```shell-session
$ oc adm groups sync --sync-config=active_directory_config.yaml --confirm
```


OpenShift Container Platform creates the following group record as a result of the previous sync operation: 

```yaml
apiVersion: user.openshift.io/v1
kind: Group
metadata:
  annotations:
    openshift.io/ldap.sync-time: 2015-10-13T10:08:38-0400
    openshift.io/ldap.uid: admins
    openshift.io/ldap.url: LDAP_SERVER_IP:389
  creationTimestamp:
  name: admins
users:
- jane.smith@example.com
- jim.adams@example.com
```


where: 

`metadata.annotations.openshift.io/ldap.sync-time`
     Specifies the last time this OpenShift Container Platform group was synchronized with the LDAP server, in ISO 8601 format. 
`metadata.annotations.openshift.io/ldap.uid`
     Specifies the unique identifier for the group on the LDAP server. 
`metadata.annotations.openshift.io/ldap.url`
     Specifies the IP address and host of the LDAP server where the record of the group is stored. 
`metadata.name`
     Specifies the name of the group as listed in the LDAP server. 
`users`
     Specifies the users that are members of the group, named as specified by the sync file. 




## 20.5.5. Sync groups using the augmented Active Directory schema

You can sync LDAP groups for your OpenShift Container Platform cluster using the augmented Active Directory schema by running `oc adm groups sync` with an LDAP sync configuration file. 

In this schema, users and groups are first-class LDAP entries, and group membership is stored in attributes on user entries, such as `memberOf`. 

In the augmented Active Directory schema, both users and groups exist in the LDAP server as first-class entries, and group membership is stored in attributes on the user. The following snippet of `ldif` defines the users and group for this schema: 

```plaintext
dn: ou=users,dc=example,dc=com
objectClass: organizationalUnit
ou: users

dn: cn=Jane,ou=users,dc=example,dc=com
objectClass: person
objectClass: organizationalPerson
objectClass: inetOrgPerson
objectClass: testPerson
cn: Jane
sn: Smith
displayName: Jane Smith
mail: jane.smith@example.com
memberOf: cn=admins,ou=groups,dc=example,dc=com

dn: cn=Jim,ou=users,dc=example,dc=com
objectClass: person
objectClass: organizationalPerson
objectClass: inetOrgPerson
objectClass: testPerson
cn: Jim
sn: Adams
displayName: Jim Adams
mail: jim.adams@example.com
memberOf: cn=admins,ou=groups,dc=example,dc=com

dn: ou=groups,dc=example,dc=com
objectClass: organizationalUnit
ou: groups

dn: cn=admins,ou=groups,dc=example,dc=com
objectClass: groupOfNames
cn: admins
owner: cn=admin,dc=example,dc=com
description: System Administrators
member: cn=Jane,ou=users,dc=example,dc=com
member: cn=Jim,ou=users,dc=example,dc=com
```


where: 

`memberOf`
     Specifies that the group memberships of the user are listed as attributes on the user. 
`dn: cn=admins,ou=groups,dc=example,dc=com`
     Specifies that the group is a first-class entry on the LDAP server. 

**Prerequisites**

  * An LDAP sync configuration file exists. This procedure uses an example file named `augmented_active_directory_config.yaml`. 
  * You have access to the cluster as a user with the `cluster-admin` role. 



**Procedure**

  * Sync with the `augmented_active_directory_config.yaml` file by running the following command: 

```shell-session
$ oc adm groups sync --sync-config=augmented_active_directory_config.yaml --confirm
```


OpenShift Container Platform creates the following group record as a result of the previous sync operation: 

```yaml
apiVersion: user.openshift.io/v1
kind: Group
metadata:
  annotations:
    openshift.io/ldap.sync-time: 2015-10-13T10:08:38-0400
    openshift.io/ldap.uid: cn=admins,ou=groups,dc=example,dc=com
    openshift.io/ldap.url: LDAP_SERVER_IP:389
  creationTimestamp:
  name: admins
users:
- jane.smith@example.com
- jim.adams@example.com
```


where: 

`metadata.annotations.openshift.io/ldap.sync-time`
     Specifies the last time this OpenShift Container Platform group was synchronized with the LDAP server, in ISO 8601 format. 
`metadata.annotations.openshift.io/ldap.uid`
     Specifies the unique identifier for the group on the LDAP server. 
`metadata.annotations.openshift.io/ldap.url`
     Specifies the IP address and host of the LDAP server where the record of the group is stored. 
`metadata.name`
     Specifies the name of the group as specified by the sync file. 
`users`
     Specifies the users that are members of the group, named as specified by the sync file. 




## 20.5.6. LDAP nested membership sync

Understand how nested LDAP group membership is flattened during sync so you can configure allowlisted sync jobs that include members of nested Active Directory groups. 

Groups in OpenShift Container Platform do not nest. The LDAP server must flatten group membership before the data can be consumed. The Microsoft Active Directory Server supports this feature via the `LDAP_MATCHING_RULE_IN_CHAIN` rule, which has the OID `1.2.840.113556.1.4.1941`. Furthermore, only explicitly allowlisted groups can be synced when using this matching rule. 

The following example synchronizes a group named `admins` that has one user member, `Jane`, and one nested group member, `otheradmins`, which contains `Jim`. 

This example explains: 

  * How the group and users are added to the LDAP server. 
  * What the LDAP sync configuration file looks like. 
  * What the resulting group record in OpenShift Container Platform is after synchronization. 



### 20.5.6.1. Example LDAP entries

In the augmented Active Directory schema, both users and groups exist in the LDAP server as first-class entries, and group membership is stored in attributes on the user or the group. The following `ldif` snippet defines the users and groups for this schema: 

```plaintext
dn: ou=users,dc=example,dc=com
objectClass: organizationalUnit
ou: users

dn: cn=Jane,ou=users,dc=example,dc=com
objectClass: person
objectClass: organizationalPerson
objectClass: inetOrgPerson
objectClass: testPerson
cn: Jane
sn: Smith
displayName: Jane Smith
mail: jane.smith@example.com
memberOf: cn=admins,ou=groups,dc=example,dc=com 
```


1

```plaintext
dn: cn=Jim,ou=users,dc=example,dc=com
objectClass: person
objectClass: organizationalPerson
objectClass: inetOrgPerson
objectClass: testPerson
cn: Jim
sn: Adams
displayName: Jim Adams
mail: jim.adams@example.com
memberOf: cn=otheradmins,ou=groups,dc=example,dc=com

dn: ou=groups,dc=example,dc=com
objectClass: organizationalUnit
ou: groups

dn: cn=admins,ou=groups,dc=example,dc=com
objectClass: group
cn: admins
owner: cn=admin,dc=example,dc=com
description: System Administrators
member: cn=Jane,ou=users,dc=example,dc=com
member: cn=otheradmins,ou=groups,dc=example,dc=com

dn: cn=otheradmins,ou=groups,dc=example,dc=com
objectClass: group
cn: otheradmins
owner: cn=admin,dc=example,dc=com
description: Other System Administrators
memberOf: cn=admins,ou=groups,dc=example,dc=com
member: cn=Jim,ou=users,dc=example,dc=com
```


where: 

`memberOf`
     Specifies that the memberships of the user and group are listed as attributes on the object. 
`dn: cn=admins,ou=groups,dc=example,dc=com`
     Specifies that groups are first-class entries on the LDAP server. 
`member: cn=otheradmins,ou=groups,dc=example,dc=com`
     Specifies that the `otheradmins` group is a member of the `admins` group. 

### 20.5.6.2. Configuration requirements

When syncing nested groups with Active Directory, you must provide an LDAP query definition for both user entries and group entries, as well as the attributes with which to represent them in the internal OpenShift Container Platform group records. Furthermore, certain changes are required in this configuration: 

  * The `oc adm groups sync` command requires you to explicitly allowlist groups. 
  * The `groupMembershipAttributes` field must include `"memberOf:1.2.840.113556.1.4.1941:"` to comply with the `LDAP_MATCHING_RULE_IN_CHAIN` rule. 
  * The `groupUIDAttribute` must be set to `dn`. 
  * The `groupsQuery`: 

    * Must not set `filter`. 
    * Must set a valid `derefAliases`. 
    * Should not set `baseDN` as that value is ignored. 
    * Should not set `scope` as that value is ignored. 




For clarity, the group you create in OpenShift Container Platform should use attributes other than the distinguished name whenever possible for user-facing or administrator-facing fields. For example, identify the users of an OpenShift Container Platform group by their e-mail, and use the name of the group as the common name. 

### 20.5.6.3. Example sync configuration

The following configuration file creates these relationships. Save it as `augmented_active_directory_config_nested.yaml`: 

```yaml
kind: LDAPSyncConfig
apiVersion: v1
url: ldap://LDAP_SERVICE_IP:389
augmentedActiveDirectory:
    groupsQuery:
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
    groupMembershipAttributes: [ "memberOf:1.2.840.113556.1.4.1941:" ]
```


where: 

`augmentedActiveDirectory.groupsQuery`
     Specifies that the `groupsQuery` filters cannot be specified. The `groupsQuery` base DN and scope values are ignored. `groupsQuery` must set a valid `derefAliases`. 
`augmentedActiveDirectory.groupUIDAttribute`
     Specifies the attribute that uniquely identifies a group on the LDAP server. It must be set to `dn`. 
`augmentedActiveDirectory.groupNameAttributes`
     Specifies the attribute to use as the name of the group. 
`augmentedActiveDirectory.userNameAttributes`
     Specifies the attribute to use as the username of the user in the OpenShift Container Platform group record. 
`augmentedActiveDirectory.groupMembershipAttributes`
    

Specifies the attribute on the user that stores the membership information. Note the use of `LDAP_MATCHING_RULE_IN_CHAIN`. 

Note

`mail` or `sAMAccountName` are preferred choices in most installations. 

## 20.5.7. LDAP nested membership sync example

Run the nested group LDAP sync example with an allowlisted group so you can verify that members of nested Active Directory groups appear in the resulting OpenShift Container Platform group. 

**Prerequisites**

  * An LDAP sync configuration file exists. This procedure uses an example file named `augmented_active_directory_config_nested.yaml`. 
  * You have access to the cluster as a user with the `cluster-admin` role. 



**Procedure**

  * Sync with the `augmented_active_directory_config_nested.yaml` file by running the following command: 

```shell-session
$ oc adm groups sync \
    'cn=admins,ou=groups,dc=example,dc=com' \
    --sync-config=augmented_active_directory_config_nested.yaml \
    --confirm
```


Note

You must explicitly allowlist the `cn=admins,ou=groups,dc=example,dc=com` group. 

OpenShift Container Platform creates the following group record as a result of the previous sync operation: 

```yaml
apiVersion: user.openshift.io/v1
kind: Group
metadata:
  annotations:
    openshift.io/ldap.sync-time: 2015-10-13T10:08:38-0400
    openshift.io/ldap.uid: cn=admins,ou=groups,dc=example,dc=com
    openshift.io/ldap.url: LDAP_SERVER_IP:389
  creationTimestamp:
  name: admins
users:
- jane.smith@example.com
- jim.adams@example.com
```


where: 

`metadata.annotations.openshift.io/ldap.sync-time`
     Specifies the last time this OpenShift Container Platform group was synchronized with the LDAP server, in ISO 8601 format. 
`metadata.annotations.openshift.io/ldap.uid`
     Specifies the unique identifier for the group on the LDAP server. 
`metadata.annotations.openshift.io/ldap.url`
     Specifies the IP address and host of the LDAP server where the record of the group is stored. 
`metadata.name`
     Specifies the name of the group as specified by the sync file. 
`users`
    

Specifies the users that are members of the group, named as specified by the sync file. 

Note

Members of nested groups are included because the group membership is flattened by the Microsoft Active Directory Server.
