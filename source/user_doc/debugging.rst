Debugging
##########

In order to debug the `dynaarm_driver <https://github.com/Duatic/dynaarm_driver/>`_ or any ros2control controller you need
to attach a debugger to the controller manager node. In order to do so you need adapt your launch file.

.. code-block:: python

    # This example is taken from the official ros2 control debug guide

    # Obtain the controller config file for the ros2 control node
    controller_config_file = get_package_file("<package name>", "config/controllers.yaml")

    controller_manager = Node(
        package="controller_manager",
        executable="ros2_control_node",
        parameters=[controller_config_file],
        output="both",
        emulate_tty=True,
        remappings=[
            ("~/robot_description", "/robot_description")
        ],
        prefix=['xterm -e gdb -ex run --args']  # or prefix=['gdbserver localhost:3000'] # For setup with vscode for example
    )

    ld.add_action(controller_manager)


For more information and a detailed guide see the official ros2control `debugging guide <https://control.ros.org/rolling/doc/ros2_control/doc/debugging.html>`_.


.. warning::

    Please be careful with using debug builds and breakpoints. If you tap into the realtime loop you might experience unexpected behaviour of the system. 


References
***********

* `ros2control debug guide <https://control.ros.org/rolling/doc/ros2_control/doc/debugging.html>`_
* `ros2 debug guide <https://docs.ros.org/en/jazzy/How-To-Guides/Getting-Backtraces-in-ROS-2.html>`_