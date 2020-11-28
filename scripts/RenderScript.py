import bpy  # The blender library

path = "/home/nutt/RT-TDDFT/Blender/" #Path with the obj files
for i in range(0,250): # 250 isosurfaces
    bpy.ops.import_scene.obj(filepath=path+str(i)+".obj") # Opens an isosurface
    D = bpy.data # Gathers the data of the object
    orbital = bpy.context.selected_objects[0].name # The name of the orbital object (actually, isosurface)
    D.objects[orbital].material_slots[0].material = D.materials['Glass'] # Assigns the material that I previously set up
    bpy.data.scenes['Scene'].render.filepath = path+str(i)+".png" # Render an image
    bpy.ops.render.render( write_still=True ) 
    bpy.ops.object.select_all(action='DESELECT') # Deselects everything
    bpy.data.objects[orbital].select = True # Selects the isosurface
    bpy.ops.object.delete() # Deletes the isosurface
