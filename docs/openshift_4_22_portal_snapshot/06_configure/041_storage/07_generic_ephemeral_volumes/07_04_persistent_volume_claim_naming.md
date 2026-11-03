# 7.4. Persistent volume claim naming

Automatically created persistent volume claims (PVCs) are named using pod name and volume name with a hyphen separator, potentially causing conflicts with other pods or manual PVCs. 

For example, `pod-a` with volume `scratch` and `pod` with volume `a-scratch` both end up with the same PVC name, `pod-a-scratch`. 

Such conflicts are detected, and a PVC is only used for an ephemeral volume if it was created for the pod. This check is based on the ownership relationship. An existing PVC is not overwritten or modified, but this does not resolve the conflict. Without the right PVC, a pod cannot start. 

Important

Be careful when naming pods and volumes inside the same namespace so that naming conflicts do not occur.
