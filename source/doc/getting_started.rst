Getting Started
################

This guide provides a quick overview of how to set up and start using the DynaArm. For detailed instructions, refer to the linked sections.

Hardware Setup
--------------

**Mount the Robot**

- Place the robot on a stable, level base.
- Secure it using the mounting holes on the base plate with M5 screws (top access) or M6 screws (bottom access).
- See detailed mounting instructions in :ref:`Mounting Instructions <mounting_instructions>`.

**Connect Power and Communication**

- Connect an appropriate 48 V power supply to the robot.
- Attach the EtherCAT cable to the Controller PC.
- Ensure cables are secured and free of damage.

For detailed wiring and connection instructions, refer to :ref:`Wiring and Connections <wiring_and_connections>`.

Software Setup
--------------

**Install ROS 2 Jazzy**

- Follow the :ref:`detailed steps <install_ros_2_jazzy>` to set up ROS 2 Jazzy.
- Ensure a compatible ROS 2 environment is configured.

**Enable Realtime (if using hardware)**

- Refer to the :doc:`detailed steps </user_doc/realtime>` for configuring realtime performance.
- Proper configuration ensures stable hardware operation.

**Set Up the Workspace**

- Follow the :ref:`detailed steps <create_your_workspace>` to create and configure a ROS 2 workspace.
- Build the workspace:

.. code-block:: bash

    colcon build

First Operation
----------------

**Place the Robot in a Stable Position**

.. warning::

    **Important Notice:** The DynaArm does not currently have brakes.

    - When the power is removed or during the start-up process, the arm will not hold itself in position.
    - Before starting or shutting down the robot, ensure the arm is placed in a stable, secure position where it cannot fall or cause damage.
    - If possible, physically support the arm or ensure it rests on a stable surface to prevent uncontrolled movement.

**Power On the Robot**

- Connect the power supply to the robot and switch it on.
- Modify the `ethercat_bus` parameter to match your Ethernet interface:

.. code-block:: bash

    ros2 launch dynaarm_examples real.launch.py ethercat_bus:=enp86s0

- During the start-up process, the arm may briefly enter an uncontrolled state. Ensure no one is within its operating range.
- The robot is now in freeze control mode.

**Activate Freedrive Mode**

To freely move the robot around, activate the `freedrive_controller`:

.. code-block:: bash

    ros2 control switch_controllers --activate freedrive_controller --deactivate freeze_controller

Once enabled, you can manually move the robot by guiding it with your hands.

**Control the Robot with a Gamepad**

To control the robot using a gamepad:

1. Ensure that your gamepad is connected to the computer.
2. Deactivate the `freedrive_controller` (if it is currently active) and activate the `joint_trajectory_controller`:

.. code-block:: bash

    ros2 control switch_controllers --activate joint_trajectory_controller --deactivate freedrive_controller

3. Launch the gamepad interface:

.. code-block:: bash

    ros2 launch dynaarm_gamepad_interface gamepad_interface.launch.py

With the gamepad interface active, you can control the robot's movement using the connected gamepad. The following controls are available:

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



**Shutdown**

- Always move the arm to a stable position before powering off, as the arm will become unpowered and unable to hold itself.
- Follow the shutdown procedure detailed in :doc:`Robot Usage </user_doc/robot_usage>`.
- Secure the arm in place or ensure it is resting on a stable surface before disconnecting the power supply.
