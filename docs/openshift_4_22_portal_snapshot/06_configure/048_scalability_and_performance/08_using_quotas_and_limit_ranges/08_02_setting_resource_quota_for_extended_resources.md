# 8.2. Setting resource quota for extended resources

To manage the consumption of extended resources, such as `nvidia.com/gpu`, define a resource quota by using the `requests` prefix. Since overcommitment is prohibited for these resources, you must explicitly specify both requests and limits to ensure valid configuration. 

**Procedure**

  1. To determine how many GPUs are available on a node in your cluster, use the following command: 

```shell-session
$ oc describe node ip-172-31-27-209.us-west-2.compute.internal | egrep 'Capacity|Allocatable|gpu'
```


**Example output**

```shell-session
openshift.com/gpu-accelerator=true
Capacity:
 nvidia.com/gpu:  2
Allocatable:
 nvidia.com/gpu:  2
 nvidia.com/gpu:  0           0
```


In this example, 2 GPUs are available. 

  2. Use this command to set a quota in the namespace `nvidia`. In this example, the quota is `1`: 

```shell-session
$ cat gpu-quota.yaml
```


**Example output**

```shell-session
apiVersion: v1
kind: ResourceQuota
metadata:
  name: gpu-quota
  namespace: nvidia
spec:
  hard:
    requests.nvidia.com/gpu: 1
```


  3. Create the quota with the following command: 

```shell-session
$ oc create -f gpu-quota.yaml
```


**Example output**

```shell-session
resourcequota/gpu-quota created
```


  4. Verify that the namespace has the correct quota set using the following command: 

```shell-session
$ oc describe quota gpu-quota -n nvidia
```


**Example output**

```shell-session
Name:                    gpu-quota
Namespace:               nvidia
Resource                 Used  Hard
--------                 ----  ----
requests.nvidia.com/gpu  0     1
```


  5. Run a pod that asks for a single GPU with the following command: 

```shell-session
$ oc create pod gpu-pod.yaml
```


**Example output**

```shell-session
apiVersion: v1
kind: Pod
metadata:
  generateName: gpu-pod-s46h7
  namespace: nvidia
spec:
  restartPolicy: OnFailure
  containers:
  - name: rhel7-gpu-pod
    image: rhel7
    env:
      - name: NVIDIA_VISIBLE_DEVICES
        value: all
      - name: NVIDIA_DRIVER_CAPABILITIES
        value: "compute,utility"
      - name: NVIDIA_REQUIRE_CUDA
        value: "cuda>=5.0"

    command: ["sleep"]
    args: ["infinity"]

    resources:
      limits:
        nvidia.com/gpu: 1
```


  6. Verify that the pod is running with the following command: 

```shell-session
$ oc get pods
```


**Example output**

```shell-session
NAME              READY     STATUS      RESTARTS   AGE
gpu-pod-s46h7     1/1       Running     0          1m
```


  7. Verify that the quota `Used` counter is correct by running the following command: 

```shell-session
$ oc describe quota gpu-quota -n nvidia
```


**Example output**

```shell-session
Name:                    gpu-quota
Namespace:               nvidia
Resource                 Used  Hard
--------                 ----  ----
requests.nvidia.com/gpu  1     1
```


  8. Using the following command, attempt to create a second GPU pod in the `nvidia` namespace. This is technically available on the node because it has 2 GPUs: 

```shell-session
$ oc create -f gpu-pod.yaml
```


**Example output**

```shell-session
Error from server (Forbidden): error when creating "gpu-pod.yaml": pods "gpu-pod-f7z2w" is forbidden: exceeded quota: gpu-quota, requested: requests.nvidia.com/gpu=1, used: requests.nvidia.com/gpu=1, limited: requests.nvidia.com/gpu=1
```


You receive this `Forbidden` error message because you have a quota of 1 GPU and the pod tried to allocate a second GPU, which exceeds the allowed quota.
