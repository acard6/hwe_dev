import numpy as np 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D 
from matplotlib.animation import FuncAnimation
from functions import *

from consts import *
'''
    file is used for previewing what a certain function will look like on an (x,y,z) space
    animation allowed

'''


def main():
    n = points
    x = np.linspace(0,points-1, points)
    y = np.linspace(0,points-1,points)
    plot_3d(n,Z=func,a=x,b=y,var=0, ani=True,plot='scat')
    #plot_3d(n, ani=True,mode='bounce')
    
    


class func_animate():
    def __init__(self, save=False, animate=False, show=False):
        self.save = save
        self.animate = animate
        self.show = show

    def __str__(self):
        return f"{self.save}, {self.animate}, {self.show}"
    
    def set_func(self):
        """
        set the function of
        """
        pass


N=points
def plot_3d(n=points,Z=z_func, a=np.linspace(0, N-1, N), b=np.linspace(0, N-1, N),var=0,  ani=False, plot='mesh',mode='none' ):
    """
    this function will plot a predetermined function on a 3d-plane [z(x,y)]

    paramaters:
    n (int)    - the number of sample points to use for the plot (nxn)
    ani (bool) - allow animation of a certain type of sweep on the function
    plot (str) - how to plot the graph (only scatter plot and mesh at the moment) 
    mode (str) - how to animate the function (at this moment "none" does a horizontal sweep 
                 and "bounce" bounces the function )

    Z (function) - function to be mapped. the function MUST HAVE the parameters in 
                        Z(X,Y,var), *set mode="none', is an optional param used for 
                        animating but need to be able to properly run 
        X,Y -   np array
        var -   variable that will change with time
        mode -  a way for certain variables in your func to change with time and how 
                they will change by defining a different mode of changing.
    """
    #initialize the fig for plotting
    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')
    #plt.xlabel('X-axis')
    #plt.ylabel('Y-axis')
    #ax.set_label('Z-axis')

    #initalize the x and y coords with your predefined range on the mesh grid
    x = a
    y = b
    X, Y = np.meshgrid(x, y)

    #using your range plot the function
    z = Z(X, Y, 0,mode=mode)

    # min and max val of function for plotting limits
    ma = np.max(z)
    mi = np.min(z)
    
    if plot == 'scat':  #current plotting type support scat and surface
        X = X.ravel()
        Y = Y.ravel()    
        z = z.ravel()
        scat = ax.scatter(X,Y,z,c=z,cmap=color_map)
    else:       # surface plotting
        scat = ax.plot_surface(X,Y,z, cmap=color_map)

    # limits set by your input
    ax.set_xlim(0,n-1)
    ax.set_ylim(0,n-1)
    ax.set_zlim(mi,ma)
    
    if ani==False:
        plt.show()

    # animating a variable changing with time by updating frames
    else:
        def update(frame):
            ax.clear()
            z = Z(X,Y, frame*0.05, mode=mode)
            if plot == 'scat':
                scat = ax.scatter(X,Y,z,c=z,cmap=color_map)    #scatter plot
            else:
                scat = ax.plot_surface(X,Y,z, cmap=color_map)   #surface plot

            ax.set_zlim(mi,ma)
            return scat

        ani = FuncAnimation(fig,update,frames=frame_rate, interval=40,blit=False)
        #ani.save('C://Users//cardi//Documents//git-repo//hwe_dev//LED_cube//animations//sample.gif', writer='pillow', fps=30) #save the animation
        #plt.colorbar()
        plt.show()



if __name__ == '__main__':
    main()

