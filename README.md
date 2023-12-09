This repository describes how to create, build, and run a Python-based ROS package.

Here is how to build this software.

```
  mkdir simontest
  cd simontest
  mkdir src
  git clone https://github.com/SimonBirrell/simontest src/simontest
  catkin build
  source devel/setup.bash
```

To run it, one can do:

```
  rosrun simontest simon_node1
```

And here is how to launch it as a node:

```
 roslaunch simontest simon_launch1.launch
```

For more details and step-by-step explanations, see http://www.artificialhumancompanions.com/structure-python-based-ros-package/.

NOTE: (9th December 2023)
The code has changed slightly for Python3 (relative imports and print with parentheses). You can access either from the two branches:
```
git checkout ros-python2
git checkout ros-python3
```

The master branch remains the historic Python 2 version, for the moment.



