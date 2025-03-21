import pyvista as pv
import numpy as np
from pyvista.core.pointset import PolyData
from utils import Utils

class MeshRenderer:
    def __init__(self, mesh, utils):
        self.mesh: PolyData = mesh
        self.plotter = pv.Plotter(window_size=[1920, 1080])
        self.utils: Utils = utils
        self.highlight_actor = None
        self._setup_plotter()
        
    def _setup_plotter(self):
        self.plotter.add_text("Left-click on a face to highlight its group", 
                              font_size=12, color="white")
        
        group_ids, _ = self.utils.process_polydata(self.mesh.faces, self.mesh.points)
        print(len(group_ids))
        self.mesh.cell_data["group_id"] = np.array(group_ids)

        self.plotter.add_mesh(self.mesh, color="lightgray", pickable=True)
        self.plotter.enable_anti_aliasing('fxaa')
        self.plotter.enable_element_picking(callback=self.pick_callback, 
                                            mode='cell', 
                                            left_clicking=True, 
                                            show_message=False)
        self.plotter.reset_camera()

    def pick_callback(self, picked_mesh):
        if picked_mesh is None:
            return
        
        if "group_id" in picked_mesh.cell_data and len(picked_mesh.cell_data["group_id"]) > 0:
            selected_group_id = int(picked_mesh.cell_data["group_id"][0])
            print(f"Picked group_id: {selected_group_id}")
            
            threshold_mesh = self.mesh.threshold([selected_group_id - 0.5, selected_group_id + 0.5], scalars="group_id")
            
            if self.highlight_actor is not None:
                self.plotter.remove_actor(self.highlight_actor)
            
            self.highlight_actor = self.plotter.add_mesh(threshold_mesh, color="red", opacity=1.0)
            
            self.highlight_actor.GetProperty().SetPolygonOffset(1, 1)
            self.highlight_actor.GetProperty().SetUsePolygonOffset(True)
            
            self.plotter.render()
        else:
            print("No group id")
    def show(self):
        self.plotter.show()