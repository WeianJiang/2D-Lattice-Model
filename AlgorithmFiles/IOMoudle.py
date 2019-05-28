import numpy as np
import circleGenerator


# def outPutData(circleInfo=[]):
#         CurrentTime=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
#         with open(str(CurrentTime)+'.txt','w') as fwrite:
#                 fwrite.write(str(circleInfo))
#         with open('Integrate.txt','a') as inteFile:
#                 inteFile.write(str(CurrentTime)+'.txt')
#                 inteFile.write('\n')
#         return str(CurrentTime)+'.txt'


# def inPutData(filename):
#         with open(str(filename),'r') as fread:
#                 circleInfo=fread.read()
#         return circleInfo


# def getFileName():
#         filename=[]
#         with open('Integrate.txt','r') as fread:
#                 for line in fread.readlines():
#                         filename.append(line.strip('\n'))
#         return filename

if __name__ == "__main__":
        import matplotlib.pyplot as plt
        size=10
        fig = plt.figure(figsize=(6, 6), dpi=100)
        plt.axis([0, size, 0, size])
        circleData=np.loadtxt('Circle.txt')
        print len(circleData)
        # with open('file.txt','w') as f:
        #     f.write(str(circleData))
        #print overlapCounting(circleData)
        #print areaRatio(circleData)
        for i in range(len(circleData)):  # draw module
        # "*" used for transfer three parameters in one
                circleGenerator.drawCircle(circleData[i][0],circleData[i][1],circleData[i][2])
        plt.show()