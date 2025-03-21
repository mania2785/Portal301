import pyvista as pv
from pyvista.core.pointset import PolyData

class MeshRenderer:
    def __init__(self, mesh: list[PolyData]):
        self.mesh = mesh
        self.plotter = pv.Plotter(window_size=[1920, 1080])
        self._setup_plotter()
        
    def _setup_plotter(self):
        self.plotter.add_text("Left-click on a face to highlight its group", 
                              font_size=12, color="white")
        
        for i, mesh in enumerate(self.mesh):
            self.plotter.add_mesh(mesh, color='lightgray', label=f"Face {i}")

        self.plotter.enable_anti_aliasing('fxaa')

        self.plotter.enable_element_picking(callback=self.pick_callback, mode='mesh', left_clicking=True, show_message=False)
        self.plotter.reset_camera()

    def pick_callback(self, picked_mesh):
        if picked_mesh is None:
            return

    def show(self):
        self.plotter.show()