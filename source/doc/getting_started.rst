Getting Started
################

This guide provides a quick overview of how to set up and start using the DynaArm. For detailed instructions, refer to the linked sections.

Hardware Setup
--------------

1. **Mount the Robot:**

    - Place the robot on a stable, level base.
    - Secure it using the mounting holes on the base plate.
    - See detailed mounting instructions in :doc:`Integration and Safety </tech_doc/integration_and_safety>`.

2. **Connect Power and Communication:**

    - Connect the 48 V power supply to the robot.
    - Attach the Ethercat cable to the Controller PC.
    - Ensure cables are secured and free of damage.

For detailed wiring and connection instructions, refer to :doc:`Integration and Safety </tech_doc/integration_and_safety>`.

Software Setup
--------------

1. **Install ROS 2:**

    - Set up a compatible ROS 2 environment (e.g., Jazzy or Iron).
    - Follow the steps in :doc:`Setup Controller PC </user_doc/setup_controller_pc>`.

2. **Set Up the Workspace:**

    - Create and configure a ROS 2 workspace with the DynaArm packages.
    - Build the workspace:
     
    .. code-block:: bash

        colcon build --packages-up-to dynaarm_examples

3. **Enable Realtime (if using hardware):**

    - Configure the system for realtime performance to ensure stable operation.
    - See :doc:`Realtime Setup </user_doc/realtime>` for detailed steps.

First Operation
---------------

1. **Power On the Robot:**

    - Connect the power supply and turn on the robot.
    - Start the `dynaarm_driver`:

    .. code-block:: bash

        ros2 launch dynaarm_driver startup.launch.py

2. **Move the Robot:**

    - Send the arm to its home position:

    .. code-block:: bash

        ros2 service call /go_to_home std_srvs/srv/Trigger "{}"

   - Test other basic commands from :doc:`Robot Usage </user_doc/robot_usage>`.

3. **Shutdown:**

   - Always secure the robot before powering off.
   - Follow the shutdown procedure in :doc:`Robot Usage </user_doc/robot_usage>`.
