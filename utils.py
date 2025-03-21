import cadquery as cq
import numpy as np
import pyvista as pv

class Utils:
    def __init__(self, filepath, normal_threshold=0.98):
        step_file = cq.importers.importStep(filepath)
        cq.exporters.export(step_file, 'converted.stl', exportType='STL')
        self.mesh = pv.read('converted.stl')
        self.normal_threshold = normal_threshold

    def compute_face_normals(self, faces, points):
        normals = []
        i = 0
        while i < len(faces):
            n = int(faces[i])
            face_ids = faces[i+1 : i+1+n]
            if n >= 3:
                pts = points[face_ids]
                v1 = pts[1] - pts[0]
                v2 = pts[2] - pts[0]
                normal = np.cross(v1, v2)
                norm_val = np.linalg.norm(normal)
                if norm_val != 0:
                    normal = normal / norm_val
                else:
                    normal = np.array([0, 0, 0])
            else:
                normal = np.array([0, 0, 0])
            normals.append(normal)
            i += 1 + n
        return normals

    def group_faces_by_normal(self, normals):
        group_ids = [-1] * len(normals)
        groups = []
        for i, normal in enumerate(normals):
            assigned = False
            for group_index, rep in enumerate(groups):
                if np.dot(normal, rep) >= self.normal_threshold:
                    group_ids[i] = group_index
                    new_rep = rep + normal
                    norm_new = np.linalg.norm(new_rep)
                    if norm_new != 0:
                        groups[group_index] = new_rep / norm_new
                    else:
                        groups[group_index] = rep
                    assigned = True
                    break
            if not assigned:
                groups.append(normal)
                group_ids[i] = len(groups) - 1
        return group_ids

    def process_polydata(self, faces, points):
        normals = self.compute_face_normals(faces, points)
        group_ids = self.group_faces_by_normal(normals)
        return group_ids, normals