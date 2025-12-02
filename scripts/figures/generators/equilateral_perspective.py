"""
Equilateral perspective search figure generator.

Shows the search for equilateral perspective in the PCF torus, demonstrating
how vertices P, C, F form an equilateral triangle in the XY projection of the
cylinder but not in the 3D torus where the coupling z = φy introduces metric distortion.
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
R0 = 3  # Base radius of the cylinder
R_major = 7.5  # Major radius of torus (α * R0 where α = 2.5)
R_minor = 3  # Minor radius of torus (equal to R0)


def torus_parametrization(u, v, R_major, R_minor):
    """Parametrization of torus: Ψ(u, v)"""
    x = (R_major + R_minor * np.cos(v)) * np.cos(u)
    y = (R_major + R_minor * np.cos(v)) * np.sin(u)
    z = R_minor * np.sin(v)
    return np.array([x, y, z])


@register("equilateral_perspective")
def generate_equilateral_perspective(output_dir: Path, verbose: bool = False) -> None:
    """
    Generate figure showing search for equilateral perspective in PCF torus.
    
    Args:
        output_dir: Directory where to save the figure
        verbose: If True, show additional information
    """
    if verbose:
        print("  Generating equilateral perspective figure...")
    
    # Create figure for 3 panels
    fig = plt.figure(figsize=(18, 6))
    
    # Calculate torus bounds to center it in all views
    torus_max_extent = R_major + R_minor  # 10.5
    margin = 1.0
    x_range = torus_max_extent + margin
    y_range = torus_max_extent + margin
    z_range = R_minor + margin
    
    # Vertices on torus (exact coordinates from paper, §1163-1168)
    P_t = np.array([10.5, 0, 0])
    C_t = np.array([9.077, 0, 2.552])
    F_t = np.array([5.923, 0, -2.552])
    
    # Torus surface (shared by all panels)
    u_torus = np.linspace(0, 2*np.pi, 50)
    v_torus = np.linspace(0, 2*np.pi, 50)
    U, V = np.meshgrid(u_torus, v_torus)
    X_torus = (R_major + R_minor * np.cos(V)) * np.cos(U)
    Y_torus = (R_major + R_minor * np.cos(V)) * np.sin(U)
    Z_torus = R_minor * np.sin(V)
    
    # === Panel 1: Front view (elev=0, azim=0) - Torus ===
    # Same torus as panels 2 and 3, but viewed from the front
    # In this view, vertices P, C, F appear colinear vertically (along Z)
    ax1 = fig.add_subplot(131, projection='3d')
    
    ax1.plot_surface(X_torus, Y_torus, Z_torus, alpha=0.15, color='gray')
    
    # In front view, these vertices appear colinear vertically
    # They all have y=0, so they appear as a vertical line
    vertices_torus = np.array([F_t, P_t, C_t])  # F (blue, bottom), P (red, middle), C (green, top)
    
    colors = ['blue', 'red', 'green']
    labels = ['F', 'P', 'C']
    
    for v, c, l in zip(vertices_torus, colors, labels):
        ax1.scatter(v[0], v[1], v[2], c=c, s=250, edgecolors='black', linewidth=2, zorder=10)
        ax1.text(v[0]+0.4, v[1]+0.4, v[2]+0.4, l, fontsize=16, fontweight='bold', color=c)
    
    # Green line connecting vertices (appear colinear vertically in front view)
    ax1.plot([F_t[0], P_t[0], C_t[0]], 
             [F_t[1], P_t[1], C_t[1]], 
             [F_t[2], P_t[2], C_t[2]], 'g-', linewidth=3, alpha=0.8)
    
    ax1.set_xlabel('X', fontsize=14)
    ax1.set_ylabel('Y', fontsize=14)
    ax1.set_zlabel('Z', fontsize=14)
    ax1.tick_params(labelsize=12)
    # Format ticks to remove .0 and reduce number of ticks
    ax1.xaxis.set_major_locator(plt.MaxNLocator(5))
    ax1.yaxis.set_major_locator(plt.MaxNLocator(5))
    ax1.zaxis.set_major_locator(plt.MaxNLocator(5))
    ax1.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{int(x) if x == int(x) else x}'))
    ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{int(x) if x == int(x) else x}'))
    ax1.zaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{int(x) if x == int(x) else x}'))
    ax1.set_xlim(-x_range, x_range)
    ax1.set_ylim(-y_range, y_range)
    ax1.set_zlim(-z_range, z_range)
    ax1.view_init(elev=0, azim=0)  # Front view
    
    # === Panel 2: Top view (elev=90, azim=0) - Torus ===
    ax2 = fig.add_subplot(132, projection='3d')
    
    ax2.plot_surface(X_torus, Y_torus, Z_torus, alpha=0.15, color='gray')
    
    for v, c, l in zip(vertices_torus, ['blue', 'red', 'green'], ['F', 'P', 'C']):
        ax2.scatter(v[0], v[1], v[2], c=c, s=250, edgecolors='black', linewidth=2, zorder=10)
        ax2.text(v[0]+0.4, v[1]+0.4, v[2]+0.4, l, fontsize=16, fontweight='bold', color=c)
    
    # Light blue/cyan lines connecting vertices
    ax2.plot([F_t[0], C_t[0]], [F_t[1], C_t[1]], [F_t[2], C_t[2]], 
             'cyan', linewidth=2, alpha=0.7)
    ax2.plot([C_t[0], P_t[0]], [C_t[1], P_t[1]], [C_t[2], P_t[2]], 
             'cyan', linewidth=2, alpha=0.7)
    
    ax2.set_xlabel('X', fontsize=14)
    ax2.set_ylabel('Y', fontsize=14)
    ax2.set_zlabel('Z', fontsize=14)
    ax2.tick_params(labelsize=12)
    # Format ticks to remove .0 and reduce number of ticks (especially important for panel 2)
    ax2.xaxis.set_major_locator(plt.MaxNLocator(4))
    ax2.yaxis.set_major_locator(plt.MaxNLocator(4))
    ax2.zaxis.set_major_locator(plt.MaxNLocator(4))
    ax2.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{int(x) if x == int(x) else x}'))
    ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{int(x) if x == int(x) else x}'))
    ax2.zaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{int(x) if x == int(x) else x}'))
    ax2.set_xlim(-x_range, x_range)
    ax2.set_ylim(-y_range, y_range)
    ax2.set_zlim(-z_range, z_range)
    ax2.view_init(elev=90, azim=0)  # Top view
    
    # === Panel 3: Isometric view (elev=30, azim=45) - Torus ===
    ax3 = fig.add_subplot(133, projection='3d')
    
    ax3.plot_surface(X_torus, Y_torus, Z_torus, alpha=0.15, color='gray')
    
    for v, c, l in zip(vertices_torus, ['blue', 'red', 'green'], ['F', 'P', 'C']):
        ax3.scatter(v[0], v[1], v[2], c=c, s=250, edgecolors='black', linewidth=2, zorder=10)
        ax3.text(v[0]+0.4, v[1]+0.4, v[2]+0.4, l, fontsize=16, fontweight='bold', color=c)
    
    # Yellow lines forming triangle
    ax3.plot([F_t[0], P_t[0]], [F_t[1], P_t[1]], [F_t[2], P_t[2]], 
             'yellow', linewidth=2.5, alpha=0.8)
    ax3.plot([P_t[0], C_t[0]], [P_t[1], C_t[1]], [P_t[2], C_t[2]], 
             'yellow', linewidth=2.5, alpha=0.8)
    ax3.plot([C_t[0], F_t[0]], [C_t[1], F_t[1]], [C_t[2], F_t[2]], 
             'yellow', linewidth=2.5, alpha=0.8)
    
    # Light blue curved path along torus surface connecting vertices
    # From paper §1156-1161: v_P = 0, v_C ≈ 1.0172, v_F ≈ -2.1244
    v_P = 0
    v_C = np.arctan2(2.552, 9.077 - 7.5)  # ≈ 1.0172
    v_F = np.arctan2(-2.552, 5.923 - 7.5)  # ≈ -2.1244
    
    # Draw arc from F to C along the torus surface (u=0, v from v_F to v_C)
    v_arc = np.linspace(v_F, v_C, 50)
    u_arc = np.zeros_like(v_arc)  # u = 0
    arc_points = np.array([torus_parametrization(u, v, R_major, R_minor) for u, v in zip(u_arc, v_arc)])
    ax3.plot(arc_points[:,0], arc_points[:,1], arc_points[:,2], 
             'cyan', linewidth=2, alpha=0.7)
    
    ax3.set_xlabel('X', fontsize=14)
    ax3.set_ylabel('Y', fontsize=14)
    ax3.set_zlabel('Z', fontsize=14)
    ax3.tick_params(labelsize=12)
    # Format ticks to remove .0 and reduce number of ticks (especially important for panel 3)
    ax3.xaxis.set_major_locator(plt.MaxNLocator(4))
    ax3.yaxis.set_major_locator(plt.MaxNLocator(4))
    ax3.zaxis.set_major_locator(plt.MaxNLocator(4))
    ax3.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{int(x) if x == int(x) else x}'))
    ax3.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{int(x) if x == int(x) else x}'))
    ax3.zaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{int(x) if x == int(x) else x}'))
    ax3.set_xlim(-x_range, x_range)
    ax3.set_ylim(-y_range, y_range)
    ax3.set_zlim(-z_range, z_range)
    ax3.view_init(elev=30, azim=45)  # Isometric view
    
    plt.tight_layout(pad=3.0)
    
    # Save figure
    output_path = output_dir / "equilateral_perspective"
    save_figure(fig, output_path, verbose=verbose)
    
    # Cleanup
    plt.close(fig)
    
    if verbose:
        print("  ✓ Equilateral perspective figure generated")
