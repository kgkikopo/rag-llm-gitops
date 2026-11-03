# 7.3. Security

Generic ephemeral volumes allow users who can create pods to indirectly create persistent volume claims (PVCs), even without direct PVC creation permissions. You can restrict this behavior if it conflicts with your security model. 

To restrict this behavior, use an admission webhook that rejects objects such as pods that have a generic ephemeral volume. 

The normal namespace quota for PVCs still applies, so even if users are allowed to use this new mechanism, they cannot use it to circumvent other policies.
