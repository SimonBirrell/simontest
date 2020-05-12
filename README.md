This repository describes how to create, build, and run a-Python based ROS package.

Here is how to build this software.

mkdir simontest
cd simontest
mkdir src
git clone https://github.com/SimonBirrell/simontest src/simontest
catkin build
source devel/setup.bash

To run it, one can do:

  rosrun simontest simon_node1

And here is how to launch it as a node:

 roslaunch simontest simon_launch1.launch

For more details and step-by-step explanations, see http://www.artificialhumancompanions.com/structure-python-based-ros-package/.
