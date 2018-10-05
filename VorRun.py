# -*- coding: utf-8 -*-
"""
VorRun
Plots wireframe output in 2017 version of Vorlax

NOTE! Type: "%matplotlib auto" in iPython console to 
switch to interactive plots, or "%matplotlib inline" 
to switch to inline, in the console.

Lance Bays
12/13/2017
"""

import os
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

# Establish working directory with exe...
# Copy & paste absolute path on Local machine here within double quotes
userExePath = "C:\AeroProgs\Vorlax\VORLAX"

# Split drive Letter from path
drive, exePath = userExePath.split("\\", 1)

# Handle case where user doesn't include drive in path —
# we will assume it's on the C drive 
if not drive: drive="C:"

# Run program
# Command-line instructions to change drive & directory, and run program 
runString = drive + " && cd \\" + exePath + " && vorlax.exe" 
os.system(	runString)

# Read output file
fout = open(drive + "\\" + exePath + "\\VORLAX.WIRE", 'r')
lines=fout.readlines()
fout.close()

# Convert to numpy array 
panelData=[]
for index, line in enumerate(lines):
    panelData.append(np.array(list(map(float,lines[index].split()))))
panelData=np.array(panelData)

# Determine array of unique panel ID's
panelNums = np.unique(panelData[0:,0:1])

# Add subplot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the Vorlax wireframe	(one side)
for index in panelNums:
    ax.plot_wireframe(
    panelData[panelData[:,0]==index][:,np.array([False,True,False,False,False])],
    panelData[panelData[:,0]==index][:,np.array([False,False,True,False,False])],
    panelData[panelData[:,0]==index][:,np.array([False,False,False,True,False])])

# Plot the mirror image (if symmetry is indicated in wire file)
for index in panelNums:
    symFlag=panelData[panelData[:,0]==index][0,np.array([False,False,False,False,True])]
    if symFlag==0 or symFlag==2:
        ax.plot_wireframe(
        panelData[panelData[:,0]==index][:,np.array([False,True,False,False,False])],
        -1*panelData[panelData[:,0]==index][:,np.array([False,False,True,False,False])],
        panelData[panelData[:,0]==index][:,np.array([False,False,False,True,False])])

# Format plot
ax.grid()
ax.set(ylabel='y-in',
       xlabel='x-in',
       zlabel='z-in',
       title='')
ax.xaxis.label.set_size(16)
ax.yaxis.label.set_size(16)
ax.zaxis.label.set_size(16)

# Create super-set of data to establish ranges 
x=panelData[:,1]
y=panelData[:,2]
negativey = -1 * panelData[:,2]

y=np.concatenate((y, negativey), axis=0)
z=panelData[:,3]

# Set equal scales on axes
ax.set_aspect('equal')

# Set ranges for plot
max_range = np.array([x.max() - x.min(),
                      y.max() - y.min(),
                      z.max() - z.min()]).max() / 2.0

# Compute midpoints in each direction 
mid_x = (x.max() + x.min()) * 0.5 
mid_y = (y.max() + y.min()) * 0.5
mid_z = (z.max() + z.min()) * 0.5

# Set final ranges
ax.set_xlim(mid_x - max_range, mid_x + max_range)
ax.set_ylim(mid_y - max_range, mid_y + max_range)
ax.set_zlim(mid_z - max_range, mid_z + max_range)
plt.show()