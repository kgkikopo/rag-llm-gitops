# Chapter 2. BuildConfig [build.openshift.io/v1]

Description
    

Build configurations define a build process for new container images. There are three types of builds possible - a container image build using a Dockerfile, a Source-to-Image build that uses a specially prepared base image that accepts source code that it can make runnable, and a custom build that can run // arbitrary container images as a base and accept the build parameters. Builds run on the cluster and on completion are pushed to the container image registry specified in the "output" section. A build can be triggered via a webhook, when the base image changes, or when a user manually requests a new build be // created. 

Each build created by a build configuration is numbered and refers back to its parent configuration. Multiple builds can be triggered at once. Builds that do not have "output" set can be used to test code or run a verification build. 

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer). 

Type
     `object`
Required
    

  * `spec`

- [2.1. Specification](02_01_specification.md)
- [2.2. API endpoints](02_02_api_endpoints.md)
