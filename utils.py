import cadquery as cq
import pyvista as pv

class Utils:
    def __init__(self, filepath):
        step_file = cq.importers.importStep(filepath)
        cq.exporters.export(step_file, 'converted.stl', exportType='STL')

        self.mesh = pv.read('converted.stl')