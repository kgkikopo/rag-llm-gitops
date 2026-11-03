# 3.5. Verifying that the current installation host can pull release images

After you boot the agent image and network services are made available to the host, the agent console application performs a pull check to verify that the current host can retrieve release images. 

If the primary pull check passes, you can quit the application to continue with the installation. If the pull check fails, the application performs additional checks, as seen in the `Additional checks` section of the TUI, to help you troubleshoot the problem. A failure for any of the additional checks is not necessarily critical as long as the primary pull check succeeds. 

If there are host network configuration issues that might cause an installation to fail, you can use the console application to make adjustments to your network configurations. 

Important

If the agent console application detects host network configuration issues, the installation workflow will be halted until the user manually stops the console application and signals the intention to proceed. 

**Procedure**

  1. Wait for the agent console application to check whether or not the configured release image can be pulled from a registry. 
  2. If the agent console application states that the installer connectivity checks have passed, wait for the prompt to time out to continue with the installation. 

Note

You can still choose to view or change network configuration settings even if the connectivity checks have passed. 

However, if you choose to interact with the agent console application rather than letting it time out, you must manually quit the TUI to proceed with the installation. 

  3. If the agent console application checks have failed, which is indicated by a red icon beside the `Release image URL` pull check, use the following steps to reconfigure the host’s network settings: 

     1. Read the `Check Errors` section of the TUI. This section displays error messages specific to the failed checks. 

![The home screen of the agent console application displaying check errors](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Installing_an_on-premise_cluster_with_the_Agent-based_Installer-en-US/images/5c4395c78264f5de7e4355a2c21bd41d/agent-tui-home.png) ![The home screen of the agent console application displaying check errors](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Installing_an_on-premise_cluster_with_the_Agent-based_Installer-en-US/images/5c4395c78264f5de7e4355a2c21bd41d/agent-tui-home.png)

     2. Select **Configure network** to launch the NetworkManager TUI. 
     3. Select **Edit a connection** and select the connection you want to reconfigure. 
     4. Edit the configuration and select **OK** to save your changes. 
     5. Select **Back** to return to the main screen of the NetworkManager TUI. 
     6. Select **Activate a Connection**. 
     7. Select the reconfigured network to deactivate it. 
     8. Select the reconfigured network again to reactivate it. 
     9. Select **Back** and then select **Quit** to return to the agent console application. 
     10. Wait at least five seconds for the continuous network checks to restart using the new network configuration. 
     11. If the `Release image URL` pull check succeeds and displays a green icon beside the URL, select **Quit** to exit the agent console application and continue with the installation.
