import numpy as np
import matplotlib.pyplot as plt

# The wave code is from my PH 367 course where we spent a week in pairs writing a simulation of balls on spring

# get variable from the user or use default values
# default values
amplitude = 'A'
wave_num = 'k'
angular_frequency = 'w'
# user values
arr = []
# opening the text file
with open('wave_info.txt', 'r') as file:
    # reading each line
    for line in file:
        # reading each word
        for word in line.split():
            if word == 'default' or word == 'transverse':
                continue
            else:
                arr.append(word)
if len(arr) == 3:
    amplitude = arr[0]
    wave_num = arr[1]
    angular_frequency = arr[2]

# this block is for setting up the parameters of the program
m=1.0 # mass
T=1.0 # tension
nBalls=500 # number of balls
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
    plt.plot(xArr,y[:,t],ls='-',marker='.',color='green')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Transverse Wave')
    plt.ylim([y.min(),y.max()])
    plt.pause(0.01)

print("Here is the wave equation for this wave: y(x,t) = " + str(amplitude) + "cos(" + str(wave_num) + "*x - " + str(angular_frequency) + "*t)")