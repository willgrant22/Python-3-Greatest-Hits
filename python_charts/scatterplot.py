#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Will Grant
# Description : Scatterplot
# =============================================================================
import matplotlib.pyplot as plot 

# x-axis values 
x = [1,2,3,4,5,6,7,8,9,10] 
# y-axis values 
y = [2,4,5,7,6,8,9,11,12,12] 

# plotting points as a scatter plot 
plot.scatter(x, y, label= "stars", color= "green", 
			marker= "*", s=30) 

# x-axis label 
plot.xlabel('x - axis') 
# frequency label 
plot.ylabel('y - axis') 
# plot title 
plot.title('My scatter plot!') 
# showing legend 
plot.legend() 

# function to show the plot 
plot.show() 
