from functions import *
from consts import *
import numpy as np
import sys
from map import data_map as hash_map
'''
    for "snake" method of connecting wires switches direction every other row
    need to ensure that data is properly corrected so that it can be converted correctly.
    additional corrections while need to be made for the fact that x and y at each height
    will also differ

    TODO
    - convert the base case where z=0 and points snake
    - consider how the points will differ at different height and how to deal with them

'''


def gen_data(f=func, n=points, frames=frame_rate, rate=0.04):
    '''
    using n*n matrix returns the output for a given function of f(x,y)
    note: planes are hard set to have (0,0) as the first point

    paramaters:
        f (function) - a function of 2 inputs to give one output, i.e. a 3d plotter 
        that returns an array of the heights
    
        X,Y     -   np array that define the nxn plane
        n(int)  -   the size of the array as well as determining the upper bound 
        frames  -   number of frames to be generated for the animation
        rate    -   the time interval between frames in seconds(default is 40 milliseconds)
    NOTE: (frames x rate) will give you the total time of the 

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
        data[i] = f(X,Y,i*rate)

    return data
    

def arr2int(data):
    #base case z = 0 regular snaking
    l = len(data)
    data_frame = np.zeros(shape=(l,points*points),dtype=np.uint16)  #2d array containing frames where each frame contains the idx of the values to turn on
    for frame in range(l):
        for x in range(len(data[0])):                   # iterate through rows
            for y in range(len(data[0][0])):            # iterate through columns
                z = data[frame][x][y]
                idx = hash_map[x,y,z]     
                data_frame[frame][y+x*points] = idx   
    return data_frame


    
def color_mapper(color_map):
    pass


def main():
    data = gen_data(func, frames=60, rate=0.2)
    # for i in range(frame_rate):
    #     print("{}:\n {}".format(i,data[i]))
    print(data[0])
    int_frames = arr2int(data)
    print(int_frames[0])

    #color_mapper(color_map)

if __name__ == '__main__':
    main()