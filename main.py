import main_PartGen
import main_PartAssem
import NodecodeGenerator
import numpy as np
import main_Property
import main_Interaction
import ToolKit
def callFunction(Func,looptimes):
    for number in range(looptimes):
        Func(partName[number])

        
length=3


eleNum=2*length*(length+1)
SideBeamNum=length**2
nodeNum=(length+1)**2


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
        main_Property.materialCreate(partName[number],elasticMod[number],possionRat[number])
        main_Property.sectionCreate(partName[number],'profile-1',partName[number])
map(main_Property.assignBeamDirect,partName)
map(main_Property.assignSection,partName,partName)
#-------------------------------------------------------------------------------------------------Assembly Process
map(main_PartAssem.partInst,partName)
callFunction(main_PartAssem.partRotate,eleNum/2)#rotate half of the beams
pointcode = NodecodeGenerator.nodeCodeGen(SideBeamNum)
for number in range(eleNum):
        main_PartAssem.partTranslate('Part-'+str(number),pointcode[number][0],pointcode[number][1])
#-------------------------------------------------------------------------------------------------create reference point
RPCoordinate=[]
for number in range(eleNum/2): 
        main_PartAssem.referencePointCreate(pointcode[number][0],pointcode[number][1])
        RPCoordinate.append([pointcode[number][0],pointcode[number][1]])
for number in range(eleNum/2-length-1,eleNum/2): #generate reference point for the toppest row
        main_PartAssem.referencePointCreate(pointcode[number][0],pointcode[number][1]+1)
        RPCoordinate.append([pointcode[number][0],pointcode[number][1]+1])

i=0
for number in range(len(RPCoordinate)):#generate referencepoint coordinate and its index
        RPCoordinate[number].append(3*eleNum+1+i)
        i+=1
#---------------------------------------------------------------------------------------------Interaction Process

for i in range(len(pointcode)):
        x=pointcode[i][0]
        y=pointcode[i][1]
        RPIndex=ToolKit.findRPIndex(x,y,length)
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
