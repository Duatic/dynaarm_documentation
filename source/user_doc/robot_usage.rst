Robot Usage
############

This section provides instructions for operating the DynaArm, including preparation, startup, basic commands, and shutdown procedures.

System Startup
--------------

1. **Mount the Robot:**

   - Ensure the DynaArm is securely mounted on a stable and solid base. This prevents unwanted movement during operation.
   - The mounting position must ensure the robot cannot fall over during use.

2. **Ethercat Connection:**

   - Verify that the Ethercat cable is securely connected to the Controller PC.
   - Check for any loose connections or damaged cables.

3. **Inspect All Cables:**

   - Confirm that all cables are correctly connected and show no signs of damage.
   - Replace any damaged cables before proceeding.

4. **Connect and Power On:**

   - Attach the power supply to the DynaArm.
   - Power on the system and observe the indicator lights for diagnostics:
      - **Normal Operation:** Indicator lights blink in a steady sequence.
      - **Error Detected:** Lights may blink rapidly or remain solid. Refer to the troubleshooting section for details.

.. note::
   The DynaArm may move slightly when activating. Ensure the workspace is clear of obstructions.

Basic Commands
--------------

- **Start the mocked robot:**   
   
   If you have also downloaded the dynaarm_examples repository.

   .. code-block:: bash      

      ros2 launch dynaarm_examples mock.launch.py
   
   **Arguments:**

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

- **Monitor System Status:**

   Check the status of the DynaArm, including joint positions
   
   .. code-block:: bash

      ros2 topic echo /dynaarm_status_controller/state

Shutdown Procedure
------------------

1. **Prepare the Robot:**

   - Move the DynaArm to a defined position where it cannot fall over when powered off.
   - If possible, physically support the arm or secure it in a safe position.

2. **Terminate the DynaArm Software:**

   - Shut down the `dynaarm` software by terminating the process (e.g., pressing `Ctrl+C` once).
   - **Important:** Avoid pressing `Ctrl+C` multiple times, as it may disrupt the Ethercat communication improperly.

3. **Power Off the System:**

   - Once the software is safely shut down, disconnect the power supply from the DynaArm.
   - Ensure the system is fully powered off before handling the robot further.

.. warning::
   The DynaArm may fall if these steps are not followed carefully. Always secure the robot before shutting down the system.
