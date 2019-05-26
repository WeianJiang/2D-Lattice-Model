from abaqus import *
from abaqusConstants import *


def creatingTie(referencePointIndex,instanceName,end,order):#order for set-naming
    a = mdb.models['Model-1'].rootAssembly
    r1 = a.referencePoints
    refPoints1=(r1[referencePointIndex], )
    region1=a.Set(referencePoints=refPoints1, name='m_Set-'+instanceName+str(order))
    a = mdb.models['Model-1'].rootAssembly
    v1 = a.instances[instanceName].vertices
    verts1 = v1.getSequenceFromMask(mask=('[#'+str(end)+']', ), )
    region2=a.Set(vertices=verts1, name='m_Set-'+instanceName+str(order))
    mdb.models['Model-1'].Tie(name='Constraint-1'+instanceName+str(order), master=region1, slave=region2, 
        positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)



# def creatingTie2(referencePointIndex,instanceName1,end1,instanceName2,end2):
#     a = mdb.models['Model-1'].rootAssembly
#     r1 = a.referencePoints
#     refPoints1=(r1[referencePointIndex], )
#     region1=a.Set(referencePoints=refPoints1, name='m_Set-1')
#     a = mdb.models['Model-1'].rootAssembly
#     v1 = a.instances[instanceName1].vertices
#     verts1 = v1.getSequenceFromMask(mask=('[#'+str(end1)+']', ), )
#     v2 = a.instances[instanceName2].vertices
#     verts2 = v2.getSequenceFromMask(mask=('[#'+str(end2)+']', ), )
#     region2=a.Set(vertices=verts1+verts2, name='s_Set-1')
#     mdb.models['Model-1'].Tie(name='Constraint-1', master=region1, slave=region2, 
#         positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)


# def creatingTie3(referencePointIndex,instanceName1,end1,instanceName2,end2,instanceName3,end3):
#     a = mdb.models['Model-1'].rootAssembly
#     r1 = a.referencePoints
#     refPoints1=(r1[referencePointIndex], )
#     region1=a.Set(referencePoints=refPoints1, name='m_Set-1')
#     a = mdb.models['Model-1'].rootAssembly
#     v1 = a.instances[instanceName1].vertices
#     verts1 = v1.getSequenceFromMask(mask=('[#'+str(end1)+']', ), )
#     v2 = a.instances[instanceName2].vertices
#     verts2 = v2.getSequenceFromMask(mask=('[#'+str(end2)+']', ), )    
#     v3 = a.instances[instanceName3].vertices
#     verts3 = v3.getSequenceFromMask(mask=('[#'+str(end3)+']', ), )
#     region2=a.Set(vertices=verts1+verts2+verts3, name='s_Set-1')
#     mdb.models['Model-1'].Tie(name='Constraint-1', master=region1, slave=region2, 
#         positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)


# def creatingTie4(referencePointIndex,instanceName1,end1,instanceName2,end2,instanceName3,end3,instanceName4,end4):
    a = mdb.models['Model-1'].rootAssembly
    r1 = a.referencePoints
    refPoints1=(r1[referencePointIndex], )
    region1=a.Set(referencePoints=refPoints1, name='m_Set-1')
    a = mdb.models['Model-1'].rootAssembly
    v1 = a.instances[instanceName1].vertices
    verts1 = v1.getSequenceFromMask(mask=('[#'+str(end1)+']', ), )
    v2 = a.instances[instanceName2].vertices
    verts2 = v2.getSequenceFromMask(mask=('[#'+str(end2)+']', ), )    
    v3 = a.instances[instanceName3].vertices
    verts3 = v3.getSequenceFromMask(mask=('[#'+str(end3)+']', ), )
    v4 = a.instances[instanceName4].vertices
    verts4 = v4.getSequenceFromMask(mask=('[#'+str(end4)+']', ), )    
    region2=a.Set(vertices=verts1+verts2+verts3+verts4, name='s_Set-1')
    mdb.models['Model-1'].Tie(name='Constraint-1', master=region1, slave=region2, 
        positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)