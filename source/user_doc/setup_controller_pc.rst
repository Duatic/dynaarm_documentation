Setup Controller PC
####################

This section explains how to set up your workspace and hardware environment for using the DynaArm.

Prerequisites
-------------

* **General / Simulation only:**

   - Ubuntu 24.04 installation (or a similar Linux distribution).

* **Hardware Setup:**

   - Native Linux installation is required for hardware interaction
   - A native gigabit Ethernet port is recommended (USB to Ethernet adapters may work but could introduce latency or reliability issues).

.. _install_ros_2_jazzy:

Step 1 - Install ROS 2 Jazzy
----------------------------

Install ROS 2 Jazzy natively by following the `official guide <https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debs.html>`_.

.. note::
    Currently, only ROS 2 Jazzy is supported. For compatibility with other versions, please contact us.

Step 2 - Realtime Setup (Hardware Only)
---------------------------------------

For hardware interaction, your system must support real-time operations. Follow the **Realtime Setup** guide: :doc:`realtime`.

.. _create_your_workspace:

Step 3 - Create Your ROS 2 Workspace
-------------------------------------

Create a new workspace directory:

.. code-block:: bash

    mkdir -p dynaarm_demo_workspace/src && cd dynaarm_demo_workspace

Step 4 - Clone Repositories into Workspace
------------------------------------------

**Option 1 - Automatic Cloning**

If you are not already inside the workspace directory created in step 3, switch to this directory:

.. code-block:: bash

    cd dynaarm_demo_workspace

Download the `repos.list` file into the workspace for automatic cloning:

:download:`repos.list </_static/repos.list>`

.. code-block:: bash

    wget https://docs.duatic.com/_static/repos.list

Clone the necessary repositories:

.. code-block:: bash

    vcs import src < repos.list

**Option 2 - Manual Cloning**

Clone each repository listed in `repos.list` manually into the *src* directory of your workspace.

Step 5 - Build the Code / Workspace
-----------------------------------

First, install all dependencies:

.. code-block:: bash

    rosdep init
    rosdep update
    rosdep install -r --from-paths ./src --ignore-src --rosdistro $ROS_DISTRO -y

Exclude the simulation and test packages from the `cartesian_controllers` repository by placing a `COLCON_IGNORE` file in the respective directories:

.. code-block:: bash

    touch src/cartesian_controllers/cartesian_controller_simulation/COLCON_IGNORE
    touch src/cartesian_controllers/cartesian_controller_tests/COLCON_IGNORE

Build the workspace:

.. code-block:: bash

    colcon build

.. 
    colcon build --packages-up-to=dynaarm_examples --mixin release ccache

Step 6 - Run the Code
---------------------

Source your workspace after building:

.. code-block:: bash

    source install/local_setup.bash

**Run Mocked Hardware**

.. code-block:: bash

    ros2 launch dynaarm_examples mock.launch.py

**Run Real Hardware**

Modify the `ethercat_bus` parameter to match your Ethernet interface:

.. code-block:: bash

    ros2 launch dynaarm_examples real.launch.py ethercat_bus:=enp86s0

Step 7 - Integrate into Your Application
----------------------------------------

Visit the `dynaarm_demo <https://github.com/Duatic/dynaarm_demo>`_ repository for multiple examples:

* Running the DynaArm with mocked hardware.
* Simulation in Gazebo.
* Real hardware integration.
