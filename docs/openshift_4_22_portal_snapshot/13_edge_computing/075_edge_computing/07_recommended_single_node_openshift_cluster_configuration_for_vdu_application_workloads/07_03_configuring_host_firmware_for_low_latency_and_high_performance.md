# 7.3. Configuring host firmware for low latency and high performance

Bare-metal hosts require the firmware to be configured before the host can be provisioned. The firmware configuration is dependent on the specific hardware and the particular requirements of your installation. 

**Procedure**

  1. Set the **UEFI/BIOS Boot Mode** to `UEFI`. 
  2. In the host boot sequence order, set **Hard drive first**. 
  3. Apply the specific firmware configuration for your hardware. The following table describes a representative firmware configuration for an Intel Xeon Skylake server and later hardware generations, based on the Intel FlexRAN 4G and 5G baseband PHY reference design. 

Important

The exact firmware configuration depends on your specific hardware and network requirements. The following sample configuration is for illustrative purposes only. 

Table 7.2. Sample firmware configurationFirmware setting| Configuration  
---|---  
CPU Power and Performance Policy  |  Performance   
Uncore Frequency Scaling  |  Disabled   
Performance P-limit  |  Disabled   
Enhanced Intel SpeedStep ® Tech  |  Enabled   
Intel Configurable TDP  |  Enabled   
Configurable TDP Level  |  Level 2   
Intel® Turbo Boost Technology  |  Enabled   
Energy Efficient Turbo  |  Disabled   
Hardware P-States  |  Disabled   
Package C-State  |  C0/C1 state   
C1E  |  Disabled   
Processor C6  |  Disabled   
Show more

Note

Enable global SR-IOV and VT-d settings in the firmware for the host. These settings are relevant to bare-metal environments.
