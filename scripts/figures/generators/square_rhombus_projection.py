"""
Square to rhombus projection figure generator.

Shows how a square in (u, w) coordinates projects to a rectangle in (u, z+φw)
coordinates, demonstrating the golden coupling transformation.
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


@register("square_rhombus_projection")
def generate_square_rhombus_projection(output_dir: Path, verbose: bool = False) -> None:
    """
    Generate figure showing square to rhombus projection.
    
    Args:
        output_dir: Directory where to save the figure
        verbose: If True, show additional information
    """
    if verbose:
        print("  Generating square to rhombus projection figure...")
    
    fig, ax = plt.subplots(figsize=(7, 6))
    
    # Original square
    sq = np.array([[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]])
    ax.plot(sq[:, 0], sq[:, 1], 'b-', linewidth=2, label='Square in $(u, w)$')
    ax.fill(sq[:-1, 0], sq[:-1, 1], alpha=0.2, color='blue')
    
    # Projected
    sq_proj = np.array([[0, 0], [1, 0], [1, PHI], [0, PHI], [0, 0]])
    ax.plot(sq_proj[:, 0], sq_proj[:, 1], 'r-', linewidth=2, 
           label='Projected $(u, z+\\varphi w)$')
    ax.fill(sq_proj[:-1, 0], sq_proj[:-1, 1], alpha=0.2, color='red')
    
    # Label
    ax.annotate('', xy=(0.5, PHI + 0.1), xytext=(0.5, 1.1),
               arrowprops=dict(arrowstyle='->', color='gray', lw=1.5))
    ax.text(0.6, (1 + PHI)/2, r'$\times \varphi$', fontsize=13)
    
    ax.set_xlabel('$u$', fontsize=14)
    ax.set_ylabel('$z + \\varphi w$', fontsize=14)
    ax.set_aspect('equal')
    ax.legend(fontsize=12, loc='upper left')
    ax.grid(True, alpha=0.3)
    ax.set_xlim(-0.3, 1.5)
    ax.set_ylim(-0.3, 2)
    ax.tick_params(labelsize=12)
    
    plt.tight_layout()
    
    output_path = output_dir / "square_rhombus_projection"
    save_figure(fig, output_path, verbose=verbose)
    plt.close(fig)
    
    if verbose:
        print("  ✓ Square to rhombus projection figure generated")

