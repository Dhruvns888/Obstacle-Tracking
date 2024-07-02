                   CASE STUDY: COOPERATIVE AND AUTONOMOUS SYSTEMS

TOPIC: (Ackerman) Steering-based autonomous vehicle with radar and Lidar for tracking obstacles 

GROUP 16

Group Members: 

                      Chandramohanan Jothishkala  Amal            

                             Bansi Anderson Tam 				         

                                Dhruv Shah                       





Introduction: 

Our case study aimed to develop a steering-based robot for obstacle avoidance using LiDAR and radar. For the execution of our objective, 
we developed a Python script that continuously registers data from a LiDAR sensor installed on our robot. The script then partitions the data into left, 
front left, front, front right, and right sections and determines the presence of obstacles. Using the data, our robot manoeuvres itself to avoid obstacles
and navigates itself in any environment. The script also saves the data received from the LiDAR and stores it in a CSV format. 

 

This project involves creating a ROS (Robot Operating System) node for obstacle avoidance in a robot using LIDAR (Light Detection and Ranging) data.
The objective is to enable the robot to navigate autonomously while avoiding obstacles in its path. This is accomplished by processing LIDAR scan data
to detect obstacles and then determine and execute appropriate manoeuvres such as moving forward, turning left or right, or backing up when an obstacle is detected. 

The node is implemented in Python and subscribes to the LIDAR scan topic to get distance measurements of obstacles around the robot.
It also subscribes to the odometry topic to get the robot's current pose. Based on the LIDAR data, the node decides the robot's movements to avoid obstacles and publishes velocity commands to control the robot's motion. 

Key features of the implementation include: 

Subscribing to sensor data (LIDAR and odometry). 

Processing LIDAR data to detect obstacles. 

Making decisions on the robot's movements based on obstacle detection. 

Publishing velocity commands to control the robot's motion. 

Logging data for analysis and debugging. 

The code is organized into a class named Obstacle Avoidance, which encapsulates the entire functionality of the obstacle avoidance node. The class initializes the ROS node, sets up subscribers and publishers, processes sensor data, and controls the robot's movements based on the processed data. The node is designed to be configurable through ROS parameters, allowing for flexible adjustments to the robot's behaviour. 
