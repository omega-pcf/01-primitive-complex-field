"""
Sierpiński triangle 2D (top view) figure generator.

Shows the Sierpiński triangle fractal pattern in 2D projection,
with vertices P, C, F marked.
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
R0 = 3.0
COLOR_P = '#D62728'  # Red
COLOR_C = '#2CA02C'  # Green
COLOR_F = '#1F77B4'  # Blue
COLOR_SIERPINSKI = '#9467BD'


@register("sierpinski_2d")
def generate_sierpinski_2d(output_dir: Path, verbose: bool = False) -> None:
    """
    Generate figure showing Sierpiński triangle in 2D.
    
    Args:
        output_dir: Directory where to save the figure
        verbose: If True, show additional information
    """
    if verbose:
        print("  Generating Sierpiński 2D figure...")
    
    fig, ax = plt.subplots(figsize=(8, 7))
    
    def draw_sierpinski(ax, v1, v2, v3, level, max_level):
        """Recursively draw Sierpiński triangle."""
        if level >= max_level:
            t = plt.Polygon([v1, v2, v3], fill=True, facecolor=COLOR_SIERPINSKI, 
                           edgecolor='black', alpha=0.7, linewidth=0.3)
            ax.add_patch(t)
            return
        m12 = (v1 + v2) / 2
        m23 = (v2 + v3) / 2
        m31 = (v3 + v1) / 2
        draw_sierpinski(ax, v1, m12, m31, level+1, max_level)
        draw_sierpinski(ax, m12, v2, m23, level+1, max_level)
        draw_sierpinski(ax, m31, m23, v3, level+1, max_level)
    
    # Base triangle
    h = R0 * np.sqrt(3)
    v1 = np.array([0, h * 2/3])
    v2 = np.array([-R0, -h/3])
    v3 = np.array([R0, -h/3])
    
    draw_sierpinski(ax, v1, v2, v3, 0, 6)
    
    # Mark P, C, F
    ax.scatter(*v1, c=COLOR_P, s=120, marker='o', edgecolors='black', 
              linewidths=1, zorder=5)
    ax.scatter(*v2, c=COLOR_C, s=120, marker='o', edgecolors='black', 
              linewidths=1, zorder=5)
    ax.scatter(*v3, c=COLOR_F, s=120, marker='o', edgecolors='black', 
              linewidths=1, zorder=5)
    
    ax.text(v1[0]+0.2, v1[1]+0.3, '$P$', fontsize=14)
    ax.text(v2[0]-0.5, v2[1]-0.3, '$C$', fontsize=14)
    ax.text(v3[0]+0.2, v3[1]-0.3, '$F$', fontsize=14)
    
    ax.set_xlim(-4.5, 4.5)
    ax.set_ylim(-3, 4.5)
    ax.set_aspect('equal')
    ax.axis('off')
    
    plt.tight_layout()
    
    output_path = output_dir / "sierpinski_2d"
    save_figure(fig, output_path, verbose=verbose)
    plt.close(fig)
    
    if verbose:
        print("  ✓ Sierpiński 2D figure generated")

