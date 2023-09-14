==========
Philosophy
==========

This package offer you a new floating-base control strategy.

Intuitively, we might wanna control the orientation and position of base directly or by any
inverse kinematics like approach. However, the contact point which could be abstracted to a
ball joint hinge make it almost impossible.

Others try to introduce the mimic 6 joints in configuration space to control base directly.
However, this control is unrealistic.

Here, if we assume the contract point isn't slip. The connection between all contact points
will form a virtual rigid object.

We are controling this virtual object relative to base.

Take quadruped robot dog as a example. Please think it from a astronaut view in space.

    "There is quadruped robot dog contact with Earth"

When you try to control the floating base of quadruped relative to Earth, you could just control the
contact area on earth relative to base. By doing this, forward caluculation is all you need.


If there are multiple end effectors need to coordinate move together. We manipulate those EE by define
a virtual obejct among those EE.

If we define it in a seriously way. 

This object could have a orientation and position if a frame fix on it.

If the number of end effector(num)

N = 2, X is a line

N = 3, X is a triangle

N = 4, X is a tetrahedron


In a prioritized tasks definition:
We might have a tasks from higher priority to lower:

  1.fixed distance between each end effectors, that's conbination of N
  2.there is a target position of Object
  3.there is a target orientation Object

These tasks could be achieved by nullspace method

Some examples which could be benefit from this strategy:

Robot hand(3 fingers)
There is a triangle between 3 fingers. If you coordinate control task 2 and 3 together by considering lead of screw, bottle cap could be moved very
decently.

Qudrupeds(4)

Hexapods(6)

Octopods(8)
