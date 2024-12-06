Realtime
#########

Within the ros2control based software stack for the DynaArm there are two componentes which are timing critical.

1. The ros2control `controller manager <https://control.ros.org/rolling/doc/ros2_control/controller_manager/doc/userdoc.html>`_ itself (contains also the official rt-guide)
2. The ethercat update thread in the `dynaarm_driver hardware interface <https://github.com/Duatic/dynaarm_driver/blob/main/dynaarm_driver/dynaarm_driver/src/dynaarm_hardware_interface.cpp>`_

Not meeting the necessary update rates can lead to either an unstable connection between the computer running the ROS2 stack and the robot arm
or can lead to suboptimal operation such as uneven trajectory tracking. 

It is therefore necessary to prepare the computer running the ROS2 stack.

Setup
*****

Setting up basic realtime capabilities is fortunately rather easy nowadays on a linux system. 

.. note::
    
    Even though Windows is fully supported by ROS2 any realtime capabilities are not supported on Windows.
    We therefore strongly recommand running at least the ros2control controller manager on a linux host system. (No WSL)

Kernel
=======

You will achieve the best performance running your system with a `PREEMPT_RT` enabled kernel. 
Unfortunately Ubuntu doesn't ship a pre-built rt-kernel in their official repository.

We therefore recommend using the `linux-lowlatency <https://launchpad.net/ubuntu/+source/linux-lowlatency>`_ kernel package shipped by ubuntu. 
Install the linux-lowlatency package via `sudo apt install linux-lowlatency`. Afterwards reboot your system.

.. note::
    
    Different linux distribution may ship different kernel packages. E.g. Debian already ships a pre-built rt-kernel package but does not ship a low latency package.



Permissions
============

| Additionally the user you are running the ROS2 stack with needs to have sufficient permissions in order to change the scheduler priorities. 
| First create a group called `realtime` and add your current user to it.

.. code-block:: bash

    sudo addgroup realtime
    sudo usermod -a -G realtime $(whoami)

Then configure the rt related limits in `etc/security/limits.conf` by adding to the end of the file:

.. code-block:: bash

    @realtime soft rtprio 99
    @realtime soft priority 99
    @realtime soft memlock 102400
    @realtime hard rtprio 99
    @realtime hard priority 99
    @realtime hard memlock 102400

Afterwards you need to reboot or at least logout and log back into your user session.


Notes
*****

Running a rt/lowlatency kernel will allow the control related parts to achieve the necessary stable update rates. On the other hand it will reduce the total throughput of your system.
It is not advised to run especially the rt-kernel on your normal developer computer!

References
**********

* `ros2control rt documentation <https://control.ros.org/rolling/doc/ros2_control/controller_manager/doc/userdoc.html>`_
* `linux-lowlatency package <https://launchpad.net/ubuntu/+source/linux-lowlatency>`_
* Background to different kernel types `stackoverflow link <https://unix.stackexchange.com/questions/553980/why-would-anyone-choose-not-to-use-the-lowlatency-kernel>`_
* `limits.conf information <https://linux.die.net/man/5/limits.conf>`_