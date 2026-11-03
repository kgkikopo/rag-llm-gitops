# 11.2. Example Containerfiles

Image mode for OpenShift allows you to use the following types of images to create custom layered images: 

  * **OpenShift Container Platform Hotfixes**. You can work with Customer Experience and Engagement (CEE) to obtain and apply Hotfix packages on top of your RHCOS image. In some instances, you might want a bug fix or enhancement before it is included in an official OpenShift Container Platform release. Image mode for OpenShift allows you to easily add the Hotfix before it is officially released and remove the Hotfix when the underlying RHCOS image incorporates the fix. 

Important

Some Hotfixes require a Red Hat Support Exception and are outside of the normal scope of OpenShift Container Platform support coverage or life cycle policies. 

Hotfixes are provided to you based on Red Hat Hotfix policy. Apply it on top of the base image and test that new custom layered image in a non-production environment. When you are satisfied that the custom layered image is safe to use in production, you can roll it out on your own schedule to specific node pools. For any reason, you can easily roll back the custom layered image and return to using the default RHCOS. 

**Example on-cluster Containerfile to apply a Hotfix**

```yaml
containerfileArch: noarch
content: |-
  FROM configs AS final
  #Install hotfix package
  RUN dnf update -y https://example.com/files/systemd-252-46.el9_4.x86_64.rpm \
                    https://example.com/files/systemd-journal-remote-252-46.el9_4.x86_64.rpm \
                    https://example.com/files/systemd-libs-252-46.el9_4.x86_64.rpm  \
                    https://example.com/files/systemd-pam-252-46.el9_4.x86_64.rpm \
                    https://example.com/files/systemd-udev-252-46.el9_4.x86_64.rpm \
                    https://example.com/files/systemd-rpm-macros-252-46.el9_4.noarch.rpm && \
      dnf clean all && \
      bootc container lint
```


**Example out-of-cluster Containerfile to apply a Hotfix**

```yaml
FROM quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256...
#Install hotfix package
RUN dnf update -y https://example.com/files/systemd-252-46.el9_4.x86_64.rpm \
                  https://example.com/files/systemd-journal-remote-252-46.el9_4.x86_64.rpm \
                  https://example.com/files/systemd-libs-252-46.el9_4.x86_64.rpm  \
                  https://example.com/files/systemd-pam-252-46.el9_4.x86_64.rpm \
                  https://example.com/files/systemd-udev-252-46.el9_4.x86_64.rpm \
                  https://example.com/files/systemd-rpm-macros-252-46.el9_4.noarch.rpm && \
    dnf clean all && \
    bootc container lint
```


  * **RHEL packages**. You can download Red Hat Enterprise Linux (RHEL) packages from the Red Hat Customer Portal, such as chrony, firewalld, and iputils. 

**Example out-of-cluster Containerfile to apply the rsyslog utility**

```yaml
# Using a 4.18.0 image
FROM quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256...
# Install rsyslog package
RUN dnf install -y rsyslog && \
    bootc container lint
# Copy your custom configuration in
ADD remote.conf /etc/rsyslog.d/remote.conf
```


  * **Third-party packages**. You can download and install RPMs from third-party organizations, such as the following types of packages: 

    * Bleeding edge drivers and kernel enhancements to improve performance or add capabilities. 
    * Forensic client tools to investigate possible and actual break-ins. 
    * Security agents. 
    * Inventory agents that provide a coherent view of the entire cluster. 
    * SSH Key management packages. 

**Example on-cluster Containerfile to apply a third-party package from EPEL**

```yaml
FROM configs AS final

#Enable EPEL (more info at https://docs.fedoraproject.org/en-US/epel/ ) and install htop
RUN dnf install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm && \
    dnf install -y htop && \
    dnf clean all && \
    bootc container lint
```


**Example out-of-cluster Containerfile to apply a third-party package from EPEL**

```yaml
# Get RHCOS base image of target cluster `oc adm release info --image-for rhel-coreos`
FROM quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256...

#Enable EPEL (more info at https://docs.fedoraproject.org/en-US/epel/ ) and install htop
RUN dnf install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm && \
    dnf install -y htop && \
    dnf clean all && \
    bootc container lint
```


This Containerfile installs the RHEL fish program. Because fish requires additional RHEL packages, the image must be built on an entitled RHEL host. For RHEL entitlements to work, you must copy the `etc-pki-entitlement` secret into the `openshift-machine-config-operator` namespace. 

**Example on-cluster Containerfile to apply a third-party package that has RHEL dependencies**

```yaml
FROM configs AS final

# RHEL entitled host is needed here to access RHEL packages
# Install fish as third party package from EPEL
RUN dnf install -y https://dl.fedoraproject.org/pub/epel/9/Everything/x86_64/Packages/f/fish-3.3.1-3.el9.x86_64.rpm && \
    dnf clean all && \
    bootc container lint
```


**Example out-of-cluster Containerfile to apply a third-party package that has RHEL dependencies**

```yaml
# Get RHCOS base image of target cluster `oc adm release info --image-for rhel-coreos`
FROM quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256...

# RHEL entitled host is needed here to access RHEL packages
# Install fish as third party package from EPEL
RUN dnf install -y https://dl.fedoraproject.org/pub/epel/9/Everything/x86_64/Packages/f/fish-3.3.1-3.el9.x86_64.rpm && \
    dnf clean all && \
    bootc container lint
```


After you create the machine config, the Machine Config Operator (MCO) performs the following steps: 

  1. Renders a new machine config for the specified pool or pools. 
  2. Performs cordon and drain operations on the nodes in the pool or pools. 
  3. Writes the rest of the machine config parameters onto the nodes. 
  4. Applies the custom layered image to the node. 
  5. Reboots the node using the new image. 



Important

It is strongly recommended that you test your images outside of your production environment before rolling out to your cluster.
