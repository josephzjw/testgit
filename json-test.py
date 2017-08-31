# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 15:47:09 2017

@author: z81022682

blokus json processing
"""

import json
import numpy as np
import matplotlib.pyplot as plt

## myPlot(myCurrentChessState[:,:,step])
def myPlot(H):
    fig = plt.figure(figsize=(8, 4))

    ax = fig.add_subplot(111)
    ax.set_title('colorMap')
    plt.imshow(H)
    ax.set_aspect('equal')

    cax = fig.add_axes([0.12, 0.1, 0.78, 0.8])
    cax.get_xaxis().set_visible(False)
    cax.get_yaxis().set_visible(False)
    cax.patch.set_alpha(0)
    cax.set_frame_on(False)
    plt.colorbar(orientation='vertical')
    plt.show()


## myplt(label2axis(myAxisLabel[step]))
def myplt(data):
    numOfScatter = len(data)
    ix = []
    iy = []
    for i in range(numOfScatter):
        ix.append(data[i][0])
        iy.append(data[i][1])
    plt.scatter(iy,ix)
    plt.xlim([-5,24])
    plt.ylim([-5,24])
    plt.gca().invert_yaxis()

#print(os.path.isfile(fileName))
    


############################## map from axis to label #########################
def axis2label(axisList):
    myMap = []
    # 101: 400
    for i in range(20):
        for j in range(20):
            myMap.append([[i,j]])

# 201: 800
    for i in range(20):
        for j in range(20):
            myMap.append([[i,j],[i,j+1]])
            myMap.append([[i,j],[i+1,j]])
    
# 301: 800
    for i in range(20):
        for j in range(20):
            myMap.append([[i,j-1],[i,j],[i,j+1]])
            myMap.append([[i-1,j],[i,j],[i+1,j]])

# 302: 1600
    for i in range(20):
        for j in range(20):
            myMap.append([[i,j-1],[i,j],[i+1,j]])
            myMap.append([[i,j-1],[i,j],[i-1,j]])
            myMap.append([[i,j],[i-1,j],[i,j+1]])
            myMap.append([[i,j],[i+1,j],[i,j+1]])

# 401: 800
    for i in range(20):
        for j in range(20):
            myMap.append([[i,j-1],[i,j],[i,j+1],[i,j+2]])
            myMap.append([[i-1,j],[i,j],[i+1,j],[i+2,j]])

# 402: 4*400
    for i in range(20):
        for j in range(20):
            myMap.append([[i,j-1],[i,j],[i,j+1],[i+1,j]])
            myMap.append([[i-1,j],[i,j],[i+1,j],[i,j+1]])
            myMap.append([[i,j-1],[i,j],[i,j+1],[i-1,j]])
            myMap.append([[i,j-1],[i,j],[i-1,j],[i+1,j]])

# 403: 4*400
    for i in range(20):
        for j in range(20):
            myMap.append([[i,j],[i+1,j],[i,j+1],[i+1,j-1]])
            myMap.append([[i,j],[i,j-1],[i-1,j-1],[i+1,j]])
            myMap.append([[i,j],[i,j-1],[i+1,j],[i+1,j+1]])
            myMap.append([[i,j],[i-1,j],[i,j-1],[i+1,j-1]])
        
# 404: 8*400
    for i in range(20):
        for j in range(20):
            myMap.append([[i,j],[i,j-1],[i,j+1],[i-1,j+1]])
            myMap.append([[i,j],[i-1,j],[i+1,j],[i+1,j+1]])
            myMap.append([[i,j],[i,j-1],[i+1,j-1],[i,j+1]])
            myMap.append([[i,j],[i-1,j],[i+1,j],[i-1,j-1]])
            myMap.append([[i,j],[i,j-1],[i-1,j-1],[i,j+1]])
            myMap.append([[i,j],[i+1,j],[i-1,j],[i-1,j+1]])
            myMap.append([[i,j],[i,j-1],[i,j+1],[i+1,j+1]])
            myMap.append([[i,j],[i-1,j],[i+1,j],[i+1,j-1]])

# 405: 1
    for i in range(20):
        for j in range(20):
            myMap.append([[i,j],[i,j+1],[i+1,j],[i+1,j+1]])
        
        
# 501: 2*400
    for i in range(20):
        for j in range(20):
            myMap.append([[i,j],[i,j-1],[i,j-2],[i,j+1],[i,j+2]])
            myMap.append([[i,j],[i-1,j],[i-2,j],[i+1,j],[i+2,j]])

# 502: 4
    for i in range(20):
        for j in range(20):
            myMap.append([[i,j],[i-1,j],[i-2,j],[i,j-1],[i,j+1]])
            myMap.append([[i,j],[i,j+1],[i,j+2],[i-1,j],[i+1,j]])
            myMap.append([[i,j],[i+1,j],[i+2,j],[i,j-1],[i,j+1]])
            myMap.append([[i,j],[i,j-1],[i,j-2],[i-1,j],[i+1,j]])

# 503: 1
    for i in range(20):
        for j in range(20):
            myMap.append([[i,j],[i,j-1],[i,j+1],[i-1,j],[i+1,j]])

## 504: 4
    for i in range(20):
        for j in range(20):
            myMap.append([[i,j],[i,j+1],[i,j+2],[i-1,j],[i-2,j]])
            myMap.append([[i,j],[i+1,j],[i+2,j],[i,j+1],[i,j+2]])
            myMap.append([[i,j],[i,j-1],[i,j-2],[i+1,j],[i+2,j]])
            myMap.append([[i,j],[i,j-1],[i,j-2],[i-1,j],[i-2,j]])
        
## 505: 4
    for i in range(20):
        for j in range(20):
            myMap.append([[i,j],[i,j-1],[i+1,j-1],[i-1,j],[i-1,j+1]])
            myMap.append([[i,j],[i-1,j],[i-1,j-1],[i,j+1],[i+1,j+1]])
            myMap.append([[i,j],[i+1,j],[i+1,j-1],[i,j+1],[i-1,j+1]])
            myMap.append([[i,j],[i,j-1],[i-1,j-1],[i+1,j],[i+1,j+1]])
        

## 506: 8
    for i in range(20):
        for j in range(20):
            myMap.append([[i,j],[i-1,j],[i+1,j],[i,j+1],[i+1,j+1]])
            myMap.append([[i,j],[i,j-1],[i,j+1],[i+1,j-1],[i+1,j]])
            myMap.append([[i,j],[i-1,j],[i-1,j-1],[i,j-1],[i+1,j]])
            myMap.append([[i,j],[i,j-1],[i,j+1],[i-1,j],[i-1,j+1]])
            myMap.append([[i,j],[i-1,j],[i+1,j],[i,j-1],[i+1,j-1]])
            myMap.append([[i,j],[i,j-1],[i,j+1],[i-1,j],[i-1,j-1]])
            myMap.append([[i,j],[i-1,j],[i+1,j],[i,j+1],[i-1,j+1]])
            myMap.append([[i,j],[i,j-1],[i,j+1],[i+1,j],[i+1,j+1]])

## 507: 8
    for i in range(20):
        for j in range(20):
            myMap.append([[i,j],[i,j-1],[i,j+1],[i,j+2],[i-1,j]])
            myMap.append([[i,j],[i-1,j],[i+1,j],[i+2,j],[i,j+1]])
            myMap.append([[i,j],[i,j-1],[i,j-2],[i,j+1],[i+1,j]])
            myMap.append([[i,j],[i+1,j],[i-1,j],[i-2,j],[i,j-1]])
            myMap.append([[i,j],[i,j-1],[i,j-2],[i-1,j],[i,j+1]])
            myMap.append([[i,j],[i+1,j],[i-1,j],[i-2,j],[i,j+1]])
            myMap.append([[i,j],[i,j-1],[i,j+1],[i,j+2],[i+1,j]])
            myMap.append([[i,j],[i,j-1],[i-1,j],[i+1,j],[i+2,j]])

## 508: 8
    for i in range(20):
        for j in range(20):
            myMap.append([[i,j],[i-1,j],[i,j+1],[i,j+2],[i,j+3]])
            myMap.append([[i,j],[i,j+1],[i+1,j],[i+2,j],[i+3,j]])
            myMap.append([[i,j],[i+1,j],[i,j-1],[i,j-2],[i,j-3]])
            myMap.append([[i,j],[i,j-1],[i-1,j],[i-2,j],[i-3,j]])
            myMap.append([[i,j],[i-1,j],[i,j-1],[i,j-2],[i,j-3]])
            myMap.append([[i,j],[i,j+1],[i-1,j],[i-2,j],[i-3,j]])
            myMap.append([[i,j],[i+1,j],[i,j+1],[i,j+2],[i,j+3]])
            myMap.append([[i,j],[i,j-1],[i+1,j],[i+2,j],[i+3,j]])

## 509: 4
    for i in range(20):
        for j in range(20):
            myMap.append([[i,j],[i+1,j],[i-1,j],[i-1,j+1],[i+1,j+1]])
            myMap.append([[i,j],[i,j-1],[i,j+1],[i+1,j-1],[i+1,j+1]])
            myMap.append([[i,j],[i-1,j],[i+1,j],[i-1,j-1],[i+1,j-1]])
            myMap.append([[i,j],[i,j-1],[i,j+1],[i-1,j-1],[i-1,j+1]])


## 510: 8
    for i in range(20):
        for j in range(20):
            myMap.append([[i,j],[i+1,j],[i+1,j-1],[i,j+1],[i,j+2]])
            myMap.append([[i,j],[i,j-1],[i-1,j-1],[i+1,j],[i+2,j]])
            myMap.append([[i,j],[i,j-1],[i,j-2],[i-1,j],[i-1,j+1]])
            myMap.append([[i,j],[i,j+1],[i+1,j+1],[i-1,j],[i-2,j]])
            myMap.append([[i,j],[i,j-1],[i,j-2],[i+1,j],[i+1,j+1]])
            myMap.append([[i,j],[i,j-1],[i+1,j-1],[i-1,j],[i-2,j]])
            myMap.append([[i,j],[i,j+1],[i,j+2],[i-1,j],[i-1,j-1]])
            myMap.append([[i,j],[i+1,j],[i+2,j],[i,j+1],[i-1,j+1]])

## 511: 4
    for i in range(20):
        for j in range(20):
            myMap.append([[i,j],[i,j-1],[i,j+1],[i+1,j-1],[i-1,j+1]])
            myMap.append([[i,j],[i-1,j],[i+1,j],[i-1,j-1],[i+1,j+1]])
            myMap.append([[i,j],[i,j-1],[i,j+1],[i-1,j-1],[i+1,j+1]])
            myMap.append([[i,j],[i+1,j],[i-1,j],[i+1,j-1],[i-1,j+1]])

## 512: 8
    for i in range(20):
        for j in range(20):
            myMap.append([[i,j],[i,j-1],[i+1,j],[i-1,j],[i-1,j+1]])
            myMap.append([[i,j],[i,j-1],[i,j+1],[i-1,j],[i+1,j+1]])
            myMap.append([[i,j],[i+1,j],[i-1,j],[i,j+1],[i+1,j-1]])
            myMap.append([[i,j],[i,j-1],[i,j+1],[i+1,j],[i-1,j-1]])
            myMap.append([[i,j],[i,j+1],[i+1,j],[i-1,j],[i-1,j-1]])
            myMap.append([[i,j],[i,j-1],[i,j+1],[i+1,j],[i-1,j+1]])
            myMap.append([[i,j],[i+1,j],[i-1,j],[i,j-1],[i+1,j+1]])
            myMap.append([[i,j],[i,j-1],[i,j+1],[i-1,j],[i+1,j-1]])
            
    myMapSorted = []
    for i in range(36400):
        myMapSorted.append(sorted(myMap[i]))

    return myMapSorted.index(axisList)

##### map from axis to label end   ###########################################
##############################################################################


##################################################################
########   map from label to axis ################################
def label2axis(mylabel):
    myMap = []
    for i in range(20):
        for j in range(20):
            myMap.append([[i,j]])

# 201: 800
    for i in range(20):
        for j in range(20):
            myMap.append([[i,j],[i,j+1]])
            myMap.append([[i,j],[i+1,j]])
    
# 301: 800
    for i in range(20):
        for j in range(20):
            myMap.append([[i,j-1],[i,j],[i,j+1]])
            myMap.append([[i-1,j],[i,j],[i+1,j]])

# 302: 1600
    for i in range(20):
        for j in range(20):
            myMap.append([[i,j-1],[i,j],[i+1,j]])
            myMap.append([[i,j-1],[i,j],[i-1,j]])
            myMap.append([[i,j],[i-1,j],[i,j+1]])
            myMap.append([[i,j],[i+1,j],[i,j+1]])

# 401: 800
    for i in range(20):
        for j in range(20):
            myMap.append([[i,j-1],[i,j],[i,j+1],[i,j+2]])
            myMap.append([[i-1,j],[i,j],[i+1,j],[i+2,j]])

# 402: 4*400
    for i in range(20):
        for j in range(20):
            myMap.append([[i,j-1],[i,j],[i,j+1],[i+1,j]])
            myMap.append([[i-1,j],[i,j],[i+1,j],[i,j+1]])
            myMap.append([[i,j-1],[i,j],[i,j+1],[i-1,j]])
            myMap.append([[i,j-1],[i,j],[i-1,j],[i+1,j]])

# 403: 4*400
    for i in range(20):
        for j in range(20):
            myMap.append([[i,j],[i+1,j],[i,j+1],[i+1,j-1]])
            myMap.append([[i,j],[i,j-1],[i-1,j-1],[i+1,j]])
            myMap.append([[i,j],[i,j-1],[i+1,j],[i+1,j+1]])
            myMap.append([[i,j],[i-1,j],[i,j-1],[i+1,j-1]])
        
# 404: 8*400
    for i in range(20):
        for j in range(20):
            myMap.append([[i,j],[i,j-1],[i,j+1],[i-1,j+1]])
            myMap.append([[i,j],[i-1,j],[i+1,j],[i+1,j+1]])
            myMap.append([[i,j],[i,j-1],[i+1,j-1],[i,j+1]])
            myMap.append([[i,j],[i-1,j],[i+1,j],[i-1,j-1]])
            myMap.append([[i,j],[i,j-1],[i-1,j-1],[i,j+1]])
            myMap.append([[i,j],[i+1,j],[i-1,j],[i-1,j+1]])
            myMap.append([[i,j],[i,j-1],[i,j+1],[i+1,j+1]])
            myMap.append([[i,j],[i-1,j],[i+1,j],[i+1,j-1]])

# 405: 1
    for i in range(20):
        for j in range(20):
            myMap.append([[i,j],[i,j+1],[i+1,j],[i+1,j+1]])
        
        
# 501: 2*400
    for i in range(20):
        for j in range(20):
            myMap.append([[i,j],[i,j-1],[i,j-2],[i,j+1],[i,j+2]])
            myMap.append([[i,j],[i-1,j],[i-2,j],[i+1,j],[i+2,j]])

# 502: 4
    for i in range(20):
        for j in range(20):
            myMap.append([[i,j],[i-1,j],[i-2,j],[i,j-1],[i,j+1]])
            myMap.append([[i,j],[i,j+1],[i,j+2],[i-1,j],[i+1,j]])
            myMap.append([[i,j],[i+1,j],[i+2,j],[i,j-1],[i,j+1]])
            myMap.append([[i,j],[i,j-1],[i,j-2],[i-1,j],[i+1,j]])

# 503: 1
    for i in range(20):
        for j in range(20):
            myMap.append([[i,j],[i,j-1],[i,j+1],[i-1,j],[i+1,j]])

## 504: 4
    for i in range(20):
        for j in range(20):
            myMap.append([[i,j],[i,j+1],[i,j+2],[i-1,j],[i-2,j]])
            myMap.append([[i,j],[i+1,j],[i+2,j],[i,j+1],[i,j+2]])
            myMap.append([[i,j],[i,j-1],[i,j-2],[i+1,j],[i+2,j]])
            myMap.append([[i,j],[i,j-1],[i,j-2],[i-1,j],[i-2,j]])
        
## 505: 4
    for i in range(20):
        for j in range(20):
            myMap.append([[i,j],[i,j-1],[i+1,j-1],[i-1,j],[i-1,j+1]])
            myMap.append([[i,j],[i-1,j],[i-1,j-1],[i,j+1],[i+1,j+1]])
            myMap.append([[i,j],[i+1,j],[i+1,j-1],[i,j+1],[i-1,j+1]])
            myMap.append([[i,j],[i,j-1],[i-1,j-1],[i+1,j],[i+1,j+1]])
        

## 506: 8
    for i in range(20):
        for j in range(20):
            myMap.append([[i,j],[i-1,j],[i+1,j],[i,j+1],[i+1,j+1]])
            myMap.append([[i,j],[i,j-1],[i,j+1],[i+1,j-1],[i+1,j]])
            myMap.append([[i,j],[i-1,j],[i-1,j-1],[i,j-1],[i+1,j]])
            myMap.append([[i,j],[i,j-1],[i,j+1],[i-1,j],[i-1,j+1]])
            myMap.append([[i,j],[i-1,j],[i+1,j],[i,j-1],[i+1,j-1]])
            myMap.append([[i,j],[i,j-1],[i,j+1],[i-1,j],[i-1,j-1]])
            myMap.append([[i,j],[i-1,j],[i+1,j],[i,j+1],[i-1,j+1]])
            myMap.append([[i,j],[i,j-1],[i,j+1],[i+1,j],[i+1,j+1]])

## 507: 8
    for i in range(20):
        for j in range(20):
            myMap.append([[i,j],[i,j-1],[i,j+1],[i,j+2],[i-1,j]])
            myMap.append([[i,j],[i-1,j],[i+1,j],[i+2,j],[i,j+1]])
            myMap.append([[i,j],[i,j-1],[i,j-2],[i,j+1],[i+1,j]])
            myMap.append([[i,j],[i+1,j],[i-1,j],[i-2,j],[i,j-1]])
            myMap.append([[i,j],[i,j-1],[i,j-2],[i-1,j],[i,j+1]])
            myMap.append([[i,j],[i+1,j],[i-1,j],[i-2,j],[i,j+1]])
            myMap.append([[i,j],[i,j-1],[i,j+1],[i,j+2],[i+1,j]])
            myMap.append([[i,j],[i,j-1],[i-1,j],[i+1,j],[i+2,j]])

## 508: 8
    for i in range(20):
        for j in range(20):
            myMap.append([[i,j],[i-1,j],[i,j+1],[i,j+2],[i,j+3]])
            myMap.append([[i,j],[i,j+1],[i-1,j],[i-2,j],[i-3,j]])
            myMap.append([[i,j],[i+1,j],[i,j-1],[i,j-2],[i,j-3]])
            myMap.append([[i,j],[i,j-1],[i-1,j],[i-2,j],[i-3,j]])
            myMap.append([[i,j],[i-1,j],[i,j-1],[i,j-2],[i,j-3]])
            myMap.append([[i,j],[i,j+1],[i-1,j],[i-2,j],[i-3,j]])
            myMap.append([[i,j],[i+1,j],[i,j+1],[i,j+2],[i,j+3]])
            myMap.append([[i,j],[i,j-1],[i+1,j],[i+2,j],[i+3,j]])

## 509: 4
    for i in range(20):
        for j in range(20):
            myMap.append([[i,j],[i+1,j],[i-1,j],[i-1,j+1],[i+1,j+1]])
            myMap.append([[i,j],[i,j-1],[i,j+1],[i+1,j-1],[i+1,j+1]])
            myMap.append([[i,j],[i-1,j],[i+1,j],[i-1,j-1],[i+1,j-1]])
            myMap.append([[i,j],[i,j-1],[i,j+1],[i-1,j-1],[i-1,j+1]])


## 510: 8
    for i in range(20):
        for j in range(20):
            myMap.append([[i,j],[i+1,j],[i+1,j-1],[i,j+1],[i,j+2]])
            myMap.append([[i,j],[i,j-1],[i-1,j-1],[i+1,j],[i+2,j]])
            myMap.append([[i,j],[i,j-1],[i,j-2],[i-1,j],[i-1,j+1]])
            myMap.append([[i,j],[i,j+1],[i+1,j+1],[i-1,j],[i-2,j]])
            myMap.append([[i,j],[i,j-1],[i,j-2],[i+1,j],[i+1,j+1]])
            myMap.append([[i,j],[i,j-1],[i+1,j-1],[i-1,j],[i-2,j]])
            myMap.append([[i,j],[i,j+1],[i,j+2],[i-1,j],[i-1,j-1]])
            myMap.append([[i,j],[i+1,j],[i+2,j],[i,j+1],[i-1,j+1]])

## 511: 4
    for i in range(20):
        for j in range(20):
            myMap.append([[i,j],[i,j-1],[i,j+1],[i+1,j-1],[i-1,j+1]])
            myMap.append([[i,j],[i-1,j],[i+1,j],[i-1,j-1],[i+1,j+1]])
            myMap.append([[i,j],[i,j-1],[i,j+1],[i-1,j-1],[i+1,j+1]])
            myMap.append([[i,j],[i+1,j],[i-1,j],[i+1,j-1],[i-1,j+1]])

## 512: 8
    for i in range(20):
        for j in range(20):
            myMap.append([[i,j],[i,j-1],[i+1,j],[i-1,j],[i-1,j+1]])
            myMap.append([[i,j],[i,j-1],[i,j+1],[i-1,j],[i+1,j+1]])
            myMap.append([[i,j],[i+1,j],[i-1,j],[i,j+1],[i+1,j-1]])
            myMap.append([[i,j],[i,j-1],[i,j+1],[i+1,j],[i-1,j-1]])
            myMap.append([[i,j],[i,j+1],[i+1,j],[i-1,j],[i-1,j-1]])
            myMap.append([[i,j],[i,j-1],[i,j+1],[i+1,j],[i-1,j+1]])
            myMap.append([[i,j],[i+1,j],[i-1,j],[i,j-1],[i+1,j+1]])
            myMap.append([[i,j],[i,j-1],[i,j+1],[i-1,j],[i+1,j-1]])
    
    myMapSorted = []
    for i in range(36400):
        myMapSorted.append(sorted(myMap[i]))
    return myMapSorted[mylabel]

##### map from label to axis end ##############################################
###############################################################################      

## usage: myplt2(myCurrentChessState[:,:,1],myAxisLabel[3])
def myplt2(chessState,label):
    chessIndex = np.argwhere(chessState)
    labelAxis = label2axis(label)
    ix = []
    iy = []
    for i in range(len(chessIndex)):
        ix.append(chessIndex[i][0])
        iy.append(chessIndex[i][1])
        
    for i in range(len(labelAxis)):
        ix.append(labelAxis[i][0])
        iy.append(labelAxis[i][1])
        
    plt.scatter(iy,ix)
    plt.xlim([0,19])
    plt.ylim([0,19])
    plt.gca().invert_yaxis()

myChessBoard = np.zeros((20,20,5),dtype=np.int)

#with open('20170828_141406.txt','r') as f:
#    execfile(f)

with open('20170828_141406.txt', 'r') as f:
     mydata = f.read()
     mydata_new = mydata[10:-1]
#    data = json.load(f)

data = json.loads(mydata_new)

numOfHand = len(data)-2 # the total steps of the chess game

myCurrentChessBoard = np.zeros((20,20,5,numOfHand),dtype=np.int) # where to put the current squareness

##### myCurrentChessState: qi pan zhuang tai
myCurrentChessState = np.zeros((20,20,numOfHand+1),dtype=np.int) # what does the current chessboard look like
myFriendEnemyState = np.zeros((20,20,4,numOfHand),dtype=np.int) # 0:null,1:me,

######## every step output
myAxisLabel = []
#my_data = json.load(open("20170828_141406.txt").read())

numOfCause = 0

for i in range(numOfHand): # the i-th hand
    if i != 0:
        myCurrentChessState[:,:,i+1] = myCurrentChessState[:,:,i]
        
    if data[i+1]['msg_data']['player_id'] == 1:
        [ix,iy] = np.where(myCurrentChessState[:,:,i]==1) # wofang
        myFriendEnemyState[ix,iy,1,i] = 1
        [ix,iy] = np.where(myCurrentChessState[:,:,i]==2) # difang
        myFriendEnemyState[ix,iy,3,i] = 1
        [ix,iy] = np.where(myCurrentChessState[:,:,i]==4) # difang
        myFriendEnemyState[ix,iy,3,i] = 1
        [ix,iy] = np.where(myCurrentChessState[:,:,i]==3) # youfang
        myFriendEnemyState[ix,iy,2,i] = 1
    elif data[i+1]['msg_data']['player_id'] == 2:
        [ix,iy] = np.where(myCurrentChessState[:,:,i]==2) # wofang
        myFriendEnemyState[ix,iy,1,i] = 1
        [ix,iy] = np.where(myCurrentChessState[:,:,i]==3) # difang
        myFriendEnemyState[ix,iy,3,i] = 1
        [ix,iy] = np.where(myCurrentChessState[:,:,i]==1) # difang
        myFriendEnemyState[ix,iy,3,i] = 1
        [ix,iy] = np.where(myCurrentChessState[:,:,i]==4) # youfang
        myFriendEnemyState[ix,iy,2,i] = 1
    elif data[i+1]['msg_data']['player_id'] == 3:
        [ix,iy] = np.where(myCurrentChessState[:,:,i]==3) # wofang
        myFriendEnemyState[ix,iy,1,i] = 1
        [ix,iy] = np.where(myCurrentChessState[:,:,i]==4) # difang
        myFriendEnemyState[ix,iy,3,i] = 1
        [ix,iy] = np.where(myCurrentChessState[:,:,i]==2) # difang
        myFriendEnemyState[ix,iy,3,i] = 1
        [ix,iy] = np.where(myCurrentChessState[:,:,i]==1) # youfang
        myFriendEnemyState[ix,iy,2,i] = 1
    elif data[i+1]['msg_data']['player_id'] == 4:
        [ix,iy] = np.where(myCurrentChessState[:,:,i]==4) # wofang
        myFriendEnemyState[ix,iy,1,i] = 1
        [ix,iy] = np.where(myCurrentChessState[:,:,i]==1) # difang
        myFriendEnemyState[ix,iy,3,i] = 1
        [ix,iy] = np.where(myCurrentChessState[:,:,i]==3) # difang
        myFriendEnemyState[ix,iy,3,i] = 1
        [ix,iy] = np.where(myCurrentChessState[:,:,i]==2) # youfang
        myFriendEnemyState[ix,iy,2,i] = 1
        
                
    if bool(data[i+1]['msg_data']['chessman'].get('squareness')): # this player can play
        numOfSquareness = len(data[i+1]['msg_data']['chessman']['squareness'])
        myTmpAxis = []
        if numOfSquareness >1:
            for j in range(numOfSquareness):
                xid = data[i+1]['msg_data']['chessman']['squareness'][j]['x'] # x_axis
                yid = data[i+1]['msg_data']['chessman']['squareness'][j]['y'] # y_axis
                zid = data[i+1]['msg_data']['player_id'] # player_id
                myCurrentChessBoard[xid,yid,zid,i]=1
                myCurrentChessState[xid,yid,i+1] = zid
                myTmpAxis.append([xid,yid])
        else:
            myTmpAxis = [[data[i+1]['msg_data']['chessman']['squareness'][0]['x'],data[i+1]['msg_data']['chessman']['squareness'][0]['y']]]
        myTmpAxisSorted = sorted(myTmpAxis)
        myAxisLabel.append(axis2label(myTmpAxisSorted))
    else:
        myAxisLabel.append(-1)

#np.save("step-label",myAxisLabel)
#
#stepLabel = np.load("step-label.npy")


### test the array show
#for i in range(len(stepLabel)):
#    fig = plt.figure(figsize=(8, 4))
#    myplt(label2axis(stepLabel[i]))
#    plt.title("%d"%i)
#    plt.show()

# classify kongbai, wofang, youfang, difang
    
# myPlot(myCurrentChessState[:,:,0])
#H = myTotalChessBoard[:,:,1,0] # added some commas and array creation code
#myPlot(myCurrentChessBoard[:,:,1,0])

#for i in range(numOfHand):
#    myPlot(myCurrentChessState[:,:,i])


