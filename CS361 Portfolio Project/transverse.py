import numpy as np
import matplotlib.pyplot as plt

# this block is for setting up the parameters of the program
m=1.0 # mass
T=1.0 # tension
nBalls=100 # number of balls
nTimes=100000
dx=0.1
dt=0.01
L=(nBalls-1)*dx
yi = 0.1 # initial y height of wave (amplitude)

# this block sets up the y matrix of every balls y position for every time step
y=np.zeros([nBalls,nTimes])
y[5:10,1]= yi

# this block carries out the calculations to fill out the rest of the cells
for t in range(1,nTimes-1):
    yLeft=y[0:-2,t]
    yRight=y[2:,t]
    y[1:-1,t+1]=2*y[1:-1,t]-y[1:-1,t-1]+dt**2*T/m/dx*(yLeft+yRight-2*y[1:-1,t])

# this block plots the animation of the ball positions
xArr=np.arange(0,L+dx/1000,dx)
for t in range(0,nTimes,int(nTimes/100)):
    plt.cla()
    plt.plot(xArr,y[:,t],ls='-',marker='.')
    plt.xlabel('position along the balls')
    plt.ylabel('displacement in the y direction')
    plt.ylim([y.min(),y.max()])
    plt.pause(0.01)

print("Here is the wave equation for this wave: PRINT SOMETHING LATER")