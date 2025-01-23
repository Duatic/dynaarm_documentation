Getting Started
################

This guide offers a concise overview of setting up and using the DynaArm. For more detailed instructions, follow the linked sections.

Hardware Setup
--------------

**Mount the Robot**

- Use a stable, level surface for the robot.
- Secure it with M5 screws (top) or M6 screws (bottom).

For detailed steps, see :ref:`Mounting Instructions <mounting_instructions>`.

**Connect Power and Communication**

- Connect an appropriate 48 V power supply to the robot.
- Attach the EtherCAT cable to the Controller PC.
- Ensure cables are secured and free of damage.

For detailed wiring and connection instructions, refer to :ref:`Wiring and Connections <wiring_and_connections>`.

Software Setup
--------------

**Install ROS 2 Jazzy**

- Follow the :ref:`detailed steps <install_ros_2_jazzy>` to install ROS 2 Jazzy.
- Verify that your ROS 2 environment is properly configured.

**Enable Realtime (for hardware use)**

- See :doc:`detailed steps </user_doc/setup_controller_pc/components/realtime>` to configure realtime performance.
- Proper configuration ensures stable hardware operation.

**Set Up the Workspace**

- Follow the :ref:`detailed steps <create_your_workspace>` to create and configure a ROS 2 workspace.

First Operation
----------------

**Place the Robot in a Stable Position**

.. warning::

   **Important Notice:** The DynaArm does not have brakes.

   - The arm will not hold its position when power is off or during start-up.
   - Ensure the arm is placed securely to prevent it from falling or causing damage.
   - If necessary, physically support the arm or rest it on a stable surface.

**Power On the Robot**

- Connect the power supply to the robot and switch it on.

**Start the Software Driver**

- Modify the `ethercat_bus` parameter to match your Ethernet interface:

.. include:: /user_doc/robot_usage/components/commands.rst
   :start-after: .. include-start-real-command
   :end-before: .. include-end-real-command

- During start-up, the arm may briefly move uncontrollably. Keep a safe distance from its range of motion.
- Once started, the robot will enter freeze control mode.

**Activating Freedrive Mode**

.. include:: /user_doc/robot_usage/components/commands.rst
   :start-after: .. include-start-freedrive-mode
   :end-before: .. include-end-freedrive-mode

**Using a Gamepad to Control the Robot**

.. include:: /user_doc/robot_usage/components/commands.rst
   :start-after: .. include-start-gamepad
   :end-before: .. include-end-gamepad

For details on gamepad controls, including button mappings, see :ref:`the mapping list <gamepad_controls>`.


Shutdown
---------

- Move the arm to a stable position before powering off. When unpowered, the arm cannot hold its position.
- Follow the shutdown procedure in :doc:`Robot Usage </user_doc/robot_usage/robot_usage>`.
- Secure the arm or place it on a stable surface before disconnecting the power supply.