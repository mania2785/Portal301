import pyvista as pv
import numpy as np
from pyvista.core.pointset import PolyData

class MeshRenderer:
    def __init__(self, mesh: list[PolyData], gap: float = 25.0):
        self.mesh = mesh
        self.plotter = pv.Plotter(window_size=[1920, 1080])
        self.disassembled = False
        self.gap = gap
        
        self.original_points = [m.points.copy() for m in self.mesh]
        
        centers = np.array([m.center for m in self.mesh])
        overall_center = centers.mean(axis=0)
        
        self.offsets = []
        for m in self.mesh:
            direction = m.center - overall_center
            norm = np.linalg.norm(direction)
            if norm != 0:
                direction = direction / norm
            else:
                direction = np.array([0, 0, 0])
            self.offsets.append(direction * self.gap)

        self._setup_plotter()
        
    def _setup_plotter(self):
        self.plotter.add_text("Left-click on a face to highlight its group", 
                              font_size=12, color="black")
        
        for i, mesh in enumerate(self.mesh):
            self.plotter.add_mesh(mesh, color='lightgray', label=f"Face {i}")

        self.plotter.enable_anti_aliasing('fxaa')

        self.plotter.enable_element_picking(callback=self.pick_callback, mode='mesh', left_clicking=True, show_message=False)
        self.plotter.add_key_event("d", self.toggle_disassemble)
        self.plotter.reset_camera()

    def pick_callback(self, picked_mesh):
        if picked_mesh is None:
            return
        
    def toggle_disassemble(self):
        if not self.disassembled:
            for i, m in enumerate(self.mesh):
                new_points = self.original_points[i] + self.offsets[i]
                m.points[:] = new_points
        else:
            for i, m in enumerate(self.mesh):
                m.points[:] = self.original_points[i]
        self.disassembled = not self.disassembled
        self.plotter.render()

    def show(self):
        self.plotter.show()