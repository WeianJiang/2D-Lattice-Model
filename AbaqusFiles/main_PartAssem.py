from abaqus import *
from abaqusConstants import *


def partInst(partname):
    a = mdb.models['Model-1'].rootAssembly
    a.DatumCsysByDefault(CARTESIAN)
    p = mdb.models['Model-1'].parts[partname]
    a.Instance(name=partname, part=p, dependent=ON)


def partRotate(InstanceName):
    a = mdb.models['Model-1'].rootAssembly
    a.rotate(instanceList=(InstanceName, ), axisPoint=(0.0, 0.0, 0.0), 
        axisDirection=(0.0, 0.0, 1.0), angle=90.0)
    #: The instance Part-99-Ins was rotated by 90. degrees about the axis defined by the point 0., 0., 0. and the vector 0., 0., 1.


def partTranslate(InstanceName,target_x,target_y):
    a = mdb.models['Model-1'].rootAssembly
    a.translate(instanceList=(InstanceName, ), vector=(target_x,target_y, 0.0))
    #: The instance Part-49 was translated by 500.E-03, 0., 0. with respect to the assembly coordinate system


def referencePointCreate(cordin_x,cordin_y):
    a = mdb.models['Model-1'].rootAssembly
    RPIndex=a.ReferencePoint(point=(cordin_x, cordin_y, 0.0))
    return RPIndex.id