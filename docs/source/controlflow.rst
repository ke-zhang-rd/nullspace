============
Control Flow
============

.. image:: ../images/NullspaceControlFlow.svg
    :width: 1000
    :align: center


There are 3 coordinates
    
    * Body, coordinate on robot body(origin point)
    * Support, coordinate by the connection of end effectors
    * Horizon, coordinate defined by direction of gravity

When we try to control the body movement, instead control body, we control the Support rigid.

The Support rigid is defined by the connection of end effector.

We convert our target(no matter what which coordinate in which coordinate) to target of Support rigid on
Boday coordinate. And the current Support rigid on Body coordinate is very easy calculated by forward
kinematics. The error could be achieved to pass to nullspace controller.

