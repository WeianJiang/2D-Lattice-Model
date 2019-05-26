from abaqus import *
from abaqusConstants import *



def setLoad(referencePointIndex,load,order):
    a = mdb.models['Model-1'].rootAssembly
    r1 = a.referencePoints
    refPoints1=(r1[referencePointIndex], )
    region = a.Set(referencePoints=refPoints1, name='LoadSet-'+str(order))
    mdb.models['Model-1'].ConcentratedForce(name='Load-'+str(order), createStepName='Step-1', 
        region=region, cf2=load, distributionType=UNIFORM, field='', localCsys=None)


def setBoundary(referencePointIndex,order):
    a = mdb.models['Model-1'].rootAssembly
    r1 = a.referencePoints
    refPoints1=(r1[referencePointIndex], )
    region = a.Set(referencePoints=refPoints1, name='BoudSet-'+str(order))
    mdb.models['Model-1'].DisplacementBC(name='BC-'+str(order), createStepName='Initial', 
        region=region, u1=SET, u2=SET, ur3=UNSET, amplitude=UNSET, 
        distributionType=UNIFORM, fieldName='', localCsys=None)