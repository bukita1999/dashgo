#!/usr/bin/env python
#coding=utf-8

from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray
import rospy
import json_file
import time

markerArray = MarkerArray()
count = 0
rospy.init_node('path_point_pub')

mark_pub = rospy.Publisher('/path_point', MarkerArray,queue_size=100)

file_name="goals_app";
goals=list()
goals=json_file.json_read_lines(goals , file_name)
for goal in goals:
    marker = Marker()
    marker.header.frame_id = "/map"
    marker.type = marker.TEXT_VIEW_FACING
    marker.action = marker.ADD
    marker.scale.x = 1
    marker.scale.y = 1
    marker.scale.z = 1
    marker.color.a = 1.0
    marker.color.r = 1.0
    marker.color.g = 0.0
    marker.color.b = 0.0
    marker.pose.position.x = goal["position"]["x"]
    marker.pose.position.y = goal["position"]["y"]
    marker.pose.position.z = goal["position"]["z"]
    marker.pose.orientation.x = goal["quaternion"]["x"]
    marker.pose.orientation.y = goal["quaternion"]["y"]
    marker.pose.orientation.z = goal["quaternion"]["z"]
    marker.pose.orientation.w = goal["quaternion"]["w"]
    count=count+1
    marker.text = str(count)
    marker.id = len(markerArray.markers);
    markerArray.markers.append(marker)

time.sleep(1)
mark_pub.publish(markerArray)
