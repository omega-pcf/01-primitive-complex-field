"""
Combined lattice PCF and square projection figure generator.

Shows two related views:
1. PCF lattice with cells M_σ = M·φ^σ growing
2. Square to rectangle projection via golden coupling φ
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import sys
from pathlib import Path as PathLib
from matplotlib.patches import Rectangle

_parent_dir = PathLib(__file__).parent.parent
if str(_parent_dir) not in sys.path:
    sys.path.insert(0, str(_parent_dir))

from generators import register
from utils import save_figure, PHI

# Constants
M = 1  # Unit module for clarity
colors = ['#2980b9', '#27ae60', '#f39c12', '#e74c3c', '#9b59b6']  # blue, green, orange, red, purple


@register("lattice_square_combined")
def generate_lattice_square_combined(output_dir: Path, verbose: bool = False) -> None:
    """
    Generate combined figure showing lattice PCF and square projection.
    
    Args:
        output_dir: Directory where to save the figure
        verbose: If True, show additional information
    """
    if verbose:
        print("  Generating combined lattice-square figure...")
    
    fig, axes = plt.subplots(1, 2, figsize=(16, 8))
    
    # === Panel 1: PCF Lattice with growing cells ===
    ax1 = axes[0]
    
    # Base lattice points
    for n1 in range(-1, 8):
        for n2 in range(-1, 5):
            ax1.scatter(n1*M, n2*M, c='gray', s=20, alpha=0.5)
    
    # Cells at different σ, all from origin
    for sigma in range(4):
        M_sigma = M * PHI**sigma
        rect = Rectangle((0, 0), M_sigma, M_sigma, fill=True,
                         facecolor=colors[sigma], alpha=0.15,
                         edgecolor=colors[sigma], linewidth=2.5)
        ax1.add_patch(rect)
    
    # Arrows showing ×φ between consecutive cells
    for sigma in range(3):
        M_s = M * PHI**sigma
        M_s1 = M * PHI**(sigma+1)
        mid = (M_s + M_s1) / 2
        ax1.annotate('', xy=(mid, M_s1), xytext=(mid, M_s),
                    arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
        ax1.text(mid + 0.1, (M_s + M_s1)/2, r'$\times\varphi$', fontsize=14)
    
    ax1.set_xlim(-0.5, 8)
    ax1.set_ylim(-0.5, 5)
    ax1.set_xlabel('$u$ (Re)', fontsize=14)
    ax1.set_ylabel('$v$ (Im)', fontsize=14)
    ax1.set_aspect('equal')
    ax1.tick_params(labelsize=12)
    ax1.grid(True, alpha=0.3)
    
    # Legend
    legend_elements = []
    for sigma in range(4):
        legend_elements.append(
            plt.Line2D([0], [0], color=colors[sigma], linewidth=2, 
                      label=rf'$\sigma={sigma}$: $M_{sigma}={PHI**sigma:.2f}$')
        )
    ax1.legend(handles=legend_elements, loc='upper right', fontsize=12)
    
    # === Panel 2: Square to rectangle projection ===
    ax2 = axes[1]
    
    # Original square
    sq = np.array([[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]])
    ax2.plot(sq[:, 0], sq[:, 1], 'b-', linewidth=2, label='Square in $(u, w)$')
    ax2.fill(sq[:-1, 0], sq[:-1, 1], alpha=0.2, color='blue')
    
    # Projected rectangle
    sq_proj = np.array([[0, 0], [1, 0], [1, PHI], [0, PHI], [0, 0]])
    ax2.plot(sq_proj[:, 0], sq_proj[:, 1], 'r-', linewidth=2, 
           label='Projected $(u, z+\\varphi w)$')
    ax2.fill(sq_proj[:-1, 0], sq_proj[:-1, 1], alpha=0.2, color='red')
    
    # Label
    ax2.annotate('', xy=(0.5, PHI + 0.1), xytext=(0.5, 1.1),
               arrowprops=dict(arrowstyle='->', color='gray', lw=1.5))
    ax2.text(0.6, (1 + PHI)/2, r'$\times \varphi$', fontsize=14)
    
    ax2.set_xlabel('$u$', fontsize=14)
    ax2.set_ylabel('$z + \\varphi w$', fontsize=14)
    ax2.set_aspect('equal')
    ax2.legend(fontsize=12, loc='upper left')
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim(-0.3, 1.5)
    ax2.set_ylim(-0.3, 2)
    ax2.tick_params(labelsize=12)
    
    plt.tight_layout()
    
    output_path = output_dir / "lattice_square_combined"
    save_figure(fig, output_path, verbose=verbose)
    plt.close(fig)
    
    if verbose:
        print("  ✓ Combined lattice-square figure generated")

