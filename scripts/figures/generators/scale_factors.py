"""
Scale factors figure generator.

Shows the scaling behavior of different factors: φ^σ (expansion), (1/2)^σ (contraction),
and (φ/2)^σ (balance) as functions of the scale level σ.
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


@register("scale_factors")
def generate_scale_factors(output_dir: Path, verbose: bool = False) -> None:
    """
    Generate figure showing scale factors as functions of σ.
    
    Args:
        output_dir: Directory where to save the figure
        verbose: If True, show additional information
    """
    if verbose:
        print("  Generating scale factors figure...")
    
    fig, ax = plt.subplots(figsize=(8, 6))
    
    sigma = np.linspace(0, 6, 100)
    
    ax.semilogy(sigma, PHI**sigma, 'b-', linewidth=2.5, 
               label=r'$\varphi^\sigma$ (expansion)')
    ax.semilogy(sigma, 0.5**sigma, 'r-', linewidth=2.5, 
               label=r'$(1/2)^\sigma$ (contraction)')
    ax.semilogy(sigma, (PHI/2)**sigma, 'g-', linewidth=2.5, 
               label=r'$(\varphi/2)^\sigma$ (balance)')
    
    ax.axhline(y=1, color='gray', linestyle='--', linewidth=1, alpha=0.7)
    
    # Discrete points
    sigmas_int = np.arange(0, 7)
    ax.scatter(sigmas_int, PHI**sigmas_int, c='blue', s=50, zorder=5)
    ax.scatter(sigmas_int, 0.5**sigmas_int, c='red', s=50, zorder=5)
    ax.scatter(sigmas_int, (PHI/2)**sigmas_int, c='green', s=50, zorder=5)
    
    ax.set_xlabel(r'$\sigma$', fontsize=14)
    ax.set_ylabel('Scale factor', fontsize=14)
    ax.legend(fontsize=12, loc='center right')
    ax.grid(True, alpha=0.3, which='both')
    ax.set_xlim(0, 6)
    ax.set_xticks(range(7))
    ax.tick_params(labelsize=12)
    
    plt.tight_layout()
    
    output_path = output_dir / "scale_factors"
    save_figure(fig, output_path, verbose=verbose)
    plt.close(fig)
    
    if verbose:
        print("  ✓ Scale factors figure generated")

