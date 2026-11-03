# 4.22. Debugging and troubleshooting

Unsigned or incorrectly signed kmods in KMM driver containers on OpenShift Container Platform can cause `PostStartHookError` or `CrashLoopBackOff` states. You can verify signing issues by running `oc describe` on the container and checking for a `Required key not available` error. 

The following message appears in this scenario: 

```shell-session
modprobe: ERROR: could not insert '<your_kmod_name>': Required key not available
```
