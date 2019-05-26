import NodecodeGenerator


def findRPIndex(x,y,length):#where x y the coordinate and length the length of the model,retrun corresponding index
    eleNum=2*length*(length+1)
    nodeNum=length**2
    localRP=[]
    pointcode=NodecodeGenerator.nodeCodeGen(nodeNum)
    for number in range(len(pointcode)): 
            localRP.append([pointcode[number][0],pointcode[number][1]])
    for number in range(eleNum/2-length-1,eleNum/2): #generate reference point for the toppest row
            localRP.append([pointcode[number][0],pointcode[number][1]+1])
    i=0
    for number in range(len(localRP)):#generate referencepoint coordinate and its index
            localRP[number].append(3*eleNum+1+i)
            i+=1
    for number in range(len(localRP)):
        if x==localRP[number][0] and y==localRP[number][1]:
            return localRP[number][2]


if __name__=='__main__':
    print findRPIndex(0,1,3)