# 1.2. Requirements for installing OpenShift Container Platform on Google Cloud

Before installing OpenShift Container Platform on Google Cloud, you must create a service account and configure a Google Cloud project by creating a project, enabling API services, configuring DNS, setting Google Cloud account limits, and selecting supported Google Cloud regions. For more information, see "Configuring a Google Cloud project". 

If the cloud Identity and Access Management (IAM) APIs are not accessible in your environment, or if you do not want to store an administrator-level credential secret in the `kube-system` namespace, you can configure your cluster to use short-term credentials, manually create long-term credentials, or both. For more information, see "Configuring a Google Cloud cluster to use short-term credentials" and "Manually creating long-term credentials". 

**Additional resources**

  * [Configuring a Google Cloud project](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_google_cloud/installing-gcp-account "Chapter 2. Configuring a Google Cloud project")
  * [Configuring a Google Cloud cluster to use short-term credentials](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_google_cloud/installing-gcp-customizations#installing-gcp-with-short-term-creds_installing-gcp-customizations "4.10.2. Short-term credential configuration for a Google Cloud cluster")
  * [Manually creating long-term credentials for Google Cloud](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_google_cloud/installing-gcp-customizations#manually-create-iam_installing-gcp-customizations "4.10.1. Manually creating long-term credentials")
