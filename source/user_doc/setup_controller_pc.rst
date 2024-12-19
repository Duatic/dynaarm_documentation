Setup Controller PC
####################

This section describes how to set up your workspace and hardware environment for using the DynaArm.

Prerequisites
-------------

* **General / Simulation only:**

   - Ubuntu 24.04 installation (or similar).

* **Hardware Setup:**

   - Native Linux installation required for hardware interaction.
   - Native gigabit Ethernet port (USB to Ethernet adapters might work but could introduce issues).

Step 1 - Install ROS 2 Jazzy
----------------------------

Install ROS 2 Jazzy natively according to the `official guide <https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debs.html>`_.

.. note::
    At the moment, we only support ROS 2 Jazzy. For compatibility with other versions, please contact us.

Step 2 - Realtime Setup (Hardware Only)
---------------------------------------

For hardware interaction, your system must support real-time operations. Follow the **Realtime Setup** guide: :doc:`realtime`.

Step 3 - Create Your Workspace
------------------------------

To import and build the DynaArm package, create a new workspace:

.. code-block:: bash

    # Create a new workspace
    mkdir -p dynaarm_demo_workspace && cd dynaarm_demo_workspace
    # Get the repos.list (description of dependent repositories)
    wget https://github.com/Duatic/dev_workspace/blob/main/repos.list
    # Import the repositories
    mkdir -p src
    vcs import src < repos.list

Step 4 - Build the Code
-----------------------

.. code-block:: bash

    # Build the workspace
    colcon build --packages-up-to=dynaarm_examples --mixin release ccache

Step 5 - Run the Code
---------------------

You can now run the DynaArm using either mocked or real hardware:

.. code-block:: bash

    # Source the workspace
    source install/local_setup.bash

    # Run with mocked hardware
    ros2 launch dynaarm_examples mock.launch.py

    # Or with real hardware
    ros2 launch dynaarm_examples real.launch.py 

Step 6 - Integrate into Your Application
----------------------------------------

Visit the `dynaarm_demo <https://github.com/Duatic/dynaarm_demo>`_ repository for multiple examples. These include:
- Running the DynaArm with mocked hardware.
- Simulation in Gazebo.
- Real hardware integration.
