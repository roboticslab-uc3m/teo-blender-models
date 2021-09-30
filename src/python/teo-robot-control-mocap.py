bl_info = {
    "name": "TEO robot control",
    "description": "TEO robot control configuration and data display panel",
    "author": "Raul de Santos rico (rasantos@it.uc3m.es)",
    "version": (0, 0, 1),
    "blender": (2, 80, 0),
    "location": "3D View > Mode Pose> TEO Robot Control",
    "warning": "", # used for warning icon and text in addons panel
    "category": "Development"
}

import bpy
from bpy.app.handlers import persistent
import math
import csv


class CustomPropertyGroup(bpy.types.PropertyGroup):
    
    # Motion update functions for left arm
    def frontalLeftShoulderUpdate(self, context):
        if not self.enableIkLeftArm: bpy.context.object.pose.bones["FrontalLeftShoulder"].rotation_euler[1]  = self.frontalLeftShoulder
    def sagittalLeftShoulderUpdate(self, context):
        if not self.enableIkLeftArm: bpy.context.object.pose.bones["SagittalLeftShoulder"].rotation_euler[0] =-self.sagittalLeftShoulder
    def axialLeftShoulderUpdate(self, context):
        if not self.enableIkLeftArm: bpy.context.object.pose.bones["AxialLeftShoulder"].rotation_euler[1]    =-self.axialLeftShoulder
    def frontalLeftElbowUpdate(self, context):
        if not self.enableIkLeftArm: bpy.context.object.pose.bones["FrontalLeftElbow"].rotation_euler[2]     = self.frontalLeftElbow
    def axialLeftWristUpdate(self, context):
        if not self.enableIkLeftArm: bpy.context.object.pose.bones["AxialLeftWrist"].rotation_euler[1]       =-self.axialLeftWrist
    def frontalLeftWristUpdate(self, context):
        if not self.enableIkLeftArm: bpy.context.object.pose.bones["FrontalLeftWrist"].rotation_euler[2]     = self.frontalLeftWrist
    def updateLeftArmIk(self,context):
        if self.enableIkLeftArm:
            bpy.context.object.pose.bones["FrontalLeftWrist"].constraints["IK"].mute = False # activate
        else:
            bpy.context.object.pose.bones["FrontalLeftWrist"].constraints["IK"].mute = True  # deactivate
            if self.joinIKtoLeftArm: # if the trunk is joined to left arm
                self.joinIKtoLeftArm = False


    enableIkLeftArm: bpy.props.BoolProperty (name='Enable IK',
                                             default=True,
                                             description='Enable or disable left-arm movement using Inverse Kinematics',
                                             update=updateLeftArmIk)


    frontalLeftShoulder: bpy.props.FloatProperty(name='FrontalLeftShoulder', subtype='ANGLE', precision=4, min=math.radians(-96.8), max=math.radians(113.2), update=frontalLeftShoulderUpdate)
    sagittalLeftShoulder: bpy.props.FloatProperty(name='SagittalLeftShoulder', subtype='ANGLE', precision=4, min=math.radians(-23.9), max=math.radians(76.5), update=sagittalLeftShoulderUpdate)
    axialLeftShoulder: bpy.props.FloatProperty(name='AxialLeftShoulder', subtype='ANGLE', precision=4, min=math.radians(-51.6), max=math.radians(84.1), update=axialLeftShoulderUpdate)
    frontalLeftElbow: bpy.props.FloatProperty(name='FrontalLeftElbow', subtype='ANGLE', precision=4, min=math.radians(-101.1), max=math.radians(96.8), update=frontalLeftElbowUpdate)
    axialLeftWrist: bpy.props.FloatProperty(name='AxialLeftWrist', subtype='ANGLE', precision=4, min=math.radians(-101), max=math.radians(76.4), update=axialLeftWristUpdate)
    frontalLeftWrist: bpy.props.FloatProperty(name='FrontalLeftWrist', subtype='ANGLE', precision=4, min=math.radians(-113.3), max=math.radians(61.6), update=frontalLeftWristUpdate)


    # Motion update functions for right arm
    def frontalRightShoulderUpdate(self, context):
        if not self.enableIkRightArm: bpy.context.object.pose.bones["FrontalRightShoulder"].rotation_euler[1]  =-self.frontalRightShoulder
    def sagittalRightShoulderUpdate(self, context):
        if not self.enableIkRightArm: bpy.context.object.pose.bones["SagittalRightShoulder"].rotation_euler[0] =-self.sagittalRightShoulder
    def axialRightShoulderUpdate(self, context):
        if not self.enableIkRightArm: bpy.context.object.pose.bones["AxialRightShoulder"].rotation_euler[1]    =-self.axialRightShoulder
    def frontalRightElbowUpdate(self, context):
        if not self.enableIkRightArm: bpy.context.object.pose.bones["FrontalRightElbow"].rotation_euler[2]     = self.frontalRightElbow
    def axialRightWristUpdate(self, context):
        if not self.enableIkRightArm: bpy.context.object.pose.bones["AxialRightWrist"].rotation_euler[1]       =-self.axialRightWrist
    def frontalRightWristUpdate(self, context):
        if not self.enableIkRightArm: bpy.context.object.pose.bones["FrontalRightWrist"].rotation_euler[2]     = self.frontalRightWrist
    def updateRightArmIk(self,context):
        if self.enableIkRightArm:
            bpy.context.object.pose.bones["FrontalRightWrist"].constraints["IK"].mute = False # activae
        else:
            bpy.context.object.pose.bones["FrontalRightWrist"].constraints["IK"].mute = True  # deactivae
            if self.joinIKtoRightArm: # if the trunk is joined to left arm
                self.joinIKtoRightArm = False

    enableIkRightArm: bpy.props.BoolProperty (name='Enable IK',
                                             default=True,
                                             description='Enable or disable right-arm movement using Inverse Kinematics',
                                             update=updateRightArmIk)
    frontalRightShoulder: bpy.props.FloatProperty(name='FrontalRightShoulder', subtype='ANGLE', precision=4, min=math.radians(-98.1), max=math.radians(106), update=frontalRightShoulderUpdate)
    sagittalRightShoulder: bpy.props.FloatProperty(name='SagittalRightShoulder', subtype='ANGLE', precision=4, min=math.radians(-75.5), max=math.radians(22.4), update=sagittalRightShoulderUpdate)
    axialRightShoulder: bpy.props.FloatProperty(name='AxialRightShoulder', subtype='ANGLE', precision=4, min=math.radians(-80.1), max=math.radians(57), update=axialRightShoulderUpdate)
    frontalRightElbow: bpy.props.FloatProperty(name='FrontalRightElbow', subtype='ANGLE', precision=4, min=math.radians(-99.6), max=math.radians(98.4), update=frontalRightElbowUpdate)
    axialRightWrist: bpy.props.FloatProperty(name='AxialRightWrist', subtype='ANGLE', precision=4, min=math.radians(-80.4), max=math.radians(99.6), update=axialRightWristUpdate)
    frontalRightWrist: bpy.props.FloatProperty(name='FrontalRightWrist', subtype='ANGLE', precision=4, min=math.radians(-115), max=math.radians(44.7), update=frontalRightWristUpdate)

    
     # Motion update functions for left leg
    def axialLeftHipUpdate(self, context):
        if not self.enableIkLeftLeg: bpy.context.object.pose.bones["AxialSagittalLeftHip"].rotation_euler[1]  =-self.axialLeftHip
    def sagittalLeftHipUpdate(self, context):
        if not self.enableIkLeftLeg: bpy.context.object.pose.bones["FrontalLeftHip"].rotation_euler[2]        =-self.sagittalLeftHip
    def frontalLeftHipUpdate(self, context):
        if not self.enableIkLeftLeg: bpy.context.object.pose.bones["FrontalLeftHip"].rotation_euler[0]        =self.frontalLeftHip
    def frontalLeftKneeUpdate(self, context):
        if not self.enableIkLeftLeg: bpy.context.object.pose.bones["FrontalLeftKnee"].rotation_euler[0]       =self.frontalLeftKnee
    def frontalLeftAnkleUpdate(self, context):
        if not self.enableIkLeftLeg: bpy.context.object.pose.bones["FrontalLeftAnkle"].rotation_euler[0]      =-self.frontalLeftAnkle
    def sagittalLeftAnkleUpdate(self, context):
        if not self.enableIkLeftLeg: bpy.context.object.pose.bones["FrontalLeftAnkle"].rotation_euler[2]      =self.sagittalLeftAnkle
    def updateLeftLegIk(self,context):
        if self.enableIkLeftLeg:
            bpy.context.object.pose.bones["FrontalLeftAnkle"].constraints["IK"].mute = False # activate 
            bpy.context.object.pose.bones["SagittalLeftAnkle"].constraints["IK"].mute = False # activate   
        else:
            bpy.context.object.pose.bones["FrontalLeftAnkle"].constraints["IK"].mute = True  # deactivate
            bpy.context.object.pose.bones["SagittalLeftAnkle"].constraints["IK"].mute = True # deactivate

    enableIkLeftLeg: bpy.props.BoolProperty (name='Enable IK',
                                             default=True,
                                             description='Enable or disable left-leg movement using Inverse Kinematics',
                                             update=updateLeftLegIk)
    def updateLeftLegFloorOrientation(self,context):
        if self.enableFloorOrientationLeftLeg:
            bpy.context.object.pose.bones["FrontalLeftAnkle"].constraints["Copy Rotation"].mute = False   #activate
        else:
            bpy.context.object.pose.bones["FrontalLeftAnkle"].constraints["Copy Rotation"].mute = True    #deactivate

    enableFloorOrientationLeftLeg: bpy.props.BoolProperty (name='Enable Floor Orientation',
                                             default=True,
                                             description='Enable or disable left-leg floor orientation of the foot',
                                             update=updateLeftLegFloorOrientation)         
    axialLeftHip: bpy.props.FloatProperty(name='AxialLeftHip', subtype='ANGLE', precision=4, min=math.radians(-27.9), max=math.radians(32.8), update=axialLeftHipUpdate)
    sagittalLeftHip: bpy.props.FloatProperty(name='SagittalLeftHip', subtype='ANGLE', precision=4, min=math.radians(-12.5), max=math.radians(14.2), update=sagittalLeftHipUpdate)
    frontalLeftHip: bpy.props.FloatProperty(name='FrontalLeftHip', subtype='ANGLE', precision=4, min=math.radians(-31.6), max=math.radians(42.3), update=frontalLeftHipUpdate)
    frontalLeftKnee: bpy.props.FloatProperty(name='FrontalLeftKnee', subtype='ANGLE', precision=4, min=math.radians(-5), max=math.radians(82.4), update=frontalLeftKneeUpdate)
    frontalLeftAnkle: bpy.props.FloatProperty(name='FrontalLeftAnkle', subtype='ANGLE', precision=4, min=math.radians(-23.1), max=math.radians(25.4), update=frontalLeftAnkleUpdate)
    sagittalLeftAnkle: bpy.props.FloatProperty(name='SagittalLeftAnkle', subtype='ANGLE', precision=4, min=math.radians(-42.5), max=math.radians(19.8), update=sagittalLeftAnkleUpdate)
   
    
    # Motion update functions for right leg
    def axialRightHipUpdate(self, context):
        if not self.enableIkRightLeg: bpy.context.object.pose.bones["AxialSagittalRightHip"].rotation_euler[1]  =-self.axialRightHip
    def sagittalRightHipUpdate(self, context):
        if not self.enableIkRightLeg: bpy.context.object.pose.bones["FrontalRightHip"].rotation_euler[2]        =-self.sagittalRightHip
    def frontalRightHipUpdate(self, context):
        if not self.enableIkRightLeg: bpy.context.object.pose.bones["FrontalRightHip"].rotation_euler[0]        =self.frontalRightHip
    def frontalRightKneeUpdate(self, context):
        if not self.enableIkRightLeg: bpy.context.object.pose.bones["FrontalRightKnee"].rotation_euler[0]       =self.frontalRightKnee
    def frontalRightAnkleUpdate(self, context):
        if not self.enableIkRightLeg: bpy.context.object.pose.bones["FrontalRightAnkle"].rotation_euler[0]      =-self.frontalRightAnkle
    def sagittalRightAnkleUpdate(self, context):
        if not self.enableIkRightLeg: bpy.context.object.pose.bones["FrontalRightAnkle"].rotation_euler[2]      =self.sagittalRightAnkle
    def updateRightLegIk(self,context):
        if self.enableIkRightLeg:
            bpy.context.object.pose.bones["FrontalRightAnkle"].constraints["IK"].mute = False # activate 
            bpy.context.object.pose.bones["SagittalRightAnkle"].constraints["IK"].mute = False # activate  
        else:
            bpy.context.object.pose.bones["FrontalRightAnkle"].constraints["IK"].mute = True  # deactivate
            bpy.context.object.pose.bones["SagittalRightAnkle"].constraints["IK"].mute = True  # deactivate

    enableIkRightLeg: bpy.props.BoolProperty (name='Enable IK',
                                             default=True,
                                             description='Enable or disable right-leg floor orientation of the foot',
                                             update=updateRightLegIk)
    def updateRightLegFloorOrientation(self,context):
        if self.enableFloorOrientationRightLeg:
            bpy.context.object.pose.bones["FrontalRightAnkle"].constraints["Copy Rotation"].mute = False   #activate
        else:
            bpy.context.object.pose.bones["FrontalRightAnkle"].constraints["Copy Rotation"].mute = True    #deactivate

    enableFloorOrientationRightLeg: bpy.props.BoolProperty (name='Enable Floor Orientation',
                                             default=True,
                                             description='Enable or disable right-leg floor orientation using Copy Rotation',
                                             update=updateRightLegFloorOrientation) 
    axialRightHip: bpy.props.FloatProperty(name='AxialRightHip', subtype='ANGLE', precision=4, min=math.radians(-32.8), max=math.radians(27.9), update=axialRightHipUpdate)
    sagittalRightHip: bpy.props.FloatProperty(name='SagittalRightHip', subtype='ANGLE', precision=4, min=math.radians(-14.2), max=math.radians(12.5), update=sagittalRightHipUpdate)
    frontalRightHip: bpy.props.FloatProperty(name='FrontalRightHip', subtype='ANGLE', precision=4, min=math.radians(-31.6), max=math.radians(42.3), update=frontalRightHipUpdate)
    frontalRightKnee: bpy.props.FloatProperty(name='FrontalRightKnee', subtype='ANGLE', precision=4, min=math.radians(-5), max=math.radians(82.4), update=frontalRightKneeUpdate)
    frontalRightAnkle: bpy.props.FloatProperty(name='FrontalRightAnkle', subtype='ANGLE', precision=4,  min=math.radians(-23), max=math.radians(25.4), update=frontalRightAnkleUpdate)
    sagittalRightAnkle: bpy.props.FloatProperty(name='SagittalRightAnkle', subtype='ANGLE', precision=4, min=math.radians(-19.8), max=math.radians(42.5), update=sagittalRightAnkleUpdate)
    
    
    # Trunk: Motion update functions for trunk
    def frontalTrunkUpdate(self, context):
        if not self.joinIKtoLeftArm: bpy.context.object.pose.bones["FrontalTrunk"].rotation_euler[2]         = self.frontalTrunk
    def axialTrunkUpdate(self, context):
        if not self.joinIKtoLeftArm: bpy.context.object.pose.bones["AxialTrunk"].rotation_euler[1]           = self.axialTrunk

    frontalTrunk: bpy.props.FloatProperty(name='FrontalTrunk', subtype='ANGLE', precision=4, min=math.radians(-90.3), max=math.radians(10), update=frontalTrunkUpdate)
    axialTrunk: bpy.props.FloatProperty(name='AxialTrunk', subtype='ANGLE', precision=4, min=math.radians(-59.2), max=math.radians(46.2), update=axialTrunkUpdate)

    
    def updateJoinIKtoLeftArm(self, context):
        if self.joinIKtoLeftArm:
            self.enableIkLeftArm = True # activate leftArm IK
            bpy.context.object.pose.bones["FrontalLeftWrist"].constraints["IK"].chain_count = 8 # join trunk to left arm IK
        else:
            bpy.context.object.pose.bones["FrontalLeftWrist"].constraints["IK"].chain_count = 6 # disunite trunk

    joinIKtoLeftArm: bpy.props.BoolProperty (name='Join Trunk to Left Arm IK',
                                             default=True,
                                             description='Enable or disable trunk movement using Inverse Kinematics of left Arm',
                                             update=updateJoinIKtoLeftArm)

    def updateJoinIKtoRightArm(self, context):
        if self.joinIKtoRightArm:
            self.enableIkRightArm = True # activate rightArm IK
            bpy.context.object.pose.bones["FrontalRightWrist"].constraints["IK"].chain_count = 8 # join trunk to left arm IK
        else:
            bpy.context.object.pose.bones["FrontalRightWrist"].constraints["IK"].chain_count = 6 # disunite trunk

    joinIKtoRightArm: bpy.props.BoolProperty (name='Join Trunk to Right Arm IK',
                                             default=True,
                                             description='Enable or disable trunk movement using Inverse Kinematics of right Arm',
                                             update=updateJoinIKtoRightArm)
    
    #----------------------------NUEVO--------------------------------------------------------------------------------

    exportUpperExtremities: bpy.props.BoolProperty (name='Upper Extremities Values (Arms + Trunk)',
                                             default=True,
                                             description='Export the values of the upper extremities to the .csv file')
    

                                                
    exportLowerExtremities: bpy.props.BoolProperty (name='Lower Extremities Values (Legs)',
                                             default=True,
                                             description='Export the values of the lower extremities to the .csv file')
   #-------------------------------------------------------------------------------------------------------------------

    yarpRobotPrefix: bpy.props.StringProperty(name='robot prefix', default='/teoSim')

    fileNameTrajectory: bpy.props.StringProperty(name='name', default='trajectory.csv')
    enableExport : bpy.props.BoolProperty(name='Export File', default=False)
    enableExport = False # force value
    



class CustomObjectGroup():
    csv_file = None
    csv_obj = None

class OBJECT_PT_LeftArmControlPanel(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Left Arm'
    bl_context = 'posemode'
    bl_category = 'TEO Robot Control'

    def draw(self, context):
        layout = self.layout
        layout.prop(context.scene.custom_props, 'enableIkLeftArm')
        layout.label(text="Joint Positions:")
        layout.prop(context.scene.custom_props, 'frontalLeftShoulder')
        layout.prop(context.scene.custom_props, 'sagittalLeftShoulder')
        layout.prop(context.scene.custom_props, 'axialLeftShoulder')
        layout.prop(context.scene.custom_props, 'frontalLeftElbow')
        layout.prop(context.scene.custom_props, 'axialLeftWrist')
        layout.prop(context.scene.custom_props, 'frontalLeftWrist')
        layout.operator('leftarm.home', text =  'Home Position')

class OBJECT_OT_HomeLeftArm(bpy.types.Operator):

    bl_idname = 'leftarm.home'
    bl_label = 'Home Position'
    bl_options = {'INTERNAL'}

    @classmethod
    def poll(cls, context):
        return context.object is not None

    def execute(self, context):
        bpy.context.object.pose.bones["TCP-leftArm"].location = (0,0,0)
        bpy.context.object.pose.bones["TCP-leftArm"].rotation_euler = (0,0,0)
        properties = bpy.context.scene.custom_props
        properties.frontalLeftShoulder  = 0.0
        properties.sagittalLeftShoulder = 0.0
        properties.axialLeftShoulder    = 0.0
        properties.frontalLeftElbow     = 0.0
        properties.axialLeftWrist       = 0.0
        properties.frontalLeftWrist     = 0.0
        return {'FINISHED'}

class OBJECT_PT_RightArmControlPanel(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Right Arm'
    bl_context = 'posemode'
    bl_category = 'TEO Robot Control'

    def draw(self, context):
        layout = self.layout
        layout.prop(context.scene.custom_props, 'enableIkRightArm')
        layout.label(text="Joint Positions:")
        layout.prop(context.scene.custom_props, 'frontalRightShoulder')
        layout.prop(context.scene.custom_props, 'sagittalRightShoulder')
        layout.prop(context.scene.custom_props, 'axialRightShoulder')
        layout.prop(context.scene.custom_props, 'frontalRightElbow')
        layout.prop(context.scene.custom_props, 'axialRightWrist')
        layout.prop(context.scene.custom_props, 'frontalRightWrist')
        layout.operator('rightarm.home', text = 'Home Position')

class OBJECT_OT_HomeRightArm(bpy.types.Operator):

    bl_idname = 'rightarm.home'
    bl_label = 'Home Position'
    bl_options = {'INTERNAL'}

    @classmethod
    def poll(cls, context):
        return context.object is not None

    def execute(self, context):
        bpy.context.object.pose.bones["TCP-rightArm"].location = (0,0,0)
        bpy.context.object.pose.bones["TCP-rightArm"].rotation_euler = (0,0,0)
        properties = bpy.context.scene.custom_props
        properties.frontalRightShoulder  = 0.0
        properties.sagittalRightShoulder = 0.0
        properties.axialRightShoulder    = 0.0
        properties.frontalRightElbow     = 0.0
        properties.axialRightWrist       = 0.0
        properties.frontalRightWrist     = 0.0
        return {'FINISHED'}
    
    

class OBJECT_PT_LeftLegControlPanel(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Left Leg'
    bl_context = 'posemode'
    bl_category = 'TEO Robot Control'

    def draw(self, context):
        layout = self.layout
        layout.prop(context.scene.custom_props, 'enableIkLeftLeg')
        layout.prop(context.scene.custom_props, 'enableFloorOrientationLeftLeg')
        layout.label(text="Joint Positions:")
        layout.prop(context.scene.custom_props, 'axialLeftHip')
        layout.prop(context.scene.custom_props, 'sagittalLeftHip')
        layout.prop(context.scene.custom_props, 'frontalLeftHip')
        layout.prop(context.scene.custom_props, 'frontalLeftKnee')
        layout.prop(context.scene.custom_props, 'frontalLeftAnkle')
        layout.prop(context.scene.custom_props, 'sagittalLeftAnkle')
        layout.operator('leftleg.home', text =  'Home Position')

class OBJECT_OT_HomeLeftLeg(bpy.types.Operator):

    bl_idname = 'leftleg.home'
    bl_label = 'Home Position'
    bl_options = {'INTERNAL'}

    @classmethod
    def poll(cls, context):
        return context.object is not None

    def execute(self, context):
        #bpy.context.object.pose.bones["LeftLeg-TCP"].location = (0,0,0)
        #bpy.context.object.pose.bones["LeftLeg-TCP"].rotation_euler = (0,0,0)
        properties = bpy.context.scene.custom_props
        properties.axialLeftHip          = 0.0
        properties.sagittalLeftHip       = 0.0
        properties.frontalLeftHip        = 0.0
        properties.frontalLeftKnee       = 0.0
        properties.frontalLeftAnkle      = 0.0
        properties.sagittalLeftAnkle     = 0.0
        return {'FINISHED'}

class OBJECT_PT_RightLegControlPanel(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Right Leg'
    bl_context = 'posemode'
    bl_category = 'TEO Robot Control'

    def draw(self, context):
        layout = self.layout
        layout.prop(context.scene.custom_props, 'enableIkRightLeg')
        layout.prop(context.scene.custom_props, 'enableFloorOrientationRightLeg')
        layout.label(text="Joint Positions:")
        layout.prop(context.scene.custom_props, 'axialRightHip')
        layout.prop(context.scene.custom_props, 'sagittalRightHip')
        layout.prop(context.scene.custom_props, 'frontalRightHip')
        layout.prop(context.scene.custom_props, 'frontalRightKnee')
        layout.prop(context.scene.custom_props, 'frontalRightAnkle')
        layout.prop(context.scene.custom_props, 'sagittalRightAnkle')
        layout.operator('rightleg.home', text = 'Home Position')

class OBJECT_OT_HomeRightLeg(bpy.types.Operator):

    bl_idname = 'rightleg.home'
    bl_label = 'Home Position'
    bl_options = {'INTERNAL'}

    @classmethod
    def poll(cls, context):
        return context.object is not None

    def execute(self, context):
        #bpy.context.object.pose.bones["TCP-RightLeg1"].location = (0,0,0)
        #bpy.context.object.pose.bones["TCP-RightLeg1"].rotation_euler = (0,0,0)
        properties = bpy.context.scene.custom_props
        properties.axialRightHip          = 0.0
        properties.sagittalRightHip       = 0.0
        properties.frontalRightHip        = 0.0
        properties.frontalRightKnee       = 0.0
        properties.frontalRightAnkle      = 0.0
        properties.sagittalRightAnkle     = 0.0
        return {'FINISHED'}


class OBJECT_PT_TrunkControlPanel(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Trunk'
    bl_context = 'posemode'
    bl_category = 'TEO Robot Control'

    def draw(self, context):
        layout = self.layout
        layout.prop(context.scene.custom_props, 'joinIKtoLeftArm')
        layout.prop(context.scene.custom_props, 'joinIKtoRightArm')
        layout.label(text="Trunk Positions:")
        layout.prop(context.scene.custom_props, 'frontalTrunk')
        layout.prop(context.scene.custom_props, 'axialTrunk')
        layout.operator('trunk.home', text = 'Home Position')

class OBJECT_OT_HomeTrunk(bpy.types.Operator):
    bl_idname = 'trunk.home'
    bl_label = 'Home Postion'
    bl_options = {'INTERNAL'}

    @classmethod
    def poll(cls, context):
        return context.object is not None

    def execute(self, context):
        properties = bpy.context.scene.custom_props
        properties.frontalTrunk   = 0.0
        properties.axialTrunk     = 0.0
        return {'FINISHED'}

# TRAJECTORY PANEL

                                             
class OBJECT_PT_TrajectoryPanel(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Trajectory'
    bl_context = 'posemode'
    bl_category = 'TEO Robot Control'

    def draw(self, context):
        layout = self.layout
        layout.label(text="Actions:")
        subrow = layout.row(align=True)
        subrow.operator('trajectory.play', text = 'PLAY')
        subrow.operator('trajectory.play', text = 'STOP')
        layout.label(text="Export CSV:")
        layout.prop(context.scene.custom_props, 'exportUpperExtremities')
        layout.prop(context.scene.custom_props, 'exportLowerExtremities')
        layout.prop(context.scene.custom_props, 'fileNameTrajectory')
        layout.operator('trajectory.export', text = 'Export')

class OBJECT_OT_PlayTrayectory(bpy.types.Operator):
    bl_idname = 'trajectory.play'
    bl_label = 'PLAY'
    bl_options = {'INTERNAL'}

    def execute(self, context):
        bpy.ops.screen.animation_play()
        return {'FINISHED'}

class OBJECT_OT_StopTrayectory(bpy.types.Operator):
    bl_idname = 'trajectory.stop'
    bl_label = 'STOP'
    bl_options = {'INTERNAL'}

    def execute(self, context):
        bpy.ops.screen.animation_cancel(restore_frame=True)
        return {'FINISHED'}

class OBJECT_OT_ExportTrajectory(bpy.types.Operator):
    bl_idname = 'trajectory.export'
    bl_label = 'EXPORT'
    bl_options = {'INTERNAL'}

    def execute(self, context):
        properties = bpy.context.scene.custom_props
        self.report({'INFO'}, 'exporting file: '+str(properties.fileNameTrajectory))
        if properties.enableExport is False:
            properties.enableExport = True
        bpy.ops.screen.animation_play()
        bpy.context.scene.custom_objs.csv_file = open(properties.fileNameTrajectory,"w")
        bpy.context.scene.custom_objs.csv_obj  = csv.writer(bpy.context.scene.custom_objs.csv_file, delimiter=',') #, delimiter=','

        return {'FINISHED'}

### Skeleton code
ob = bpy.data.objects['Skeleton']
bpy.context.view_layer.objects.active = ob
bpy.ops.object.mode_set(mode='POSE')

# left arm bones
frontalLeftShoulderBone  = ob.pose.bones['FrontalLeftShoulder']
sagittalLeftShoulderBone = ob.pose.bones['SagittalLeftShoulder']
axialLeftShoulderBone    = ob.pose.bones['AxialLeftShoulder']
frontalLeftElbowBone     = ob.pose.bones['FrontalLeftElbow']
axialLeftWristBone       = ob.pose.bones['AxialLeftWrist']
frontalLeftWristBone     = ob.pose.bones['FrontalLeftWrist']

# right arm bones
frontalRightShoulderBone  = ob.pose.bones['FrontalRightShoulder']
sagittalRightShoulderBone = ob.pose.bones['SagittalRightShoulder']
axialRightShoulderBone    = ob.pose.bones['AxialRightShoulder']
frontalRightElbowBone     = ob.pose.bones['FrontalRightElbow']
axialRightWristBone       = ob.pose.bones['AxialRightWrist']
frontalRightWristBone     = ob.pose.bones['FrontalRightWrist']

# left leg bones
axialLeftHipBone          = ob.pose.bones['AxialSagittalLeftHip']
sagittalLeftHipBone       = ob.pose.bones['FrontalLeftHip']          
frontalLeftHipBone        = ob.pose.bones['FrontalLeftHip']   
frontalLeftKneeBone       = ob.pose.bones['FrontalLeftKnee']   
frontalLeftAnkleBone      = ob.pose.bones['FrontalLeftAnkle']
sagittalLeftAnkleBone     = ob.pose.bones['FrontalLeftAnkle']      

# right leg bones
axialRightHipBone          = ob.pose.bones['AxialSagittalRightHip']
sagittalRightHipBone       = ob.pose.bones['FrontalRightHip']          
frontalRightHipBone        = ob.pose.bones['FrontalRightHip']   
frontalRightKneeBone       = ob.pose.bones['FrontalRightKnee']   
frontalRightAnkleBone      = ob.pose.bones['FrontalRightAnkle']
sagittalRightAnkleBone     = ob.pose.bones['FrontalRightAnkle']     

# trunk bones
frontalTrunkBone             = ob.pose.bones['FrontalTrunk']
axialTrunkBone               = ob.pose.bones['AxialTrunk']


def getJointAngles(pose_bone):
    local_orientation = pose_bone.matrix_channel.to_quaternion()
    if pose_bone.parent is None:
        return local_orientation.to_euler()

    else:
        quaternion_result = local_orientation.rotation_difference(pose_bone.parent.matrix_channel.to_quaternion())
        x = math.degrees( quaternion_result.to_euler().x )
        y = math.degrees( quaternion_result.to_euler().y )
        z = math.degrees( quaternion_result.to_euler().z )
        return (x, y, z)

def processAngles():

    properties = bpy.context.scene.custom_props

    object = bpy.context.object

    # Left Arm: Local axis rotation (x=[0], y=[1], z=[2])
    frontalLeftShoulderAngle  =-getJointAngles(frontalLeftShoulderBone)[2]  # z
    sagittalLeftShoulderAngle = getJointAngles(sagittalLeftShoulderBone)[0] # x
    axialLeftShoulderAngle    =-getJointAngles(axialLeftShoulderBone)[1]    # y
    frontalLeftElbowAngle     =-getJointAngles(frontalLeftElbowBone)[2]     # z
    axialLeftWristAngle       =-getJointAngles(axialLeftWristBone)[1]       # y
    frontalLeftWristAngle     =-getJointAngles(frontalLeftWristBone)[2]     # z

    leftArmBoneAngles = [frontalLeftShoulderAngle,
                         sagittalLeftShoulderAngle,
                         axialLeftShoulderAngle,
                         frontalLeftElbowAngle,
                         axialLeftWristAngle,
                         frontalLeftWristAngle]

    if properties.enableIkLeftArm:
        properties.frontalLeftShoulder  = math.radians(round(frontalLeftShoulderAngle,2))
        properties.sagittalLeftShoulder = math.radians(round(sagittalLeftShoulderAngle,2))
        properties.axialLeftShoulder    = math.radians(round(axialLeftShoulderAngle,2))
        properties.frontalLeftElbow     = math.radians(round(frontalLeftElbowAngle,2))
        properties.axialLeftWrist       = math.radians(round(axialLeftWristAngle,2))
        properties.frontalLeftWrist     = math.radians(round(frontalLeftWristAngle,2))

    # Right Arm: Local axis rotation (x=[0], y=[1], z=[2])
    frontalRightShoulderAngle  =-getJointAngles(frontalRightShoulderBone)[2]  # z
    sagittalRightShoulderAngle = getJointAngles(sagittalRightShoulderBone)[0] # x
    axialRightShoulderAngle    =-getJointAngles(axialRightShoulderBone)[1]    # y
    frontalRightElbowAngle     =-getJointAngles(frontalRightElbowBone)[2]     # z
    axialRightWristAngle       =-getJointAngles(axialRightWristBone)[1]       # y
    frontalRightWristAngle     =-getJointAngles(frontalRightWristBone)[2]     # z

    rightArmBoneAngles = [frontalRightShoulderAngle,
                         sagittalRightShoulderAngle,
                         axialRightShoulderAngle,
                         frontalRightElbowAngle,
                         axialRightWristAngle,
                         frontalRightWristAngle]

    if properties.enableIkRightArm:
        properties.frontalRightShoulder  = math.radians(round(frontalRightShoulderAngle,2))
        properties.sagittalRightShoulder = math.radians(round(sagittalRightShoulderAngle,2))
        properties.axialRightShoulder    = math.radians(round(axialRightShoulderAngle,2))
        properties.frontalRightElbow     = math.radians(round(frontalRightElbowAngle,2))
        properties.axialRightWrist       = math.radians(round(axialRightWristAngle,2))
        properties.frontalRightWrist     = math.radians(round(frontalRightWristAngle,2))
 
    # Left Leg: Local axis rotation (x=[0], y=[1], z=[2])
    axialLeftHipAngle         =-getJointAngles(axialLeftHipBone)[1]      # y
    sagittalLeftHipAngle      = getJointAngles(sagittalLeftHipBone)[0]   # x
    frontalLeftHipAngle       =-getJointAngles(frontalLeftHipBone)[2]    # z
    frontalLeftKneeAngle      =-getJointAngles(frontalLeftKneeBone)[2]   # z
    frontalLeftAnkleAngle     =-getJointAngles(frontalLeftAnkleBone)[2]  # z
    sagittalLeftAnkleAngle    = getJointAngles(sagittalLeftAnkleBone)[0] # x

    leftLegBoneAngles = [axialLeftHipAngle,
                         sagittalLeftHipAngle,
                         frontalLeftHipAngle,
                         frontalLeftKneeAngle,
                         frontalLeftAnkleAngle,
                         sagittalLeftAnkleAngle]

    if properties.enableIkLeftLeg:
        properties.axialLeftHip         = math.radians(round(axialLeftHipAngle,2))
        properties.sagittalLeftHip      = math.radians(round(sagittalLeftHipAngle,2))
        properties.frontalLeftHip       = math.radians(round(frontalLeftHipAngle,2))
        properties.frontalLeftKnee      = math.radians(round(frontalLeftKneeAngle,2))
        properties.frontalLeftAnkle     = math.radians(round(frontalLeftAnkleAngle,2))
        properties.sagittalLeftAnkle    = math.radians(round(sagittalLeftAnkleAngle,2))
    
    # Right Leg: Local axis rotation (x=[0], y=[1], z=[2])
    axialRightHipAngle         =-getJointAngles(axialRightHipBone)[1]      # y
    sagittalRightHipAngle      = getJointAngles(sagittalRightHipBone)[0]   # x
    frontalRightHipAngle       =-getJointAngles(frontalRightHipBone)[2]    # z
    frontalRightKneeAngle      =-getJointAngles(frontalRightKneeBone)[2]   # z
    frontalRightAnkleAngle     =-getJointAngles(frontalRightAnkleBone)[2]  # z
    sagittalRightAnkleAngle    = getJointAngles(sagittalRightAnkleBone)[0] # x

    rightLegBoneAngles = [axialRightHipAngle,
                         sagittalRightHipAngle,
                         frontalRightHipAngle,
                         frontalRightKneeAngle,
                         frontalRightAnkleAngle,
                         sagittalRightAnkleAngle]

    if properties.enableIkRightLeg:
        properties.axialRightHip         = math.radians(round(axialRightHipAngle,2))
        properties.sagittalRightHip      = math.radians(round(sagittalRightHipAngle,2))
        properties.frontalRightHip       = math.radians(round(frontalRightHipAngle,2))
        properties.frontalRightKnee      = math.radians(round(frontalRightKneeAngle,2))
        properties.frontalRightAnkle     = math.radians(round(frontalRightAnkleAngle,2))
        properties.sagittalRightAnkle    = math.radians(round(sagittalRightAnkleAngle,2))
    
    # Trunk
    frontalTrunkAngle = -getJointAngles(frontalTrunkBone)[2] # z
    axialTrunkAngle   = -getJointAngles(axialTrunkBone)[1]   # x

    trunkBoneAngles = [axialTrunkAngle, frontalTrunkAngle]

    if properties.joinIKtoLeftArm or properties.joinIKtoRightArm:
        properties.frontalTrunk = math.radians(round(frontalTrunkAngle,2))
        properties.axialTrunk = math.radians(round(axialTrunkAngle,2))
        
    if properties.enableExport:
        print("Export animation ENABLED")
        if bpy.context.scene.frame_current == bpy.context.scene.frame_end:
            bpy.context.scene.custom_objs.csv_file.close()
            bpy.ops.screen.animation_cancel()
            properties.enableExport = False
            
#------------------------------------NUEVO--------------------------------------------        
        elif bpy.context.scene.custom_props.exportUpperExtremities==True and bpy.context.scene.custom_props.exportLowerExtremities==False:
            bpy.context.scene.custom_objs.csv_obj.writerow(leftArmBoneAngles+rightArmBoneAngles+trunkBoneAngles)
        elif bpy.context.scene.custom_props.exportLowerExtremities==True and bpy.context.scene.custom_props.exportUpperExtremities==False:
            bpy.context.scene.custom_objs.csv_obj.writerow(leftLegBoneAngles+rightLegBoneAngles)
        elif bpy.context.scene.custom_props.exportUpperExtremities==True and bpy.context.scene.custom_props.exportLowerExtremities==True:
            bpy.context.scene.custom_objs.csv_obj.writerow(leftArmBoneAngles+rightArmBoneAngles+trunkBoneAngles+leftLegBoneAngles+rightLegBoneAngles)
        else:
            bpy.context.scene.custom_objs.csv_obj.writerow(leftArmBoneAngles+rightArmBoneAngles+trunkBoneAngles+leftLegBoneAngles+rightLegBoneAngles)
            
#------------------------------------------------------------------------------------------------------------------------------
# Persistent Handler: https://docs.blender.org/api/current/bpy.app.handlers.html#persistent-handler-example

#@persistent
def run(scene):
    processAngles()
    
classes = (
    CustomPropertyGroup,
    OBJECT_OT_HomeLeftArm,
    OBJECT_OT_HomeRightArm,
    OBJECT_PT_LeftArmControlPanel,
    OBJECT_PT_RightArmControlPanel,
    OBJECT_OT_HomeLeftLeg,
    OBJECT_OT_HomeRightLeg,
    OBJECT_PT_LeftLegControlPanel,
    OBJECT_PT_RightLegControlPanel,
    OBJECT_PT_TrunkControlPanel,
    OBJECT_OT_HomeTrunk,
    OBJECT_PT_TrajectoryPanel,
    OBJECT_OT_PlayTrayectory,
    OBJECT_OT_StopTrayectory,
    OBJECT_OT_ExportTrajectory
)

def register():   
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
    
    #this one especially, it adds the property group class to the scene context (instantiates it)
    bpy.types.Scene.custom_props = bpy.props.PointerProperty(type=CustomPropertyGroup)
    bpy.types.Scene.custom_objs = CustomObjectGroup() # class used to share custom objects    
    
    #register the classes with the correct function
    bpy.app.handlers.depsgraph_update_pre.clear() # clear the handler list
    bpy.app.handlers.depsgraph_update_pre.append(run)
    bpy.app.handlers.frame_change_pre.append(run)

#same as register but backwards, deleting references
def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)

    del bpy.types.Scene.custom_props
    del bpy.types.Scene.custom_objs
    

#a quick line to autorun the script from the text editor when we hit 'run script'
if __name__ == '__main__':
    register()