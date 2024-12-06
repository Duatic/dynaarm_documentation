Getting Started
################


Basic Setup
***********

This section describes how to do the basic setup of your workspace.


Prerequisites
-------------

* General / Simulation only
    * Ubuntu 24.04 installation (or similar)
* Hardware 
    * For hardware interaction we only support a native Linux installation
    * A native gigabit ethernet port (USB to Ethernet adapters can work but might introduces issues)


Step 1  - Install ROS2
----------------------


Variant A - docker installation:
""""""""""""""""""""""""""""""""

| This is the recommended installation way. 
| We provide two pre-configured docker images. One with the full software stack installed and one with just the necessary dependencies for development.

Variant B - native installation:
""""""""""""""""""""""""""""""""

Install ROS2 Jazzy natively according to the official guide `here <https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debs.html>`_.


Step 2 - Realtime Setup
------------------------

If you plan to work with hardware on your setup it is necessary to enable enable realtime support on your system. 
See the realtime `setup guide <realtime>`_.



Examples
*********

Take a look at the `dynaarm_demo <https://github.com/Duatic/dynaarm_demo>`_ repository.
