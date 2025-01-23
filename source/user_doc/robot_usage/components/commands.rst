Commands
---------

This section provides essential commands for operating the DynaArm in both mock and real hardware modes.

Start the Robot
~~~~~~~~~~~~~~~

If you have downloaded the `dynaarm_examples` repository, you can start the robot in **mocked mode** or in **real mode**. 
In both modes, the robot launches into freeze control.

.. note::
    Ensure that your workspace is sourced before running the robot commands.

**Mock Mode**

Start the robot with **mocked hardware**:

.. code-block:: bash      

   ros2 launch dynaarm_examples mock.launch.py

**Real Hardware**


Start the robot with **real hardware**:

.. include-start-real-command

.. code-block:: bash      

   ros2 launch dynaarm_examples real.launch.py ethercat_bus:=enp86s0

.. include-end-real-command

**Arguments (Mock & Real)**

- **gui** - flag to enable `joint_state_publisher_gui`.
   - Valid choices: `True`, `False`
   - Default: `True`

- **dof** - select the desired degrees of freedom (DoF).
   - Valid choices: `1`, `2`, `3`, `4`, `5`, `6`
   - Default: `6`

- **covers** - show or hide the covers of the robot.
   - Default: `False`

- **version** - select the desired version of the robot.
   - Valid choices: `arowna4`, `baracuda12`
   - Default: `baracuda12`

**Arguments (Real Only)**

- **ethercat_bus** - select your connected interface
   - Default: `enp86s0`

Monitor System Status
~~~~~~~~~~~~~~~~~~~~~

   Check the status of the DynaArm, including joint positions
   
   .. code-block:: bash

      ros2 topic echo /dynaarm_status_controller/state

Freedrive
~~~~~~~~~

.. include-start-freedrive-mode

To freely move the robot around, activate the `freedrive_controller`:

.. code-block:: bash

    ros2 control switch_controllers --activate freedrive_controller --deactivate freeze_controller

Once enabled, you can manually move the robot by guiding it with your hands.

.. include-end-freedrive-mode

Control with a Gamepad
~~~~~~~~~~~~~~~~~~~~~~

.. include-start-gamepad

With the gamepad interface active, you can control the robot's movement using the connected gamepad.

1. Ensure that your gamepad is connected to the computer.
2. Activate the `joint_trajectory_controller`:

.. code-block:: bash

   ros2 control switch_controllers --activate joint_trajectory_controller

To launch the gamepad interface:

.. code-block:: bash

    ros2 launch dynaarm_gamepad_interface gamepad_interface.launch.py

.. include-end-gamepad

.. _gamepad_controls:

The following functions are available:

.. list-table:: Basic Button Commands
   :header-rows: 1

   * - Control
     - Function
   * - **L1 (Left Shoulder)**
     - Acts as the "deadman_switch". It must be pressed to enable movement.

.. list-table:: Joint Trajectory Button Commands
   :header-rows: 1

   * - Control
     - Joint Name
   * - **Left Joystick X-Axis**
     - shoulder_rotation
   * - **Left Joystick Y-Axis**
     - shoulder_flexion
   * - **Right Joystick Y-Axis**
     - elbow_flexion
   * - **Right Joystick X-Axis**
     - forearm_rotation
   * - **L2 (Left Trigger) / R2 (Right Trigger)**
     - wrist_flexion
   * - **Left Joystick Press / Right Joystick Press**
     - wrist_rotation