from abaqus import *
from abaqusConstants import *


def partGen(partname):
    #Part------------------------------------------
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=5.0) #start creating wire beam with length = 1 mm
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    s.Line(point1=(0.0,0.0), point2=(1.0, 0.0))
    s.HorizontalConstraint(entity=g[2], addUndoState=False)
    p = mdb.models['Model-1'].Part(name=partname, dimensionality=TWO_D_PLANAR, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts[partname]
    p.BaseWire(sketch=s)
    s.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts[partname]
    del mdb.models['Model-1'].sketches['__profile__']
