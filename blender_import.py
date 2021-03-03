import sys
import bpy
import os
from bpy import context

# Read model from last positional argument
filepath = sys.argv[-1]
bpy.ops.import_scene.obj(filepath=filepath)

for ii in range(1, 5):
    bpy.context.scene.frame_set(ii)
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.view3d.camera_to_view_selected()

    bpy.data.scenes['Scene'].render.filepath = os.path.splitext(
        filepath)[0] + "_{:04d}.png".format(ii)
    bpy.data.scenes['Scene'].render.resolution_x = 512
    bpy.data.scenes['Scene'].render.resolution_y = 512

    bpy.ops.render.render(write_still=True)
