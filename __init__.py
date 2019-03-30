import bpy
import bpy_extras.io_utils
from bpy.types import Operator, AddonPreferences
from bpy.props import *
from bpy_extras.io_utils import ExportHelper, ImportHelper
from bpy.utils import register_class
from bpy.utils import unregister_class

bl_info = {
    "name": "SEModel Support",
    "author": "DTZxPorter",
    "version": (0, 0, 1),
    "blender": (2, 80, 0),
    "location": "File > Import",
    "description": "Import SEModel",
    "wiki_url": "https://github.com/dtzxporter/io_model_semodel",
    "tracker_url": "https://github.com/dtzxporter/io_model_semodel/issues",
    "support": "COMMUNITY",
    "category": "Import-Export"
}


class ImportSEModel(bpy.types.Operator, ImportHelper):
    bl_idname = "import_scene.semodel"
    bl_label = "Import SEModel"
    bl_description = "Import one or more SEModel files"
    bl_options = {'PRESET'}

    filename_ext = ".semodel"
    filter_glob: StringProperty(default="*.semodel", options={'HIDDEN'})

    files: CollectionProperty(type=bpy.types.PropertyGroup)

    def execute(self, context):
        from . import import_semodel
        result = import_semodel.load(
            self, context, **self.as_keywords(ignore=("filter_glob", "files")))
        if result:
            self.report({'INFO'}, 'SEModel has been loaded')
            return {'FINISHED'}
        else:
            self.report({'ERROR'}, 'Failed to load SEModel')
            return {'CANCELLED'}

    @classmethod
    def poll(self, context):
        return True


def menu_func_semodel_import(self, context):
    self.layout.operator(ImportSEModel.bl_idname, text="SEModel (.semodel)")


def register():
    bpy.utils.register_class(ImportSEModel)
    bpy.types.TOPBAR_MT_file_import.append(menu_func_semodel_import)


def unregister():
    bpy.utils.unregister_module(__name__)
    bpy.types.TOPBAR_MT_file_import.remove(menu_func_semodel_import)


if __name__ == "__main__":
    register()
