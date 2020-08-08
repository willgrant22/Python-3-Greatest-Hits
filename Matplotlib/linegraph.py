#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Will Grant
# Description : Linegraph
# =============================================================================
import matplotlib.pyplot as plot 

# line 1 points 
x1 = [1,2,3] 
y1 = [2,4,1] 
# plotting the line 1 points 
plot.plot(x1, y1, label = "line 1") 

# line 2 points 
x2 = [1,2,3] 
y2 = [4,1,3] 
# plotting the line 2 points 
plot.plot(x2, y2, label = "line 2") 

# naming the x axis 
plot.xlabel('x - axis') 
# naming the y axis 
plot.ylabel('y - axis') 
# giving a title to my graph 
plot.title('Two lines on same graph!') 

# show a legend on the plot 
plot.legend() 

# function to show the plot 
plot.show() 
