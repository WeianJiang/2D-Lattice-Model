from abaqus import *
from abaqusConstants import *


def Mesh(partname):
    p = mdb.models['Model-1'].parts[partname]
    p.seedPart(size=0.1, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts[partname]
    p.generateMesh()