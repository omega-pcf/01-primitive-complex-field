"""
Dual towers figure generator.

Shows the duality between expansion and contraction towers:
- EXPANSION: Radius GROWS as φ^σ, always 3 points per level
- CONTRACTION (Sierpiński): Fixed outer size, complexity GROWS as 3^σ

In both cases σ increases upward. The Sierpiński subdivision becomes finer
(more small triangles) while maintaining the same outer boundary.
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


def get_triangle_vertices_2d(R, center=(0, 0)):
    """Get equilateral triangle vertices of radius R centered at center."""
    angles = [np.pi/2 + k * 2*np.pi/3 for k in range(3)]
    return [(center[0] + R * np.cos(a), center[1] + R * np.sin(a)) for a in angles]


def subdivide_triangle(v0, v1, v2):
    """Subdivide triangle into 3 (removing center = Sierpiński)."""
    m01 = ((v0[0]+v1[0])/2, (v0[1]+v1[1])/2)
    m12 = ((v1[0]+v2[0])/2, (v1[1]+v2[1])/2)
    m02 = ((v0[0]+v2[0])/2, (v0[1]+v2[1])/2)
    return [
        (v0, m01, m02),
        (m01, v1, m12),
        (m02, m12, v2)
    ]


def sierpinski(vertices, depth):
    """Generate Sierpiński triangles at depth."""
    if depth == 0:
        return [vertices]
    triangles = [tuple(vertices)]
    for _ in range(depth):
        new_tri = []
        for t in triangles:
            new_tri.extend(subdivide_triangle(*t))
        triangles = new_tri
    return triangles


@register("dual_towers")
def generate_dual_towers(output_dir: Path, verbose: bool = False) -> None:
    """
    Generate figure showing dual towers: expansion vs contraction (Sierpiński).
    
    Args:
        output_dir: Directory where to save the figure
        verbose: If True, show additional information
    """
    if verbose:
        print("  Generating dual towers figure...")
    
    fig = plt.figure(figsize=(16, 7))
    n_levels = 5
    z_spacing = 4
    
    # === Panel 1: EXPANSION TOWER ===
    ax1 = fig.add_subplot(121, projection='3d')
    
    for sigma in range(n_levels):
        R_sigma = R0 * PHI**sigma
        z = sigma * z_spacing
        
        verts = get_triangle_vertices_2d(R_sigma)
        
        # Triangle
        xs = [v[0] for v in verts] + [verts[0][0]]
        ys = [v[1] for v in verts] + [verts[0][1]]
        zs = [z] * 4
        ax1.plot(xs, ys, zs, 'cyan', linewidth=2.5)
        
        # Vertices P, C, F
        colors_pcf = [COLOR_P, COLOR_C, COLOR_F]
        labels_pcf = ['P', 'C', 'F']
        for i, (x, y) in enumerate(verts):
            ax1.scatter([x], [y], [z], c=colors_pcf[i], s=100, 
                       edgecolors='black', linewidths=1.5, zorder=5)
    
    # Lines connecting levels
    for k in range(3):
        angle = np.pi/2 + k * 2*np.pi/3
        xs = [R0 * PHI**s * np.cos(angle) for s in range(n_levels)]
        ys = [R0 * PHI**s * np.sin(angle) for s in range(n_levels)]
        zs = [s * z_spacing for s in range(n_levels)]
        ax1.plot(xs, ys, zs, 'gray', linewidth=1, linestyle='--', alpha=0.5)
    
    ax1.set_xlabel('$x$', fontsize=14)
    ax1.set_ylabel('$y$', fontsize=14)
    ax1.set_zlabel('$\\sigma$', fontsize=14)
    ax1.set_title(r'Expansion: $R_\sigma = R_0 \cdot \varphi^\sigma$' + '\n' +
                  'Triangle GROWS, 3 points/level', fontsize=14, fontweight='bold')
    ax1.tick_params(labelsize=12)
    ax1.view_init(elev=25, azim=45)
    ax1.set_xlim(-25, 25)
    ax1.set_ylim(-25, 25)
    
    # === Panel 2: CONTRACTION TOWER (Sierpiński) ===
    # Fixed outer size, subdivision GROWS
    ax2 = fig.add_subplot(122, projection='3d')
    
    R_fixed = R0 * PHI**2  # Fixed size for visualization
    
    for sigma in range(n_levels):
        z = sigma * z_spacing
        
        # Outer triangle vertices (fixed size)
        verts = get_triangle_vertices_2d(R_fixed)
        
        # Sierpiński at depth sigma
        triangles = sierpinski(verts, sigma)
        
        # Color according to level
        color = plt.cm.Purples(0.4 + 0.12*sigma)
        
        # Draw all small triangles
        for tri in triangles:
            xs = [v[0] for v in tri] + [tri[0][0]]
            ys = [v[1] for v in tri] + [tri[0][1]]
            zs = [z] * 4
            ax2.plot(xs, ys, zs, color='magenta', linewidth=0.8, alpha=0.9)
        
        # Outer contour
        xs_out = [v[0] for v in verts] + [verts[0][0]]
        ys_out = [v[1] for v in verts] + [verts[0][1]]
        zs_out = [z] * 4
        ax2.plot(xs_out, ys_out, zs_out, 'purple', linewidth=2)
        
        # Label
        n_tri = 3**sigma
        ax2.text(R_fixed + 2, 0, z, f'$\\sigma={sigma}: {n_tri}$', 
                fontsize=11, color='purple')
    
    ax2.set_xlabel('$x$', fontsize=14)
    ax2.set_ylabel('$y$', fontsize=14)
    ax2.set_zlabel('$\\sigma$', fontsize=14)
    ax2.set_title(r'Contraction (Sierpiński): scale $(1/2)^\sigma$' + '\n' +
                  r'Fixed size, complexity $3^\sigma$ GROWS', fontsize=14, fontweight='bold')
    ax2.tick_params(labelsize=12)
    ax2.view_init(elev=25, azim=45)
    ax2.set_xlim(-15, 15)
    ax2.set_ylim(-15, 15)
    
    plt.tight_layout()
    
    output_path = output_dir / "dual_towers"
    save_figure(fig, output_path, verbose=verbose)
    plt.close(fig)
    
    if verbose:
        print("  ✓ Dual towers figure generated")

