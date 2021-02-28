#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Will Grant
# Description : Piechart
# =============================================================================
import matplotlib.pyplot as plot 

# defining labels 
activities = ['eat', 'sleep', 'work', 'play'] 

# portion covered by each label 
slices = [3, 7, 8, 6] 

# color for each label 
colors = ['r', 'y', 'g', 'b'] 

# plotting the pie chart 
plot.pie(slices, labels = activities, colors=colors, 
		startangle=90, shadow = True, explode = (0, 0, 0.1, 0), 
		radius = 1.2, autopct = '%1.1f%%') 

# plotting legend 
plot.legend() 

# showing the plot 
plot.show() 
