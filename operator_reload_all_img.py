import bpy

from bpy.types import Operator


class ReloadAllImages(Operator):
    """Reloads all images currently in the file"""
    bl_idname = "images.reload_all" 
    bl_label = "Reload All Images"
    

    def execute(self, context):
        for image in bpy.data.images:
            image.reload()
        self.report({'INFO'}, ("Reloaded {} images").format(len(bpy.data.images)))
        return {'FINISHED'}


# Only needed if you want to add into a dynamic menu
def menu_func_reload_all_img(self, context):
    self.layout.separator()
    self.layout.operator(ReloadAllImages.bl_idname, text="Reload All Images")

def register():
    bpy.utils.register_class(ReloadAllImages)
    bpy.types.TOPBAR_MT_file_external_data.append(menu_func_reload_all_img)


def unregister():
    bpy.utils.unregister_class(ReloadAllImages)
    bpy.types.TOPBAR_MT_file_external_data.remove(menu_func_reload_all_img)
