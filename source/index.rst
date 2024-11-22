DynaArm Software Documentation
##############################

Official documentation for the Duatic `DynaArm <https://duatic.com/robotic-arm/>`_
For inquirie


Getting started
***************

Structure
**********

The structure of the software stack is shown in the following image:

.. image:: _static/software_stack.png

.. list-table:: Packages
   :widths: 25 75 
   :header-rows: 1

   * - Package
     - Description
   * - `dynaarm_description <https://github.com/Duatic/dynaarm_description>`_
     - Description package containing URDF and meshes for the DynaArm
   * - `dynaarm_driver <https://github.com/Duatic/dynaarm_driver>`_
     - ros2_control based driver for the DynaArm.
   * - `dynaarm_demo <https://github.com/Duatic/dynaarm_demo>`_
     - Demo applications for the DynaArm. Usually used for testing a new hardware setup.
   * - `rsl_drive_sdk <https://github.com/leggedrobotics/rsl_drive_sdk>`_
     - Underlying SDK for directly controlling the drives. Can be used to control the arm without ROS

.. toctree::
   :maxdepth: 2
   :caption: Contents:

