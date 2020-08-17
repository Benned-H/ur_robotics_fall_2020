# Intro to Robotics Workshop 6: Planning with A*
This is the source code for the sixth and final workshop in the Intro to Robotics Workshop Series for the Robotics Club at the University of Rochester.

## What's in this directory

### *Answers*
#### answer1.txt
The answer for the first exercise of this workshop.
#### answer2.txt
The answer for the second exercise of this workshop.

### *Arm A\* files*
#### arm_astar.py
Source code for an interactive A* planner implementation over the joint space of our robotic arm. This uses the general A* methods used throughout this workshop as defined in general_astar.py.
#### arm_driver.py
This file runs the A* planner and GUI for the physical robot arm. Only works on the Raspberry Pi.
#### arm_gui.py
Source code for visualizing the joint angles and planning process on the 2DOF two-dimensional arm.
#### arm.py
Source code for a two-dimensional arm with forward kinematics, the result of WS 5.
#### link.py
Source code for a two-dimensional link in an arm with an adjustable angle, as well as a version with a fixed joint.

### *Other A\* files*
#### general_astar.py
Source code for a general implementation of the A* algorithm which is used in the planners for arm\_astar.py and grid\_astar.py.
#### grid_astar.py
Source code for an A* planner implementation over a 2D grid. This interactive demo illustrates the open and closed lists and may help you understand what A* does in an easier-to-visualize space than the arm's joint angles.
#### setup.py
This file allows us to pip install the workshop as a Python package, if we wanted to.

## Which files to run
There are two A\* demonstrations in this workshop and both work using the A\* implementation found in general_astar.py, demonstrating the generality of the formalism we've set up. As usual, make sure your current directory is this workshop's folder. The two demos are then:

1. *Grid Demo* - Run `python3 grid_astar.py`. Follow along with the instructions in the window that pops up to see some A\* planning over a randomized 2D grid. This demonstration starts with a 4-connected action set but one of the exercises will ask you to improve on this.
2. *Arm Demo* - First rerun the commands to clone and pip install the `stepper_motors` library into this workshop's directory. Next, if you aren't on a Raspberry Pi, run `python3 arm_astar.py`. This will bring up a GUI to interface with a simulated arm. Drag the green x on the right to a point, click Plan, and the GUI will show the open and closed lists during the search before animating the arm moving to the specified position. The command line will print the search and action execution process. On Raspberry Pi, instead run `python3 arm_driver.py` to launch the same functionality but with the physical arm.

## What you have to implement
We've made it to the final workshop, so the exercises here are more open-ended. We propose three activities, each a bit more difficult than the last.

1. Read over the A* implementation in general_astar.py starting on line 178. There are comments connecting it line-by-line with the pseudocode in the slides. Check the other functions in the file to see what the interface requires: `neighbors(n)`, `cost(c, n)`, and `h(n, G)`.
2. Implement an 8-connected neighbors function for the grid A\* demo. You'll need to write one line inside the `actions8(n)` function starting on line 115 of grid_astar.py. Test your implementation by changing line 143 to call `actions8(n)` instead and then run `python3 grid_star.py`. Hint: Look at the `actions4(n)` function for an idea of the action format.
3. Let's improve the `neighbors(curr)` function for the arm A\*. Currently the function  considers all states which have one angle changed by one discretization step. Your task is to combine this list of neighbors with the one returned by `expand_2n(state)`, which gives all states with two angles changed by one discretization step. Including more complex actions will allow A\* to converge to a faster solution with fewer actions. *Hint*: See line 108 calling `expand_1n(state)`? You'll want to call `expand_2n(state)` in a similar way and concatenate the lists.

We could probably do even better. What if we allowed even more angles to change in one action? What if we weighted the heuristic more than the cost so that actions are biased towards the goal? What if we added obstacles that block certain arm configurations? We'll leave these questions for future workshops. For now, I hope you've learned something new from this series.

Please email any questions or comments to bhedegaa@u.rochester.edu to help improve these workshops for the future.