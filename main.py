from AbaqusFiles import main_PartGen
from AbaqusFiles import main_PartAssem
from AlgorithmFiles import NodecodeGenerator
import numpy as np
from AbaqusFiles import main_Property
from AbaqusFiles import main_Interaction
from AlgorithmFiles import ToolKit
from AbaqusFiles import main_Mesh
from AbaqusFiles import main_Load
from AlgorithmFiles import circleGenerator
from AlgorithmFiles import pointDeterminator
from caeModules import *
def callFunction(Func,looptimes):
    for number in range(looptimes):
        Func(partName[number])

        
length=5


eleNum=2*length*(length+1)
SideBeamNum=length**2
nodeNum=(length+1)**2

pointcode = NodecodeGenerator.nodeCodeGen(SideBeamNum) #generating the basic coordinate
partName=[]
for number in range(eleNum):
    partName.append('Part-'+str(number))#naming 'part' objects


#---------------------------------------------------------------------------------------------------Part Process
map(main_PartGen.partGen,partName)
#--------------------------------------------------------------------------------------------------Property Process
elasticMod=[]
possionRat=[]
main_Property.profileCreate('profile-1',0.1,0.1)
for number in range(eleNum):
        elasticMod.append(48000)
        possionRat.append(0.2)
circleData=circleGenerator.circleGenerator(200,1,1)
pointNOTIncircle=pointDeterminator.pointDeterminator(pointcode,circleData)
for number in range(eleNum):
        for numberofpointNOtinCircle in range(len(pointNOTIncircle)):#giving different para to the element
                if number==pointNOTIncircle[numberofpointNOtinCircle][2]:
                        elasticMod[number]=10000
                        possionRat[number]=0.3
for number in range(eleNum):
        main_Property.materialCreate(partName[number],elasticMod[number],possionRat[number])
        main_Property.sectionCreate(partName[number],'profile-1',partName[number])
map(main_Property.assignBeamDirect,partName)
map(main_Property.assignSection,partName,partName)
#-------------------------------------------------------------------------------------------------Assembly Process
map(main_PartAssem.partInst,partName)
callFunction(main_PartAssem.partRotate,eleNum/2)#rotate half of the beams
for number in range(eleNum):
        main_PartAssem.partTranslate('Part-'+str(number),pointcode[number][0],pointcode[number][1])
#-------------------------------------------------------------------------------------------------create reference point
RPCoordinate=[]
for number in range(eleNum/2): 
        RPIndex=main_PartAssem.referencePointCreate(pointcode[number][0],pointcode[number][1])
        RPCoordinate.append([pointcode[number][0],pointcode[number][1],RPIndex])
for number in range(eleNum/2-length-1,eleNum/2): #generate reference point for the toppest row
        RPIndex=main_PartAssem.referencePointCreate(pointcode[number][0],pointcode[number][1]+1)
        RPCoordinate.append([pointcode[number][0],pointcode[number][1]+1,RPIndex])

# i=0
# for number in range(len(RPCoordinate)):#generate referencepoint coordinate and its index
#         RPCoordinate[number].append(3*eleNum+1+i)
#         i+=1
#---------------------------------------------------------------------------------------------Interaction Process

for i in range(len(pointcode)):
        x=pointcode[i][0]
        y=pointcode[i][1]
        RPIndex=ToolKit.findRPIndex(x,y,RPCoordinate)
        print RPIndex
        leftIns=ToolKit.findLeftInstance(x,y,length,pointcode)
        rightIns=ToolKit.findRightInstance(x,y,length,pointcode)
        upIns=ToolKit.findUpInstance(x,y,length,pointcode)
        downIns=ToolKit.findDownInstance(x,y,length,pointcode)
        if leftIns>=0:
                main_Interaction.creatingTie(RPIndex,'Part-'+str(leftIns),2,i)
        if rightIns>=0:
                main_Interaction.creatingTie(RPIndex,'Part-'+str(rightIns),1,i)
        if upIns>=0:
                main_Interaction.creatingTie(RPIndex,'Part-'+str(upIns),1,i)
        if downIns>=0:
                main_Interaction.creatingTie(RPIndex,'Part-'+str(downIns),2,i)
RPIndex=ToolKit.findRPIndex(length,length,length)
leftIns=ToolKit.findLeftInstance(length,length,length,pointcode)
downIns=ToolKit.findDownInstance(length,length,length,pointcode)
main_Interaction.creatingTie(RPIndex,'Part-'+str(leftIns),2,'last')
main_Interaction.creatingTie(RPIndex,'Part-'+str(downIns),2,'last')
#---------------------------------------------------------------------------step process
mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial')
#---------------------------------------------------------------------------Load process
highestPointRPIndex=ToolKit.findToppestNode(length,pointcode)
for i in range(len(highestPointRPIndex)):
        main_Load.setLoad(highestPointRPIndex[i],0.1,i)
lowestPointRPIndex=ToolKit.findLowestNode(length,pointcode)
for i in range(len(lowestPointRPIndex)):
        main_Load.setBoundary(lowestPointRPIndex[i],i)
#----------------------------------------------------------------------------Mesh Process
for i in range(len(partName)):
        main_Mesh.Mesh(partName[i])

#print circleData
# a = mdb.models['Model-1'].rootAssembly
# a.regenerate()
# a = mdb.models['Model-1'].rootAssembly
mdb.Job(name='Job-1', model='Model-1', description='')
mdb.jobs['Job-1'].writeInput(consistencyChecking=OFF)
print 'success input'