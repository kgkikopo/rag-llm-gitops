# 7.5. Creating generic ephemeral volumes

To create ephemeral volumes that are automatically provisioned and deleted with pod lifecycle, define a `volumeClaimTemplate` in your pod spec specifying storage class, size, and access modes. 

**Procedure**

  1. Create the `pod` object definition and save it to a file. 
  2. Include the generic ephemeral volume information in the file. 

**my-example-pod-with-generic-vols.yaml**

```yaml
kind: Pod
apiVersion: v1
metadata:
  name: my-app
spec:
  containers:
    - name: my-frontend
      image: busybox:1.28
      volumeMounts:
      - mountPath: "/mnt/storage"
        name: data
      command: [ "sleep", "1000000" ]
  volumes:
    - name: data
      ephemeral:
        volumeClaimTemplate:
          metadata:
            labels:
              type: my-app-ephvol
          spec:
            accessModes: [ "ReadWriteOnce" ]
            storageClassName: "gp2-csi"
            resources:
              requests:
                storage: 1Gi
```


Where `spec.volumes.name` is the name of the generic ephemeral volume.
