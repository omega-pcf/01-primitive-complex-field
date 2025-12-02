"""
Tower of expansion figure generator.

Shows the PCF operator structure across multiple scale levels σ, with each level
showing a cylinder of radius R_σ = R₀·φ^σ containing the triangle P-C-F.
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


@register("tower_expansion")
def generate_tower_expansion(output_dir: Path, verbose: bool = False) -> None:
    """
    Generate figure showing tower of expansion across scale levels σ.
    
    Args:
        output_dir: Directory where to save the figure
        verbose: If True, show additional information
    """
    if verbose:
        print("  Generating tower of expansion figure...")
    
    fig = plt.figure(figsize=(8, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    for sigma in range(5):
        R_sigma = R0 * (PHI ** sigma)
        z_base = sigma * 8
        
        # Translucent cylinder
        theta = np.linspace(0, 2*np.pi, 50)
        z_cyl = np.linspace(z_base - 3, z_base + 3, 10)
        Theta, Z = np.meshgrid(theta, z_cyl)
        X = R_sigma * np.cos(Theta)
        Y = R_sigma * np.sin(Theta)
        ax.plot_surface(X, Y, Z, alpha=0.08, color=COLOR_CYLINDER, edgecolor='none')
        
        # Triangle P-C-F
        verts = get_PCF_vertices_3D(R_sigma, z_base)
        tri = np.vstack([verts, verts[0]])
        ax.plot(tri[:, 0], tri[:, 1], tri[:, 2], 'k-', linewidth=1.5, alpha=0.8)
        
        # Vertices
        ax.scatter(*verts[0], c=COLOR_P, s=100, marker='o', edgecolors='black', 
                  linewidths=0.5, zorder=5)
        ax.scatter(*verts[1], c=COLOR_C, s=100, marker='o', edgecolors='black', 
                  linewidths=0.5, zorder=5)
        ax.scatter(*verts[2], c=COLOR_F, s=100, marker='o', edgecolors='black', 
                  linewidths=0.5, zorder=5)
        
        # Level label
        ax.text(R_sigma + 2, 0, z_base, f'$\\sigma={sigma}$', fontsize=12)
    
    ax.set_xlabel('$x$', fontsize=14)
    ax.set_ylabel('$y$', fontsize=14)
    ax.set_zlabel('$z$', fontsize=14)
    ax.tick_params(labelsize=12)
    ax.set_box_aspect([1, 1, 1.3])
    
    # Simple legend
    ax.scatter([], [], c=COLOR_P, s=80, marker='o', label='$P$')
    ax.scatter([], [], c=COLOR_C, s=80, marker='o', label='$C$')
    ax.scatter([], [], c=COLOR_F, s=80, marker='o', label='$F$')
    ax.legend(loc='upper left', fontsize=12)
    
    plt.tight_layout()
    
    output_path = output_dir / "tower_expansion"
    save_figure(fig, output_path, verbose=verbose)
    plt.close(fig)
    
    if verbose:
        print("  ✓ Tower of expansion figure generated")

