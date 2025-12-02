"""
Hausdorff dimension figure generator.

Shows the relationship between number of triangles N = 3^σ and inverse scale
1/r = 2^σ in the Sierpiński triangle, demonstrating the Hausdorff dimension
dim_H = log₂(3) ≈ 1.585.
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
from utils import save_figure

# Constants
COLOR_SIERPINSKI = '#9467BD'
dim_H = np.log(3) / np.log(2)  # Hausdorff dimension ≈ 1.585


@register("hausdorff_dimension")
def generate_hausdorff_dimension(output_dir: Path, verbose: bool = False) -> None:
    """
    Generate figure showing Hausdorff dimension relationship.
    
    Args:
        output_dir: Directory where to save the figure
        verbose: If True, show additional information
    """
    if verbose:
        print("  Generating Hausdorff dimension figure...")
    
    fig, ax = plt.subplots(figsize=(7, 6))
    
    sigmas = np.arange(0, 8)
    n_triangles = 3 ** sigmas
    inv_scale = 2 ** sigmas
    
    ax.loglog(inv_scale, n_triangles, 'o-', color=COLOR_SIERPINSKI, 
             linewidth=2, markersize=10, markeredgecolor='black', markeredgewidth=1)
    
    # Line with slope dim_H
    x_fit = np.logspace(0, 2.5, 100)
    y_fit = x_fit ** dim_H
    ax.loglog(x_fit, y_fit, 'k--', linewidth=1.5, alpha=0.7, 
             label=f'Slope $= \\log_2 3 \\approx {dim_H:.3f}$')
    
    ax.set_xlabel(r'$1/r = 2^\sigma$', fontsize=14)
    ax.set_ylabel(r'$N = 3^\sigma$', fontsize=14)
    ax.legend(fontsize=12)
    ax.grid(True, alpha=0.3, which='both')
    ax.tick_params(labelsize=12)
    
    plt.tight_layout()
    
    output_path = output_dir / "hausdorff_dimension"
    save_figure(fig, output_path, verbose=verbose)
    plt.close(fig)
    
    if verbose:
        print("  ✓ Hausdorff dimension figure generated")

