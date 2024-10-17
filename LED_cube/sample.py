from urllib.request import urlopen, Request
import pandas as pd


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


def main():
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

if __name__ == '__main__':
    main()