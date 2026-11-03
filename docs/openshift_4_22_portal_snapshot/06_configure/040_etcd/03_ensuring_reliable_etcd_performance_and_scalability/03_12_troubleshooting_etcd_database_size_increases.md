# 3.12. Troubleshooting etcd database size increases

Resolve common errors when increasing the etcd disk quota, including values that are too small, too large, or lower than the current setting. 

If you encounter issues when you try to increase the database size for etcd, the following examples might help. 

## 3.12.1. Value is too small

If the value that you specify is less than `8`, you see an error message. For example, if you enter the following command: 

```shell-session
$ oc patch etcd/cluster --type=merge -p '{"spec": {"backendQuotaGiB": 5}}'
```


The following error message is displayed: 

**Example error message**

```shell-session
The Etcd "cluster" is invalid:
* spec.backendQuotaGiB: Invalid value: 5: spec.backendQuotaGiB in body should be greater than or equal to 8
* spec.backendQuotaGiB: Invalid value: "integer": etcd backendQuotaGiB may not be decreased
```


To resolve this issue, specify an integer between `8` and `32`. 

## 3.12.2. Value is too large

If the value that you specify is greater than `32`, you see an error message. For example, if you enter the following command: 

```shell-session
$ oc patch etcd/cluster --type=merge -p '{"spec": {"backendQuotaGiB": 64}}'
```


The following error message is displayed: 

**Example error message**

```shell-session
The Etcd "cluster" is invalid: spec.backendQuotaGiB: Invalid value: 64: spec.backendQuotaGiB in body should be less than or equal to 32
```


To resolve this issue, specify an integer between `8` and `32`. 

## 3.12.3. Value is decreasing

If the value is set to a valid value between `8` and `32`, you cannot decrease the value. Otherwise, you see an error message. 

For example, check the current value by entering the following command: 

```shell-session
$ oc describe etcd/cluster | grep "Backend Quota"
```


**Example output**

```shell-session
Backend Quota Gi B: 10
```


If you decrease the disk quota value by entering the following command, an error message is displayed. 

```shell-session
$ oc patch etcd/cluster --type=merge -p '{"spec": {"backendQuotaGiB": 8}}'
```


**Example error message**

```shell-session
The Etcd "cluster" is invalid: spec.backendQuotaGiB: Invalid value: "integer": etcd backendQuotaGiB may not be decreased
```


To resolve this issue, specify an integer greater than `10`.
