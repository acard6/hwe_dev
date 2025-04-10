import numpy as np
import matplotlib.pyplot as plt

def create_staircase(nums):
  while len(nums) != 0:
    step = 1
    subsets = []
    if len(nums) >= step:
      subsets.append(nums[0:step])
      nums = nums[step:]
      step += 1
    else:
      return False

  return subsets

def create_staircase2(nums):
  step = 1
  subsets = []
  while len(nums) != 0:
    if len(nums) >= step:
      subsets.append(nums[0:step])
      nums = nums[step:]
      step += 1
    else:
      return False
      
  return subsets

def testcase():
    nums1 = [1,2,3]
    nums2 = [1,2,3,4,5,6,7,8,9]
    C10 = create_staircase(nums1)
    C11 = create_staircase(nums2)
    print(C10,":\t", C11)
    C20 = create_staircase2(nums1)
    C21 = create_staircase2(nums2)
    print(C20,":\t", C21)

##################################################

def func(x,y):
    return (np.power(x,2)+np.power(y,2))/10

def plot(a,b,n,Z):
    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')
   
    #initalize the x and y coords with your predefined range on the mesh grid
    x = a
    y = b
    X, Y = np.meshgrid(x, y)

    #using your range plot the function
    z = Z(X, Y)

    # min and max val of function for plotting limits
    ma = np.max(z)
    mi = np.min(z)
    
    scat = ax.plot_surface(X,Y,z, cmap='viridis')

    # limits set by our input
    ax.set_xlim(0,n-1)
    ax.set_ylim(0,n-1)
    ax.set_zlim(mi,ma)
    plt.show()

##################################################

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



def main():
    '''    n = 16
    a = np.linspace(0, 15, n)
    b = np.linspace(0, 15, n)
    plot(a,b,n, Z=func)'''


    #converted an integer into a point in 3d space
    for i in range(512):
       z = i//64
       if (z%2 == 0):
          x = ((i //8)%8)
       else:
          x = 7- ((i //8)%8)
       temp = i%16
       if (temp >= 8):
          y = 15-temp
       else:
          y = temp
       print("({},{},{}):{},".format(x,y,z,i))
    
    pass

######################################################



if __name__=='__main__':
  main()