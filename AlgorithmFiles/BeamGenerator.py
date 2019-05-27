# import matplotlib.pyplot as plt
import numpy as np


def beamGen(eleNum):#Return an Array
    beamCode=np.zeros((eleNum,3),dtype=np.int)
    for i in range(len(beamCode)):#generating sequence of beams
        beamCode[i,2]=i
#x axis-----------------------------------------------
    x=0#start generating x coordinates
    for row in range(int(np.sqrt(eleNum))+1):
        if x<int(np.sqrt(eleNum)):
            beamCode[row,0]=x
            x=x+1
        else:
            x=0
            beamCode[row,0]=x
            x=x+1
    y=0#start generating y coordinates
    counter=0
    for row in range(int(np.sqrt(eleNum))-1):
        if counter<int(np.sqrt(eleNum)):
            beamCode[row,1]=y
            counter=counter+1
        else:
            counter=1
            y=y+1
            beamCode[row,1]=y

#about the vertical axis----------------------------------------------
    x=0#start generating x coordinates
    for row in range(int(np.sqrt(eleNum)),eleNum):
        if x<int(np.sqrt(eleNum)):
            beamCode[row,0]=x
            x=x+1
        else:
            x=0
            beamCode[row,0]=x
            x=x+1
    y=0#start generating y coordinates
    counter=0
    for row in range(int(np.sqrt(eleNum)-1),eleNum):
        if counter<int(np.sqrt(eleNum)):
            beamCode[row,1]=y
            counter=counter+1
        else:
            counter=1
            y=y+1
            beamCode[row,1]=y
    return beamCode

if __name__=="__main__":
    beamcode=beamGen(25)
    print beamcode#test for 200 elements
    # fig=plt.figure(figsize=(6,6),dpi=100)
    # plt.axis([0,30,0,30])
    # x=[]
    # y=[]
    # for i in range(100):
    #     x.append(beamcode[i,1])
    #     y.append(beamcode[i,2])
    #     plt.plot(x,y,marker='.')
    #     plt.plot(y,x,marker='.')
    # plt.show()


#plt.plot(x,y,'.-')
#plt.show()