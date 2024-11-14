import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

def main():
    n = 16
    x = np.linspace(0,15, n)
    y = np.linspace(0,15,n)
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



def func(X,Y,var,mode="none"):
    """
    function used to test out passing functions into my plotter
    """
    #return (np.power(X-1+var,2)+np.power(Y,2))/10-1
    k = np.pi/112.5
    l = 7.5
    A = 8
    return np.round(A*np.cos(np.power(X-l,2)*k+np.power(Y-l,2)*k+var)+8)

def z_func(X, Y, var, mode='none'):
    """
    Default plotted function used by my animated/plotter to show its capabilities
    """
    #l = 7.5 # horizontal shift(where it will be centered around)
    l = np.pi/2
    k = (np.pi/8)             # period -> T=2*pi/k
    h = 8
    A = 8
    if mode == 'bounce':
        A = A*np.cos(var)    # amplitude    
        #A = np.pow(var,1/3)
        #A = np.power(var-8,2)/32-1
        #A = 2.1*np.exp(-np.pow(var-2.5,2)/1.4)-1.06
    else:
        l += var
    #z = cos(A)*sin(kx+l)*sin(ky+l)
    return np.round(A*np.sin(k*X+l)*np.sin(k*Y+l)+h)

N=16
def plot_3d(n=16,Z=z_func, a=np.linspace(0, N-1, N), b=np.linspace(0, N-1, N),var=0,  ani=False, plot='mesh',mode='none' ):
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
        scat = ax.scatter(X,Y,z,c=z,cmap='viridis')
    else:       # surface plotting
        scat = ax.plot_surface(X,Y,z, cmap='viridis')

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
                scat = ax.scatter(X,Y,z,c=z,cmap='viridis')    #scatter plot
            else:
                scat = ax.plot_surface(X,Y,z, cmap='viridis')   #surface plot

            ax.set_zlim(mi,ma)
            return scat

        ani = FuncAnimation(fig,update,frames=125, interval=40,blit=False)
        #ani.save('animation.gif', writer='pillow', fps=30) #save the animation
        #plt.colorbar()
        plt.show()



def LED_count():
    k=200
    a = [0]*k
    
    a[1] = 1
    a[2] = 2
    a[3] = 3
    
    m = 2
    n = 2
    x = m*n
    while (x <= k):
        a[x] = m+n
        x = m*n
        if (m>n):
            n += 1
        else:
            m += 1
    #print(n," ", m)
        
    
    for i in range(k-4):
        if (a[i+4] == 0):
            a[i+4] = a[i+3]

    #print(a[63])
    #plt.plot(a)
    #plt.show()



if __name__ == '__main__':
    main()


'''
Accent, Accent_r, Blues, Blues_r, BrBG, BrBG_r, BuGn, BuGn_r, BuPu, BuPu_r, CMRmap, CMRmap_r, Dark2, Dark2_r,GnBu, GnBu_r, Grays,
Greens, Greens_r, Greys, Greys_r, OrRd, OrRd_r, Oranges, Oranges_r, PRGn, PRGn_r, Paired,Paired_r, Pastel1, Pastel1_r, Pastel2, Pastel2_r, 
PiYG, PiYG_r, PuBu, PuBuGn, PuBuGn_r, PuBu_r, PuOr, PuOr_r,PuRd, PuRd_r, Purples, Purples_r, RdBu, RdBu_r, RdGy, RdGy_r, RdPu, RdPu_r, 
RdYlBu, RdYlBu_r, RdYlGn, RdYlGn_r,Reds, Reds_r, Sray_ray, gray_r, grey, hot, hot_r, hsv, hsv_r, inferno, inferno_r, jet, jet_r, magma,
magma_r,nipy_spectral, nipy_spectral_r, ocean, ocean_r, pink, pink_r, plasma, plasma_r, prism, prism_r, rainbow, rainbow_r,seismic,
seismic_r, spring, spring_r, summer, summer_r, tab10, tab10_r, tab20, tab20_r, tab20b, tab20b_r, tab20c,tab20c_r, terrain, terrain_r,
turbo, turbo_r, twilight, twilight_r, twilight_shifted, twilight_shifted_r, viridis,viridis_r, winter, winter_r
'''