# 1.11. Asynchronous errata updates

Security, bug fix, and enhancement updates for OpenShift Container Platform 4.22 are released as asynchronous errata through the Red Hat Network. All OpenShift Container Platform 4.22 errata is [available on the Red Hat Customer Portal](https://access.redhat.com/downloads/content/290/). See the [OpenShift Container Platform Life Cycle](https://access.redhat.com/support/policy/updates/openshift) for more information about asynchronous errata. Red Hat Customer Portal users can enable errata notifications in the account settings for Red Hat Subscription Management (RHSM). When errata notifications are enabled, users are notified through email whenever new errata relevant to their registered systems are released. 

Note

Red Hat Customer Portal user accounts must have systems registered and consuming OpenShift Container Platform entitlements for OpenShift Container Platform errata notification emails to generate. 

This section will continue to be updated over time to provide notes on enhancements and bug fixes for future asynchronous errata releases of OpenShift Container Platform 4.22. Versioned asynchronous releases, for example with the form OpenShift Container Platform 4.22.z, will be detailed in subsections. In addition, releases in which the errata text cannot fit in the space provided by the advisory will be detailed in subsections that follow. 

Important

For any OpenShift Container Platform release, always review the instructions on [updating your cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/updating_clusters/#updating-cluster-web-console) properly. 

## 1.11.1. RHSA-2026:79154 - OpenShift Container Platform 4.22.18 bug fix and security update

Issued: 19 October 2026 

OpenShift Container Platform release 4.22.18 is now available. The list of fixed issues that are included in the update is documented in the [RHSA-2026:79154](https://access.redhat.com/errata/RHSA-2026:79154) advisory. The RPM packages that are included in the update are provided by the [RHSA-2026:79150](https://access.redhat.com/errata/RHSA-2026:79150) advisory. 

Space precluded documenting all of the container images for this release in the advisory. 

You can view the container images in this release by running the following command: 

```shell-session
$ oc adm release info 4.22.18 --pullspecs
```


### 1.11.1.1. Enhancements

  * As a General Availability feature, you can deploy a 4.22 cluster without an external registry, using self-contained installation media that also provides a simplified user interface similar to the Assisted Installer during on-premise installations. The installation media also contains Operators you can install that are required to run OpenShift Virtualization Engine. As a postinstallation task, you can also configure your cluster to use an external registry and use the registry for cluster updates. 

For more information, see [Installing a cluster without an external registry](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_an_on-premise_cluster_with_the_agent-based_installer/#installing-ove) and [Configuring your cluster to use an external registry](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/disconnected_environments/#configuring-registry-external). 




### 1.11.1.2. Fixed issues

  * Before this update, the Berkeley Packet Filter (BPF) file system did not allow dots (".") in file names. As a consequence, the Ingress Node Firewall could not attach rules to virtual LAN (VLAN) sub-interfaces such as `bond0.12`. Attempting to pin a link for an interface containing a dot failed with an `operation not permitted` error. With this release, the Ingress Node Firewall sanitizes pin file names by converting dots to a placeholder string. For example, `vlan.100` becomes `vlan_dot_100` before writing to the BPF file system. As a result, firewall rules can be successfully applied to sub-interfaces such as VLANs on top of bonded interfaces. ([OCPBUGS-31495](https://issues.redhat.com/browse/OCPBUGS-31495)) 
  * Before this update, the OpenShift Container Platform Router performed synchronous and sequential `SubjectAccessReview` (SAR) API calls to validate each externally-managed certificate for a route during startup. As a consequence for a cluster with a high amount of external certificate routes, the kubelet stopped any router pod that exceeded the `120` second startup probe timeout value. With this release, a SAR caching mechanism, `sarCache`, and a semaphore throttles concurrent SAR API calls in the router. This process happens alongside any increasing route status that has a writer-lease concurrency. As a result, the initialization time of an OpenShift Container Platform Router is dramatically reduced. This change allows thousands of routes with external certificates to load within the startup probe window and prevents router pods from entering a `CrashLoopBackOff` loop. ([OCPBUGS-99286](https://issues.redhat.com/browse/OCPBUGS-99286)) 
  * Before this update, installing a Helm chart by using the Chart URL option in the OpenShift Container Platform web console with an Open Container Initiative (OCI) URL that included a version number, for example, `oci://registry-1.docker.io/bitnamicharts/nginx:22.6.12` failed with an error indicating that the chart was not available or could not be found. As a consequence, users could not install Helm charts from OCI registries when specifying the version number directly in the URL. With this release, the Helm chart installation process correctly handles OCI URLs that include version numbers. As a result, users can successfully install Helm charts from OCI registries by providing the complete URL with the version number in the web console Chart URL field. ([OCPBUGS-122042](https://issues.redhat.com/browse/OCPBUGS-122042)) 
  * Before this update, when a node with an EgressIP was rebooted, the `ovnkube-cluster-manager` plugin reassigned the EgressIP to a new node but did not immediately remove it from the rebooting node. Both the old and new nodes responded to ARP requests for the same IP address. As a consequence, this MAC address flapping could cause network switches, firewalls, or other devices to malfunction or block EgressIP traffic. With this release, nftables rules block ARP responses from the old node after EgressIP migration. As a result, EgressIP failover completes without MAC address conflicts during node reboots. ([OCPBUGS-128643](https://issues.redhat.com/browse/OCPBUGS-128643)) 
  * Before this update, the Google Cloud platform quota check of the installation program did not retry transient HTTP errors from the Service Usage API. When the Service Usage API returned HTTP 503 `backendError` or HTTP 429 responses, the installation program exited. As a consequence, installations failed due to temporary Google Cloud API issues. With this release, the installation program retries Google Cloud Service Usage quota reads after HTTP 429 and 5xx responses, stopping after five attempts. As a result, installations proceed successfully despite transient Google Cloud Service Usage API errors. ([OCPBUGS-128831](https://issues.redhat.com/browse/OCPBUGS-128831)) 



### 1.11.1.3. Updating

To update an OpenShift Container Platform 4.22 cluster to this latest release, see [Updating a cluster using the CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/updating_clusters/#updating-cluster-cli). 

## 1.11.2. RHSA-2026:74429 - OpenShift Container Platform 4.22.17 bug fix and security update

Issued: 06 October 2026 

OpenShift Container Platform release 4.22.17 is now available. The list of fixed issues that are included in the update is documented in the [RHSA-2026:74429](https://access.redhat.com/errata/RHSA-2026:74429) advisory. The RPM packages that are included in the update are provided by the [RHSA-2026:74427](https://access.redhat.com/errata/RHSA-2026:74427) advisory. 

Space precluded documenting all of the container images for this release in the advisory. 

You can view the container images in this release by running the following command: 

```shell-session
$ oc adm release info 4.22.17 --pullspecs
```


### 1.11.2.1. Fixed issues

  * Before this update, when you removed failure domains from the infrastructure specification, the VMware vSphere Problem Detector (VPD) logged errors about failure domain labels missing from nodes. As a consequence, VPD logged warnings that were not relevant. With this release, VPD improves processing logic for failure domain changes in the infrastructure specification. As a result, these unnecessary warnings no longer appear. ([OCPBUGS-105280](https://issues.redhat.com/browse/OCPBUGS-105280)) 
  * Before this update, in dual-stack hosted clusters, mismatched IP SAN byte lengths such as 4-byte versus 16-byte IPv4-mapped addresses caused false validation failures. As a consequence, the Control Plane Operator was forced to continuously regenerate `kas-server-crt`, causing generation churn that could stall installations. With this release, IP SANs are normalized using net.IP.To1ptp Operator config6() before comparison. As a result, unnecessary certificate regeneration and continuous `kube-apiserver` rolling updates do not occur. ([OCPBUGS-112731](https://issues.redhat.com/browse/OCPBUGS-112731)) 
  * Before this update, for Microsoft Azure OpenShift Container Platform hosted clusters that used private Azure Key Vaults, unreachable private endpoints caused Kubernetes Key Management Service (KMS) validation to be reported as failed. With this update, the `ValidAzureKMSConfig` parameter is reported as `Unknown`. As a result, false failures are not reported due to network reachability limits. ([OCPBUGS-123727](https://issues.redhat.com/browse/OCPBUGS-123727)) 
  * Before this update, when you removed a `MachineConfig` resource that required a revert to a `MachineOSBuild` in a terminal state, the digested image push configuration was not changed. As a consequence, the associated `MachineConfigPool` resource was stuck in an `Updating` state. With this release, terminal builds update correctly when the digested image push configuration changes, enabling image reuse for a new build. As a result, you can successfully delete `MachineConfig` resources in an image mode cluster. ([OCPBUGS-127018](https://issues.redhat.com/browse/OCPBUGS-127018)) 
  * Before this update, the rendezvous node IP address list was not refreshed after a static IP address was added through the agent TUI networking screen. As a consequence, the newly added IP address was not shown or available in the rendezvous node IP address selection screen. With this release, the host IP address list refreshes whenever the selection screen opens. As a result, newly configured IP addresses appear for selection. ([OCPBUGS-127041](https://issues.redhat.com/browse/OCPBUGS-127041)) 
  * Before this update, sometimes during startup the default Precision Time Protocol (PTP) Operator configuration failed to create because the webhook was not ready. As a consequence, the `linuxptp-daemon` service was not scheduled. With this release, the Operator waits for the webhook to become ready before creating the default PTP Operator configuration. As a result, the default PTP Operator configuration is populated reliably. ([OCPBUGS-128642](https://issues.redhat.com/browse/OCPBUGS-128642)) 



### 1.11.2.2. Updating

To update an OpenShift Container Platform 4.22 cluster to this latest release, see [Updating a cluster using the CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/updating_clusters/#updating-cluster-cli). 

## 1.11.3. RHSA-2026:71454 - OpenShift Container Platform 4.22.16 bug fix and security update

Issued: 29 September 2026 

OpenShift Container Platform release 4.22.16 is now available. The list of fixed issues that are included in the update is documented in the [RHSA-2026:71454](https://access.redhat.com/errata/RHSA-2026:71454) advisory. The RPM packages that are included in the update are provided by the [RHSA-2026:71445](https://access.redhat.com/errata/RHSA-2026:71445) advisory. 

Space precluded documenting all of the container images for this release in the advisory. 

You can view the container images in this release by running the following command: 

```shell-session
$ oc adm release info 4.22.16 --pullspecs
```


### 1.11.3.1. Enhancements

  * In OpenShift Container Platform release 4.22.16 and later, you can install OpenShift Container Platform in Google Cloud Dedicated (GCD) regions by using installer-provisioned infrastructure. GCD is a sovereign cloud platform that provides Google Cloud technology in a fully isolated environment with strict data and operational sovereignty guarantees. If you require strict data residency and operational control, you can deploy to sovereign cloud environments. 



### 1.11.3.2. Fixed issues

  * Before this update, when you deployed a hosted cluster on OpenShift Virtualization with external infrastructure, the `virt-launcher` network policy was not created on the infrastructure cluster where the KubeVirt `virt-launcher` pods and virtual machines (VM)s run. As a consequence, the KubeVirt VMs had unrestricted network access to all pods and services on the infrastructure cluster, breaking tenant isolation. With this release, the `virt-launcher` network policy is created with CIDR-based egress restrictions. As a result, multitenant isolation is no longer compromised. ([OCPBUGS-100445](https://issues.redhat.com/browse/OCPBUGS-100445)) 
  * Before this update, when upgrading standalone clusters from 4.21.16 to 4.22.8, worker nodes with older Red Hat Enterprise Linux CoreOS (RHCOS) boot images failed during the operating system pivot with an `rpm-ostree rebase` error: `A signature was required, but no signature exists`. As a consequence, the worker MachineConfigPool became degraded, preventing completion of the upgrade, with some workers remaining on 4.21 RHCOS while the control plane was on 4.22.8. With this release, the Machine Config Operator includes a workaround for nodes running older boot images with skopeo versions earlier than 1.22.2, enabling successful rebase to 4.22 RHCOS images that require `Sigstore` signatures. As a result, all workers can complete the operating system pivot during upgrades from 4.21 to 4.22.z releases. ([OCPBUGS-122961](https://issues.redhat.com/browse/OCPBUGS-122961)) 



### 1.11.3.3. Updating

To update an OpenShift Container Platform 4.22 cluster to this latest release, see [Updating a cluster using the CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/updating_clusters/#updating-cluster-cli). 

## 1.11.4. RHSA-2026:68552 - OpenShift Container Platform 4.22.15 bug fix and security update

Issued: 22 September 2026 

OpenShift Container Platform release 4.22.15 is now available. The list of fixed issues that are included in the update is documented in the [RHSA-2026:68552](https://access.redhat.com/errata/RHSA-2026:68552) advisory. The RPM packages that are included in the update are provided by the [RHSA-2026:68550](https://access.redhat.com/errata/RHSA-2026:68550) advisory. 

Space precluded documenting all of the container images for this release in the advisory. 

You can view the container images in this release by running the following command: 

```shell-session
$ oc adm release info 4.22.15 --pullspecs
```


### 1.11.4.1. Fixed issues

  * Before this update, in Amazon Web Services (AWS), the installation program created a security group rule that applied to cluster nodes and allowed ports 6441 and 6442. However, these ports are not needed or used anywhere. With this update, this security group rule is removed. ([OCPBUGS-95072](https://issues.redhat.com/browse/OCPBUGS-95072)) 
  * Before this update, the `AWSMachine` controller was requeuing machine instances before confirming the presence of tags. As a consequence, duplicate Amazon Web Services (AWS) EC2 instances were created. With this release, the `AWSMachine` controller verifies tags before requeuing instances. As a result, duplicate EC2 instances are not created. ([OCPBUGS-112305](https://issues.redhat.com/browse/OCPBUGS-112305)) 
  * Before this update, the Machine Config Operator (MCO) boot image controller on VMware vSphere incorrectly concatenated failure domain and compute cluster inventory paths using the `path.Join` parameter. As a consequence, the controller created an invalid path when you used absolute paths, for example, `<datacenter>/network/<portgroup>`. The invalid path caused a `failed to find` network error. With this update, the network name is passed directly to the vSphere finder library, which natively supports all network identifier formats. As a result, the failure domain networks are correctly resolved and MCO degradation is prevented. ([OCPBUGS-121849](https://issues.redhat.com/browse/OCPBUGS-121849)) 



### 1.11.4.2. Updating

To update an OpenShift Container Platform 4.22 cluster to this latest release, see [Updating a cluster using the CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/updating_clusters/#updating-cluster-cli). 

## 1.11.5. RHSA-2026:66358 - OpenShift Container Platform 4.22.14 bug fix and security update

Issued: 15 September 2026 

OpenShift Container Platform release 4.22.14 is now available. The list of fixed issues that are included in the update is documented in the [RHSA-2026:66358](https://access.redhat.com/errata/RHSA-2026:66358) advisory. The RPM packages that are included in the update are provided by the [RHSA-2026:66356](https://access.redhat.com/errata/RHSA-2026:66356) advisory. 

Space precluded documenting all of the container images for this release in the advisory. 

You can view the container images in this release by running the following command: 

```shell-session
$ oc adm release info 4.22.14 --pullspecs
```


### 1.11.5.1. Fixed issues

  * Before this update, during `disk-to-mirror` operations, the `oc-mirror` tool reconstructed Helm chart tarball paths by using a fixed format `{name}-{version}.tgz`, for example, `csi-driver-nfs-4.9.0.tgz`, but the Helm downloader could include a "v" prefix in the version, for example, `csi-driver-nfs-v4.9.0.tgz`. As a consequence, `disk-to-mirror` operations failed with the `file not found` errors even though the `mirror-to-disk` download completed successfully. With this update, the `oc-mirror` tool correctly handles both version format variations. As a result, mirror operations complete successfully. [OCPBUGS-90149](https://issues.redhat.com/browse/OCPBUGS-90149)
  * Before this update, on Google Cloud Platform (GCP) clusters, the GCP cloud controller manager could not properly adhere to the `node.kubernetes.io/exclude-from-external-load-balancers` label when selecting load balancer backend nodes. As a consequence, master nodes with the exclusion label were still added as backends to external load balancers. With this release, the cloud controller manager correctly checks for the exclusion label. As a result, master nodes labeled with `node.kubernetes.io/exclude-from-external-load-balancers` are no longer included as load balancer backends. [OCPBUGS-99228](https://issues.redhat.com/browse/OCPBUGS-99228)
  * Before this update, the `baremetal` cluster Operator did not set its `Progressing` status condition to `True` during cluster upgrades. As a consequence, the Cluster Version Operator (CVO) waited for the Operator without receiving proper progress signals, and upgrade monitoring tests failed. With this release, the baremetal Operator correctly reports `Progressing=True` during version changes. As a result, cluster upgrades proceed with accurate Operator status reporting. [OCPBUGS-99390](https://issues.redhat.com/browse/OCPBUGS-99390)
  * Before this update, containers in the `openshift-monitoring` namespace ran with writable root filesystems because `readOnlyRootFilesystem: true` was not enabled in their security contexts. As a consequence, customer compliance scans flagged these containers as security policy violations. With this release, monitoring components enable read-only root filesystems with dedicated `emptyDir` volumes for paths requiring write access. As a result, monitoring containers meet compliance requirements for read-only root filesystems. [OCPBUGS-105469](https://issues.redhat.com/browse/OCPBUGS-105469)
  * Before this update, on Google Cloud Platform (GCP) clusters, values specified in `defaultMachinePlatform` were not applied to individual machine pools during cluster installation. As a consequence, settings such as `osDisk.diskType` were ignored, and control plane nodes used default values instead of the specified configuration. With this release, the installation program correctly applies `defaultMachinePlatform` settings to all machine pools. As a result, GCP machine configurations honor the specified platform defaults. [OCPBUGS-114639](https://issues.redhat.com/browse/OCPBUGS-114639)
  * Before this update, for pods with multiple containers that each requested SR-IOV virtual functions (VFs) from the same shared resource pool via separate network attachments, the Multus container network interface sorted device IDs alphabetically when assigning VFs to network interfaces. As a consequence, the PCI address that the SR-IOV device plugin granted to a container did not always match the PCI address that Multus container network interface wired into that container network namespace, causing pod startup failures with `No such device` errors. With this release, Multus container network interface correctly aligns VF assignments between the device plugin and network attachment operations. As a result, pods with multiple containers sharing SR-IOV resources start successfully without PCI address mismatches. [OCPBUGS-114732](https://issues.redhat.com/browse/OCPBUGS-114732)
  * Before this update, in hosted control planes deployments where the management cluster required a proxy for external access, the CSI driver controller deployments did not receive `HTTP_PROXY`, `HTTPS_PROXY`, and `NO_PROXY` environment variables. As a consequence, CSI driver controller containers could not reach cloud provider APIs through the proxy, causing all volume provisioning operations to fail. With this release, the CSI Operator injects proxy environment variables into hosted control planes CSI driver controller deployments. As a result, volume provisioning operations complete successfully in proxy-enabled hosted control planes environments. [OCPBUGS-119697](https://issues.redhat.com/browse/OCPBUGS-119697)
  * Before this update, upstream GitHub workflow files and issue templates that are not used in OpenShift Container Platform CI were present in the `cluster-api-provider-aws` release branches. As a consequence, the `golangci-lint` CI job failed on every pull request. With this release, the unused `.github` directory files are removed from the release branches. As a result, CI lint jobs complete successfully. [OCPBUGS-119954](https://issues.redhat.com/browse/OCPBUGS-119954)



### 1.11.5.2. Updating

To update an OpenShift Container Platform 4.22 cluster to this latest release, see [Updating a cluster using the CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/updating_clusters/#updating-cluster-cli). 

## 1.11.6. RHSA-2026:63096 - OpenShift Container Platform 4.22.13 bug fix and security update

Issued: 08 September 2026 

OpenShift Container Platform release 4.22.13 is now available. The list of fixed issues that are included in the update is documented in the [RHSA-2026:63096](https://access.redhat.com/errata/RHSA-2026:63096) advisory. The RPM packages that are included in the update are provided by the [RHSA-2026:63091](https://access.redhat.com/errata/RHSA-2026:63091) advisory. 

Space precluded documenting all of the container images for this release in the advisory. 

You can view the container images in this release by running the following command: 

```shell-session
$ oc adm release info 4.22.13 --pullspecs
```


### 1.11.6.1. Enhancements

  * In OpenShift Container Platform release 4.22.13 and later, you can add bare-metal compute machines to an existing OpenShift Container Platform cluster on vSphere. With this capability, you can migrate workloads to physical hardware without reinstalling the cluster. Previously, that bare-metal compute machines feature was listed as a Technology Preview feature. The feature is now generally available for OpenShift Container Platform release 4.22.13 and later. 



### 1.11.6.2. Fixed issues

  * Before this update, the `IngressNodeFirewall` custom resource (CR) could not apply rules on sub-interfaces with dotted names because the Berkeley Packet Filter (BPF) file system did not allow dots (".") in the filenames. With this release, the dots in the interface names are replaced by a placeholder before writing to the BPF file system. As a result, the `IngressNodeFirewall` CR can apply rules on the sub-interfaces. ([OCPBUGS-86993](https://redhat.atlassian.net/browse/OCPBUGS-86993)) 
  * Before this update, the Bare Metal Operator (BMO) `getChecksum()` function accepted non-empty checksums for Oracle Cloud Infrastructure (OCI) images. As a consequence, OCI image provisioning failed. With this release, a check in the `getChecksum()` function rejects non-empty user-provided checksums for OCI images. As a result, OCI image provisioning does not fail. ([OCPBUGS-90570](https://redhat.atlassian.net/browse/OCPBUGS-90570)) 
  * Before this update, detaching and re-attaching a bare-metal host (BMH) using the Redfish Virtual Media driver did not set the `bootMACAddress` parameter. As a consequence, host provisioning failed because port records for the network interface controllers (NICs) were not re-created for the host. With this release, port records are recreated on-demand using the information from the inventory, that is, the HardwareData schema resources. As a result, re-attached hosts are successfully provisioned. ([OCPBUGS-99420](https://redhat.atlassian.net/browse/OCPBUGS-99420)) 
  * Before this update, when the bare-metal host (BMH) `spec.online` parameter was set to `False`, the Bare Metal Operator (BMO) forced Ironic to issue a power off command to the node at the end of inspection, after the ramdisk had been ejected. As a consequence, the node OS lost access to the boot media during shutdown, and filesystem corruption errors were visible on the BMH console. With this release, the node is powered off after inspection, while cleaning up the ramdisk, before ejecting Redfish virtual media. As a result, the host does not lose access to the boot media. ([OCPBUGS-112341](https://redhat.atlassian.net/browse/OCPBUGS-112341)) 
  * Before this update, the `GetMarketplaceImage` function for the installation program experienced timeout issues because the function used a deprecated SDK that lacked a retry mechanism. As a consequence, the marketplace image fetch failed, which terminated the installation. With this release, the timeout for retrieving marketplace images is increased from 30 seconds to five minutes because the `GetMarketplaceImage` function now uses the new Azure SDK to retry requests. As a result, timeout issues do not cause installation failure.([OCPBUGS-112471](https://redhat.atlassian.net/browse/OCPBUGS-112471)) 
  * Before this update, the Node Tuning Operator reconciliation used the rate-limited work queue for all event enqueues. As a consequence, node-tuning configuration was delayed for cluster notes greater than 100. With this release, the Node Tuning Operator reconciliation loop uses the rate-limited work queue only for failures instead of all event enqueues. As a result, node-tuning configuration for cluster nodes greater than 100 is not delayed. ([OCPBUG-112554](https://redhat.atlassian.net/browse/OCPBUGS-112554)) 
  * Before this update, the short description for the `info` command in the Performance Profile Creator (PPC) tool was not updated after the cluster inspection was moved. As a consequence, inconsistencies between the parent help and the info help occurred when you ran the PPC tool. With this release, the short description for the `info` command in the PPC tool is updated to match the current CLI. As a result, the help inconsistencies do not occur when you run the tool. ([OCPBUGS-113579](https://redhat.atlassian.net/browse/OCPBUGS-113579)) 
  * Before this update, the Machine Config Controller `EventRecorder` was initialized with the MCO-specific client set scheme, which did not include core Kubernetes types such as `Node`. As a consequence, drain failure events were silently dropped when a node drain failed, for example, due to a blocking `PodDisruptionBudget` parameter. When a node drain failed, the expected warning events, such as the `DrainThresholdExceeded` event, were not emitted. This issue made drain failures more difficult to diagnose and observe. With this release, the `EventRecorder` scheme is updated to include the core Kubernetes types, which ensures that drain failure events are correctly recorded against `Node` objects. As a result, drain failure events are correctly emitted, which improves observability for node drain issues. ([OCPBUG-114392](https://redhat.atlassian.net/browse/OCPBUGS-114392)) 



### 1.11.6.3. Updating

To update an OpenShift Container Platform 4.22 cluster to this latest release, see [Updating a cluster using the CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/updating_clusters/#updating-cluster-cli). 

## 1.11.7. RHSA-2026:60441 - OpenShift Container Platform 4.22.12 bug fix and security update

Issued: 01 September 2026 

OpenShift Container Platform release 4.22.12 is now available. The list of bug fixes and enhancements that are included in the update is documented in the [RHSA-2026:60441](https://access.redhat.com/errata/RHSA-2026:60441) advisory. The RPM packages that are included in the update are provided by the [RHBA-2026:60439](https://access.redhat.com/errata/RHBA-2026:60439) advisory. 

Space precluded documenting all of the container images for this release in the advisory. 

You can view the container images in this release by running the following command: 

```shell-session
$ oc adm release info 4.22.12 --pullspecs
```


### 1.11.7.1. Enhancements

  * You can now pin the HAProxy version to `2.8` by using the new `haproxyVersion` field from the `IngressResource` API, before upgrading OpenShift Container Platform cluster to 4.23 or 5.0. If you do not pin the HAProxy version, it is upgraded to version `3.2`. ([OCPBUGS-105168](https://issues.redhat.com/browse/OCPBUGS-105168)) 



### 1.11.7.2. Fixed issues

  * Before this update, the machine controller in the Hosted Cluster Config Operator (HCCO) included non-routable ovn-kubernetes routes in the node network configuration. As a consequence, it caused networking conflicts and routing issues. With this release, non-routable routes are filtered out during configuration. As a result, networking conflicts are resolved. ([OCPBUGS-98328](https://issues.redhat.com/browse/OCPBUGS-98328)) 
  * Before this update, by default, the Vertical Pod Autoscaler (VPA) Operator required a control plane node for running workloads. As a consequence, it caused issues in single-node deployments. With this release, the Operator is updated to support deployment without control plane node requirements. As a result, the VPA Operator now functions correctly in single-node configurations. ([OCPBUGS-98604](https://issues.redhat.com/browse/OCPBUGS-98604)) 
  * Before this update, socket connections triggered multiple state synchronization, leading to excessive socket connection reconciliation. As a consequence, it caused unnecessary API calls and reduced performance. With this release, the reconciliation logic is updated to synchronize only on meaningful state changes. As a result, API calls are reduced and performance is improved. ([OCPBUGS-105877](https://issues.redhat.com/browse/OCPBUGS-105877)) 
  * Before this update, the console required cloud credentials during Operator initialization. As a consequence, installation failed when credentials were not immediately available. With this release, the initialization process is updated to defer credential requirements. As a result, installation succeeds without requiring immediate cloud credentials. ([OCPBUGS-111417](https://issues.redhat.com/browse/OCPBUGS-111417)) 



### 1.11.7.3. Updating

To update an OpenShift Container Platform 4.22 cluster to this latest release, see [Updating a cluster using the CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/updating_clusters/#updating-cluster-cli). 

## 1.11.8. RHSA-2026:57365 - OpenShift Container Platform 4.22.11 bug fix and security update

Issued: 25 August 2026 

OpenShift Container Platform release 4.22.11 is now available with updates to packages and images that fix several bugs. The list of bug fixes that are included in the update is documented in the [RHSA-2026:57365](https://access.redhat.com/errata/RHSA-2026:57365) advisory. The RPM packages that are included in the update are provided by the [RHSA-2026:57361](https://access.redhat.com/errata/RHSA-2026:57361) advisory. 

Space precluded documenting all of the container images for this release in the advisory. 

You can view the container images in this release by running the following command: 

```shell-session
$ oc adm release info 4.22.11 --pullspecs
```


### 1.11.8.1. Fixed issues

  * Before this update, the OpenShift Container Platform web console used the identity UID as the settings key, and that UID differed across identity providers. As a consequence, the OpenShift Container Platform web console created a duplicate `user-settings` `ConfigMap` object each time you logged in if you had multiple identity providers such as LDAP and OpenID. With this release, the console now uses a stable hash of your user name as the settings key instead of the identity UID and automatically migrates existing settings on upgrade. As a result, the OpenShift Container Platform web console reuses a single `user-settings` `ConfigMap` object per user across all identity providers and login sessions. ([OCPBUGS-87832](https://issues.redhat.com/browse/OCPBUGS-87832)) 
  * Before this update, when you navigated to a **Terminal** tab of a node in the OpenShift Container Platform web console, the component checked for the debug pod even if the pod was still being created. As a consequence, a `Debug pod not found or was deleted.` error appeared before the terminal loaded successfully. With this release, a loading spinner is shown when the debug pod is being created, and the cleanup logic guards against an undefined namespace to prevent errors on early unmount. As a result, the **Terminal** tab of a node loads without displaying a false error message. ([OCPBUGS-100402](https://issues.redhat.com/browse/OCPBUGS-100402)) 
  * Before this update, the Cluster Monitoring Operator did not specify resource limits for some of its managed components. As a consequence, in clusters with limited resources, these components could be evicted due to memory pressure. With this release, the Cluster Monitoring Operator now sets appropriate resource limits for all managed components. As a result, components are less likely to be evicted in resource-constrained environments. ([OCPBUGS-105190](https://issues.redhat.com/browse/OCPBUGS-105190)) 
  * Before this update, the `azure-disk` CSI driver controller attempted to read the `kube-system/azure-cloud-provider` secret. As a consequence, the controller could crash when reading this secret. With this release, the `azure-disk` CSI driver controller no longer attempts to read the `kube-system/azure-cloud-provider` secret and instead falls back to `AZURE_CREDENTIAL_FILE` unconditionally. As a result, the `azure-disk` CSI driver controller no longer crashes. ([OCPBUGS-106152](https://issues.redhat.com/browse/OCPBUGS-106152)) 
  * Before this update, the `kas-connection-checker` deployment created in the `kube-system` namespace of a hosted cluster did not set a security context. Because the `kube-system` is an exempt from both SCC and Pod Security admission, no UID was assigned. As a consequence, the `kas-connection-checker` pods ran as root (UID 0) in the hosted cluster even though the workload does not need elevated privileges. With this release, an explicit non-root security context is set for the `kas-connection-checker` pods. As a result, the pods no longer run as root. ([OCPBUGS-111083](https://issues.redhat.com/browse/OCPBUGS-111083)) 
  * Before this update, the Go OpenSSL FIPS provider could potentially overwhelm the `libcrypto` library with concurrent requests. As a consequence, processes could hit the `maxThreads` limit of 10,000 and crash. With this release, the Go OpenSSL FIPS provider is updated to limit concurrent requests to the `libcrypto` library to four times the number of CPUs, buffering requests as lightweight Go routines. As a result, processes avoid the `maxThreads` limit and do not crash. ([OCPBUGS-112084](https://issues.redhat.com/browse/OCPBUGS-112084)) 



### 1.11.8.2. Updating

To update an OpenShift Container Platform 4.22 cluster to this latest release, see [Updating a cluster using the CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/updating_clusters/#updating-cluster-cli). 

## 1.11.9. RHSA-2026:54770 - OpenShift Container Platform 4.22.10 bug fix and security update

Issued: 18 August 2026 

OpenShift Container Platform release 4.22.10 is now available. The list of fixed issues that are included in the update is documented in the [RHSA-2026:54770](https://access.redhat.com/errata/RHSA-2026:54770) advisory. The RPM packages that are included in the update are provided by the [RHBA-2026:54768](https://access.redhat.com/errata/RHBA-2026:54768) advisory. 

Space precluded documenting all of the container images for this release in the advisory. 

You can view the container images in this release by running the following command: 

```shell-session
$ oc adm release info 4.22.10 --pullspecs
```


### 1.11.9.1. Enhancements

  * Azure OpenShift Container Platform hosted control planes clusters can now authenticate to Azure Container Registry (ACR) by using managed identities through a new optional `containerRegistry` field in the `AzurePlatformSpec` specification. When you configure ACR credentials with a user-assigned managed identity, worker nodes can authenticate to ACR by using managed identities without requiring manual configuration of image pull secrets in every namespace. ([OCPBUGS-94518](https://redhat.atlassian.net/browse/OCPBUGS-94518)) 



### 1.11.9.2. Fixed issues

  * Before this update, changing non-hardware fields such as `clusterInstance` labels, annotations, or policy parameters in a `ProvisioningRequest` spec triggered an unnecessary `NodeAllocationRequest` reconfiguration. As a consequence, the `ProvisioningRequest` could remain stuck in `Hardware provisioning completed: Created` state with the message `Waiting for NodeAllocationRequest to be configured`. With this release, the controller no longer reconfigures `NodeAllocationRequest` for non-hardware spec changes. As a result, day-2 `ProvisioningRequest` spec updates that do not affect hardware provisioning complete successfully. ([OCPBUGS-90659](https://redhat.atlassian.net/browse/OCPBUGS-90659)) 
  * Before this update, the `NetworkPolicy` object in the `openshift-apiserver` namespace blocked traffic on the port used by the `check-endpoints` service. As a consequence, Prometheus could not scrape those metrics, and the `TargetDown` warning alert could fire when all `check-endpoints` targets were unreachable for more than 15 minutes. With this release, the `NetworkPolicy` object allows traffic on the designated port for the `check-endpoints` service. As a result, Prometheus can reach the endpoints successfully, and the `TargetDown` alert no longer fires for this target. ([OCPBUGS-100168](https://redhat.atlassian.net/browse/OCPBUGS-100168)) 
  * Before this update, on a single-stack IPv4 hosted control planes KubeVirt hosted cluster running on a dual-stack management cluster, the konnectivity proxy could resolve external host names to IPv6 addresses. As a consequence, external requests from the hosted control planes could be sent over IPv6 and time out because the single-stack IPv4 data plane could not reach those addresses. With this release, konnectivity proxy DNS resolution prefers IPv4 addresses on single-stack IPv4 hosted control planes. As a result, external requests use reachable IPv4 addresses and complete successfully. ([OCPBUGS-100332](https://redhat.atlassian.net/browse/OCPBUGS-100332)) 
  * Before this update, when a HostedCluster `spec.configuration.proxy` setting was scoped to data-plane components in 4.18, the Cluster Version Operator (CVO) was not updated to ignore that proxy configuration on hosted control planes. As a consequence, when a proxy setting did not work in the management cluster control-plane network, CVO egress to the OpenShift Update Service and PromQL services could fail and block update advice retrieval. With this release, the CVO ignores the hosted Proxy resource on hosted control planes and assumes no proxy configuration is needed for control-plane egress. As a result, CVO can reach update services in environments where the data-plane proxy setting is incompatible with the management cluster control-plane network. ([OCPBUGS-104545](https://redhat.atlassian.net/browse/OCPBUGS-104545)) 
  * Before this update, when you added a new vSphere failure domain that used a MachineSet with a custom `providerSpec.Template` name, the Machine Config Operator boot image controller looked up the VM template only by its own computed name and ignored `providerSpec.Template`. As a consequence, reconciliation for that failure domain could fail, and a customer-managed VM with the same computed name outside the MCO workspace folder could be mistaken for the MCO template and overwritten. With this release, the controller checks `providerSpec.Template` first, falls back to the computed name only when the template is not found, creates the template from the OVA when needed, and leaves name matches outside `providerSpec.Workspace.Folder` untouched. As a result, new vSphere failure domains with custom template names reconcile successfully, and customer-managed VMs outside the MCO workspace folder are no longer at risk of being overwritten. ([OCPBUGS-104563](https://redhat.atlassian.net/browse/OCPBUGS-104563)) 
  * Before this update, on a Telecom Boundary Clock (T-BC) PTP configuration, the `ts2phc` system daemon could start before the upstream PTP source was stable enough and before `phc2sys` system clock sync was ready. As a consequence, the T-BC took a long time to converge, and `phc2sys` system clock sync could adjust the system clock too early based on an irrelevant `ts2phc` system daemon offset. With this release, the `ts2phc` system daemon start on T-BC is delayed until the upstream source is qualified and the `phc2sys` system clock is ready; Telecom Grandmaster (T-GM) behavior is unchanged. As a result, T-BC no longer starts the `ts2phc` system daemon against an unqualified upstream source. ([OCPBUGS-104578](https://redhat.atlassian.net/browse/OCPBUGS-104578)) 
  * Before this update, when you viewed `execute code` snippets on the **Quick Start** page in the OpenShift Container Platform web console, leading whitespace in the code block could render as an empty line before the command text. As a consequence, `execute code` snippets across the **Quick Start** page could display an extra blank line above the command, making the content harder to read. With this release, leading whitespace rendering in the `execute code` snippet on the **Quick Start** page is corrected. As a result, execute code blocks display the command text without a spurious empty line above it. ([OCPBUGS-105611](https://redhat.atlassian.net/browse/OCPBUGS-105611)) 



### 1.11.9.3. Updating

To update an OpenShift Container Platform 4.22 cluster to this latest release, see [Updating a cluster using the CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/updating_clusters/#updating-cluster-cli). 

## 1.11.10. RHSA-2026:51038 - OpenShift Container Platform 4.22.9 bug fix and security update

Issued: 11 August 2026 

OpenShift Container Platform release 4.22.9 is now available. The list of fixed issues that are included in the update is documented in the [RHSA-2026:51038](https://access.redhat.com/errata/RHSA-2026:51038) advisory. The RPM packages that are included in the update are provided by the [RHSA-2026:51036](https://access.redhat.com/errata/RHSA-2026:51036) advisory. 

Space precluded documenting all of the container images for this release in the advisory. 

You can view the container images in this release by running the following command: 

```shell-session
$ oc adm release info 4.22.9 --pullspecs
```


### 1.11.10.1. Enhancements

  * Dry-run was not generating cluster resource files before this enhancement. Now in disk-to-mirror (`d2m`) and mirror-to-mirror (`m2m`) workflows, the dry-run also generates the resource files without the need of mirroring the images. ([OCPBUGS-93773](https://redhat.atlassian.net/browse/OCPBUGS-93773)) 



### 1.11.10.2. Fixed issues

There are no notable fixed issues in this release. 

### 1.11.10.3. Updating

To update an OpenShift Container Platform 4.22 cluster to this latest release, see [Updating a cluster using the CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/updating_clusters/#updating-cluster-cli). 

## 1.11.11. RHSA-2026:48693 - OpenShift Container Platform 4.22.8 bug fix and security update

Issued: 04 August 2026 

OpenShift Container Platform release 4.22.8 is now available. The list of fixed issues that are included in the update is documented in the [RHSA-2026:48693](https://access.redhat.com/errata/RHSA-2026:48693) advisory. The RPM packages that are included in the update are provided by the [RHBA-2026:48694](https://access.redhat.com/errata/RHBA-2026:48694) advisory. 

Space precluded documenting all of the container images for this release in the advisory. 

You can view the container images in this release by running the following command: 

```shell-session
$ oc adm release info 4.22.8 --pullspecs
```


### 1.11.11.1. Notable technical changes

Metrics forwarding annotation is deprecated
    

As of OpenShift Container Platform 4.22.8, the `hypershift.openshift.io/enable-metrics-forwarding` annotation is deprecated. The `spec.monitoring.metricsForwarding` field on the `HostedCluster` API replaces this annotation and provides per-cluster configuration that the annotation cannot support. 

The annotation continues to be honored when `spec.monitoring` is not set on the `HostedCluster` object. If you set `spec.monitoring.metricsForwarding` on a cluster, the spec field takes precedence and the annotation is ignored for that cluster, even if both are present. 

Migrate all hosted clusters that use the `hypershift.openshift.io/enable-metrics-forwarding` annotation to use `spec.monitoring.metricsForwarding` before the annotation is removed in a future release. For more information, see [Migrating from annotation-based to API-based metrics forwarding](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/hosted_control_planes/#hcp-cp-metrics-forwarding-migrate_hcp-observability). 

### 1.11.11.2. Fixed issues

  * Before this update, setting the `.spec.timeZone` parameter in a cron job might have crashed the kube-state-metrics (KSM) pod. This issue removed the cluster metrics and monitoring alerts. With this release, kube-state-metrics (KSM) gracefully skip cron job objects with unparseable schedules instead of crashing. As a result, the KSM pod remains stable and continues to serve metrics for all cluster resources, even when individual cron job objects have schedules or time zones that cannot be parsed. ([OCPBUGS-87957](https://redhat.atlassian.net/browse/OCPBUGS-87957)) 
  * Before this update, KubeVirt-based `NodePool` resources incorrectly reported `ClusterNetworkCIDRConflict` errors because the controller flagged OVN-Kubernetes internal overlay IP addresses as conflicting with the cluster network. With this release, Classless Inter-Domain Routing (CIDR) conflict detection is triggered only when all the non-link local addresses for the machine fall within the cluster network. As a result, when external addresses exist, in-network addresses are correctly treated as expected container network interface (CNI) internal IP addresses, which prevents false positive conflict reports. ([OCPBUGS-97921](https://redhat.atlassian.net/browse/OCPBUGS-97921)) 
  * Before this update, on hosted control plane (HCP) clusters where the management cluster required a proxy for outbound internet access, the `Konnectivity` proxy sidecar containers did not receive the management cluster proxy environment variables such as `HTTP_PROXY`, `HTTPS_PROXY`, and `NO_PROXY`. As a consequence, cloud API calls to Amazon Web Services (AWS), Microsoft Azure, or IBM Cloud® endpoints made through the direct cloud API bypass path failed with TLS handshake timeouts. With this release, management cluster proxy environment variables are propagated to the `Konnectivity` sidecar containers when the direct cloud API connection feature is enabled. As a result, cloud API calls succeed through the proxy. ([OCPBUGS-99299](https://redhat.atlassian.net/browse/OCPBUGS-99299)) 
  * Before this update, Alertmanager crashed because the `tzdata` package was missing in the OpenShift Container Platform base images, This issue caused the absence of the `/usr/share/zoneinfo` directory. As a consequence, Alertmanager pods failed to start, which made time-based alerts inaccessible for the time zones. With this release, the `tzdata` package has been reinstated in OpenShift Container Platform images. As a result, Alertmanager does not crash on startup when location fields are present in the `active_interval` or `mute_interval` entries. ([OCPBUGS-99442](https://redhat.atlassian.net/browse/OCPBUGS-99442)) 
  * Before this update, the web console storage unit parser treated a `findIndex` result of `0` for the largest unit, `Ei` or `EiB`, as not found, and the binary byte unit list omitted `EiB`. As a consequence, creating a persistent volume claim (PVC) with an exbibyte-sized request, for example `1Ei` or `1EiB`, displayed the requested capacity as `0 B` on the PVC details page, even though the API stored the correct value. With this release, the unit lookup logic recognizes index `0` as valid and includes `EiB` in the binary byte units used for humanization. As a result, the PVC details page displays the correct capacity, for example `1 EiB`, when storage is requested in exbibyte units. ([OCPBUGS-99545](https://redhat.atlassian.net/browse/OCPBUGS-99545)) 
  * Before this update, locale files under `locales/{xx}/olm.json` translated the Kubernetes custom resource kind names `CatalogSource` and `OperatorGroup` into local languages. As a consequence, in non-English UI locales, Operator Lifecycle Manager (OLM) pages displayed localized labels for these resource kinds that did not match the API, the CLI (`oc`), or YAML, which caused inconsistency and confusion. With this release, the canonical English kind names `CatalogSource` and `OperatorGroup` are restored in the affected OLM locale files so that they are not translated. As a result, `CatalogSource` and `OperatorGroup` labels are in English across all locales and stay consistent with the API and CLI. ([OCPBUGS-99548](https://redhat.atlassian.net/browse/OCPBUGS-99548)) 
  * Before this update, the Cluster Monitoring Operator (CMO) checked only the `openshift-config/pull-secret` for the `cloud.openshift.com` authentication token used by the telemeter client. As a consequence, on platforms where this secret did not contain the token, such as the Microsoft Azure Red Hat OpenShift hosted control plane, the telemeter client was not deployed, which prevented cluster registration in Red Hat OpenShift Cluster Manager. With this release, the CMO falls back to `kube-system/global-pull-secret` if the token is not found in the primary secret. As a result, the telemeter client is deployed correctly. ([OCPBUGS-99748](https://redhat.atlassian.net/browse/OCPBUGS-99748)) 



### 1.11.11.3. Updating

To update an OpenShift Container Platform 4.22 cluster to this latest release, see [Updating a cluster using the CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/updating_clusters/#updating-cluster-cli). 

## 1.11.12. RHSA-2026:44237 - OpenShift Container Platform 4.22.7 bug fix and security update

Issued: 28 July 2026 

OpenShift Container Platform release 4.22.7 is now available. The list of fixed issues that are included in the update is documented in the [RHSA-2026:44237](https://access.redhat.com/errata/RHSA-2026:44237) advisory. The RPM packages that are included in the update are provided by the [RHBA-2026:44229](https://access.redhat.com/errata/RHBA-2026:44229) advisory. 

Space precluded documenting all of the container images for this release in the advisory. 

You can view the container images in this release by running the following command: 

```shell-session
$ oc adm release info 4.22.7 --pullspecs
```


### 1.11.12.1. Fixed issues

  * Before this update, when multiple KubeVirt virtual machines shared the same hostname on localnet or layer2 networks, OVN-Kubernetes could not correctly discover virtual machine names from virt-launcher pods. As a consequence, live migration failed for these virtual machines. With this release, the method by which OVN-Kubernetes discovers virtual machine names from virt-launcher pods has been updated. As a result, virtual machines can live migrate without issues even when sharing a hostname. ([OCPBUGS-88733](https://issues.redhat.com/browse/OCPBUGS-88733)) 
  * Before this update, during pod deletion on localnet topologies with interconnect, the `enableSourceLSPFailedLiveMigration` attribute attempted to re-enable the logical switch port (LSP) of the source pod after a failed live migration. This occurred even if the source pod was not on the local node. As a consequence, target pod cleanup was blocked, creating a stale LSP for an already deleted virtual machine and causing a loss of network connectivity. With this release, a locality guard ensures that the source LSP is re-enabled only when the source pod is scheduled in the local zone or the network uses layer2 interconnect transport. As a result, the system re-enables the source LSP only if the source pod is in the local zone, or if the network uses a layer 2 interconnect transport. As a result, the system prevents stale LSPs and maintains network connectivity after a live migration. ([OCPBUGS-88734](https://issues.redhat.com/browse/OCPBUGS-88734)) 
  * Before this update, the Vertical Pod Autoscaler (VPA) Operator required a control plane node for running VPA controllers, even on hosted control planes clusters where no such nodes exist in the guest cluster. As a consequence, installing the VPA Operator on hosted control planes clusters failed. With this release, VPA controllers can run on any available nodes in hosted control planes clusters. As a result, the VPA Operator installs successfully on hosted control planes clusters. ([OCPBUGS-89265](https://issues.redhat.com/browse/OCPBUGS-89265)) 
  * Before this update, when managing a high volume of `BareMetalHost` resources on a single Multicluster Engine instance, the BareMetal Operator issued excessive requests to the Provisioner API during reconciliation. As a consequence, VirtualMedia injection and node reconciliation were noticeably slower at this scale. With this release, the BareMetal Operator reconciliation loop is optimized to issue fewer requests to the Provisioner API. As a result, responsiveness improves when managing large numbers of BareMetalHost resources. ([OCPBUGS-94109](https://issues.redhat.com/browse/OCPBUGS-94109)) 
  * Before this update, when telemeter-client availability flickered because of monitoring pod restarts or node disruptions, the console Operator produced different ConfigMap content on each sync cycle. As a consequence, continuous console pod rollouts destroyed in-memory sessions and logged users out of the OpenShift Container Platform web console approximately every 5 minutes. With this release, the telemetry configuration always produces a stable key set regardless of telemeter-client availability. As a result, unnecessary console pod rollouts are prevented and users are no longer logged out unexpectedly. ([OCPBUGS-97828](https://issues.redhat.com/browse/OCPBUGS-97828)) 



### 1.11.12.2. Updating

To update an OpenShift Container Platform 4.22 cluster to this latest release, see [Updating a cluster using the CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/updating_clusters/#updating-cluster-cli). 

## 1.11.13. RHSA-2026:40768 - OpenShift Container Platform 4.22.6 bug fix and security update

Issued: 21 July 2026 

OpenShift Container Platform release 4.22.6 is now available. The list of fixed issues that are included in the update is documented in the [RHSA-2026:40768](https://access.redhat.com/errata/RHSA-2026:40768) advisory. The RPM packages that are included in the update are provided by the [RHBA-2026:40763](https://access.redhat.com/errata/RHBA-2026:40763) advisory. 

Space precluded documenting all of the container images for this release in the advisory. 

You can view the container images in this release by running the following command: 

```shell-session
$ oc adm release info 4.22.6 --pullspecs
```


### 1.11.13.1. New features

Self-service Technical Supportability Review
    

You can use the self-service Technical Supportability Review (TSR) on the Red Hat Customer Portal to validate your cluster configuration against Red Hat common practices. The self-service TSR uses AI to evaluate your cluster’s `must-gather` data and provides a prioritized executive summary that identifies your cluster’s top risks and recommends corrective actions. The TSR performs hundreds of checks across the OpenShift Container Platform platform, including OpenShift Virtualization, and coverage is continually expanding. 

For more information, see [Technical Supportability Review with AI tool](https://access.redhat.com/support/cases/#/analyze) and [Red Hat Technical Supportability Review with AI: Proactive AI-Driven Cluster Assessments for OpenShift Container Platform](https://access.redhat.com/solutions/7141255). 

### 1.11.13.2. Fixed issues

  * Before this update, vSphere Container Storage Interface (CSI) volume provisioning could fail when new ESXi hosts in maintenance mode lacked datastore access. With this release, volume provisioning skips ESXi hosts that are in maintenance mode, and the CSI driver is updated to version 3.6.2. As a result, volume provisioning succeeds when hosts are in maintenance mode. ([OCPBUGS-92190](https://redhat.atlassian.net/browse/OCPBUGS-92190)) 
  * Before this update, when you navigated to **Compute** **Nodes** **[node]** **Terminal** in the OpenShift Container Platform web console, the component checked for the debug pod while the pod was still being created. As a consequence, a `Debug pod not found or was deleted.` error briefly flashed before the terminal loaded successfully. With this release, a loading spinner is shown while the debug pod is being created, and the cleanup logic guards against an undefined namespace to prevent errors on early unmount. As a result, the node **Terminal** tab loads without displaying a false error message. ([OCPBUGS-95580](https://redhat.atlassian.net/browse/OCPBUGS-95580)) 
  * Before this update, the Cluster Ingress Operator migrated Gateway API from Operator Life Management (OLM) to the Sail Library. As a consequence, the subscription persisted with the `ingress.operator.openshift.io/owned` annotation and Red Hat OpenShift Service Mesh users did not know whether to retain or delete these subscriptions. With this release, an `OrphanedOSSMSubscription` Prometheus alert, gauge metric, and `ClusterOperator` status condition identify these orphaned Service Mesh subscriptions and provide remediation guidance. As a result, the metric resets after the annotation is removed. ([OCPBUGS-97563](https://redhat.atlassian.net/browse/OCPBUGS-97563)) 
  * Before this update, the oc-mirror plugin failed to find signatures for multi-architecture OpenShift Container Platform payloads. As a consequence, the mirror-to-disk process failed when writing the `tar` archive file. With this release, oc-mirror correctly handles multi-architecture OpenShift Container Platform payloads that have unsigned manifest lists. As a result, mirror-to-disk operations complete successfully for multi-architecture payloads. ([OCPBUGS-97946](https://redhat.atlassian.net/browse/OCPBUGS-97946)) 



### 1.11.13.3. Updating

To update an OpenShift Container Platform 4.22 cluster to this latest release, see [Updating a cluster using the CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/updating_clusters/#updating-cluster-cli). 

## 1.11.14. RHSA-2026:37585 - OpenShift Container Platform 4.22.5 bug fix and security update

Issued: 14 July 2026 

OpenShift Container Platform release 4.22.5 is now available. The list of fixed issues that are included in the update is documented in the [RHSA-2026:37585](https://access.redhat.com/errata/RHSA-2026:37585) advisory. The RPM packages that are included in the update are provided by the [RHBA-2026:37583](https://access.redhat.com/errata/RHBA-2026:37583) advisory. 

Space precluded documenting all of the container images for this release in the advisory. 

You can view the container images in this release by running the following command: 

```shell-session
$ oc adm release info 4.22.5 --pullspecs
```


### 1.11.14.1. Fixed issues

  * Before this update, when deploying a hosted cluster on AWS in non-commercial ISO or classified regions, the Cluster Network Operator (CNO) assumed a maximum transmission unit (MTU) of `9001` for hosted cluster nodes. Because some of these regions do not support jumbo frames at this MTU value, and the setting could not be overridden during cluster creation, networking for hosted clusters in these regions could fail to configure correctly. With this release, you can specify an OVN-Kubernetes tunnel interface MTU between `576` and `9216` at cluster creation time. You can configure this setting by using the optional, immutable `mtu` field in the `ovnKubernetesConfig` configuration of the `HostedCluster` custom resource (CR) or by using the `--ovn-kubernetes-mtu` hosted control planes CLI flag. As a result, you can successfully deploy hosted clusters in AWS regions that do not support jumbo frames, and the CNO applies the correct MTU value. ([OCPBUGS-77078](https://redhat.atlassian.net/browse/OCPBUGS-77078)) 
  * Before this update, when you filtered projects on the **Projects** list page in the OpenShift Container Platform web console, the filter matched only the project `metadata.name` value and not the display name stored in the `openshift.io/display-name` annotation. As a consequence, typing a project display name in the filter toolbar returned no results even when a matching project existed. With this release, the **Projects** list filter includes the display name in its matching logic for both fuzzy and exact search modes. As a result, you can filter projects by either their technical name or their display name. ([OCPBUGS-90495](https://redhat.atlassian.net/browse/OCPBUGS-90495)) 
  * Before this update, on Secure Boot-enabled clusters with nodes originally installed on OpenShift Container Platform 4.15 or earlier, the Machine Config Operator (MCO) verified the shim version in the node operating system image rather than in the EFI System Partition (ESP). Nodes that were updated in place could have outdated shim and GRand Unified Bootloader (GRUB) binaries on the ESP while the operating system image contained newer versions. As a consequence, the MCO incorrectly skipped the boot loader update workaround for those nodes during a cluster update, and the nodes could fail to boot after the update. With this release, when a node runs Red Hat Enterprise Linux (RHEL) 9.6 or later, the MCO runs a node-level boot loader update by using `bootupctl` before it pulls the new node image container, and falls back to the existing container-based update path if the node-level update fails. As a result, nodes with stale boot loader files on the ESP are updated correctly and boot successfully after updating to this release. ([OCPBUGS-93743](https://redhat.atlassian.net/browse/OCPBUGS-93743)) 
  * Before this update, when Prometheus compacted time series data, it attempted to enable direct input/output on files that were already open. Some file systems, such as IBM Storage Scale, do not support this operation. As a consequence, compaction failed with a `cannot enable Direct IO: invalid argument` error, Prometheus could not write chunks to disk, and memory usage in Prometheus pods increased until the pods hit their memory limits and restarted or affected other workloads on the node. With this release, Prometheus detects when a file system does not support direct input/output on open files and handles the condition gracefully. As a result, Prometheus writes chunks to disk and completes compaction successfully on these storage back ends. ([OCPBUGS-93919](https://redhat.atlassian.net/browse/OCPBUGS-93919)) 
  * Before this update, the ironic-agent container image was missing the `iproute` package at runtime, which provides the `ip` command required for network configuration. As a consequence, the Ironic Python Agent (IPA) failed to heartbeat to Ironic during bare-metal node cleaning, and node cleaning operations timed out. With this release, the ironic-agent container image build process is updated to retain required packages such as `iproute` and `psmisc`. As a result, IPA completes network configuration successfully and bare-metal node cleaning operations complete without timing out. ([OCPBUGS-95061](https://redhat.atlassian.net/browse/OCPBUGS-95061)) 
  * Before this update, when you provisioned machines on an OpenStack cloud provider that does not support the optional Standard Attributes Tag extension, the Machine API Provider for OpenStack (MAPO) attempted to apply port tags during network port creation. As a consequence, network port creation failed and machine provisioning did not complete. With this release, MAPO checks whether the OpenStack Neutron `standard-attr-tag` extension is available before applying port tags. If the extension is not supported, MAPO skips tag assignment during provisioning. If you explicitly configure port tags on an unsupported OpenStack deployment, MAPO returns an error that prompts you to remove the port tags configuration. As a result, machine provisioning completes successfully on OpenStack deployments that do not support the tag extension. ([OCPBUGS-97826](https://redhat.atlassian.net/browse/OCPBUGS-97826)) 



### 1.11.14.2. Updating

To update an OpenShift Container Platform 4.22 cluster to this latest release, see [Updating a cluster using the CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/updating_clusters/#updating-cluster-cli). 

## 1.11.15. RHSA-2026:34794 - OpenShift Container Platform 4.22.4 bug fix and security update

Issued: 07 July 2026 

OpenShift Container Platform release 4.22.4 is now available. The list of fixed issues that are included in the update is documented in the [RHSA-2026:34794](https://access.redhat.com/errata/RHSA-2026:34794) advisory. The RPM packages that are included in the update are provided by the [RHSA-2026:34789](https://access.redhat.com/errata/RHSA-2026:34789) advisory. 

Space precluded documenting all of the container images for this release in the advisory. 

You can view the container images in this release by running the following command: 

```shell-session
$ oc adm release info 4.22.4 --pullspecs
```


### 1.11.15.1. Fixed issues

  * Before this update, Role Based Access Control (RBAC) permissions were insufficient for the Secrets Store CSI driver in the Control Plane Operator on the management cluster. As a consequence, users could not create hosted clusters with the Secrets Store CSI driver and the Control Plane Operator on versions later than 4.19.19. With this release, the Control Plane Operator now checks the accessibility of resource types before creation, granting access to the Secrets Store CSI driver and enabling successful hosted cluster creation. ([OCPBUGS-65687](https://redhat.atlassian.net/browse/OCPBUGS-65687)) 
  * Before this update, a transient failure to attach or detach a persistent volume to a node sometimes occurred. As a consequence, the Machine API Operator incorrectly marked the Machine as permanently failed. With this release, the Machine API provider for Microsoft Azure does not misinterpret the failure of any asynchronous operation on an Azure VM as a failure to provision the VM. As a result, the failure of a volume attach or a volume detach does not affect the status of the Machine object. ([OCPBUGS-86996](https://issues.redhat.com/browse/OCPBUGS-86996)) 
  * Before this update, changes to the `tlsAdherence` feature, such as `""` `StrictAllComponents`, would not trigger a Cluster Baremetal Operator (CBO) restart. As a consequence, the Operator would run with a stale TLS (Transport Layer Security) configuration. With this release, the `controller-runtime-common` resource is updated to watch both the `tlsAdherence` field and the TLS security profile on the API Server custom resource (CR) in the Security Profile Watcher. As a result, changes to the `tlsAdherence` feature triggers a CBO restart as expected. ([OCPBUGS-87212](https://issues.redhat.com/browse/OCPBUGS-87212)) 
  * Before this update, the Hosted Cluster Config Operator would crash loop on an uncustomized Kubernetes cluster because the Operator was unconditionally attempting to watch the OpenShift Container Platform Route resource. With this release, the Operator attempts to watch the resource only when it exists on the management cluster. As a result, the Operator is no longer crash looping on an uncustomized Kubernetes cluster. ([OCPBUGS-87364](https://issues.redhat.com/browse/OCPBUGS-87364)) 
  * Before this update, the `kube-apiserver-to-kubelet` client signer certificate was being refreshed every 30 days despite having a 365-day validity period. With this release, the refresh interval is corrected to 292 days, 80% of validity, which is consistent with other signers. As a result, certificate rotations are prevented and the signer behavior is aligned with the intended configuration. ([OCPBUGS-87844](https://issues.redhat.com/browse/OCPBUGS-87844)) 
  * Before this update, deleting a BareMetalHost (BMH) that referenced a pre-provisioning network data Secret through the `spec.preprovisioningNetworkDataName` parameter could report a `RegistrationError` if the Secret was removed before the BMH finished deleting. As a consequence, the BMH deletion would take minutes to complete before an eventual force-delete by the controller. With this enhancement, the Bare Metal Operator (BMO) manages the lifecycle of that Secret in the same way as the BMC credential Secrets. The BMO now protects the Secret using a finalizer while the host is active, which prevents the Secret deletion until the finalizer is removed by the controller. As a result, the BMH is removed successfully before the Secret is allowed to be deleted. ([OCPBUGS-87963](https://issues.redhat.com/browse/OCPBUGS-87963)) 
  * Before this update, in vSphere installer-provisioned infrastructure clusters using static IPs, the control plane machine set (CPMS) Operator was not copying the name server into the CPMS when the CPMS was deleted. As a consequence, the CPMS Operator would identify current masters as not valid and would identify the masters as needing to be recreated. With this release, the CPMS Operator logic is updated to copy the name server definition into the CPMS when the clusters used static IPs. As a result, the name server information is configured in the CPMS when recreating the CPMS cluster instance. ([OCPBUGS-87968](https://issues.redhat.com/browse/OCPBUGS-87968)) 
  * Before this update, when generateRelease used the digest-only `ImageDigestMirrorSet` (IDMS) mode, images that were referenced as tag and digest, for example, nvcr.io/…​/container-toolkit:v1.19.1@sha256:…​, were treated as tag-only and excluded from IDMS generation. As a consequence, those images appeared only in the `ImageTagMirrorSet` (ITMS) mode. For disconnected installs that rely on IDMS for digest-based resolution, the mirroring install could fail for Operator-related images that were referenced as ITMS. With this release, updated `generateImageMirrors` objects are updated so that the tag and digest references are included in IDMS and ITMS. As a result, tag and digest images are written to both IDMS and ITMS. ([OCPBUGS-88484](https://issues.redhat.com/browse/OCPBUGS-88484)) 
  * Before this update, the **Column Management** modal did not display the help text that informed you that the namespace column is shown only when you select **All projects**. With this release, the help text displays correctly. ([OCPBUGS-90110](https://issues.redhat.com/browse/OCPBUGS-90110)) 
  * Before this update, the Ingress Node Firewall Operator used the `reflect.DeepEqual` parameter for node label comparison which required an exact label match instead of Kubernetes label selector semantics. As a consequence, the `IngressNodeFirewallNodeState` objects that were not created for nodes were added after the Ingress Node Firewall Operator startup. With this release, the `reflect.DeepEqual` parameter is replaced with the `labels.SelectorFromSet().Matches()` parameter for correct Kubernetes label selector matching. As a result, the Ingress Node Firewall Operator correctly creates the `IngressNodeFirewallNodeState` parameter for dynamically added nodes and label changes. ([OCPBUGS-90550](https://issues.redhat.com/browse/OCPBUGS-90550)) 
  * Before this update, the metrics-proxy scraper created a new HTTP client with a new `http.Transport` on an every 30-60-second scrape cycle without ever closing idle connections. The `http.Transport` for Go retained idle connections and their TLS buffers until `CloseIdleConnections` was explicitly called. As a consequence, idle connections and the TLS (Transport Layer Security) session state accumulated indefinitely across scrape cycles, which caused unbounded memory growth in metrics-proxy pods on request-serving nodes. Up to 2774Mi usage was observed against a 40Mi request, which triggered `RequestServingNodesNeedUpscale` alerts. With this release, the `DisableKeepAlives` parameter is set on the ephemeral transport to prevent connection pooling on single-use clients, and `CloseIdleConnections` is deferred as a safety net after each `ScrapeAll` call. As a result, the `metrics-proxy` memory usage remains stable over time within reasonable bounds. ([OCPBUGS-90563](https://issues.redhat.com/browse/OCPBUGS-90563)) 
  * Before this update, the GatewayClass controller set up watches on the Operator Lifecycle Management (OLM) `Subscription` and `InstallPlan` resources without checking whether the `OperatorLifecycleManager` capability was enabled on the cluster. As a consequence, on clusters that did not have the OLM capability, the GatewayClass controller blocked indefinitely during startup because the OLM CRDs did not exist. This blocking prevented the controller reconcile workers from starting, making Gateway API non-functional on those clusters. With this release, the Subscription and InstallPlan watches in the GatewayClass controller are guarded with an `OperatorLifecycleManagerEnabled` check so that the watches are only registered when OLM is present. The status controller `subscriptionCache` creation is also guarded with the same check. As a result, the GatewayClass controller starts successfully on clusters without OLM, and Gateway API functions correctly on non-OLM clusters. ([OCPBUGS-91967](https://issues.redhat.com/browse/OCPBUGS-91967)) 



### 1.11.15.2. Updating

To update an OpenShift Container Platform 4.22 cluster to this latest release, see [Updating a cluster using the CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/updating_clusters/#updating-cluster-cli). 

## 1.11.16. RHSA-2026:29795 - OpenShift Container Platform 4.22.3 bug fix and security update

Issued: 30 June 2026 

OpenShift Container Platform release 4.22.3 is now available. The list of fixed issues that are included in the update is documented in the [RHSA-2026:29795](https://access.redhat.com/errata/RHSA-2026:29795) advisory. There are no RPM packages for this release. 

Space precluded documenting all of the container images for this release in the advisory. 

You can view the container images in this release by running the following command: 

```shell-session
$ oc adm release info 4.22.3 --pullspecs
```


### 1.11.16.1. Fixed issues

  * Before this update, during parallel deployments of single-node OpenShift Container Platform, specifically with hypervisor-based single-node OpenShift Container Platform, some systems would hang in the middle of the deployment due to a race condition involving the BareMetalHost (BMH) custom resource. The single-node OpenShift Container Platform was never powered on by metal3 after virtual media was attached. As a consequence, parallel deployments at scale (10+ nodes) had approximately 80% success rate, with the remaining nodes requiring manual intervention to patch the `online` field to `true` for the impacted BMH custom resources. With this release, the race condition in the BMH power-on process has been resolved. As a result, parallel single-node OpenShift Container Platform deployments successfully power on all nodes without manual intervention, even at scale. ([OCPBUGS-73622](https://issues.redhat.com/browse/OCPBUGS-73622)) 
  * Before this update, the `kube-apiserver-check-endpoints` container generated a TLS certificate for the `check-endpoint` service on port `17697` with a validity of only 1 second. As a consequence, the certificate expired almost immediately after generation, which differed from previous OpenShift Container Platform versions where the certificate was valid for 1 month. With this release, the `kube-apiserver-check-endpoints` container generates certificates with an appropriate validity period. As a result, the `check-endpoint` service certificate remains valid for the expected duration, consistent with previous releases. ([OCPBUGS-84536](https://issues.redhat.com/browse/OCPBUGS-84536)) 
  * Before this update, the `oslat` latency test hard coded the runner pod memory to 1 GB regardless of the `LATENCY_TEST_CPUS` value. As a consequence, when running the CNF latency test with high CPU counts such as `LATENCY_TEST_CPUS=126`, the `oslat` pod was `OOMKilled` because the fixed 1 GB memory limit was insufficient, blocking hardware platform evaluation. With this release, the `oslat` test runner pod memory is configurable or appropriately scaled based on the `LATENCY_TEST_CPUS` setting. As a result, the documented CNF latency test flow completes successfully with higher CPU counts without `OOMKilled` failures. ([OCPBUGS-86071](https://issues.redhat.com/browse/OCPBUGS-86071)) 
  * Before this update, when the `etcd-endpoints` config map contained only the IP addresses of failed or unreachable etcd members, the etcd Operator entered a permanent deadlock. The `EtcdEndpointsController`, which updates the config map, required a working etcd connection to list members, but the etcd client pool read endpoints exclusively from the stale config map. This circular dependency prevented all Operator controllers from functioning. As a consequence, the Operator retried indefinitely against dead endpoints, logging `context deadline exceeded` errors continuously, and required manual intervention to patch the config map with healthy member IPs. With this release, the Operator detects when all config map-derived endpoints are unreachable and falls back to node-based endpoint discovery to re-establish connectivity with healthy etcd members. As a result, the `EtcdEndpointsController` automatically updates the config map with correct IP addresses and recovery proceeds without manual intervention. ([OCPBUGS-88490](https://issues.redhat.com/browse/OCPBUGS-88490)) 
  * Before this update, the Vertical Pod Autoscaler (VPA) Operator failed to create events in the cluster because it did not set the required `action` field when creating event objects. As a consequence, the VPA Operator logs contained errors such as `Server rejected event (will not retry!)` with the message `Event is invalid: action: Required value`. With this release, the VPA Operator correctly populates the `action` field when creating events. As a result, the VPA Operator successfully creates events without errors in the logs. ([OCPBUGS-90165](https://issues.redhat.com/browse/OCPBUGS-90165)) 



### 1.11.16.2. Updating

To update an OpenShift Container Platform 4.22 cluster to this latest release, see [Updating a cluster using the CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/updating_clusters/#updating-cluster-cli). 

## 1.11.17. RHSA-2026:27009 - OpenShift Container Platform 4.22.2 bug fix and security update

Issued: 23 June 2026 

OpenShift Container Platform release 4.22.2 is now available. The list of fixed issues that are included in the update is documented in the [RHSA-2026:27009](https://access.redhat.com/errata/RHSA-2026:27009) advisory. The RPM packages that are included in the update are provided by the [RHBA-2026:27007](https://access.redhat.com/errata/RHBA-2026:27007) advisory. 

Space precluded documenting all of the container images for this release in the advisory. 

You can view the container images in this release by running the following command: 

```shell-session
$ oc adm release info 4.22.2 --pullspecs
```


### 1.11.17.1. New features

The Helm CLI v4 for Red Hat OpenShift is now available as a standalone download
    

The Helm CLI v4.1.4 for Red Hat OpenShift is the first supported downstream build of Helm v4, available as a standalone binary from the OpenShift Container Platform mirror repository. This release provides access to Helm v4 capabilities, enabling you to evaluate and use Helm v4 workflows on OpenShift Container Platform. 

Note that all integrated OpenShift Container Platform console flows and software catalogs still run on Helm v3 only. If you use new Helm chart features or Helm v4-exclusive features through the command line interface (CLI), they will not map to or render in the current OpenShift Container Platform web console. 

Red Hat does not distribute Helm CLI v4 as a traditional RPM. 

For more information, see [Helm CLI for Red Hat OpenShift Container Platform](https://access.redhat.com/solutions/7144038)(Red Hat Knowledgebase). 

### 1.11.17.2. Enhancements

This release contains the following enhancement: 

  * With this release, the `chrony-wait` service no longer blocks the node bootstrap process. As a result, the time to `NodeReady` is reduced to 10-24 seconds, depending on the platform. ([OCPBUGS-88114](https://issues.redhat.com/browse/OCPBUGS-88114)) 



### 1.11.17.3. Fixed issues

  * Before this update, when you created a namespace-scoped `ProjectHelmChartRepository` object in the OpenShift Container Platform web console, the Certificate Authority (CA) certificate and Transport Layer Security (TLS) client config drop-down menus listed only the resources from the `openshift-config` namespace. With this release, the form lists CA and TLS resources from the selected project namespace for `ProjectHelmChartRepository` objects, while cluster-scoped `HelmChartRepository` objects continue to use the `openshift-config` namespace. ([OCPBUGS-76328](https://issues.redhat.com/browse/OCPBUGS-76328)) 
  * Before this update, when a boundary clock (T-BC) entered holdover, the `event.sync.sync-status.synchronization-state-change` (`/sync/sync-status/sync-state`) event would sometimes incorrectly report `FREERUN` instead of `HOLDOVER`. These reports might have occurred because of an issue with the calculation of the overall node sync state. With this release, the `ptp4l` state is ignored. As a result, the `event.sync.sync-status.synchronization-state-change` (`/sync/sync-status/sync-state`) event correctly reports `HOLDOVER`. ([OCPBUGS-86530](https://issues.redhat.com/browse/OCPBUGS-86530)) 
  * Before this update, arbiter configs previously used runc as the default container runtime. With this release, the arbiter configs have been updated to be in sync with the master nodes and use crun as the default container runtime. ([OCPBUGS-87019](https://issues.redhat.com/browse/OCPBUGS-87019)) 
  * Before this update, the `openshift-apiserver` might have failed when multiple requests accessed project authorization data at the same time. This issue occurred more often on clusters with many namespaces and role-based access control (RBAC) rules. As a consequence, `openshift-apiserver` pods restarted unexpectedly with exit code `2`, which temporarily disrupted the API availability for project and namespace operations. With this release, the project authorization cache safely handles concurrent access. As a result, the `openshift-apiserver` namespace does not fail during concurrent project authorization lookups, and project listing operations remain responsive regardless of cluster size. ([OCPBUGS-87022](https://issues.redhat.com/browse/OCPBUGS-87022)) 
  * Before this update, when you navigated to the Cluster Dashboard Overview page and clicked the Insights window on the Status card, an underlying UI component rendered the text incorrectly. As a consequence, the icons for the four severity levels (Critical, Important, Moderate, and Low) appeared, but the actual issue counts and the links to the Insights advisor were missing. With this release, the link component inside the Insights severity message is updated to ensure that the text and links render properly. As a result, each severity level in the Insights window now successfully displays its icon, the correct issue count, and a clickable link to the Insights advisor. ([OCPBUGS-87096](https://issues.redhat.com/browse/OCPBUGS-87096)) 
  * Before this update, after a `cloud-event-proxy` (CEP) sidecar restart, the linuxptp-daemon could send replayed and live `ptp4l` output on the same event socket at the same time. A stale replayed port-role event with `FAULTY` could force the clock state to `HOLDOVER`. Because port roles update only on discrete state-change events, later live offset updates could not restore `LOCKED`. A replayed `RECEIVER` to `FAULTY` transition could also overwrite the live `RECEIVER` role on the socket and persist until a real port state change occurred. This issue affects T-BC and dual-follower configurations and, with lower probability, OpenShift CLI (`oc`) configurations. As a consequence, the clock state metric and the `SyncStateChange` cloud event could remain stuck at `FREERUN` or `HOLDOVER`, and the port role could remain stuck at `FAULTY`, even when `ptp4l` was fully locked. With this release, a live gate blocks process connections from writing to the event socket until replay completes, so all historical state is processed before any live data arrives. As a result, stale replay data cannot race with live output, and the clock state and port role metrics correctly reflect the current synchronization status after a CEP restart. ([OCPBUGS-87839](https://issues.redhat.com/browse/OCPBUGS-87839)) 
  * Before this update, OpenShift Container Platform disabled timer migration to ensure that the high resolution kernel timers and cyclictest (a timer-based bench-marking tool) was not affected by extra latency. However, timer migration was required to allow the kernel to migrate previously started timers such as the TCP timeout and keep-alive away from CPUs assigned to a newly CPU-pinned guaranteed workload container. As a consequence, when the timer migration was disabled, the remaining timers kept interrupting the latency sensitive workloads. With this release, the timer migration is reinstated to enable configuration because the `PerformanceProfile` parameter is mostly used with latency sensitive workloads. As a result, newly created pods are not interrupted by timers that are stuck on the CPUs assigned to those workloads. If you do not want the latency-sensitive polling application running on the cluster, you can set the `kernel.timer_migration=0` sysctl by using the advanced configuration instructions that are provided in the Knowledge Base at [5532341](https://access.redhat.com/solutions/5532341). ([OCPBUGS-87891](https://issues.redhat.com/browse/OCPBUGS-87891)) 
  * Before this update, when you bootstrapped a new node, the extensions image was pulled regardless of whether it was required by the cluster configuration. As a consequence, node bootstrap times increased. With this release, the extensions image is only pulled when the configuration requires it. ([OCPBUGS-88120](https://issues.redhat.com/browse/OCPBUGS-88120)) 
  * Before this update, you were prompted to complete the "Restore as new PVC" action for VolumeSnapshots to work when the parent PVC was deleted aligning the console behavior with the CLI, which already supported this operation. With this release, the restore `VolumeSnapshot` modal now falls back to snapshot annotations for storage class, access modes, and size instead of requiring the original PVC to be present. ([OCPBUGS-88304](https://issues.redhat.com/browse/OCPBUGS-88304)) 



### 1.11.17.4. Updating

To update an OpenShift Container Platform 4.22 cluster to this latest release, see [Updating a cluster using the CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/updating_clusters/#updating-cluster-cli). 

## 1.11.18. RHSA-2026:25206 - OpenShift Container Platform 4.22.1 fixed issues and security update

Issued: 16 June 2026 

OpenShift Container Platform release 4.22.1 is now available. The list of fixed issues that are included in the update is documented in the [RHSA-2026:25206](https://access.redhat.com/errata/RHSA-2026:25206) advisory. The RPM packages that are included in the update are provided by the [RHBA-2026:25204](https://access.redhat.com/errata/RHBA-2026:25204) advisory. 

Space precluded documenting all of the container images for this release in the advisory. 

You can view the container images in this release by running the following command: 

```shell-session
$ oc adm release info 4.22.1 --pullspecs
```


### 1.11.18.1. Fixed issues

  * Before this update, when servicing a bare-metal host, the `service_disable_ramdisk` parameter remained set to `False` even if all servicing steps were performed out-of-band. As a result, the bare-metal host underwent an unnecessary reboot. With this release, the Ironic code has been modified to automatically set `service_disable_ramdisk` to `True` when all servicing steps are out-of-band.([OCPBUGS-84369](https://issues.redhat.com/browse/OCPBUGS-84369)) 
  * Before this update, pagination controls were not present at mobile resolutions, because PatternFly expects both top and bottom pagination controls to be in use. With this release, pagination controls are present regardless of resolution. ([OCPBUGS-84963](https://issues.redhat.com/browse/OCPBUGS-84963)) 
  * Before this update, the `MachineSet` custom resource (CR) scale subresource lacked a valid selector, preventing autoscalers such as the Horizontal Pod Autoscaler (HPA) and the Kubernetes Event-driven Autoscaling (KEDA) from scaling the machine set. With this release, the `MachineSet` CR exposes an active label selector on the scale subresource, enabling scaling using autoscalers that require the label selector to be populated. ([OCPBUGS-85102](https://issues.redhat.com/browse/OCPBUGS-85102)) 
  * Before this update, the Manila Container Storage Interface (CSI) driver node plugin could crash on startup if the Network File System (NFS) CSI plugin socket was not yet available, for example, after a node reboot. With this release, the Manila CSI node `DaemonSet` waits for the NFS plugin socket to be ready before starting the driver, preventing crash loops due to transient startup ordering. ([OCPBUGS-85532](https://issues.redhat.com/browse/OCPBUGS-85532)) 
  * Before this update, there was a race condition between network namespace management and the optional container mount namespace segmentation. Pods would become stuck and unable to restart. With this release, the race condition is solved by initializing the network namespace infrastructure before the container mount namespace. ([OCPBUGS-85962](https://issues.redhat.com/browse/OCPBUGS-85962)) 
  * Before this update, if a `PerformanceProfile` status or its associated conditions failed to update because the API server was temporarily unavailable, the degraded condition might get stuck and never be resolved, even when the cluster was healthy. With this release, the Node Tuning Operator schedules a retry of the status update until it succeeds. ([OCPBUGS-86024](https://issues.redhat.com/browse/OCPBUGS-86024)) 
  * Before this update, the Control Plane Operator used Secret and ConfigMap custom resource names as Kubernetes volume names when building the `metrics-proxy` deployment. Because Kubernetes volume names must conform to RFC 1123 DNS label rules, which do not allow dots, the `metrics-proxy` deployment failed to create when a `ServiceMonitor` object referenced a ConfigMap with dots in its name, such as `openshift-service-ca.crt`. With this update, the Control Plane Operator sanitizes volume names by replacing dots with dashes while preserving the original resource names in the ConfigMap and Secret source references and mount paths. As a result, the `metrics-proxy` deployment is created successfully regardless of dots in referenced resource names. ([OCPBUGS-86026](https://issues.redhat.com/browse/OCPBUGS-86026)) 
  * Before this update, the `CertificateRevocationController` object verified certificate revocation through the Kubernetes API Server (KAS) service load balancer, which routes to a single pod. In high availability (HA) deployments with three KAS replicas, the check could hit a pod that had loaded the updated trust bundle while others did not, causing premature state transitions in the revocation flow. With this release, the controller has been updated to verify certificate trust and revocation against every individual KAS pod by IP, rather than through the service. Certificate revocation now completes reliably in HA deployments by confirming all KAS pods have propagated the change. ([OCPBUGS-86039](https://issues.redhat.com/browse/OCPBUGS-86039)) 
  * Before this update, the web console repeatedly downloaded the full OpenAPI v2 schema at startup, after API discovery and every 5 minutes without using HTTP conditional request headers. With this release, the console caches the `ETag` from the OpenAPI responses and sends an `If-None-Match` request header on subsequent requests. When the schema has not changed, the server returns a `304 Not Modified` response, avoiding redundant network transfers and JSON parsing. ([OCPBUGS-86222](https://issues.redhat.com/browse/OCPBUGS-86222)) 
  * Before this update, users without any projects saw a `Restricted access` error when navigating to certain resource list pages such as **Pods** , **PodDisruptionBudgets** , **RoleBindings, VolumeSnapshots** , and **Helm**. With this release, these pages now correctly display an empty state instead of the misleading "403" error. ([OCPBUGS-86227](https://issues.redhat.com/browse/OCPBUGS-86227)) 
  * Before this update, Prometheus dashboard queries used a hard-coded 15-second polling interval regardless of how long queries took to complete. On slow or large clusters, rapid re-polling added an unnecessary load on Prometheus because new requests fired before previous ones finished. With this release, the fixed 15-second interval has been replaced with an adaptive delay based on an exponential moving average of response times. The polling interval dynamically adjusts up to 60 seconds for slow queries while maintaining the 15-second baseline for fast ones. As a result, dashboard polling adapts to cluster performance, reducing unnecessary Prometheus loads on slow clusters without affecting fast ones. ([OCPBUGS-86239](https://issues.redhat.com/browse/OCPBUGS-86239)) 
  * Before this update, when a user applied a `MachineConfig` object to install extensions, the Machine Config Operator (MCO) did not validate that all packages were installed. This would lead to situations where users believed their extension installation was successful, but packages were actually missing. If one or more packages was not present, the node and associated `MachineConfigPool`, degraded. With this release, the post node reboot validates that all packages associated with the user-required extension were successfully installed before reporting a successful update. ([OCPBUGS-86262](https://issues.redhat.com/browse/OCPBUGS-86262)) 
  * Before this update, when the `configure-ovs.sh` script created the `br-ex` bridge, the link layer discovery protocol (LLDP) settings from the underlying interface were not preserved. As a result, there was no supported way to enable LLDP on the bridge. With this release, LLDP settings are now persisted so that LLDP can be enabled in a supported fashion. ([OCPBUGS-86297](https://issues.redhat.com/browse/OCPBUGS-86297)) 
  * Before this update, the macOS **Option** key was treated as a Meta key instead of a compose key in the pod terminal. As a consequence, characters that rely on **Option** key combinations, such as `@`, `{`, `}`, `|`, `\`, and `~`, could not be entered. With this release, the terminal correctly identifies macOS, so the **Option** key functions as a compose key. ([OCPBUGS-86580](https://issues.redhat.com/browse/OCPBUGS-86580)) 
  * Before this update, Vital Product Data (VPD) would incorrectly identify that a custom resource (CR) pool would require additional privileges instead of just being `read-only`. With this release, the evaluation logic within the VPD mechanism has been corrected to properly recognize and validate `read-only` access requirements for CR pools. ([OCPBUGS-86866](https://issues.redhat.com/browse/OCPBUGS-86866)) 
  * Before this update, the collection and emission of SELinux conflict metrics was inefficient and consumed excessive system resources. As a consequence, cluster performance degraded during metric collection cycles, leading to delayed reporting and high processor usage. With this release, the collection and emission logic has been optimized to streamline data processing. As a result, metric collection is now significantly faster, improving overall cluster performance and responsiveness. ([OCPBUGS-86898](https://issues.redhat.com/browse/OCPBUGS-86898)) 
  * Before this update, cluster restore operations did not validate snapshot integrity or verify hashes before executing destructive actions. As a consequence, corrupt or hashless snapshots could be applied to the cluster, resulting in data overwrites that could leave the system in an unrecoverable state. With this release, a validation step has been added to check snapshot integrity before any destructive operations are performed. As a result, corrupt snapshots are safely rejected early in the process, preventing cluster failure and ensuring data integrity.([OCPBUGS-86960](https://issues.redhat.com/browse/OCPBUGS-86960)) 
  * Before this update, when running `oc-mirror` in `mirror-to-disk` mode, Operator catalog tags were resolved during collection and mirroring. If a catalog was updated on the registry between these phases, the tag would point to a different digest. This caused a mismatch that prevented `oc-mirror` from locating the catalog in the local working directory during `disk-to-mirror` operations in air-gapped environments. This in turn, resulted in authentication failures when `oc-mirror` tried to fetch from the external registry. With this release, the Operator catalog images are pinned to their resolved digests during workflow initialization before collection starts. As a result, the same digest is used consistently across all phases, allowing `disk-to-mirror` workflows to complete successfully in air-gapped environments without attempting to access external registries. ([OCPBUGS-87806](https://issues.redhat.com/browse/OCPBUGS-87806)) 



### 1.11.18.2. Updating

To update an OpenShift Container Platform 4.22 cluster to this latest release, see [Updating a cluster using the CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/updating_clusters/#updating-cluster-cli).
