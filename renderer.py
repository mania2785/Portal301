import pyvista as pv

class MeshRenderer:
    def __init__(self, mesh):
        self.mesh = mesh
        self.actor_group_mapping = {}
        self.plotter = pv.Plotter()
        self._setup_plotter()
        
    def _setup_plotter(self):
        self.plotter.add_text("Left-click on a face to highlight its group", 
                              font_size=12, color="white")
        self.plotter.add_mesh(self.mesh, color="lightgray", pickable=True)
        self.plotter.reset_camera()

    def show(self):
        self.plotter.show()