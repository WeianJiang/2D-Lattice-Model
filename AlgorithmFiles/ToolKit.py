import NodecodeGenerator


def findRPIndex(x,y,length):#where x y the coordinate and length the length of the model,retrun corresponding index
    eleNum=2*length*(length+1)
    nodeNum=length**2
    localRP=[]
    pointcode=NodecodeGenerator.nodeCodeGen(nodeNum)
    for number in range(eleNum/2): 
            localRP.append([pointcode[number][0],pointcode[number][1]])
    for number in range(eleNum/2-length-1,eleNum/2): #generate reference point for the toppest row
            localRP.append([pointcode[number][0],pointcode[number][1]+1])
    i=0
    for number in range(len(localRP)):#generate referencepoint coordinate and its index
                if 3*eleNum+1+i==1000:
                        localRP[number].append(3*eleNum+1+1+i)
                        i+=1
                else:
                        localRP[number].append(3*eleNum+1+i)
                        i+=1
    for number in range(len(localRP)):
        if x==localRP[number][0] and y==localRP[number][1]:
            return localRP[number][2]

def findLeftInstance(x,y,length,pointcode=[]):#input the coordinate and return the left instance (part number) of the point
        if x-1<0:
                return -1
        else:
                for i in range(len(pointcode)/2,len(pointcode)):
                        if x-1==pointcode[i][0] and y==pointcode[i][1]:
                                return pointcode[i][2]


def findRightInstance(x,y,length,pointcode=[]):#input the coordinate and return the left instance (part number) of the point
        if x+1>length:
                return -1
        else:
                for i in range(len(pointcode)/2,len(pointcode)):
                        if x==pointcode[i][0] and y==pointcode[i][1]:
                                return pointcode[i][2]


def findUpInstance(x,y,length,pointcode=[]):#input the coordinate and return the left instance (part number) of the point
        if y+1>length:
                return -1
        else:
                for i in range(len(pointcode)/2):#since the vertical beams is in the range of 0~1/2
                        if x==pointcode[i][0] and y==pointcode[i][1]:
                                return pointcode[i][2]


def findDownInstance(x,y,length,pointcode=[]):#input the coordinate and return the left instance (part number) of the point
        if y-1<0:
                return -1
        else:
                for i in range(len(pointcode)/2):
                        if x==pointcode[i][0] and y-1==pointcode[i][1]:
                                return pointcode[i][2]


def findToppestNode(length,pointcode=[]):
        topPointRPIndex=[]
        for i in range(len(pointcode)/2):
                if pointcode[i][1]==length-1:
                        RPIndex=findRPIndex(pointcode[i][0],pointcode[i][1]+1,length)
                        topPointRPIndex.append(RPIndex)
        return topPointRPIndex


def findLowestNode(length,pointcode=[]):
        lowPointRPIndex=[]
        for i in range(len(pointcode)/2):
                if pointcode[i][1]==0:
                        RPIndex=findRPIndex(pointcode[i][0],pointcode[i][1],length)
                        lowPointRPIndex.append(RPIndex)
        return lowPointRPIndex




if __name__=='__main__':
    print findRPIndex(0,0,20)