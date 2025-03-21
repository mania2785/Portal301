from renderer import MeshRenderer
from utils import Utils
import tkinter as tk
from tkinter import filedialog

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(
        initialdir="/",
        title="Select STEP File",
        filetypes=(("STEP File", "*.STEP"), ("All Files", "*.*"))
    )

    if file_path:
        utils = Utils(file_path)
        renderer = MeshRenderer(utils.mesh)

    renderer.show()