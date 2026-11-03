# Chapter 9. Dynamic provisioning

In dynamic provisioning, instead of a manually creating a pool of persistent volumes (PVs), an administrator creates a storage class. Using the storage class, OpenShift Container Platform automatically triggers the storage backend to create a brand-new volume of the exact size and type requested, creates the PV object, and then the PV binds to the persistent volume claim (PVC).

- [9.1. About dynamic provisioning](09_01_about_dynamic_provisioning.md)
- [9.2. Available dynamic provisioning plugins](09_02_available_dynamic_provisioning_plugins.md)
- [9.3. Defining a storage class](09_03_defining_a_storage_class.md)
- [9.4. Setting the default storage class](09_04_setting_the_default_storage_class.md)
- [9.5. Changing the default storage class](09_05_changing_the_default_storage_class.md)
