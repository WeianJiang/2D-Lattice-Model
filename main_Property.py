from abaqus import *
from abaqusConstants import *

def materialCreate(materialName,elaticModules,possionRatio):
    mdb.models['Model-1'].Material(name=materialName)
    mdb.models['Model-1'].materials[materialName].Elastic(table=((int(elaticModules), int(possionRatio)), ))


def profileCreate(profileName,length,height):
    mdb.models['Model-1'].RectangularProfile(name=profileName, a=length, b=height)


def sectionCreate(sectionName,profileName,materialName):
    mdb.models['Model-1'].BeamSection(name=sectionName, 
    integration=DURING_ANALYSIS, poissonRatio=0.0, profile=profileName, 
    material=materialName, temperatureVar=LINEAR, consistentMassMatrix=False)

def assignBeamDirect(partName):
    p = mdb.models['Model-1'].parts[partName]
    e = p.edges
    edges = e.getSequenceFromMask(mask=('[#1 ]', ), )
    region=p.Set(edges=edges, name='Set-1')
    p = mdb.models['Model-1'].parts[partName]
    p.assignBeamSectionOrientation(region=region, method=N1_COSINES, n1=(0.0, 0.0, 
        -1.0))
    #: Beam orientations have been assigned to the selected regions.


def assignSection(parName,sectionName):
    p = mdb.models['Model-1'].parts[parName]
    e = p.edges
    edges = e.getSequenceFromMask(mask=('[#1 ]', ), )
    region=p.Set(edges=edges, name='Set-1')
    p = mdb.models['Model-1'].parts[parName]
    p.SectionAssignment(region=region, sectionName=sectionName, offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)