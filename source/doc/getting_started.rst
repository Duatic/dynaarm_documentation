Getting Started
################

This guide provides a quick overview of how to set up and start using the DynaArm. For detailed instructions, refer to the linked sections.

Hardware Setup
--------------

#. **Mount the Robot:**

    - Place the robot on a stable, level base.
    - Secure it using the mounting holes on the base plate @Eris: which screws?
    - See detailed mounting instructions in :ref:`Mounting Instructions <mounting_instructions>`.

#. **Connect Power and Communication:**

    - Connect an appropriate 48 V power supply to the robot.
    - Attach the Ethercat cable to the Controller PC.
    - Ensure cables are secured and free of damage.

For detailed wiring and connection instructions, refer to :ref:`Wiring and Connections <wiring_and_connections>`.

Software Setup
--------------

#. **Install ROS 2 Jazzy:**

    - :ref:`Detailed steps <install_ros_2_jazzy>`     
    - Set up a compatible ROS 2 environment (e.g., Jazzy)    

#. **Enable Realtime (if using hardware):**

    - :doc:`Detailed steps </user_doc/realtime>`
    - Configure the system for realtime performance to ensure stable operation.    

#. **Set Up the Workspace:**

    - :ref:`Detailed steps <create_your_workspace>`
    - Create and configure a ROS 2 workspace with the DynaArm packages.
    - Build the workspace:
     
    .. code-block:: bash

        colcon build    

First Operation
----------------

#. **Place the Robot in a Stable Position**

    .. warning::

        **Important Notice:** The DynaArm does not currently have brakes. 
        
    - When the power is removed or during the start-up process, the arm will not hold itself in position.
    - Before starting or shutting down the robot, ensure the arm is placed in a stable, secure position where it cannot fall or cause damage.
    - If possible, physically support the arm or ensure it rests on a stable surface to prevent uncontrolled movement.

#. **Power On the Robot**

    - Connect the power supply to the robot and switch it on.
    - Launch the dynaarm software to initialize the system:

    .. code-block:: bash

        ros2 launch dynaarm_examples startup.launch.py

    - During the start-up process, the arm may briefly enter an uncontrolled state. Ensure no one is within its operating range.

#. **Activate Freedrive Mode**

    - TBD: Enable the Freedrive mode (instructions to be added).
    - Once enabled, you can manually move the robot by guiding it with your hands.

#. **Shutdown**

    - Always move the arm to a stable position before powering off, as the arm will become unpowered and unable to hold itself.
    - Follow the shutdown procedure detailed in :doc:Robot Usage </user_doc/robot_usage>.
    - Secure the arm in place or ensure it is resting on a stable surface before disconnecting the power supply.
