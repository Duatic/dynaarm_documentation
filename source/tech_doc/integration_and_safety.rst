Integration and Safety
#######################

This section provides guidelines for integrating the DynaArm into your setup and ensuring safe operation. Proper integration and adherence to safety measures are critical for optimal performance and to minimize risks.

.. _mounting_instructions:

Mounting Instructions
---------------------

1. **Choose a Stable Base:**

   - Select a surface that can securely support the weight of the robot (9 kg) and any additional payload.
   - The base should be level and free of vibrations.

2. **Secure the Robot:**

   - Follow the dimensions provided in the technical drawing below for proper alignment.

The following drawing indicates the base plate's mounting features for secure attachment of the DynaArm.

.. _interface-holes:

.. figure:: ../_static/base_plate_interface_holes.png
   :alt: Drawing showing the mounting features of the DynaArm base plate
   :width: 100%

   Drawing showing the mounting features of the DynaArm base plate

.. list-table::
   :header-rows: 1

   * - **Detail**
     - **Description**
   * - A
     - Alignment hole
   * - B
     - Alignment slot

- Mount the robot in either a bottom or top configuration, depending on the application, as shown in the following drawings.

The following drawing illustrates the steps required for the bottom mounting of the robot arm.

.. _bottom-mounting:

.. figure:: ../_static/bottom_mounting_configuration.png
   :alt: Illustration of the bottom mounting configuration of the DynaArm
   :width: 100%

   Illustration of the bottom mounting configuration of the DynaArm

.. list-table::
   :header-rows: 1

   * - **Item**
     - **Description**
     - **Details**
   * - 1
     - DynaArm
     - 
   * - 2
     - 2x Dowel Pins Ø5 H7
     - Secure the robot arm's position and prevent further movement.
   * - 3
     - Ground
     - Ensure clearance for M6 screws at the positions marked on the diagram :numref:`interface-holes`.
   * - 4
     - 6x M6 metric screws, Strength class 8.8
     - Tighten the screws with a recommended torque of 9.5 Nm.

The following drawing illustrates the steps required for the top mounting of the robot arm.

.. _top-mounting:

.. figure:: ../_static/top_mounting_configuration.png
   :alt: Illustration of the top mounting configuration of the DynaArm
   :width: 100%

   Illustration of the top mounting configuration of the DynaArm

.. list-table::
   :header-rows: 1

   * - **Item**
     - **Description**
     - **Details**
   * - 1
     - DynaArm
     - 
   * - 2
     - 2x Dowel Pins Ø5 H7
     - Secure the robot arm's position and prevent further movement.
   * - 3
     - Ground
     - Ensure M5 tapped holes at the positions marked on the diagram :numref:`interface-holes`.
   * - 4
     - 6x M5 metric screws, Strength class 8.8
     - Tighten the screws with a recommended torque of 5.6 Nm.


3. **Verify Stability:**

   - Ensure the robot does not wobble or shift during operation.
   - Tighten all screws and bolts securely.

.. _wiring_and_connections:

Wiring and Connections
----------------------

1. **Power Connection:**

   - Use a 48 V power supply that meets the specifications listed in the **Technical Specifications** section.
   - Ensure the power supply is properly grounded.

2. **EtherCAT Connection:**

   - Connect the EtherCAT cable to the robot and the Controller PC.
   - Verify that the network interface is configured correctly:

   .. code-block:: bash

        sudo ip link set eth0 up
        sudo ip addr add 192.168.1.2/24 dev eth0

3. **Cable Management:**

   - Route cables away from moving parts to avoid entanglement.
   - Use cable ties or channels to secure cables.

Safety Guidelines
-----------------

1. **Emergency Stop:**

   - Always ensure the emergency stop button is easily accessible during operation.
   - Test the emergency stop functionality before every session.

2. **Safe Work Area:**

   - Maintain a clear workspace around the robot.
   - Avoid placing objects within the robot’s operational range.

3. **Start-Up Precautions:**

   - Be aware that the robot may move slightly during activation.
   - Never stand within the robot’s range during start-up or shutdown.

4. **Routine Inspections:**

   - Check for loose screws, damaged cables, or other potential hazards before each use.
   - Inspect the mounting base periodically to ensure stability.

5. **Warning Signs:**

   - Place visible warning signs near the robot to alert operators and bystanders of potential risks.

.. warning::
   Failure to follow these guidelines may result in equipment damage or personal injury.
