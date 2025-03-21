import cadquery as cq
import pyvista as pv

class Utils:
    def __init__(self, filepath):
        self.mesh = []

        try:
            step_file = cq.importers.importStep(filepath)
            solids = step_file.solids()

            if not isinstance(solids, list):
                solids = [solids]
        except Exception as e:
            print(f"STEP file error: {e}")
            exit()

        obj_filepaths = []

        for s_idx, solid in enumerate(solids):
            for f_idx, face in enumerate(solid.faces()):
                mesh_data = face.tessellate(tolerance=0.1)
                if mesh_data:
                    vertices, triangles = mesh_data
                    obj_filepath = f"solid_{s_idx}_face_{f_idx}.obj"
                    self.export_obj(vertices, triangles, obj_filepath)
                    print(f"Solid {s_idx} Face {f_idx} OBJ Saved: {obj_filepath}")
                    obj_filepaths.append(obj_filepath)

        for obj_filepath in obj_filepaths:
            self.mesh.append(pv.read(obj_filepath))

    def export_obj(self, vertices, triangles, filename):
        with open(filename, 'w') as f:
            for vertex in vertices:
                f.write("v {} {} {}\n".format(vertex.x, vertex.y, vertex.z))
            for triangle in triangles:
                f.write("f {} {} {}\n".format(triangle[0] + 1, triangle[1] + 1, triangle[2] + 1))
