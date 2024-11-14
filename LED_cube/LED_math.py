import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

def main():
    n = 16
    x = np.linspace(0, 15, n)
    y = np.linspace(0,15,n)
    plot_3d(n,Z=z_func,a=x,b=y,var=0, ani=True,mode='none',plot='mesh')

def func(X,Y,var,mode="none"):
    return (np.power(X-8+var,2)+np.power(Y-8,2))/10-1

def z_func(X, Y, var, mode='none'):
    l = 7.5 # horizontal shift(where it will be centered around)
    k = (np.pi/8)             # period -> T=2*pi/k
    if mode == 'bounce':
        #A = np.cos(var)    # amplitude    
        #A = np.pow(var,1/3)
        #A = np.power(var-8,2)/32-1
        A = 2.1*np.exp(-np.pow(var-2.5,2)/1.4)-1.06
    else:
        A = 1
        l += var
    
    #z = cos(A)*sin(kx+l)*sin(ky+l)
    return (A*np.sin(k*X+l)*np.sin(k*Y+l))

N=16
def plot_3d(n=16,Z=z_func, a=np.linspace(0, N-1, N), b=np.linspace(0, N-1, N),var=0,  ani=False, plot='bounce',mode='none' ):
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
        X,Y - np array
        var - variable that will change with time
        mode - a way for different variables to be affected within your function  
    """
    #initialize the fig for plotting
    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')
    #plt.xlabel('X-axis')
    #plt.ylabel('Y-axis')
    #ax.set_label('Z-axis')

    x = a
    y = b
    X, Y = np.meshgrid(x, y)
    z = Z(X, Y, 0,mode=mode)

    ma = np.max(z)   # min and max val of function for plotting limits
    mi = np.min(z)
    
    if plot == 'scat':  #current plotting type support scat and surface
        X = X.ravel()
        Y = Y.ravel()    
        z = z.ravel()
        scat = ax.scatter(X,Y,z,c=z,cmap='viridis')
    else:       # surface plotting
        scat = ax.plot_surface(X,Y,z, cmap='viridis')

    ax.set_xlim(0,n-1)
    ax.set_ylim(0,n-1)
    ax.set_zlim(mi,ma)
    
    if ani==False:
        plt.show()
        return None
    
    else:
        def update(frame):
            ax.clear()
            z = Z(X,Y, frame*0.05, mode=mode)
            if plot == 'scat':
                scat = ax.scatter(X,Y,z,c=z,cmap='viridis')    #scatter plot
            else:
                scat = ax.plot_surface(X,Y,z, cmap='viridis')   #surface plot

            ax.set_zlim(-1,1)
            return scat

        ani = FuncAnimation(fig,update,frames=125, interval=40,blit=False)
        ani.save('animation.gif', writer='pillow', fps=30)
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