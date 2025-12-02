"""
PCF hypercube tower comparison figure generator.

Shows the duality of the hypercube structure:
1. Tower where each level has MORE points (lattice expands)
2. Fixed region view showing densification (lower levels = more points)
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
epsilon_0 = np.log(PHI) / (6 * np.sqrt(3))
M_PCF = np.pi / epsilon_0

# Colors for each level
colors = {
    0: '#2980b9',  # blue
    1: '#27ae60',  # green
    2: '#f39c12',  # orange
    3: '#e74c3c',  # red
    4: '#9b59b6',  # purple
}


@register("hypercube_tower")
def generate_hypercube_tower(output_dir: Path, verbose: bool = False) -> None:
    """
    Generate figure comparing tower expansion vs densification.
    
    Args:
        output_dir: Directory where to save the figure
        verbose: If True, show additional information
    """
    if verbose:
        print("  Generating hypercube tower figure...")
    
    fig = plt.figure(figsize=(18, 8))
    
    # === Panel 1: Tower where each level has MORE points (lattice expands) ===
    ax1 = fig.add_subplot(121, projection='3d')
    
    for sigma in range(5):
        M_sigma = (PHI ** sigma) * M_PCF
        z_level = sigma * 12
        
        # Points extend more at higher levels
        n = 2 + sigma  # More points at higher levels
        
        for n1 in range(-n, n + 1):
            for n2 in range(-n, n + 1):
                u = n1 * M_sigma
                v = n2 * M_sigma
                ax1.scatter(u, v, z_level, c=colors[sigma], s=50, alpha=0.7)
        
        # Fundamental cell
        cell = np.array([[0, 0], [M_sigma, 0], [M_sigma, M_sigma], 
                         [0, M_sigma], [0, 0]])
        ax1.plot(cell[:, 0], cell[:, 1], [z_level]*5, 
                color=colors[sigma], linewidth=2.5)
        
        # Label
        ax1.text(M_sigma*1.1, 0, z_level, f'$\\sigma={sigma}$\n$M={M_sigma:.0f}$', 
                fontsize=11, color=colors[sigma])
    
    ax1.set_xlabel('$u$ (Re)', fontsize=14)
    ax1.set_ylabel('$v$ (Im)', fontsize=14)
    ax1.set_zlabel('$\\sigma$ (level)', fontsize=14)
    ax1.set_title('PCF Tower: Lattice EXPANDS with $\\sigma$\n$M_\\sigma = \\varphi^\\sigma \\cdot M_0$', 
                  fontsize=14, fontweight='bold')
    ax1.tick_params(labelsize=12)
    ax1.view_init(elev=20, azim=30)
    
    # === Panel 2: View showing densification (fixed region) ===
    ax2 = fig.add_subplot(122, projection='3d')
    L = M_PCF * 0.8  # Fixed small region
    
    for sigma in range(5):
        M_sigma = (PHI ** sigma) * M_PCF
        z_level = sigma * 12
        
        n_max = int(L / M_sigma) + 1
        count = 0
        
        for n1 in range(-n_max, n_max + 1):
            for n2 in range(-n_max, n_max + 1):
                u = n1 * M_sigma
                v = n2 * M_sigma
                if abs(u) <= L and abs(v) <= L:
                    ax2.scatter(u, v, z_level, c=colors[sigma], s=60, alpha=0.8)
                    count += 1
        
        # Fixed region
        rect = np.array([[-L, -L], [L, -L], [L, L], [-L, L], [-L, -L]])
        ax2.plot(rect[:, 0], rect[:, 1], [z_level]*5, 
                '--', color='gray', linewidth=1, alpha=0.5)
        
        ax2.text(L*1.2, L*1.2, z_level, f'#{count}pts', 
                fontsize=10, color=colors[sigma])
    
    ax2.set_xlabel('$u$ (Re)', fontsize=14)
    ax2.set_ylabel('$v$ (Im)', fontsize=14)
    ax2.set_zlabel('$\\sigma$ (level)', fontsize=14)
    ax2.set_title(f'Fixed Region $L={L:.0f}$: DENSIFICATION\nLower levels = more points', 
                  fontsize=14, fontweight='bold')
    ax2.tick_params(labelsize=12)
    ax2.view_init(elev=20, azim=30)
    
    plt.tight_layout()
    
    output_path = output_dir / "hypercube_tower"
    save_figure(fig, output_path, verbose=verbose)
    plt.close(fig)
    
    if verbose:
        print("  ✓ Hypercube tower figure generated")

