# 1.1. Scanning RHOSP endpoints for legacy HTTPS certificates

Beginning with OpenShift Container Platform 4.10, HTTPS certificates must contain subject alternative name (SAN) fields. You can run a script to scan each HTTPS endpoint in a Red Hat OpenStack Platform (RHOSP) catalog for legacy certificates that only contain the `CommonName` field. 

Important

OpenShift Container Platform does not check the underlying RHOSP infrastructure for legacy certificates before installation or updates. Use the provided script to check for these certificates yourself. Failing to update legacy certificates before installing or updating a cluster might result in issues for your cluster. 

**Prerequisites**

  * On the machine where you run the script, have the following software: 

    * Bash version 4.0 or greater 
    * `grep`
    * [OpenStack client](https://access.redhat.com/documentation/en-us/red_hat_openstack_platform/16.2/html/command_line_interface_reference/the_openstack_client)
    * [`jq`](https://stedolan.github.io/jq/)
    * [OpenSSL version 1.1.1l or greater](https://www.openssl.org/)

  * Populate the machine with RHOSP credentials for the target cloud. 



**Procedure**

  1. Save the following script to your machine: 

```bash
#!/usr/bin/env bash

set -Eeuo pipefail

declare catalog san
catalog="$(mktemp)"
san="$(mktemp)"
readonly catalog san

declare invalid=0

openstack catalog list --format json --column Name --column Endpoints \
	| jq -r '.[] | .Name as $name | .Endpoints[] | select(.interface=="public") | [$name, .interface, .url] | join(" ")' \
	| sort \
	> "$catalog"

while read -r name interface url; do
	# Ignore HTTP
	if [[ ${url#"http://"} != "$url" ]]; then
		continue
	fi

	# Remove the schema from the URL
	noschema=${url#"https://"}

	# If the schema was not HTTPS, error
	if [[ "$noschema" == "$url" ]]; then
		echo "ERROR (unknown schema): $name $interface $url"
		exit 2
	fi

	# Remove the path and only keep host and port
	noschema="${noschema%%/*}"
	host="${noschema%%:*}"
	port="${noschema##*:}"

	# Add the port if was implicit
	if [[ "$port" == "$host" ]]; then
		port='443'
	fi

	# Get the SAN fields
	openssl s_client -showcerts -servername "$host" -connect "$host:$port" </dev/null 2>/dev/null \
		| openssl x509 -noout -ext subjectAltName \
		> "$san"

	# openssl returns the empty string if no SAN is found.
	# If a SAN is found, openssl is expected to return something like:
	#
	#    X509v3 Subject Alternative Name:
	#        DNS:standalone, DNS:osp1, IP Address:192.168.2.1, IP Address:10.254.1.2
	if [[ "$(grep -c "Subject Alternative Name" "$san" || true)" -gt 0 ]]; then
		echo "PASS: $name $interface $url"
	else
		invalid=$((invalid+1))
		echo "INVALID: $name $interface $url"
	fi
done < "$catalog"

# clean up temporary files
rm "$catalog" "$san"

if [[ $invalid -gt 0 ]]; then
	echo "${invalid} legacy certificates were detected. Update your certificates to include a SAN field."
	exit 1
else
	echo "All HTTPS certificates for this cloud are valid."
fi
```


  2. Run the script. 
  3. Replace any certificates that the script reports as `INVALID` with certificates that contain SAN fields. 

Important

You must replace all legacy HTTPS certificates before you install OpenShift Container Platform 4.10 or update a cluster to that version. Legacy certificates will be rejected with the following message: 

```plaintext
x509: certificate relies on legacy Common Name field, use SANs instead
```


## 1.1.1. Scanning RHOSP endpoints for legacy HTTPS certificates manually

Starting in OpenShift Container Platform 4.10, HTTPS certificates require subject alternative name (SAN) fields. If you do not have access to the prerequisite tools that are listed in "Scanning RHOSP endpoints for legacy HTTPS certificates", you can perform certain steps. 

These steps scan each HTTPS endpoint in a Red Hat OpenStack Platform (RHOSP) catalog for legacy certificates that only contain the `CommonName` field. 

Important

OpenShift Container Platform does not check the underlying RHOSP infrastructure for legacy certificates before installation or updates. Use the procedure steps to check for these certificates yourself. Failing to update legacy certificates before installing or updating a cluster might result in issues for your cluster. 

**Procedure**

  1. On a command line, run the following command to view the URL of RHOSP public endpoints: 

```shell-session
$ openstack catalog list
```


Record the URL for each HTTPS endpoint that the command returns. 

  2. For each public endpoint, note the host and the port. 

Tip

Determine the host of an endpoint by removing the scheme, the port, and the path. 

  3. For each endpoint, run the following commands to extract the SAN field of the certificate: 

     1. Set a `host` variable: 

```shell-session
$ host=<host_name>
```


     2. Set a `port` variable: 

```shell-session
$ port=<port_number>
```


If the URL of the endpoint does not have a port, use the value `443`. 

     3. Retrieve the SAN field of the certificate: 

```shell-session
$ openssl s_client -showcerts -servername "$host" -connect "$host:$port" </dev/null 2>/dev/null \
    | openssl x509 -noout -ext subjectAltName
```


**Example output**

```shell-session
X509v3 Subject Alternative Name:
    DNS:your.host.example.net
```


For each endpoint, look for output that resembles the previous example. If there is no output for an endpoint, the certificate of that endpoint is invalid and must be re-issued. 

Important

You must replace all legacy HTTPS certificates before you install OpenShift Container Platform 4.10 or update a cluster to that version. Legacy certificates are rejected with the following message: 

```plaintext
x509: certificate relies on legacy Common Name field, use SANs instead
```
