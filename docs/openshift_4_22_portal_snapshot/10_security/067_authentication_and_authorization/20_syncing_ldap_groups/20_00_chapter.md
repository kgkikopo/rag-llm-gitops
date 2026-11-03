# Chapter 20. Syncing LDAP groups

Sync LDAP groups with OpenShift Container Platform so you can manage user membership and permissions using groups stored in your LDAP directory. 

As an administrator, you can use groups to manage users, change their permissions, and enhance collaboration. Your organization may have already created user groups and stored them in an LDAP server. OpenShift Container Platform can sync those LDAP records with internal OpenShift Container Platform records, enabling you to manage your groups in one place. OpenShift Container Platform currently supports group sync with LDAP servers using three common schemas for defining group membership: RFC 2307, Active Directory, and augmented Active Directory. 

For more information on configuring LDAP, see "Configuring an LDAP identity provider". 

Note

You must have `cluster-admin` privileges to sync groups.

- [20.1. About configuring LDAP sync](20_01_about_configuring_ldap_sync.md)
- [20.2. Run LDAP sync](20_02_run_ldap_sync.md)
- [20.3. Run a group pruning job](20_03_run_a_group_pruning_job.md)
- [20.4. Automatically syncing LDAP groups](20_04_automatically_syncing_ldap_groups.md)
- [20.5. LDAP group sync examples](20_05_ldap_group_sync_examples.md)
- [20.6. LDAP sync configuration specification](20_06_ldap_sync_configuration_specification.md)
