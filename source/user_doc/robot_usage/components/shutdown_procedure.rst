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