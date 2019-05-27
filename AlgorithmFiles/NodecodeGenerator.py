import numpy as np


def nodeCodeGen(nodeNum):
    n = int(np.sqrt(nodeNum))
    nodeCode=[]
    for ordin_x in range(n):#note that the vertical beams is generated first, due to using call function in main.py
        for ordin_y in range(n+1):
            nodeCode.append([ordin_y,ordin_x])
    for ordin_x in range(n):
        for ordin_y in range(n+1):
            nodeCode.append([ordin_x,ordin_y])
    for number in range(len(nodeCode)):
        nodeCode[number].append(number)
    return nodeCode

if __name__=='__main__':
    print nodeCodeGen(4)