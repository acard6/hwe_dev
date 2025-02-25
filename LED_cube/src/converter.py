from functions import *
from consts import *
import numpy as np
'''
    for "snake" method of connecting wires switches direction every other row
    need to ensure that data is properly corrected so that it can be converted correctly.
    additional corrections while need to be made for the fact that x and y at each height
    will also differ

    TODO
    - convert the base case where z=0 and points snake
    - consider how the points will differ at different height and how to deal with them

'''


def gen_data(f=func, frames=frame_rate, n=points, var=0):
    '''
    using n*n matrix returns the output for a given function of f(x,y)
    note: planes are hard set to have (0,0) as the first point

    paramaters:
        f (function) - a function of 2 inputs to give one output, i.e. a 3d plotter 
        that returns an array of the heights
    
        X,Y     -   np array that define the nxn plane
        frames  -   number of frames to be generated for the animation
        n(int)  -   the size of the array as well as determining the upper bound 
        var     -   step size of how much each frame will variate in its function
                    (refer to src\functions.py for more info on var)

    returns:
        z       -   a 2d array witht the final z values per frame

    data format is as follows:
        data[frame][x][y]
            |-> frame - nth frame
            |-> x - x coordinate
            |-> y - y coordinate 

    '''
    data = np.empty(frames,dtype=object)
    x = np.linspace(0,n-1, n)
    y = np.linspace(0,n-1,n)
    X, Y = np.meshgrid(x,y)
    for i in range(frames):
        data[i] = f(X,Y,i*0.05)

    return data
    

def arr2int(data):
    #base case z = 0 regular snaking
    for frame in range(len(data)):
        state = np.zeros(512)
        for x in range(len(data[0])):
            for y in range(len(data[0][0])):
                z = data[frame][x][y]
                


    
def color_mapper(color_map):
    pass


def main():
    data = gen_data(func)
    # for i in range(frame_rate):
    #     print("{}:\n {}".format(i,data[i]))
    print(data[120])

    #color_mapper(color_map)

if __name__ == '__main__':
    main()