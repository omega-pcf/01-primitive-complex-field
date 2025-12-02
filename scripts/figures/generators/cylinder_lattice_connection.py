"""
Cylinder-lattice connection figure generator.

Shows the connection between the cylinder (operator, Eisenstein structure) 
and the lattice (space, Gauss structure) through the golden coupling φ.
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import sys
from pathlib import Path as PathLib
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.ticker import MaxNLocator

# Add parent directory to path for imports
_parent_dir = PathLib(__file__).parent.parent
if str(_parent_dir) not in sys.path:
    sys.path.insert(0, str(_parent_dir))

from generators import register
from utils import save_figure, PHI

# Constants
R0 = 3  # Base radius of the cylinder
M_PCF = np.pi / (np.log(PHI) / (6 * np.sqrt(3)))  # Topological module ≈ 67.846
M_vis = 2  # Visual scale for lattice (scaled for visualization)

# Vertices of the cylinder
P_cyl = np.array([3, 0, 0])
C_cyl = np.array([-1.5, 2.598, PHI * 2.598])
F_cyl = np.array([-1.5, -2.598, PHI * (-2.598)])


@register("cylinder_lattice_connection")
def generate_cylinder_lattice_connection(output_dir: Path, verbose: bool = False) -> None:
    """
    Generate figure showing connection between cylinder and lattice.
    
    Args:
        output_dir: Directory where to save the figure
        verbose: If True, show additional information
    """
    if verbose:
        print("  Generating cylinder-lattice connection figure...")
    
    # Create figure with 3 rows x 3 columns (removed text panels)
    fig = plt.figure(figsize=(21, 18))
    
    # ============ ROW 1: 3D STRUCTURES ============
    
    # --- Panel 1: CYLINDER 3D ---
    ax1 = fig.add_subplot(331, projection='3d')
    
    # Cylinder surface
    theta = np.linspace(0, 2*np.pi, 50)
    z_surf = np.linspace(-6, 6, 30)
    Theta, Z = np.meshgrid(theta, z_surf)
    X_cyl = R0 * np.cos(Theta)
    Y_cyl = R0 * np.sin(Theta)
    ax1.plot_surface(X_cyl, Y_cyl, Z, alpha=0.15, color='lightblue', edgecolor='none')
    
    # Base circle
    ax1.plot(R0*np.cos(theta), R0*np.sin(theta), np.zeros_like(theta), 'b-', linewidth=2)
    
    # Vertices P, C, F
    ax1.scatter(*P_cyl, c='red', s=200, edgecolors='black', zorder=10)
    ax1.scatter(*C_cyl, c='green', s=200, edgecolors='black', zorder=10)
    ax1.scatter(*F_cyl, c='blue', s=200, edgecolors='black', zorder=10)
    
    # Triangle 3D
    tri_3d = [P_cyl, C_cyl, F_cyl, P_cyl]
    for i in range(3):
        ax1.plot([tri_3d[i][0], tri_3d[i+1][0]], 
                 [tri_3d[i][1], tri_3d[i+1][1]], 
                 [tri_3d[i][2], tri_3d[i+1][2]], 'purple', linewidth=2)
    
    ax1.text(P_cyl[0]+0.3, P_cyl[1], P_cyl[2]+0.5, 'P', fontsize=15, color='red', fontweight='bold')
    ax1.text(C_cyl[0]-0.5, C_cyl[1], C_cyl[2]+0.5, 'C', fontsize=15, color='green', fontweight='bold')
    ax1.text(F_cyl[0]-0.5, F_cyl[1], F_cyl[2]-0.5, 'F', fontsize=15, color='blue', fontweight='bold')
    
    ax1.view_init(elev=20, azim=45)
    ax1.set_xlabel('x', fontsize=14)
    ax1.set_ylabel('y', fontsize=14)
    ax1.set_zlabel('z=φy', fontsize=14)
    ax1.set_title('Cylinder: Triangle P-C-F\nCoupling z = φy', fontsize=14, fontweight='bold')
    ax1.tick_params(labelsize=12)
    ax1.xaxis.set_major_locator(MaxNLocator(4))
    ax1.yaxis.set_major_locator(MaxNLocator(4))
    ax1.zaxis.set_major_locator(MaxNLocator(4))
    
    # --- Panel 2: LATTICE 3D ---
    ax2 = fig.add_subplot(332, projection='3d')
    
    # Lattice points
    for n1 in range(-2, 3):
        for n2 in range(-2, 3):
            u = n1 * M_vis
            v = n2 * M_vis
            w = PHI * v  # Same coupling
            ax2.scatter(u, v, w, c='cyan', s=80, edgecolors='blue', marker='s')
    
    # Fundamental cell (parallelogram)
    v1 = np.array([M_vis, 0, 0])
    v2 = np.array([0, M_vis, PHI*M_vis])
    origin = np.array([0, 0, 0])
    p1, p2, p3 = v1, v2, v1 + v2
    verts = [[origin, p1, p3, p2]]
    ax2.add_collection3d(Poly3DCollection(verts, alpha=0.3, facecolor='cyan', edgecolor='blue', linewidth=2))
    
    # Base vectors
    ax2.quiver(0, 0, 0, v1[0]*0.8, v1[1], v1[2], color='red', linewidth=2, arrow_length_ratio=0.15)
    ax2.quiver(0, 0, 0, v2[0], v2[1]*0.8, v2[2]*0.8, color='green', linewidth=2, arrow_length_ratio=0.15)
    ax2.text(v1[0]*0.9, 0, 0.5, 'v₁=M', fontsize=13, color='red', fontweight='bold')
    ax2.text(0.3, v2[1]*0.7, v2[2]*0.7, 'v₂=(0,M,φM)', fontsize=12, color='green', fontweight='bold')
    
    ax2.view_init(elev=20, azim=45)
    ax2.set_xlabel('u', fontsize=14)
    ax2.set_ylabel('v', fontsize=14)
    ax2.set_zlabel('w=φv', fontsize=14)
    ax2.set_title('Lattice 3D: Parallelogram\nCoupling w = φv', fontsize=14, fontweight='bold')
    ax2.tick_params(labelsize=12)
    ax2.xaxis.set_major_locator(MaxNLocator(4))
    ax2.yaxis.set_major_locator(MaxNLocator(4))
    ax2.zaxis.set_major_locator(MaxNLocator(4))
    
    # --- Panel 3: SUPERPOSITION ---
    ax3 = fig.add_subplot(333, projection='3d')
    
    # Cylinder (scaled)
    scale = M_vis / R0
    ax3.plot_surface(X_cyl*scale, Y_cyl*scale, Z*scale*0.8, alpha=0.1, color='lightblue', edgecolor='none')
    
    # Triangle P-C-F scaled
    P_s = P_cyl * scale * np.array([1, 1, 0.8])
    C_s = C_cyl * scale * np.array([1, 1, 0.8])
    F_s = F_cyl * scale * np.array([1, 1, 0.8])
    
    ax3.scatter(*P_s, c='red', s=150, edgecolors='black', zorder=10)
    ax3.scatter(*C_s, c='green', s=150, edgecolors='black', zorder=10)
    ax3.scatter(*F_s, c='blue', s=150, edgecolors='black', zorder=10)
    
    # Triangle
    for a, b in [(P_s, C_s), (C_s, F_s), (F_s, P_s)]:
        ax3.plot([a[0], b[0]], [a[1], b[1]], [a[2], b[2]], 'purple', linewidth=2)
    
    # Lattice (some points)
    for n1 in range(-1, 2):
        for n2 in range(-1, 2):
            u = n1 * M_vis
            v = n2 * M_vis
            w = PHI * v * 0.8
            ax3.scatter(u, v, w, c='cyan', s=60, marker='s', alpha=0.6)
    
    # Fundamental cell
    ax3.add_collection3d(Poly3DCollection([[origin, v1, v1+v2*0.8, v2*0.8]], 
                                          alpha=0.2, facecolor='cyan', edgecolor='blue', linewidth=1))
    
    ax3.view_init(elev=20, azim=45)
    ax3.set_xlabel('x/u', fontsize=14)
    ax3.set_ylabel('y/v', fontsize=14)
    ax3.set_zlabel('z/w', fontsize=14)
    ax3.set_title('Superposition\nTriangle in lattice', fontsize=14, fontweight='bold')
    ax3.tick_params(labelsize=12)
    ax3.xaxis.set_major_locator(MaxNLocator(4))
    ax3.yaxis.set_major_locator(MaxNLocator(4))
    ax3.zaxis.set_major_locator(MaxNLocator(4))
    
    # ============ ROW 2: TOP VIEWS ============
    
    # --- Panel 4: Top view CYLINDER ---
    ax4 = fig.add_subplot(334)
    
    # Circle of cylinder
    ax4.plot(R0*np.cos(theta), R0*np.sin(theta), 'b-', linewidth=2)
    ax4.fill(R0*np.cos(theta), R0*np.sin(theta), alpha=0.1, color='blue')
    
    # Projected triangle
    ax4.scatter(P_cyl[0], P_cyl[1], c='red', s=200, edgecolors='black', zorder=10)
    ax4.scatter(C_cyl[0], C_cyl[1], c='green', s=200, edgecolors='black', zorder=10)
    ax4.scatter(F_cyl[0], F_cyl[1], c='blue', s=200, edgecolors='black', zorder=10)
    
    tri_2d = np.array([[P_cyl[0], P_cyl[1]], [C_cyl[0], C_cyl[1]], 
                      [F_cyl[0], F_cyl[1]], [P_cyl[0], P_cyl[1]]])
    ax4.fill(tri_2d[:-1,0], tri_2d[:-1,1], alpha=0.2, color='purple', edgecolor='purple', linewidth=2)
    
    ax4.annotate('P (0°)', (P_cyl[0], P_cyl[1]), textcoords="offset points", xytext=(10, 5), 
                fontsize=14, fontweight='bold', color='red')
    ax4.annotate('C (120°)', (C_cyl[0], C_cyl[1]), textcoords="offset points", xytext=(-40, 10), 
                fontsize=14, fontweight='bold', color='green')
    ax4.annotate('F (240°)', (F_cyl[0], F_cyl[1]), textcoords="offset points", xytext=(-40, -15), 
                fontsize=14, fontweight='bold', color='blue')
    
    ax4.set_xlim(-5, 5)
    ax4.set_ylim(-5, 5)
    ax4.set_aspect('equal')
    ax4.set_xlabel('x (Re)', fontsize=14)
    ax4.set_ylabel('y (Im)', fontsize=14)
    ax4.set_title('Top view: Circle R₀=3\nTriangle 120°', fontsize=14, fontweight='bold')
    ax4.tick_params(labelsize=12)
    ax4.grid(True, alpha=0.3)
    
    # --- Panel 5: Top view LATTICE ---
    ax5 = fig.add_subplot(335)
    
    # Lattice projected (square)
    for n1 in range(-2, 3):
        for n2 in range(-2, 3):
            ax5.scatter(n1*M_vis, n2*M_vis, c='cyan', s=80, marker='s', edgecolors='blue')
    
    # Fundamental cell (square in top view)
    rect = plt.Rectangle((0, 0), M_vis, M_vis, fill=True, facecolor='cyan', alpha=0.3,
                         edgecolor='blue', linewidth=3)
    ax5.add_patch(rect)
    
    ax5.annotate('', xy=(M_vis*1.2, 0), xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color='red', lw=2))
    ax5.annotate('', xy=(0, M_vis*1.2), xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color='green', lw=2))
    ax5.text(M_vis*1.3, -0.3, 'M', fontsize=14, color='red', fontweight='bold')
    ax5.text(-0.4, M_vis*1.3, 'Mi', fontsize=14, color='green', fontweight='bold')
    
    ax5.set_xlim(-5, 5)
    ax5.set_ylim(-5, 5)
    ax5.set_aspect('equal')
    ax5.set_xlabel('u (Re)', fontsize=14)
    ax5.set_ylabel('v (Im)', fontsize=14)
    ax5.set_title('Top view: Square M×M\nBase {M, Mi}', fontsize=14, fontweight='bold')
    ax5.tick_params(labelsize=12)
    ax5.grid(True, alpha=0.3)
    
    # --- Panel 6: Top view SUPERPOSITION ---
    ax6 = fig.add_subplot(336)
    
    # Scale cylinder to fit in cell
    scale_cyl = M_vis / R0
    
    # Scaled circle
    ax6.plot(R0*scale_cyl*np.cos(theta), R0*scale_cyl*np.sin(theta), 'purple', linewidth=2)
    
    # Scaled triangle
    P_2d_s = np.array([P_cyl[0], P_cyl[1]]) * scale_cyl
    C_2d_s = np.array([C_cyl[0], C_cyl[1]]) * scale_cyl
    F_2d_s = np.array([F_cyl[0], F_cyl[1]]) * scale_cyl
    
    ax6.scatter(*P_2d_s, c='red', s=150, edgecolors='black', zorder=10)
    ax6.scatter(*C_2d_s, c='green', s=150, edgecolors='black', zorder=10)
    ax6.scatter(*F_2d_s, c='blue', s=150, edgecolors='black', zorder=10)
    
    tri_s = np.array([P_2d_s, C_2d_s, F_2d_s, P_2d_s])
    ax6.fill(tri_s[:-1,0], tri_s[:-1,1], alpha=0.15, color='purple', edgecolor='purple', linewidth=2)
    
    # Lattice
    for n1 in range(-2, 3):
        for n2 in range(-2, 3):
            ax6.scatter(n1*M_vis, n2*M_vis, c='cyan', s=50, marker='s', alpha=0.5)
    
    # Cell
    rect = plt.Rectangle((0, 0), M_vis, M_vis, fill=False, edgecolor='blue', linewidth=2)
    ax6.add_patch(rect)
    
    ax6.set_xlim(-5, 5)
    ax6.set_ylim(-5, 5)
    ax6.set_aspect('equal')
    ax6.set_xlabel('x/u (Re)', fontsize=14)
    ax6.set_ylabel('y/v (Im)', fontsize=14)
    ax6.set_title('Top view: Superposition\nCircle+triangle in square', fontsize=14, fontweight='bold')
    ax6.tick_params(labelsize=12)
    ax6.grid(True, alpha=0.3)
    
    # ============ ROW 3: LATERAL VIEWS ============
    
    # --- Panel 7: Lateral view CYLINDER (yz plane) ---
    ax7 = fig.add_subplot(337)
    
    # Line z = φy
    y_line = np.linspace(-4, 4, 100)
    z_line = PHI * y_line
    ax7.plot(y_line, z_line, 'purple', linewidth=3, label=f'z = φy')
    
    # Projected vertices
    ax7.scatter(P_cyl[1], P_cyl[2], c='red', s=200, edgecolors='black', zorder=10)
    ax7.scatter(C_cyl[1], C_cyl[2], c='green', s=200, edgecolors='black', zorder=10)
    ax7.scatter(F_cyl[1], F_cyl[2], c='blue', s=200, edgecolors='black', zorder=10)
    
    ax7.annotate('P', (P_cyl[1], P_cyl[2]), textcoords="offset points", xytext=(10, 10), 
                fontsize=15, fontweight='bold', color='red')
    ax7.annotate('C', (C_cyl[1], C_cyl[2]), textcoords="offset points", xytext=(10, 5), 
                fontsize=15, fontweight='bold', color='green')
    ax7.annotate('F', (F_cyl[1], F_cyl[2]), textcoords="offset points", xytext=(10, -10), 
                fontsize=15, fontweight='bold', color='blue')
    
    ax7.axhline(y=0, color='gray', linewidth=0.5)
    ax7.axvline(x=0, color='gray', linewidth=0.5)
    ax7.set_xlim(-5, 5)
    ax7.set_ylim(-7, 7)
    ax7.set_aspect('equal')
    ax7.set_xlabel('y (Im)', fontsize=14)
    ax7.set_ylabel('z = φy', fontsize=14)
    ax7.set_title('Lateral view: Line z=φy\nVertices aligned', fontsize=14, fontweight='bold')
    ax7.tick_params(labelsize=12)
    ax7.legend(loc='upper left', fontsize=13)
    ax7.grid(True, alpha=0.3)
    
    # --- Panel 8: Lateral view LATTICE (vw plane) ---
    ax8 = fig.add_subplot(338)
    
    # Lattice projected to vw plane
    for n1 in range(-2, 3):
        for n2 in range(-2, 3):
            v = n2 * M_vis
            w = PHI * v
            ax8.scatter(v, w, c='cyan', s=80, marker='D', edgecolors='blue')
    
    # Line w = φv
    ax8.plot(y_line * M_vis/3, PHI * y_line * M_vis/3, 'b--', linewidth=2, label='w = φv')
    
    # Cell projected is a line (degenerate)
    v_cell = [0, M_vis]
    w_cell = [0, PHI*M_vis]
    ax8.plot(v_cell, w_cell, 'b-', linewidth=3, label='Cell → line')
    
    ax8.axhline(y=0, color='gray', linewidth=0.5)
    ax8.axvline(x=0, color='gray', linewidth=0.5)
    ax8.set_xlim(-5, 5)
    ax8.set_ylim(-8, 8)
    ax8.set_aspect('equal')
    ax8.set_xlabel('v (Im)', fontsize=14)
    ax8.set_ylabel('w = φv', fontsize=14)
    ax8.set_title('Lateral view: Line w=φv\nCell degenerates', fontsize=14, fontweight='bold')
    ax8.tick_params(labelsize=12)
    ax8.legend(loc='upper left', fontsize=12)
    ax8.grid(True, alpha=0.3)
    
    # --- Panel 9: Isometric view (showing RHOMBUS) ---
    ax9 = fig.add_subplot(339, projection='3d')
    
    # Complete lattice
    for n1 in range(-2, 3):
        for n2 in range(-2, 3):
            u = n1 * M_vis
            v = n2 * M_vis
            w = PHI * v
            ax9.scatter(u, v, w, c='cyan', s=80, marker='s', edgecolors='blue')
    
    # Fundamental cell (parallelogram = "rhombus" in projection)
    ax9.add_collection3d(Poly3DCollection(verts, alpha=0.4, facecolor='cyan', edgecolor='blue', linewidth=2))
    
    # Specific view showing the rhombus
    ax9.view_init(elev=45, azim=0)
    ax9.set_xlabel('u', fontsize=14)
    ax9.set_ylabel('v', fontsize=14)
    ax9.set_zlabel('w', fontsize=14)
    ax9.set_title('Isometric view (45°,0°)\nCell as rhombus', fontsize=14, fontweight='bold')
    ax9.tick_params(labelsize=12)
    ax9.xaxis.set_major_locator(MaxNLocator(4))
    ax9.yaxis.set_major_locator(MaxNLocator(4))
    ax9.zaxis.set_major_locator(MaxNLocator(4))
    
    plt.tight_layout(pad=3.0)
    
    # Save figure
    output_path = output_dir / "cylinder_lattice_connection"
    save_figure(fig, output_path, verbose=verbose)
    
    # Cleanup
    plt.close(fig)
    
    if verbose:
        print("  ✓ Cylinder-lattice connection figure generated")

