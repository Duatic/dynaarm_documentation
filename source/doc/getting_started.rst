Getting Started
################


Basic Setup - Native installation
*********************************

This section describes how to do the basic setup of your workspace.


Prerequisites
-------------

* General / Simulation only
    * Ubuntu 24.04 installation (or similar)
* Hardware 
    * For hardware interaction we only support a native Linux installation
    * A native gigabit ethernet port (USB to Ethernet adapters can work but might introduce issues)



Step 1  - Basic Setup of ROS2
-----------------------------

Install ROS2 Jazzy natively according to the  `official guide <https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debs.html>`_.

.. note::
    At the moment we only support ROS2 Jazzy. If you need to run the driver with an older version please feel free to contact us.


Step 2 - Realtime Setup (hardware only)
---------------------------------------

If you plan to work with hardware on your setup it is necessary to enable enable realtime support on your system. 
See the realtime setup guide :doc:`realtime`.

Step 3 - Create your workspace
------------------------------

Next you need to create a new underlying workspace to import the dynaarm package into. 

.. code-block:: bash

    # Create new workspace
    mkdir -p dynaarm_demo_workspace && cd dynaarm_demo_workspace
    # Get the repos.list (description of dependend reposistories)
    wget https://github.com/Duatic/dev_workspace/blob/main/repos.list
    # Import the repositories
    mkdir -p src
    vcs import src < repos.list

Step 4 - Build the code
-----------------------

.. code-block:: bash

    # Actually build the code
    colcon build --packages-up-to=dynaarm_examples --mixin release ccache

Step 5 - Run the code
---------------------

.. code-block:: bash

    # Source the workspace
    source install/local_setup.bash

    # Mocked hardware 
    ros2 launch dynaarm_examples mock.launch.py

    # Or real hardware
    ros2 launch dynaarm_examples real.launch.py 


Step 6 - Integrate it into your own application
------------------------------------------------

Take a look at the `dynaarm_demo <https://github.com/Duatic/dynaarm_demo>`_ repository.
You can find there multiple examples on how to run the the dynaarm with mocked hardware, in gazebo simulation or with real hardware. 
