# Chapter 7. Generic ephemeral volumes

Generic ephemeral volumes provide per-pod temporary storage backed by any storage driver that supports dynamic provisioning, unlike `emptyDir` volumes which are limited to local node storage. This flexibility lets you use network storage backends, control storage classes and volume characteristics, and leverage delayed volume binding for optimal pod scheduling.

- [7.1. Overview of generic ephemeral volumes](07_01_overview_of_generic_ephemeral_volumes.md)
- [7.2. Lifecycle and persistent volume claims](07_02_lifecycle_and_persistent_volume_claims.md)
- [7.3. Security](07_03_security.md)
- [7.4. Persistent volume claim naming](07_04_persistent_volume_claim_naming.md)
- [7.5. Creating generic ephemeral volumes](07_05_creating_generic_ephemeral_volumes.md)
