from urllib.request import urlopen, Request
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np

def readURL(URL):
    df = pd.read_html(URL,encoding='utf-8')
    # df[nth table][ith column][jth row]
    # df[0][0] -> x-coord column
    # df[0][1] -> char column
    # df[0][2] -> y-coord column
    ret = dict()
    rows = len(df[0][0])
    maxY = 0
    maxX = 0
    for i in range(1,rows):
            x = int(df[0][0][i])
            y = int(df[0][2][i])
            ret[(x,y)] = df[0][1][i]
            if (x > maxX):
                 maxX = x
            if (y > maxY):
                 maxY = y
    return ret, (maxX, maxY)

def URL_reader():
    #URL = "https://docs.google.com/document/u/0/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub?pli=1"
    URL = "https://docs.google.com/document/d/e/2PACX-1vShuWova56o7XS1S3LwEIzkYJA8pBQENja01DNnVDorDVXbWakDT4NioAScvP1OCX6eeKSqRyzUW_qJ/pub"
    data, maxval = readURL(URL)
    
    for j in range(maxval[1]+1,-1,-1):
        text = ""
        for i in range(maxval[0]+1):
            try:
                text += data[(i,j)]
            except KeyError:
                 text += " "
        print(text)


def read_data():
    data = [0, 40, 0, 54, 73, 76, 163, 177, 58,84, 61, 92, 140, 178, 231, 47, 84, 112, 104, 82, 181, 231, 64, 59, 53, 116, 84, 135, 158, 63, 84, 39, 65, 39, 219, 255, 78, 30, 31, 71, 95, 210, 164, 69, 40, 
             42, 69, 89, 170, 201, 69, 37, 80, 54, 45, 106, 163, 53, 21, 47, 46, 18, 167, 208, 32, 48, 37, 88, 79, 150, 199, 94, 50, 58, 137, 82, 134, 189, 58, 53, 34, 60, 69, 170, 174, 63, 48, 50, 82,
             78, 100, 179, 55, 61, 58, 78, 90, 125, 207, 90, 58, 118, 92, 58, 160, 203, 78, 22, 67, 119, 135, 149, 189, 98, 118, 144, 0, 52, 155, 154, 62, 77, 186, 50, 57, 137, 147, 26, 38, 46, 49, 53,
             73, 200, 38, 16, 45, 52, 38, 176, 173, 73, 0, 19, 57, 45, 165, 196, 44, 52, 48, 33, 74, 142, 174, 61, 36, 45, 49, 36, 106, 157, 0, 52, 36, 29, 65, 265, 197, 97, 42, 36, 57, 38, 170, 180 ]

    days = {'Sunday':[], 'Monday':[], 'Tuesday':[], 'Wednesday':[], 'Thursday':[], 'Friday':[], 'Saturday':[]}
    map = {1:'Sunday', 2:'Monday', 3:'Tuesday', 4:'Wednesday', 5:'Thursday', 6:'Friday', 0:'Saturday'}

    for i in range(1,len(data)):
        d = map[i%7]
        days[d].append(data[i])
              
    return days



def main():
    data_per_day = read_data()
    x = np.arange(0,25,1)
    for i in data_per_day:
        data = np.array(data_per_day[i])
        plt.plot(x,data, label=i)
    #plt.show()
    week_count = []
    for i in range(25):
         sum = 0
         for key in data_per_day:
              sum += data_per_day[key][i]
         week_count.append(sum)
    print(week_count)

if __name__ == '__main__':
    main()