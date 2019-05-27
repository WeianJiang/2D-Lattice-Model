import NodecodeGenerator


def findRPIndex(x,y,length,RPCoordinate=[]):#where x y the coordinate and length the length of the model,retrun corresponding index
        for number in range(len(RPCoordinate)):
                if x==RPCoordinate[number][0] and y==RPCoordinate[number][1]:
                        return RPCoordinate[number][2]

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