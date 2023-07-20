bl_info = {
    "name": "Chassis Generator",
    "blender": (2, 80, 0),
    "category": "Object",
}

import bpy

def generate_chassis(wheelbase, track_width, tire_width, aspect_ratio, wheel_diameter):
    

class ChassisGeneratorPanel(bpy.types.Panel):
    bl_label = "Chassis Generator"
    bl_idname = "OBJECT_PT_chassis_generator"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Chassis Generator"
    

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        
        # Wheelbase Input
        layout.label(text=" Wheelbase:")
        row = layout.row()
        row.prop(scene, "wheelbase")
        sub = row.row()
        sub.scale_x = 0.4
        sub.label(text="(mm)")
        
        # Track Width Input
        layout.label(text=" Track Width:")
        row = layout.row()
        row.prop(scene, "track_width")
        sub = row.row()
        sub.scale_x = 0.4
        sub.label(text="(mm)")
        
        # Tire Width Input
        layout.label(text=" Tire Width:")
        row = layout.row()
        row.prop(scene, "tire_width")
        sub = row.row()
        sub.scale_x = 0.4
        sub.label(text="(mm)")
        
        # Aspect Ratio Input
        layout.label(text=" Aspect Ratio:")
        row = layout.row()
        row.prop(scene, "aspect_ratio")
        sub = row.row()
        sub.scale_x = 0.4
        sub.label(text="(R)")
        
        # Wheel Diameter Input
        layout.label(text=" Wheel Diameter:")
        row = layout.row()
        row.prop(scene, "wheel_diameter")
        sub = row.row()
        sub.scale_x = 0.4
        sub.label(text="(in)")
        
        
        
        layout.label(text=" Generate Chassis:")
        row = layout.row()
        row.scale_y = 2.0
        row.operator("object.generate_chassis", text="Create")
        

class OBJECT_OT_generate_chassis(bpy.types.Operator):
    bl_idname = "object.generate_chassis"
    bl_label = "Generate Chassis"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        scene = context.scene
        generate_chassis(
            scene.wheelbase,
            scene.track_width,
            scene.tire_width,
            scene.aspect_ratio,
            scene.wheel_diameter
        )
        return {'FINISHED'}

def register():
    bpy.types.Scene.wheelbase = bpy.props.FloatProperty(name="", default=3000.0, min=1000.0)
    bpy.types.Scene.track_width = bpy.props.FloatProperty(name="", default=1500.0, min=1000.0)
    bpy.types.Scene.tire_width = bpy.props.FloatProperty(name="", default=200.0, min=100.0)
    bpy.types.Scene.aspect_ratio = bpy.props.FloatProperty(name="", default=0.65, min=0.2, max=2.0)
    bpy.types.Scene.wheel_diameter = bpy.props.FloatProperty(name="", default=600.0, min=200.0)

    bpy.utils.register_class(ChassisGeneratorPanel)
    bpy.utils.register_class(OBJECT_OT_generate_chassis)

def unregister():
    bpy.utils.unregister_class(ChassisGeneratorPanel)
    bpy.utils.unregister_class(OBJECT_OT_generate_chassis)
    del bpy.types.Scene.wheelbase
    del bpy.types.Scene.track_width
    del bpy.types.Scene.tire_width
    del bpy.types.Scene.aspect_ratio
    del bpy.types.Scene.wheel_diameter

if __name__ == "__main__":
    register()
