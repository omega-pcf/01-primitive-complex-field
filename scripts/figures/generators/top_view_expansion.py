"""
Top view expansion figure generator.

Shows concentric circles representing different scale levels σ in the XY plane,
with each circle containing the triangle P-C-F, demonstrating the expansion
pattern R_σ = R₀·φ^σ.
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import sys
from pathlib import Path as PathLib

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


@register("top_view_expansion")
def generate_top_view_expansion(output_dir: Path, verbose: bool = False) -> None:
    """
    Generate figure showing top view with concentric circles (expansion).
    
    Args:
        output_dir: Directory where to save the figure
        verbose: If True, show additional information
    """
    if verbose:
        print("  Generating top view expansion figure...")
    
    fig, ax = plt.subplots(figsize=(8, 8))
    
    for sigma in range(5):
        R_sigma = R0 * (PHI ** sigma)
        theta = np.linspace(0, 2*np.pi, 100)
        color = plt.cm.Blues(0.3 + 0.15 * sigma)
        ax.plot(R_sigma * np.cos(theta), R_sigma * np.sin(theta), 
               '-', linewidth=2, color=color, alpha=0.8)
        
        # Triangle
        verts = get_PCF_vertices_2D(R_sigma)
        tri = np.vstack([verts, verts[0]])
        ax.plot(tri[:, 0], tri[:, 1], '-', linewidth=1.5, color=color, alpha=0.6)
        
        # Label positioned diagonally, each at different angle to avoid overlap
        # Vary angle slightly for each sigma to distribute labels diagonally
        base_angle = np.pi / 4  # 45 degrees base
        angle_offset = sigma * 0.15  # Small offset per sigma
        angle_label = base_angle + angle_offset
        label_x = (R_sigma + 0.5) * np.cos(angle_label)
        label_y = (R_sigma + 0.5) * np.sin(angle_label)
        ax.text(label_x, label_y, f'$\\sigma={sigma}$', fontsize=12, 
                ha='left', va='bottom')
    
    ax.set_xlabel('$x$', fontsize=14)
    ax.set_ylabel('$y$', fontsize=14)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_xlim(-25, 25)
    ax.set_ylim(-25, 25)
    ax.tick_params(labelsize=12)
    
    plt.tight_layout()
    
    output_path = output_dir / "top_view_expansion"
    save_figure(fig, output_path, verbose=verbose)
    plt.close(fig)
    
    if verbose:
        print("  ✓ Top view expansion figure generated")

