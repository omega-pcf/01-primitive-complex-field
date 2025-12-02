"""
Cylinder with P-C-F vertices figure generator.

Shows the base cylinder with vertices P, C, F and the helical curve z = φy,
demonstrating the golden coupling in the cylinder structure.
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
COLOR_P = '#D62728'  # Red
COLOR_C = '#2CA02C'  # Green
COLOR_F = '#1F77B4'  # Blue
COLOR_CYLINDER = '#17BECF'


def get_PCF_vertices_3D(R, z_offset=0):
    """Get P, C, F vertices in 3D with golden coupling z = φy."""
    angles = [0, 2*np.pi/3, 4*np.pi/3]
    vertices = []
    for theta in angles:
        x = R * np.cos(theta)
        y = R * np.sin(theta)
        z = PHI * y + z_offset
        vertices.append([x, y, z])
    return np.array(vertices)


@register("cylinder_pcf")
def generate_cylinder_pcf(output_dir: Path, verbose: bool = False) -> None:
    """
    Generate figure showing cylinder with P-C-F vertices.
    
    Args:
        output_dir: Directory where to save the figure
        verbose: If True, show additional information
    """
    if verbose:
        print("  Generating cylinder PCF figure...")
    
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Cylinder
    theta = np.linspace(0, 2*np.pi, 100)
    z = np.linspace(-6, 6, 50)
    Theta, Z = np.meshgrid(theta, z)
    X = R0 * np.cos(Theta)
    Y = R0 * np.sin(Theta)
    ax.plot_surface(X, Y, Z, alpha=0.15, color=COLOR_CYLINDER, edgecolor='none')
    
    # Helix z = φy
    theta_helix = np.linspace(0, 4*np.pi, 200)
    x_helix = R0 * np.cos(theta_helix)
    y_helix = R0 * np.sin(theta_helix)
    z_helix = PHI * y_helix
    ax.plot(x_helix, y_helix, z_helix, 'k-', linewidth=1.5, alpha=0.6, 
           label='$z = \\varphi y$')
    
    # Vertices P, C, F
    verts = get_PCF_vertices_3D(R0, 0)
    ax.scatter(*verts[0], c=COLOR_P, s=200, marker='o', edgecolors='black', 
              linewidths=1, zorder=5)
    ax.scatter(*verts[1], c=COLOR_C, s=200, marker='o', edgecolors='black', 
              linewidths=1, zorder=5)
    ax.scatter(*verts[2], c=COLOR_F, s=200, marker='o', edgecolors='black', 
              linewidths=1, zorder=5)
    
    # Triangle
    tri = np.vstack([verts, verts[0]])
    ax.plot(tri[:, 0], tri[:, 1], tri[:, 2], 'k-', linewidth=2)
    
    # Labels
    ax.text(verts[0, 0]+0.5, verts[0, 1], verts[0, 2], '$P$', fontsize=14)
    ax.text(verts[1, 0]-0.8, verts[1, 1]+0.5, verts[1, 2], '$C$', fontsize=14)
    ax.text(verts[2, 0]-0.8, verts[2, 1]-0.5, verts[2, 2], '$F$', fontsize=14)
    
    ax.set_xlabel('$x$', fontsize=14)
    ax.set_ylabel('$y$', fontsize=14)
    ax.set_zlabel('$z$', fontsize=14)
    ax.tick_params(labelsize=12)
    ax.legend(loc='upper right', fontsize=12)
    
    plt.tight_layout()
    
    output_path = output_dir / "cylinder_pcf"
    save_figure(fig, output_path, verbose=verbose)
    plt.close(fig)
    
    if verbose:
        print("  ✓ Cylinder PCF figure generated")

