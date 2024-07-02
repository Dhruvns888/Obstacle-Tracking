#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class ObstacleTracking:
    def _init_(self):
        rospy.init_node('obstacle_tracking', anonymous=True)
        
        # Publisher to the /cmd_vel topic
        self.cmd_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        
        # Subscriber to the /scan topic
        rospy.Subscriber('/scan', LaserScan, self.laser_callback)
        
        # Initialize the Twist message
        self.move_cmd = Twist()
        
        # Set the obstacle tracking parameters
        self.obstacle_distance_threshold = 1.0  # meters
        self.linear_speed = 0.2  # meters per second
        self.angular_speed = 0.5  # radians per second

    def laser_callback(self, data):
        # Process laser scan data to find the closest object
        ranges = data.ranges
        min_distance = min(ranges)
        min_index = ranges.index(min_distance)
        
        # Determine the angle to the closest object
        angle_to_obstacle = data.angle_min + min_index * data.angle_increment
        
        rospy.loginfo("Closest distance: %f at angle: %f", min_distance, angle_to_obstacle)
        
        # Check if the closest object is within the threshold distance
        if min_distance < self.obstacle_distance_threshold:
            self.track_obstacle(min_distance, angle_to_obstacle)
        else:
            self.stop()

    def track_obstacle(self, distance, angle):
        # Control the robot to follow the obstacle
        self.move_cmd.linear.x = self.linear_speed
        self.move_cmd.angular.z = -angle  # Negative to turn towards the obstacle
        self.cmd_pub.publish(self.move_cmd)
        rospy.loginfo("Tracking obstacle")

    def stop(self):
        # Stop the robot
        self.move_cmd.linear.x = 0.0
        self.move_cmd.angular.z = 0.0
        self.cmd_pub.publish(self.move_cmd)
        rospy.loginfo("Stopping")

    def run(self):
        rospy.spin()

if __name__ == '__main__':
    try:
        rospy.init_node('obstacle_tracking_node', anonymous=True)
        obstacle_tracking = ObstacleTracking()
        obstacle_tracking.run()
    except rospy.ROSInterruptException:
        pass