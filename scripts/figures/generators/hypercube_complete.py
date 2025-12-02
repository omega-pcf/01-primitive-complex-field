"""
Complete PCF hypercube figure generator.

Shows the mathematically exact PCF hypercube with:
1. Nested cubes growing exactly as φ^σ
2. Lattice points Λ_σ = φ^σ · Λ_0 at each level
3. Multi-level structure with superposition
4. Mathematical properties table
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import sys
from pathlib import Path as PathLib
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.ticker import MaxNLocator
import matplotlib.patches as mpatches

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
    5: '#1abc9c',  # turquoise
    6: '#e91e63',  # pink
}


def draw_3d_cube(ax, origin, size, color, alpha_face=0.1, alpha_edge=0.9, lw=2):
    """Draw a 3D cube with semi-transparent faces and solid edges."""
    o = np.array(origin)
    s = size
    
    # Vertices
    v = np.array([
        [0, 0, 0], [s, 0, 0], [s, s, 0], [0, s, 0],
        [0, 0, s], [s, 0, s], [s, s, s], [0, s, s]
    ]) + o
    
    # Faces
    faces = [
        [v[0], v[1], v[2], v[3]],  # bottom
        [v[4], v[5], v[6], v[7]],  # top
        [v[0], v[1], v[5], v[4]],  # front
        [v[2], v[3], v[7], v[6]],  # back
        [v[0], v[3], v[7], v[4]],  # left
        [v[1], v[2], v[6], v[5]]   # right
    ]
    
    ax.add_collection3d(Poly3DCollection(faces, alpha=alpha_face, 
                                          facecolor=color, edgecolor='none'))
    
    # Edges
    edges = [
        [v[0], v[1]], [v[1], v[2]], [v[2], v[3]], [v[3], v[0]],
        [v[4], v[5]], [v[5], v[6]], [v[6], v[7]], [v[7], v[4]],
        [v[0], v[4]], [v[1], v[5]], [v[2], v[6]], [v[3], v[7]]
    ]
    
    for edge in edges:
        ax.plot3D(*zip(*edge), color=color, linewidth=lw, alpha=alpha_edge)
    
    return v


@register("hypercube_complete")
def generate_hypercube_complete(output_dir: Path, verbose: bool = False) -> None:
    """
    Generate complete PCF hypercube visualization.
    
    Args:
        output_dir: Directory where to save the figure
        verbose: If True, show additional information
    """
    if verbose:
        print("  Generating hypercube nested cubes figure...")
    
    fig = plt.figure(figsize=(10, 10))
    sigma_max = 4
    
    # === Only Panel: Hypercube with nested cubes from origin ===
    ax1 = fig.add_subplot(111, projection='3d')
    
    for sigma in range(sigma_max):
        M_sigma = (PHI ** sigma) * M_PCF
        
        # Draw cube at this level
        draw_3d_cube(ax1, (0, 0, 0), M_sigma, colors[sigma], 
                    alpha_face=0.08, alpha_edge=0.8, lw=2.5 - 0.3*sigma)
        
        # Mark diagonal corner (star position)
        star_pos = np.array([M_sigma, M_sigma, M_sigma])
        ax1.scatter([star_pos[0]], [star_pos[1]], [star_pos[2]], 
                   c=colors[sigma], s=100, marker='*', 
                   edgecolors='black', linewidths=1, zorder=10)
        
        # Labels aligned VERTICALLY (same X, same Y, distributed in Z - the vertical axis)
        # Repositioned to ensure all are visible and none overlap
        M_sigma3 = (PHI ** 3) * M_PCF
        M_max = (PHI ** (sigma_max - 1)) * M_PCF
        
        # All labels at same X and Y, positioned to the right but within visible range
        label_x = M_max * 1.3  # To the right, but visible
        label_y = M_max * 0.5  # Middle Y position, visible
        
        # Z positions (VERTICAL axis): distributed linearly with good spacing
        # Center the distribution around the middle of the cubes
        z_center = M_max * 0.5
        z_spacing = M_max * 0.25  # Good spacing between labels
        z_start = z_center - (sigma_max - 1) * z_spacing / 2  # Center the distribution
        base_z = z_start + sigma * z_spacing
        
        # Very slight fan offset to avoid perfect alignment (minimal)
        fan_offsets = [0, 0.01 * M_max, -0.01 * M_max, 0.005 * M_max]
        label_z = base_z + fan_offsets[sigma]
        
        # Draw arrow FROM label TO star (pointing towards the star)
        ax1.plot([label_x, star_pos[0]], [label_y, star_pos[1]], [label_z, star_pos[2]],
                color=colors[sigma], linewidth=1.5, linestyle='--', alpha=0.7)
        
        # Label with background for contrast
        ax1.text(label_x, label_y, label_z, 
                f'$\\sigma={sigma}$\n$M={M_sigma:.0f}$', 
                fontsize=11, color=colors[sigma], fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white', 
                         edgecolor=colors[sigma], linewidth=1.5, alpha=0.9),
                ha='left', va='bottom')  # Align text to avoid overlap
    
    # Set axis limits based ONLY on cubes, not labels (to prevent flattening)
    M_max = (PHI ** (sigma_max - 1)) * M_PCF
    margin = M_max * 0.1
    ax1.set_xlim(-margin, M_max + margin)
    ax1.set_ylim(-margin, M_max + margin)
    ax1.set_zlim(-margin, M_max + margin)
    
    # Smaller font sizes and move labels away from axes
    ax1.set_xlabel('$u$ (Re)', fontsize=13, labelpad=15)  # labelpad moves label away
    ax1.set_ylabel('$v$ (Im)', fontsize=13, labelpad=15)
    ax1.set_zlabel('$w = \\varphi \\cdot v$', fontsize=13, labelpad=15)
    ax1.tick_params(labelsize=11)
    ax1.view_init(elev=20, azim=35)
    
    plt.tight_layout()
    
    output_path = output_dir / "hypercube_complete"
    save_figure(fig, output_path, verbose=verbose)
    plt.close(fig)
    
    if verbose:
        print("  ✓ Complete hypercube figure generated")

