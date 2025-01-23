Create Your ROS 2 Workspace
----------------------------

.. _create_your_workspace:

Create a new workspace directory:

.. code-block:: bash

    mkdir -p dynaarm_demo_workspace/src && cd dynaarm_demo_workspace

Clone Repositories into Workspace
==================================

Option 1 - Automatic Cloning
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

Option 2 - Manual Cloning
^^^^^^^^^^^^^^^^^^^^^^^^^^

Clone each repository listed in `repos.list` manually into the *src* directory of your workspace.

Build the Code / Workspace
====================================

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

Source your workspace after building:

.. code-block:: bash

    source install/local_setup.bash
