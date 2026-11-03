# 3.3. Testing the AMD GPU Operator

Use the following procedure to test the ROCmInfo installation and view the logs for the AMD MI210 GPU. 

**Procedure**

  1. Create a YAML file that tests ROCmInfo: 

```shell-session
$ cat << EOF > rocminfo.yaml

apiVersion: v1
kind: Pod
metadata:
 name: rocminfo
spec:
 containers:
 - image: docker.io/rocm/pytorch:latest
   name: rocminfo
   command: ["/bin/sh","-c"]
   args: ["rocminfo"]
   resources:
    limits:
      amd.com/gpu: 1
    requests:
      amd.com/gpu: 1
 restartPolicy: Never
EOF
```


  2. Create the `rocminfo` pod: 

```shell-session
$ oc create -f rocminfo.yaml
```


**Example output**

```shell-session
apiVersion: v1
pod/rocminfo created
```


  3. Check the `rocmnfo` log with one MI210 GPU: 

```shell-session
$ oc logs rocminfo | grep -A5 "Agent"
```


**Example output**

```shell-session
HSA Agents
==========
*******
Agent 1
*******
  Name:                    Intel(R) Xeon(R) Gold 6330 CPU @ 2.00GHz
  Uuid:                    CPU-XX
  Marketing Name:          Intel(R) Xeon(R) Gold 6330 CPU @ 2.00GHz
  Vendor Name:             CPU
--
Agent 2
*******
  Name:                    Intel(R) Xeon(R) Gold 6330 CPU @ 2.00GHz
  Uuid:                    CPU-XX
  Marketing Name:          Intel(R) Xeon(R) Gold 6330 CPU @ 2.00GHz
  Vendor Name:             CPU
--
Agent 3
*******
  Name:                    gfx90a
  Uuid:                    GPU-024b776f768a638b
  Marketing Name:          AMD Instinct MI210
  Vendor Name:             AMD
```


  4. Delete the pod: 

```shell-session
$ oc delete -f rocminfo.yaml
```


**Example output**

```shell-session
pod "rocminfo" deleted
```
