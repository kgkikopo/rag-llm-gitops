# 9.2. Disable Transparent Huge Pages

To prevent the operating system from automatically managing memory segments, disable Transparent Huge Pages (THP). 

Transparent Huge Pages (THP) tries to automate most aspects of creating, managing, and using huge pages. Since THP automatically manages the huge pages, THP does not always handle optimally for all types of workloads. THP can lead to performance regressions, since many applications handle huge pages on their own.
