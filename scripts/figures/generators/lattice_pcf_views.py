"""
Lattice PCF views figure generator.

Shows the PCF lattice with cells M_σ = M·φ^σ growing, demonstrating how
the golden ratio φ acts as an expansion factor connecting different scales
of the lattice structure.
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import sys
from pathlib import Path as PathLib
from matplotlib.patches import Rectangle
from matplotlib.ticker import MaxNLocator

_parent_dir = PathLib(__file__).parent.parent
if str(_parent_dir) not in sys.path:
    sys.path.insert(0, str(_parent_dir))

from generators import register
from utils import save_figure, PHI

# Constants
M = 1  # Unit module for clarity
colors = ['#2980b9', '#27ae60', '#f39c12', '#e74c3c', '#9b59b6']  # blue, green, orange, red, purple


@register("lattice_pcf_views")
def generate_lattice_pcf_views(output_dir: Path, verbose: bool = False) -> None:
    """
    Generate figure showing PCF lattice with growing cells.
    
    Args:
        output_dir: Directory where to save the figure
        verbose: If True, show additional information
    """
    if verbose:
        print("  Generating lattice PCF views figure...")
    
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Base lattice points
    for n1 in range(-1, 8):
        for n2 in range(-1, 5):
            ax.scatter(n1*M, n2*M, c='gray', s=20, alpha=0.5)
    
    # Cells at different σ, all from origin
    for sigma in range(4):
        M_sigma = M * PHI**sigma
        rect = Rectangle((0, 0), M_sigma, M_sigma, fill=True,
                         facecolor=colors[sigma], alpha=0.15,
                         edgecolor=colors[sigma], linewidth=2.5)
        ax.add_patch(rect)
    
    # Arrows showing ×φ between consecutive cells
    for sigma in range(3):
        M_s = M * PHI**sigma
        M_s1 = M * PHI**(sigma+1)
        mid = (M_s + M_s1) / 2
        ax.annotate('', xy=(mid, M_s1), xytext=(mid, M_s),
                    arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
        ax.text(mid + 0.1, (M_s + M_s1)/2, r'$\times\varphi$', fontsize=12)
    
    ax.set_xlim(-0.5, 8)
    ax.set_ylim(-0.5, 5)
    ax.set_xlabel('$u$ (Re)', fontsize=14)
    ax.set_ylabel('$v$ (Im)', fontsize=14)
    ax.set_title(r'PCF Lattice: cells $M_\sigma = M \cdot \varphi^\sigma$ growing', 
                 fontsize=14, fontweight='bold')
    ax.set_aspect('equal')
    ax.tick_params(labelsize=12)
    ax.grid(True, alpha=0.3)
    
    # Legend
    legend_elements = []
    for sigma in range(4):
        legend_elements.append(
            plt.Line2D([0], [0], color=colors[sigma], linewidth=2, 
                      label=rf'$\sigma={sigma}$: $M_{sigma}={PHI**sigma:.2f}$')
        )
    ax.legend(handles=legend_elements, loc='upper right', fontsize=12)
    
    plt.tight_layout()
    
    output_path = output_dir / "lattice_pcf_views"
    save_figure(fig, output_path, verbose=verbose)
    plt.close(fig)
    
    if verbose:
        print("  ✓ Lattice PCF views figure generated")

