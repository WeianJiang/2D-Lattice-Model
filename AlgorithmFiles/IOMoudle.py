import datetime


def outPutData(circleInfo=[]):
        CurrentTime=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        with open(str(CurrentTime)+'.txt','w') as fwrite:
                fwrite.write(str(circleInfo))
        with open('Integrate.txt','a') as inteFile:
                inteFile.write(str(CurrentTime)+'.txt')
                inteFile.write('\n')
        return str(CurrentTime)+'.txt'


def inPutData(filename):
        with open(str(filename),'r') as fread:
                circleInfo=fread.read()
        return circleInfo


def getFileName():
        filename=[]
        with open('Integrate.txt','r') as fread:
                for line in fread.readlines():
                        filename.append(line.strip('\n'))
        return filename

if __name__=='__main__':
        filename=outPutData([[0,0,1],[0,0,2]])
        print inPutData(filename)
        print getFileName()
        for i in getFileName():
                print inPutData(i)