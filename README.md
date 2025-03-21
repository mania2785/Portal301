# 🧩 STEP File Mesh Viewer and Disassembler

A lightweight Python application for viewing and interactively disassembling 3D STEP files. This tool converts STEP solids into OBJ mesh files and renders them using PyVista for high-quality 3D visualization with optional exploded views.

---

## ✨ Features

- 📦 **STEP File Import**: Parses and loads 3D STEP files using CadQuery.
- 🧱 **Mesh Conversion**: Tessellates each face into triangles and exports them as OBJ.
- 🎮 **Interactive 3D Viewer**: View your model in a PyVista window with mouse interaction.
- 🧯 **Exploded View**: Press `D` to toggle a disassembled view that separates faces for better inspection.
- 🗂️ **GUI File Selector**: Simple file browser to choose the input STEP file using Tkinter.

---

## ⚙️ Installation

### ✅ Requirements

- Python 3.8+
- pip

### 📦 Dependencies

Install required packages:

```bash
pip install cadquery pyvista numpy
```

> 💡 Note: CadQuery and PyVista may require platform-specific setup. Check their documentation if issues occur.

---

## 🚀 Usage

1. **Run the Application**

```bash
python main.py
```

2. **Choose STEP File**

Select a `.STEP` file via the popup dialog.

3. **Explore the Mesh**

- Rotate, zoom, and pan the model in the 3D viewer.
- Press `D` to toggle exploded view.
- Boundaries are highlighted with black lines.

---

## 🧠 Room for Exploration & Improvements

Currently, the project starts from STEP files and works well for CAD-based workflows. However, many real-world applications begin with generic 3D mesh formats. Here are some ideas for further development:

### 1. 🗃️ Working with Generic 3D Mesh Files (OBJ, FBX, etc.)

When the original STEP file is unavailable, face grouping becomes a challenge.

#### 1.1 Normal Vector Clustering
Group triangles based on similarity in normal directions.  
> ⚠️ Struggles with curved surfaces where local normals vary smoothly.

#### 1.2 Spectral Clustering with Normals + Centers
Combine triangle normals and their centroid positions to cluster adjacent faces.  
> 💭 RBF kernel spectral clustering was attempted, but the results were unsatisfactory.

#### 1.3 ML-Based Mesh Part Segmentation
Utilize deep learning models trained for 3D part segmentation (e.g., PointNet++, MeshCNN).  
> 🔜 Not yet implemented, but promising avenue for semantic segmentation of parts.

---

## 🧾 Code Structure

```bash
.
├── main.py         # GUI file dialog + app launcher
├── renderer.py     # 3D Viewer and disassembly logic
└── utils.py        # STEP parser, tessellation, and OBJ exporter
```

---