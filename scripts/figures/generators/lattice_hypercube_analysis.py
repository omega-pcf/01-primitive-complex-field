"""
Lattice hypercube analysis figure generator.

Shows the PCF lattice scaling across multiple σ levels, demonstrating how
the lattice expands with σ according to M_σ = φ^σ · M_PCF.
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import sys
from pathlib import Path as PathLib
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import MaxNLocator

# Add parent directory to path for imports
_parent_dir = PathLib(__file__).parent.parent
if str(_parent_dir) not in sys.path:
    sys.path.insert(0, str(_parent_dir))

from generators import register
from utils import save_figure, PHI

# Constants
epsilon_0 = np.log(PHI) / (6 * np.sqrt(3))  # ≈ 0.0463
M_PCF = np.pi / epsilon_0  # Topological module ≈ 67.846


@register("lattice_hypercube_analysis")
def generate_lattice_hypercube_analysis(output_dir: Path, verbose: bool = False) -> None:
    """
    Generate figure showing PCF lattice scaling across multiple σ levels.
    
    Args:
        output_dir: Directory where to save the figure
        verbose: If True, show additional information
    """
    if verbose:
        print("  Generating lattice hypercube analysis figure...")
    
    # Create figure with 3 panels
    fig = plt.figure(figsize=(18, 6))
    
    # Levels to visualize
    sigma_levels = [0, 1, 2, 3]
    colors = ['blue', 'green', 'orange', 'red']
    
    # === Panel 1: 3D view with σ as vertical axis (absolute coordinates) ===
    ax1 = fig.add_subplot(131, projection='3d')
    
    for sigma, color in zip(sigma_levels, colors):
        M_sigma = (PHI ** sigma) * M_PCF
        
        # Generate lattice points at this level
        n = 2  # points in each direction
        for n1 in range(-n, n + 1):
            for n2 in range(-n, n + 1):
                u = n1 * M_sigma
                v = n2 * M_sigma
                # σ is the vertical axis (multiplied by scale for visualization)
                z_vis = sigma * 50  # visual scale
                ax1.scatter(u, v, z_vis, c=color, s=50, alpha=0.8)
        
        # Draw fundamental cell
        cell = M_sigma * np.array([
            [0, 0], [1, 0], [1, 1], [0, 1], [0, 0]
        ])
        ax1.plot(cell[:, 0], cell[:, 1], [z_vis]*5, c=color, linewidth=2, alpha=0.7)
    
    ax1.set_xlabel('u (Re)', fontsize=14)
    ax1.set_ylabel('v (Im)', fontsize=14)
    ax1.set_zlabel('σ (level)', fontsize=14)
    ax1.set_title('PCF Hypercube\n(Absolute coordinates)', fontsize=14, fontweight='bold')
    ax1.tick_params(labelsize=12)
    ax1.xaxis.set_major_locator(MaxNLocator(4))
    ax1.yaxis.set_major_locator(MaxNLocator(4))
    ax1.zaxis.set_major_locator(MaxNLocator(4))
    
    # === Panel 2: Lattice EXPANDS with σ (2D view) ===
    ax2 = fig.add_subplot(132)
    
    for sigma, color in zip(sigma_levels, colors):
        M_sigma = (PHI ** sigma) * M_PCF
        n = 3
        for n1 in range(-n, n + 1):
            for n2 in range(-n, n + 1):
                u = n1 * M_sigma
                v = n2 * M_sigma
                ax2.scatter(u, v, c=color, s=30, alpha=0.6, 
                           label=f'σ={sigma}' if n1==-n and n2==-n else '')
        
        # Fundamental cell
        cell = M_sigma * np.array([[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]])
        ax2.plot(cell[:, 0], cell[:, 1], c=color, linewidth=2)
    
    ax2.set_xlabel('u (Re)', fontsize=14)
    ax2.set_ylabel('v (Im)', fontsize=14)
    ax2.set_title('Lattice expands with σ\nM_σ = φ^σ · M_PCF', fontsize=14, fontweight='bold')
    ax2.legend(loc='upper right', fontsize=12)
    ax2.set_aspect('equal')
    ax2.tick_params(labelsize=12)
    ax2.grid(True, alpha=0.3)
    
    # === Panel 3: Lattice density in fixed volume ===
    ax3 = fig.add_subplot(133)
    
    # In a fixed volume, how many points are there from each level?
    L_fixed = 150  # Fixed volume [-L, L] x [-L, L]
    
    for sigma, color in zip(sigma_levels, colors):
        M_sigma = (PHI ** sigma) * M_PCF
        n_max = int(L_fixed / M_sigma) + 1
        count = 0
        for n1 in range(-n_max, n_max + 1):
            for n2 in range(-n_max, n_max + 1):
                u = n1 * M_sigma
                v = n2 * M_sigma
                if abs(u) <= L_fixed and abs(v) <= L_fixed:
                    ax3.scatter(u, v, c=color, s=20, alpha=0.5)
                    count += 1
    
    ax3.axhline(y=L_fixed, color='gray', linestyle='--', alpha=0.5)
    ax3.axhline(y=-L_fixed, color='gray', linestyle='--', alpha=0.5)
    ax3.axvline(x=L_fixed, color='gray', linestyle='--', alpha=0.5)
    ax3.axvline(x=-L_fixed, color='gray', linestyle='--', alpha=0.5)
    
    ax3.set_xlabel('u (Re)', fontsize=14)
    ax3.set_ylabel('v (Im)', fontsize=14)
    ax3.set_title(f'Fixed volume [-{L_fixed}, {L_fixed}]²\n(lower σ = denser)', fontsize=14, fontweight='bold')
    ax3.set_aspect('equal')
    ax3.set_xlim(-L_fixed*1.1, L_fixed*1.1)
    ax3.set_ylim(-L_fixed*1.1, L_fixed*1.1)
    ax3.tick_params(labelsize=12)
    ax3.grid(True, alpha=0.3)
    
    plt.tight_layout(pad=3.0)
    
    # Save figure
    output_path = output_dir / "lattice_hypercube_analysis"
    save_figure(fig, output_path, verbose=verbose)
    
    # Cleanup
    plt.close(fig)
    
    if verbose:
        print("  ✓ Lattice hypercube analysis figure generated")

