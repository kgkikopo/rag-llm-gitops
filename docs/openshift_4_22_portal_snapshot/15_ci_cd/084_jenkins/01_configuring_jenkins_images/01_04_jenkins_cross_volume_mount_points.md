# 1.4. Jenkins cross volume mount points

The Jenkins image can be run with mounted volumes to enable persistent storage for the configuration: 

  * `/var/lib/jenkins` is the data directory where Jenkins stores configuration files, including job definitions.
