"""
Torus PCF figure generator.

Shows the PCF torus with vertices P, C, F marked, demonstrating the toroidal
structure obtained from the cylinder via immersion.
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
from utils import save_figure

# Constants
R0 = 3.0
COLOR_P = '#D62728'  # Red
COLOR_C = '#2CA02C'  # Green
COLOR_F = '#1F77B4'  # Blue


@register("torus_pcf")
def generate_torus_pcf(output_dir: Path, verbose: bool = False) -> None:
    """
    Generate figure showing PCF torus.
    
    Args:
        output_dir: Directory where to save the figure
        verbose: If True, show additional information
    """
    if verbose:
        print("  Generating torus PCF figure...")
    
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    R_major = R0
    r_minor = R0 * (1 + np.sqrt(5))/2 / (2 * np.pi)
    
    u = np.linspace(0, 2*np.pi, 60)
    v = np.linspace(0, 2*np.pi, 60)
    U, V = np.meshgrid(u, v)
    
    X = (R_major + r_minor * np.cos(V)) * np.cos(U)
    Y = (R_major + r_minor * np.cos(V)) * np.sin(U)
    Z = r_minor * np.sin(V)
    
    ax.plot_surface(X, Y, Z, alpha=0.4, cmap='coolwarm', edgecolor='none')
    
    # Mark P, C, F
    for angle, color, label in zip([0, 2*np.pi/3, 4*np.pi/3], 
                                    [COLOR_P, COLOR_C, COLOR_F], 
                                    ['$P$', '$C$', '$F$']):
        x = (R_major + r_minor) * np.cos(angle)
        y = (R_major + r_minor) * np.sin(angle)
        z = 0
        ax.scatter([x], [y], [z], c=color, s=150, marker='o', 
                  edgecolors='black', linewidths=1, zorder=5)
        ax.text(x*1.15, y*1.15, z+0.3, label, fontsize=14)
    
    ax.set_xlabel('$x$', fontsize=14)
    ax.set_ylabel('$y$', fontsize=14)
    ax.set_zlabel('$z$', fontsize=14)
    ax.tick_params(labelsize=12)
    ax.set_box_aspect([1, 1, 0.4])
    
    plt.tight_layout()
    
    output_path = output_dir / "torus_pcf"
    save_figure(fig, output_path, verbose=verbose)
    plt.close(fig)
    
    if verbose:
        print("  ✓ Torus PCF figure generated")

