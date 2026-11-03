# 6.3. Console and download route customization

You can customize the `console` and `downloads` routes by using the `ingress` config route configuration API. Using this API centralizes route configuration for both routes and takes precedence over the deprecated `console-operator` config method. 

If the `console` custom route is configured in both the `ingress` config and the `console-operator` config, the `ingress` config custom route configuration takes precedence. Configuring custom routes through the `console-operator` config is deprecated.
