"""
Hypercube projection figure generator.

Shows the 4D PCF hypercube projected to 3D space using the transformation
z → z + φw, demonstrating the structure of the hypercube.
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import sys
from pathlib import Path as PathLib
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import MaxNLocator

_parent_dir = PathLib(__file__).parent.parent
if str(_parent_dir) not in sys.path:
    sys.path.insert(0, str(_parent_dir))

from generators import register
from utils import save_figure, PHI


@register("hypercube_projection")
def generate_hypercube_projection(output_dir: Path, verbose: bool = False) -> None:
    """
    Generate figure showing 4D hypercube projected to 3D.
    
    Args:
        output_dir: Directory where to save the figure
        verbose: If True, show additional information
    """
    if verbose:
        print("  Generating hypercube projection figure...")
    
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    def project_4D_to_3D(v):
        """Project 4D vertex to 3D using z → z + φw."""
        return np.array([v[0], v[1], v[2] + PHI * v[3]])
    
    # Hypercube vertices (16 vertices of 4D cube)
    hypercube = [[(i >> j) & 1 for j in range(4)] for i in range(16)]
    verts_3D = np.array([project_4D_to_3D(v) for v in hypercube])
    
    # Edges
    for i in range(16):
        for j in range(i+1, 16):
            if sum(abs(hypercube[i][k] - hypercube[j][k]) for k in range(4)) == 1:
                ax.plot([verts_3D[i, 0], verts_3D[j, 0]],
                       [verts_3D[i, 1], verts_3D[j, 1]],
                       [verts_3D[i, 2], verts_3D[j, 2]],
                       'b-', alpha=0.6, linewidth=1.2)
    
    ax.scatter(verts_3D[:, 0], verts_3D[:, 1], verts_3D[:, 2], 
              c='red', s=40, edgecolors='black', linewidths=0.5)
    
    ax.set_xlabel('$u$', fontsize=14)
    ax.set_ylabel('$v$', fontsize=14)
    ax.set_zlabel('$z + \\varphi w$', fontsize=14)
    ax.tick_params(labelsize=12)
    ax.set_box_aspect([1, 1, 1])
    
    plt.tight_layout()
    
    output_path = output_dir / "hypercube_projection"
    save_figure(fig, output_path, verbose=verbose)
    plt.close(fig)
    
    if verbose:
        print("  ✓ Hypercube projection figure generated")

