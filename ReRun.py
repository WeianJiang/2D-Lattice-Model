from abaqus import *
from abaqusConstants import *


Mdb()
#: A new model database has been created.
#: The model "Model-1" has been created.
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
execfile('F:/AbaqusWorkDrt/MesoBeamModel/CodeFile/main.py', __main__.__dict__)