# 4.11. Mirror registry for Red Hat OpenShift release notes

The _mirror registry for Red Hat OpenShift_ is a small and streamlined container registry that you can use as a target for mirroring the required container images of OpenShift Container Platform for disconnected installations. 

These release notes track the development of the _mirror registry for Red Hat OpenShift_ in OpenShift Container Platform. 

## 4.11.1. Mirror registry for Red Hat OpenShift 2.0 release notes

See the Mirror registry for Red Hat OpenShift 2.0 release notes for information about updates and changes in each release. 

The following sections provide details for each 2.0 release of the mirror registry for Red Hat OpenShift. 

### 4.11.1.1. Mirror registry for Red Hat OpenShift 2.0.11

Issued: 22 June 2026 

_Mirror registry for Red Hat OpenShift_ is now available with Red Hat Quay 3.12.18. 

The following advisory, which includes bug fixes, is available for the _mirror registry for Red Hat OpenShift_ : 

  * [RHSA-2026:28441 - mirror registry for Red Hat OpenShift 2.0.11](https://access.redhat.com/errata/RHSA-2026:28441)



The following enhancements were added to this release: 

  * With this release, the `./mirror-registry upgrade` command supports `--sslCert`, `--sslKey`, and `--sslCheckSkip` flags for SSL/TLS certificate rotation during upgrades. You must provide `--sslCert` and `--sslKey` together; passing only one of these flags causes the upgrade to fail. For example: 

Rotate certificates during upgrade: 

```shell-session
$ ./mirror-registry upgrade --sslCert /path/to/new.cert --sslKey /path/to/new.key
```


Skip hostname validation, for example when you use wildcard or internal CA certificates: 

```shell-session
$ ./mirror-registry upgrade --sslCert /path/to/cert --sslKey /path/to/key --sslCheckSkip
```


Normal upgrade that uses existing certificates; no SSL flags are required: 

```shell-session
$ ./mirror-registry upgrade
```


If you do not pass SSL flags, a warning is displayed when existing certificates are not found on the target host. During a PostgreSQL to SQLite migration, missing certificates block the upgrade before any database changes are made. The `--sslCheckSkip` flag skips CLI hostname validation only; Quay still requires `ssl.cert` and `ssl.key` to start. 

  * With this release, the `./mirror-registry upgrade` command automatically preserves the existing `SERVER_HOSTNAME`, including custom ports, and the `quayRoot`, `quayStorage`, and `sqliteStorage` settings from the current installation. You do not need to pass `--quayHostname`, `--quayRoot`, `--quayStorage`, or `--sqliteStorage` for a standard upgrade. Explicit flags override the preserved values if you provide them. 



### 4.11.1.2. Mirror registry for Red Hat OpenShift 2.0.10

Issued: 03 March 2026 

_Mirror registry for Red Hat OpenShift_ is now available with Red Hat Quay 3.12.14. 

The following advisory is available for the _mirror registry for Red Hat OpenShift_ : 

  * [RHBA-2026:3953 - mirror registry for Red Hat OpenShift 2.0.10](https://access.redhat.com/errata/RHBA-2026:3953)



The following bugs were fixed as part of this release: 

  * [PROJQUAY-9799](https://redhat.atlassian.net/browse/PROJQUAY-9799). In this update, upgrading from PostgreSQL to SQLite without proper configuration previously triggered a SQLite cursor error. This error prevented Quay from starting after the SQLite upgrade, leading to service disruption. With this release, the SQLite upgrade process no longer triggers the cursor error, enabling a successful Quay upgrade without crashes due to SQLite optimization issues. 
  * [PROJQUAY-10093](https://redhat.atlassian.net/browse/PROJQUAY-10093). The _Mirror registry for Red Hat OpenShift_ has been upgraded to use the latest Redis 6 (`redis-6:1-1766406130`) version. 



### 4.11.1.3. Mirror registry for Red Hat OpenShift 2.0.9

Issued: 17 November 2025 

_Mirror registry for Red Hat OpenShift_ is now available with Red Hat Quay 3.12.13. 

The following advisory is available for the _mirror registry for Red Hat OpenShift_ : 

  * [RHBA-2025:21600 - mirror registry for Red Hat OpenShift 2.0.9](https://access.redhat.com/errata/RHBA-2025:21600)



### 4.11.1.4. Mirror registry for Red Hat OpenShift 2.0.8

Issued: 16 October 2025 

_Mirror registry for Red Hat OpenShift_ is now available with Red Hat Quay 3.12.12. 

The following advisory is available for the _mirror registry for Red Hat OpenShift_ : 

  * [RHBA-2025:17062 - mirror registry for Red Hat OpenShift 2.0.8](https://access.redhat.com/errata/RHBA-2025:17062)



### 4.11.1.5. Mirror registry for Red Hat OpenShift 2.0.7

Issued: 14 July 2025 

_Mirror registry for Red Hat OpenShift_ is now available with Red Hat Quay 3.12.10. 

The following advisory is available for the _mirror registry for Red Hat OpenShift_ : 

  * [RHBA-2025:9645 - mirror registry for Red Hat OpenShift 2.0.7](https://access.redhat.com/errata/RHBA-2025:9645)



### 4.11.1.6. Mirror registry for Red Hat OpenShift 2.0.6

Issued: 28 April 2025 

_Mirror registry for Red Hat OpenShift_ is now available with Red Hat Quay 3.12.8. 

The following advisory is available for the _mirror registry for Red Hat OpenShift_ : 

  * [RHBA-2025:4251 - mirror registry for Red Hat OpenShift 2.0.6](https://access.redhat.com/errata/RHBA-2025:4251)



### 4.11.1.7. Mirror registry for Red Hat OpenShift 2.0.5

Issued: 13 January 2025 

_Mirror registry for Red Hat OpenShift_ is now available with Red Hat Quay 3.12.5. 

The following advisory is available for the _mirror registry for Red Hat OpenShift_ : 

  * [RHBA-2025:0298 - mirror registry for Red Hat OpenShift 2.0.5](https://access.redhat.com/errata/RHBA-2025:0298)



### 4.11.1.8. Mirror registry for Red Hat OpenShift 2.0.4

Issued: 06 January 2025 

_Mirror registry for Red Hat OpenShift_ is now available with Red Hat Quay 3.12.4. 

The following advisory is available for the _mirror registry for Red Hat OpenShift_ : 

  * [RHBA-2025:0033 - mirror registry for Red Hat OpenShift 2.0.4](https://access.redhat.com/errata/RHBA-2025:0033)



### 4.11.1.9. Mirror registry for Red Hat OpenShift 2.0.3

Issued: 25 November 2024 

_Mirror registry for Red Hat OpenShift_ is now available with Red Hat Quay 3.12.3. 

The following advisory is available for the _mirror registry for Red Hat OpenShift_ : 

  * [RHBA-2024:10181 - mirror registry for Red Hat OpenShift 2.0.3](https://access.redhat.com/errata/RHBA-2024:10181)



### 4.11.1.10. Mirror registry for Red Hat OpenShift 2.0.2

Issued: 31 October 2024 

_Mirror registry for Red Hat OpenShift_ is now available with Red Hat Quay 3.12.2. 

The following advisory is available for the _mirror registry for Red Hat OpenShift_ : 

  * [RHBA-2024:8370 - mirror registry for Red Hat OpenShift 2.0.2](https://access.redhat.com/errata/RHBA-2024:8370)



### 4.11.1.11. Mirror registry for Red Hat OpenShift 2.0.1

Issued: 26 September 2024 

_Mirror registry for Red Hat OpenShift_ is now available with Red Hat Quay 3.12.1. 

The following advisory is available for the _mirror registry for Red Hat OpenShift_ : 

  * [RHBA-2024:7070 - mirror registry for Red Hat OpenShift 2.0.1](https://access.redhat.com/errata/RHBA-2024:7070)



### 4.11.1.12. Mirror registry for Red Hat OpenShift 2.0.0

Issued: 03 September 2024 

_Mirror registry for Red Hat OpenShift_ is now available with Red Hat Quay 3.12.0. 

The following advisory is available for the _mirror registry for Red Hat OpenShift_ : 

  * [RHBA-2024:5277 - mirror registry for Red Hat OpenShift 2.0.0](https://access.redhat.com/errata/RHBA-2024:5277)



The following new features are available with _mirror registry for Red Hat OpenShift_ 2.0.0: 

  * With the release of _mirror registry for Red Hat OpenShift_ , the internal database has been upgraded from PostgreSQL to SQLite. As a result, data is now stored on the `sqlite-storage` Podman volume by default, and the overall tarball size is reduced by 300 MB. 

New installations use SQLite by default. Before upgrading to version 2.0, see "Updating mirror registry for Red Hat OpenShift from a local host" or "Updating mirror registry for Red Hat OpenShift from a remote host" depending on your environment. 

  * A new feature flag, `--sqliteStorage` has been added. With this flag, you can manually set the location where SQLite database data is saved. 
  * _Mirror registry for Red Hat OpenShift_ is now available on IBM Power and IBM Z architectures (`s390x` and `ppc64le`). 



## 4.11.2. Mirror registry for Red Hat OpenShift 1.3 release notes

See the _mirror registry for Red Hat OpenShift_ 1.3 release notes for information about updates and changes. 

To view the _mirror registry for Red Hat OpenShift_ 1.3 release notes, see [Mirror registry for Red Hat OpenShift 1.3 release notes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.13/html/disconnected_installation_mirroring/installing-mirroring-creating-registry#mirror-registry-release-notes-1-3_installing-mirroring-creating-registry). 

## 4.11.3. Mirror registry for Red Hat OpenShift 1.2 release notes

See the _mirror registry for Red Hat OpenShift_ 1.2 release notes for information about updates and changes. 

To view the _mirror registry for Red Hat OpenShift_ 1.2 release notes, see [Mirror registry for Red Hat OpenShift 1.2 release notes](https://docs.openshift.com/container-platform/4.13/installing/disconnected_install/installing-mirroring-creating-registry.html#mirror-registry-release-notes-1-2_installing-mirroring-creating-registry). 

## 4.11.4. Mirror registry for Red Hat OpenShift 1.1 release notes

See the _mirror registry for Red Hat OpenShift_ 1.1 release notes for information about updates and changes. 

To view the _mirror registry for Red Hat OpenShift_ 1.1 release notes, see [Mirror registry for Red Hat OpenShift 1.1 release notes](https://docs.openshift.com/container-platform/4.13/installing/disconnected_install/installing-mirroring-creating-registry.html#mirror-registry-release-notes-1-1_installing-mirroring-creating-registry).
