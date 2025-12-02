"""
Tower of contraction (multi-level Sierpiński) figure generator.

Shows the Sierpiński triangle structure at different recursion levels σ,
demonstrating the fractal contraction pattern.
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

# Constants
R0 = 3.0


def get_PCF_vertices_2D(R):
    """Get P, C, F vertices in 2D (XY plane)."""
    angles = [0, 2*np.pi/3, 4*np.pi/3]
    return np.array([[R * np.cos(a), R * np.sin(a)] for a in angles])


@register("tower_contraction")
def generate_tower_contraction(output_dir: Path, verbose: bool = False) -> None:
    """
    Generate figure showing tower of contraction (multi-level Sierpiński).
    
    Args:
        output_dir: Directory where to save the figure
        verbose: If True, show additional information
    """
    if verbose:
        print("  Generating tower of contraction figure...")
    
    fig = plt.figure(figsize=(8, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    def draw_sierpinski_3D(ax, verts_2d, level, max_level, z_base, color, alpha):
        """Recursively draw Sierpiński triangle in 3D."""
        if level >= max_level:
            v3d = np.array([[v[0], v[1], PHI*v[1] + z_base] for v in verts_2d])
            tri = np.vstack([v3d, v3d[0]])
            ax.plot(tri[:, 0], tri[:, 1], tri[:, 2], '-', color=color, 
                   linewidth=0.6, alpha=alpha)
            return
        m01 = (verts_2d[0] + verts_2d[1]) / 2
        m12 = (verts_2d[1] + verts_2d[2]) / 2
        m20 = (verts_2d[2] + verts_2d[0]) / 2
        draw_sierpinski_3D(ax, [verts_2d[0], m01, m20], level+1, max_level, 
                          z_base, color, alpha)
        draw_sierpinski_3D(ax, [m01, verts_2d[1], m12], level+1, max_level, 
                          z_base, color, alpha)
        draw_sierpinski_3D(ax, [m20, m12, verts_2d[2]], level+1, max_level, 
                          z_base, color, alpha)
    
    base_verts = get_PCF_vertices_2D(R0)
    
    for sigma in range(5):
        z_base = sigma * 5
        color = plt.cm.viridis(sigma / 5)
        if sigma < 5:
            draw_sierpinski_3D(ax, base_verts, 0, sigma, z_base, color, 0.8)
        
        ax.text(R0 + 0.5, 0, z_base, f'$\\sigma={sigma}$', fontsize=12)
    
    ax.set_xlabel('$x$', fontsize=14)
    ax.set_ylabel('$y$', fontsize=14)
    ax.set_zlabel('$z$', fontsize=14)
    ax.tick_params(labelsize=12)
    ax.set_xlim(-4, 5)
    ax.set_ylim(-4, 4)
    ax.set_box_aspect([1, 1, 1.2])
    
    plt.tight_layout()
    
    output_path = output_dir / "tower_contraction"
    save_figure(fig, output_path, verbose=verbose)
    plt.close(fig)
    
    if verbose:
        print("  ✓ Tower of contraction figure generated")

