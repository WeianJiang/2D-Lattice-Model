import circleGenerator
import BeamGenerator
import numpy as np
import matplotlib.pyplot as plt


def pointDeterminator(pointInfo=[],circleInfo=[]):
    pointINcircle=[]
    pointNOTINcircle=[]
    for pointNum in range(len(pointInfo)):
        looptimes=0
        for circleNum in range(len(circleInfo)):
            if positionDeterminator(pointInfo[pointNum][0],pointInfo[pointNum][1],circleInfo[circleNum][0],circleInfo[circleNum][1],circleInfo[circleNum][2]):
                # print pointInfo[pointNum],circleInfo[circleNum]
                pass
            else:
                looptimes+=1
        if looptimes==len(circleInfo):
            pointNOTINcircle.append(pointInfo[pointNum])
        else:
            pointINcircle.append(pointInfo[pointNum])
    return pointNOTINcircle


def positionDeterminator(point_x,point_y,circle_x,circle_y,radi):#retrun False if point is NOT included in the circle, retrun True if included
    if radi**2>(point_x-circle_x)**2+(point_y-circle_y)**2:
        return True
    else:
        return False


if __name__=="__main__":
    # fig = plt.figure(figsize=(6, 6), dpi=100)
    # plt.axis([0, 50, 0, 50])
    # circleData = circleGenerator.circleGenerator(1, 3, 5)
    # beamData = BeamGenerator.beamGen(2601)
    beamData=BeamGenerator.beamGen(10)
    circleData=circleGenerator.circleGenerator(1,3,5)
    print pointDeterminator(beamData,circleData)
    # for i in range(len(circleData)):  # draw module
    # # "*" used for transfer three parameters in one
    #     circleGenerator.drawCircle(*circleData[i])
    # plt.show()