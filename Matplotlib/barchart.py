#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Will Grant
# Description : Barchart example
# =============================================================================
import matplotlib.pyplot as plot 

# x-coordinates of left sides of bars 
left = [1, 2, 3, 4, 5] 

# heights of bars 
height = [10, 24, 36, 40, 5] 

# labels for bars 
tick_label = ['one', 'two', 'three', 'four', 'five'] 

# plotting a bar chart 
plot.bar(left, height, tick_label = tick_label, 
		width = 0.8, color = ['red', 'green']) 

# naming the x-axis 
plot.xlabel('x - axis') 
# naming the y-axis 
plot.ylabel('y - axis') 
# plot title 
plot.title('My bar chart!') 

# function to show the plot 
plot.show() 
