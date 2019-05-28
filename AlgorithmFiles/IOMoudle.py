import datetime



def outPut(circleInfo=[]):
    CurrentTime=datetime.datetime.now()
    with open(str(CurrentTime)+'.txt','w') as fwrite:
        fwrite.write(str(circleInfo))


if __name__=='__main__':
    outPut([[0,0,1],[0,0,2]])
    