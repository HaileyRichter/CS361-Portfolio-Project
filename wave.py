import numpy as np
import matplotlib.pyplot as plt

# this block is for setting up the parameters of the program
m=1.0
T=1.0
nBalls=100
nTimes=20000
dx=0.1
dt=0.01
L=(nBalls-1)*dx

# this block does the initial condition
y=np.zeros([nBalls,nTimes])
y[5:10,1]=.01

# this block carries out the calculation
for it in range(1,nTimes-1):
    yLeft=y[0:-2,it]
    yRight=y[2:,it]
    y[1:-1,it+1]=2*y[1:-1,it]-y[1:-1,it-1]+dt**2*T/m/dx*(yLeft+yRight-2*y[1:-1,it])

# this block plots the position of ball 10 as a function of time
plt.figure(1)
plt.clf()
times=np.linspace(0,nTimes,num=nTimes)*dt
plt.plot(times,y[10,:],ls='-',marker='.')
plt.xlabel('Time (s)')
plt.ylabel('Displacement of 10th ball')

# this block plots the animation of the ball positions
plt.figure(2)
xArr=np.arange(0,L+dx/1000,dx)
for it in range(0,nTimes,int(nTimes/100)):
    plt.cla()
    plt.plot(xArr,y[:,it],ls='-',marker='.')
    plt.xlabel('position along the balls')
    plt.ylabel('displacement in the y direction')
    plt.ylim([y.min(),y.max()])
    plt.pause(.001)

# this blocks plots the 2D static visualization
plt.figure(3)
plt.clf()
plt.pcolormesh(times,xArr,y)
plt.xlabel('Time (s)')
plt.ylabel('x')

######
# A bit of change: Let's find the dispersion relation
######
#
# First let's write the loop for advancing the system as a function, since
# we'll need to call it multiple times
######
def computeY(y,dx,dt,m,T):
    nBalls,nTimes=y.shape
    for it in range(1,nTimes-1):
        yLeft=y[0:-2,it]
        yRight=y[2:,it]
        y[1:-1,it+1]=2*y[1:-1,it]-y[1:-1,it-1]+dt**2*T/m/dx*(yLeft+yRight-2*y[1:-1,it])
    return(y)

####
# Here we use the information that normal modes are sinusoidals
# Like we saw in the last activity last term, these have number
# of nodes (points that do not move) ranging from 0 to the number of balls -2 
#(we do not count the two balls at the extremes as nodes.)
####
nodes=np.arange(0,nBalls-2,1)
wavel=2*L/(nodes+1)
freq=np.zeros(nodes.size)
for i in range(nodes.size):
    y=np.zeros([nBalls,nTimes])
    xArr=np.linspace(0,nBalls,num=nBalls)*dx
    y[:,1]=np.sin(np.pi*xArr/L*(nodes[i]+1))
    y=computeY(y,dx,dt,m,T)
    yCenter=y[1,1:-1]
    yLeft=y[1,0:-2]
    yRight=y[1,2:]
    jj=np.where((yCenter>yLeft)&(yCenter>yRight))
    period=(jj[0][1]-jj[0][0])*dt
    freq[i]=1/period
