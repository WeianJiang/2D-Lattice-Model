import numpy as np


size=15

def drawCircle(centroid_x, centroid_y, radi,order):  # draw circles by given parameters, in which order is useless
    theta = np.arange(0, 2*np.pi, 0.01)
    x = centroid_x + radi * np.cos(theta)
    y = centroid_y + radi * np.sin(theta)
    plt.plot(x, y)


def boudaryDetect(x, y, r):  # Funtion used to detect whether the circle cross the boundry
    if x-r > 0 and y-r > 0 and x+r < size and y+r < size:
        return True


# Function to detect the position relatioship between two circles
def overlapDetect(x1, y1, r1, x2, y2, r2):
    distanceSquare = np.square(x1-x2)+np.square(y1-y2)
    if distanceSquare < (r1+r2)**2:
        return True  # return ture if overlap


def dataGen(minimumRadi,maximumRadi):  # generate parameters of circle
    centroid_x = np.random.rand()*size
    centroid_y = np.random.rand()*size
    radi = np.random.random_integers(minimumRadi, maximumRadi)+np.random.rand()
    if boudaryDetect(centroid_x, centroid_y, radi):
        return [centroid_x, centroid_y, radi]
    else:
        return dataGen(minimumRadi,maximumRadi)


def areaRatio(circleArray):
    area=0
    for i in range(len(circleArray)):
        area = 3.14*circleArray[i][2]**2 + area
    return area/2500


def overlapCounting(circleArray):
    count = 0
    for k in range(len(circleArray)):  # a checking module
        for j in range(k+1, len(circleArray)):
            if overlapDetect(circleArray[k][0], circleArray[k][1], circleArray[k][2], circleArray[j][0], circleArray[j][1], circleArray[j][2]):
                count += 1
                #print False
            else:
                pass
    return count


def circleGenerator(trialTimes,minimumRadi,maximumRadi,circleData=[]):
    if len(circleData)==0:
        circleData.append(dataGen(minimumRadi,maximumRadi))
    for number in range(trialTimes):
        newCircle = dataGen(minimumRadi,maximumRadi)
        looptimes = 0
        for i in range(len(circleData)):
            if overlapDetect(newCircle[0], newCircle[1], newCircle[2], circleData[i][0], circleData[i][1], circleData[i][2]):
                break
            looptimes += 1
        if looptimes == len(circleData):
            circleData.append(newCircle)
    for order in range(len(circleData)):
        circleData[order].append(order)
    return circleData


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    fig = plt.figure(figsize=(6, 6), dpi=100)
    plt.axis([0, size, 0, size])
    #print dataGen()
    circleData = circleGenerator(20,1,1)
    circleData = np.array(circleData)
    # with open('file.txt','w') as f:
    #     f.write(str(circleData))
    print circleData
    print len(circleData)
    #print overlapCounting(circleData)
    print areaRatio(circleData)
    for i in range(len(circleData)):  # draw module
        # "*" used for transfer three parameters in one
        drawCircle(*circleData[i])
    plt.show()

# plt.savefig("D:/tcount
