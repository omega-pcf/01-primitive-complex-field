"""
Towers comparison figure generator.

Shows the two interpretations of the multi-level PCF tower:
1. Expansion tower (Figure 5 of the paper): R_σ = R₀·φ^σ (grows with σ)
2. Contraction tower (Sierpiński): R_σ = R₀·(1/2)^σ (shrinks with σ)
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


@register("towers_comparison")
def generate_towers_comparison(output_dir: Path, verbose: bool = False) -> None:
    """
    Generate figure comparing expansion and contraction towers.
    
    Args:
        output_dir: Directory where to save the figure
        verbose: If True, show additional information
    """
    if verbose:
        print("  Generating towers comparison figure...")
    
    fig = plt.figure(figsize=(18, 8))
    colors = [COLOR_P, COLOR_C, COLOR_F]
    
    # === Expansion Tower (left panel) ===
    ax1 = fig.add_subplot(121, projection='3d')
    
    for sigma in range(5):
        R_sigma = R0 * (PHI ** sigma)
        z_base = sigma * 8
        
        vertices = get_PCF_vertices_3D(R_sigma, z_base)
        triangle = np.vstack([vertices, vertices[0]])
        
        ax1.plot(triangle[:, 0], triangle[:, 1], triangle[:, 2], 
                'c-', linewidth=2, alpha=0.8)
        
        for v, c in zip(vertices, colors):
            ax1.scatter(*v, c=c, s=80, marker='x', linewidths=2)
        
        # Cylinder
        theta = np.linspace(0, 2*np.pi, 50)
        z_cyl = np.linspace(z_base - 3, z_base + 3, 5)
        Theta, Z = np.meshgrid(theta, z_cyl)
        X = R_sigma * np.cos(Theta)
        Y = R_sigma * np.sin(Theta)
        ax1.plot_surface(X, Y, Z, alpha=0.08, color='cyan')
    
    ax1.set_title('Expansion Tower\n$R_\\sigma = R_0 \\cdot \\varphi^\\sigma$', 
                  fontsize=14, fontweight='bold')
    ax1.set_xlabel('$x$', fontsize=14)
    ax1.set_ylabel('$y$', fontsize=14)
    ax1.set_zlabel('$z$ (level $\\sigma$)', fontsize=14)
    ax1.tick_params(labelsize=12)
    ax1.text(0, 0, 35, '$\\uparrow$ $\\sigma$ increases\nRadius GROWS', 
            fontsize=12, ha='center')
    
    # === Contraction Tower (right panel) ===
    ax2 = fig.add_subplot(122, projection='3d')
    
    for sigma in range(5):
        R_sigma = R0 * (0.5 ** sigma)
        z_base = sigma * 3
        
        vertices = get_PCF_vertices_3D(R_sigma, z_base)
        triangle = np.vstack([vertices, vertices[0]])
        
        ax2.plot(triangle[:, 0], triangle[:, 1], triangle[:, 2], 
                'm-', linewidth=2, alpha=0.8)
        
        for v, c in zip(vertices, colors):
            ax2.scatter(*v, c=c, s=80, marker='x', linewidths=2)
        
        # Cylinder
        theta = np.linspace(0, 2*np.pi, 50)
        z_cyl = np.linspace(z_base - 1, z_base + 1, 5)
        Theta, Z = np.meshgrid(theta, z_cyl)
        X = R_sigma * np.cos(Theta)
        Y = R_sigma * np.sin(Theta)
        ax2.plot_surface(X, Y, Z, alpha=0.08, color='magenta')
    
    ax2.set_title('Contraction Tower\n$R_\\sigma = R_0 \\cdot (1/2)^\\sigma$\n(Sierpiński)', 
                  fontsize=14, fontweight='bold')
    ax2.set_xlabel('$x$', fontsize=14)
    ax2.set_ylabel('$y$', fontsize=14)
    ax2.set_zlabel('$z$ (level $\\sigma$)', fontsize=14)
    ax2.tick_params(labelsize=12)
    ax2.text(0, 0, 15, '$\\uparrow$ $\\sigma$ increases\nRadius SHRINKS', 
            fontsize=12, ha='center')
    
    plt.tight_layout()
    
    output_path = output_dir / "towers_comparison"
    save_figure(fig, output_path, verbose=verbose)
    plt.close(fig)
    
    if verbose:
        print("  ✓ Towers comparison figure generated")

