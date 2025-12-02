"""
Orthogonal views of the PCF operator figure generator.

Shows the three orthogonal views (3D, top, lateral) of the PCF operator
with vertices P, C, F on the cylinder, according to the paper.
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import sys
from pathlib import Path as PathLib

# Add parent directory to path for imports
_parent_dir = PathLib(__file__).parent.parent
if str(_parent_dir) not in sys.path:
    sys.path.insert(0, str(_parent_dir))

from generators import register
from utils import setup_figure, save_figure, PHI

# Constants
omega = np.exp(2j * np.pi / 3)
R0 = 3  # Base radius of the cylinder
M_PCF = np.pi / (np.log(PHI) / (6 * np.sqrt(3)))

# Vertices P, C, F in 3D
P_3d = np.array([3, 0, 0])
C_3d = np.array([-1.5, 2.598, PHI * 2.598])  # z = φy
F_3d = np.array([-1.5, -2.598, PHI * (-2.598)])  # z = φy


@register("orthogonal_views")
def generate_orthogonal_views(output_dir: Path, verbose: bool = False) -> None:
    """
    Generate figure showing three orthogonal views of the PCF operator.
    
    Args:
        output_dir: Directory where to save the figure
        verbose: If True, show additional information
    """
    if verbose:
        print("  Generating orthogonal views figure...")
    
    # Create figure for 3 panels only, with better spacing
    fig = plt.figure(figsize=(18, 6))
    
    # === Panel 1: Complete 3D view ===
    ax1 = fig.add_subplot(131, projection='3d')
    
    # Cylinder
    theta_cyl = np.linspace(0, 2*np.pi, 100)
    z_cyl = np.linspace(-5, 5, 50)
    Theta, Z = np.meshgrid(theta_cyl, z_cyl)
    X_cyl = R0 * np.cos(Theta)
    Y_cyl = R0 * np.sin(Theta)
    ax1.plot_surface(X_cyl, Y_cyl, Z, alpha=0.1, color='gray')
    
    # Helical curve z = φy
    theta_helix = np.linspace(0, 2*np.pi, 100)
    x_helix = R0 * np.cos(theta_helix)
    y_helix = R0 * np.sin(theta_helix)
    z_helix = PHI * y_helix
    ax1.plot(x_helix, y_helix, z_helix, 'b-', linewidth=2, label='Curve z=φy')
    
    # Vertices P, C, F
    vertices = np.array([P_3d, C_3d, F_3d])
    colors = ['red', 'green', 'blue']
    labels = ['P', 'C', 'F']
    
    for v, c, l in zip(vertices, colors, labels):
        ax1.scatter(v[0], v[1], v[2], c=c, s=200, edgecolors='black', zorder=10)
        ax1.text(v[0]+0.3, v[1]+0.3, v[2]+0.3, l, fontsize=16, fontweight='bold', color=c)
    
    # Triangle lines
    for i in range(3):
        j = (i + 1) % 3
        ax1.plot([vertices[i,0], vertices[j,0]], 
                 [vertices[i,1], vertices[j,1]], 
                 [vertices[i,2], vertices[j,2]], 'k-', linewidth=2)
    
    # xy plane (z=0)
    xx, yy = np.meshgrid(np.linspace(-4, 4, 10), np.linspace(-4, 4, 10))
    ax1.plot_surface(xx, yy, np.zeros_like(xx), alpha=0.1, color='yellow')
    
    ax1.set_xlabel('x (Re)', fontsize=14)
    ax1.set_ylabel('y (Im)', fontsize=14)
    ax1.set_zlabel('z = φy', fontsize=14)
    ax1.tick_params(labelsize=12)
    ax1.view_init(elev=20, azim=45)
    
    # === Panel 2: TOP VIEW (xy plane) ===
    ax2 = fig.add_subplot(132)
    
    # Circle of radius R0 = 3
    circle = plt.Circle((0, 0), R0, fill=False, color='gray', linewidth=2, linestyle='--')
    ax2.add_patch(circle)
    
    # Projection of vertices to xy plane
    P_xy = P_3d[:2]
    C_xy = C_3d[:2]
    F_xy = F_3d[:2]
    
    # Projected triangle
    tri_xy = np.array([P_xy, C_xy, F_xy, P_xy])
    ax2.plot(tri_xy[:,0], tri_xy[:,1], 'k-', linewidth=2)
    ax2.fill(tri_xy[:-1,0], tri_xy[:-1,1], alpha=0.2, color='purple')
    
    # Vertices
    ax2.scatter(*P_xy, c='red', s=200, edgecolors='black', zorder=10)
    ax2.scatter(*C_xy, c='green', s=200, edgecolors='black', zorder=10)
    ax2.scatter(*F_xy, c='blue', s=200, edgecolors='black', zorder=10)
    
    ax2.annotate('P (0°)', P_xy, textcoords="offset points", xytext=(15, 5), 
                fontsize=14, fontweight='bold', color='red')
    ax2.annotate('C (120°)', C_xy, textcoords="offset points", xytext=(-30, 10), 
                fontsize=14, fontweight='bold', color='green')
    ax2.annotate('F (240°)', F_xy, textcoords="offset points", xytext=(-30, -15), 
                fontsize=14, fontweight='bold', color='blue')
    
    # Lattice as rhombi (square rotated 45°)
    M_scale = R0 * 0.8
    for n1 in range(-2, 3):
        for n2 in range(-2, 3):
            x = n1 * M_scale
            y = n2 * M_scale
            ax2.scatter(x, y, c='cyan', s=30, alpha=0.5, marker='s')
            
            # Draw cell as rhombus (rotated 45°)
            if n1 < 2 and n2 < 2:
                rombo = np.array([
                    [x, y],
                    [x + M_scale, y],
                    [x + M_scale, y + M_scale],
                    [x, y + M_scale],
                    [x, y]
                ])
                ax2.plot(rombo[:,0], rombo[:,1], 'c-', linewidth=0.5, alpha=0.3)
    
    # Highlighted fundamental cell
    celda = np.array([[0, 0], [M_scale, 0], [M_scale, M_scale], [0, M_scale], [0, 0]])
    ax2.plot(celda[:,0], celda[:,1], 'c-', linewidth=2, label='Cell Λ_PCF')
    
    ax2.set_xlim(-5, 5)
    ax2.set_ylim(-5, 5)
    ax2.set_aspect('equal')
    ax2.axhline(y=0, color='gray', linewidth=0.5)
    ax2.axvline(x=0, color='gray', linewidth=0.5)
    ax2.set_xlabel('x (Re)', fontsize=14)
    ax2.set_ylabel('y (Im)', fontsize=14)
    ax2.tick_params(labelsize=12)
    ax2.grid(True, alpha=0.3)
    
    # === Panel 3: LATERAL VIEW (yz plane) - ELLIPSE ===
    ax3 = fig.add_subplot(133)
    
    # The projection in yz gives an ELLIPSE because z = φy
    # Line z = φy
    y_line = np.linspace(-4, 4, 100)
    z_line = PHI * y_line
    ax3.plot(y_line, z_line, 'b-', linewidth=2, label=f'z = φy (slope φ={PHI:.3f})')
    
    # Projection of vertices to yz plane
    P_yz = np.array([P_3d[1], P_3d[2]])
    C_yz = np.array([C_3d[1], C_3d[2]])
    F_yz = np.array([F_3d[1], F_3d[2]])
    
    ax3.scatter(*P_yz, c='red', s=200, edgecolors='black', zorder=10)
    ax3.scatter(*C_yz, c='green', s=200, edgecolors='black', zorder=10)
    ax3.scatter(*F_yz, c='blue', s=200, edgecolors='black', zorder=10)
    
    ax3.annotate('P', P_yz, textcoords="offset points", xytext=(10, 5), 
                fontsize=14, fontweight='bold', color='red')
    ax3.annotate('C', C_yz, textcoords="offset points", xytext=(10, 5), 
                fontsize=14, fontweight='bold', color='green')
    ax3.annotate('F', F_yz, textcoords="offset points", xytext=(10, -15), 
                fontsize=14, fontweight='bold', color='blue')
    
    # Cylinder envelope projected in yz
    ax3.axvline(x=3, color='gray', linestyle='--', alpha=0.5)
    ax3.axvline(x=-3, color='gray', linestyle='--', alpha=0.5)
    
    # Show that C and F are on the line z = φy
    ax3.plot([P_yz[0], C_yz[0]], [P_yz[1], C_yz[1]], 'k--', linewidth=1, alpha=0.5)
    ax3.plot([P_yz[0], F_yz[0]], [P_yz[1], F_yz[1]], 'k--', linewidth=1, alpha=0.5)
    
    ax3.set_xlim(-5, 5)
    ax3.set_ylim(-6, 6)
    ax3.set_aspect('equal')
    ax3.axhline(y=0, color='gray', linewidth=0.5)
    ax3.axvline(x=0, color='gray', linewidth=0.5)
    ax3.set_xlabel('y (Im)', fontsize=14)
    ax3.set_ylabel('z = φy', fontsize=14)
    ax3.tick_params(labelsize=12)
    ax3.legend(loc='upper left', fontsize=12)
    ax3.grid(True, alpha=0.3)
    
    plt.tight_layout(pad=3.0)
    
    # Save figure
    output_path = output_dir / "orthogonal_views"
    save_figure(fig, output_path, verbose=verbose)
    
    # Cleanup
    plt.close(fig)
    
    if verbose:
        print("  ✓ Orthogonal views figure generated")
