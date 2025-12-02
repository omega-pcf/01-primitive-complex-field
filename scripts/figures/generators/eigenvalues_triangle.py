"""
Eigenvalues and equilateral triangle figure generator.

Shows the eigenvalues λ_k = (1/2)ω^k forming an equilateral triangle
on the circle |z| = 1/2.
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
omega = np.exp(2j * np.pi / 3)  # Primitive cube root of unity


@register("eigenvalues_triangle")
def generate_eigenvalues_triangle(output_dir: Path, verbose: bool = False) -> None:
    """
    Generate figure showing eigenvalues λ_k = (1/2)ω^k forming an equilateral triangle
    on the circle |z| = 1/2.
    
    Args:
        output_dir: Directory where to save the figure
        verbose: If True, show additional information
    """
    if verbose:
        print("  Generating eigenvalues and triangle figure...")
    
    # Create figure with wider aspect for two panels
    fig, axes = plt.subplots(1, 2, figsize=(14, 7))
    
    # === Left panel: Eigenvalues in the complex plane ===
    ax1 = axes[0]
    
    theta = np.linspace(0, 2*np.pi, 100)
    
    # Unit circle (reference)
    ax1.plot(np.cos(theta), np.sin(theta), 'k--', linewidth=1, alpha=0.3)
    
    # Circle |z| = 1/2
    ax1.plot(0.5*np.cos(theta), 0.5*np.sin(theta), 'b-', linewidth=2)
    
    # Eigenvalues
    eigenvals = [0.5, 0.5*omega, 0.5*omega**2]
    colors = ['red', 'green', 'blue']
    labels = [r'$\lambda_0 = \frac{1}{2}$', 
              r'$\lambda_1 = \frac{1}{2}\omega$', 
              r'$\lambda_2 = \frac{1}{2}\omega^2$']
    
    for ev, col, lab in zip(eigenvals, colors, labels):
        ax1.plot(ev.real, ev.imag, 'o', color=col, markersize=20, 
                markeredgecolor='black', markeredgewidth=2)
        # Line from origin
        ax1.plot([0, ev.real], [0, ev.imag], '-', color=col, linewidth=2, alpha=0.5)
    
    # Triangle connecting eigenvalues
    triangle_x = [ev.real for ev in eigenvals] + [eigenvals[0].real]
    triangle_y = [ev.imag for ev in eigenvals] + [eigenvals[0].imag]
    ax1.plot(triangle_x, triangle_y, 'purple', linewidth=2, linestyle='--')
    ax1.fill(triangle_x[:-1], triangle_y[:-1], alpha=0.15, color='purple')
    
    # Angles
    for k, ev in enumerate(eigenvals):
        angle = k * 120
        ax1.annotate(f'{angle}°', xy=(ev.real*0.6, ev.imag*0.6), fontsize=10, ha='center')
    
    ax1.axhline(0, color='gray', linewidth=0.5)
    ax1.axvline(0, color='gray', linewidth=0.5)
    ax1.set_xlim(-0.8, 0.8)
    ax1.set_ylim(-0.8, 0.8)
    ax1.set_aspect('equal')
    ax1.set_xlabel('Re(λ)', fontsize=12)
    ax1.set_ylabel('Im(λ)', fontsize=12)
    ax1.set_title(r'Eigenvalues in the complex plane', fontsize=12, fontweight='bold')
    
    # === Right panel: The diagonal matrix ===
    ax2 = axes[1]
    ax2.axis('off')
    
    # Draw the matrix visually
    cell_size = 1.2
    for i in range(3):
        for j in range(3):
            x = j * cell_size
            y = (2 - i) * cell_size
            
            if i == j:
                # Diagonal
                colors_diag = ['red', 'green', 'blue']
                rect = plt.Rectangle((x, y), cell_size, cell_size, 
                                     facecolor=colors_diag[i], alpha=0.3, edgecolor='black', linewidth=2)
                ax2.add_patch(rect)
                
                if i == 0:
                    ax2.text(x + cell_size/2, y + cell_size/2, r'$\frac{1}{2}$', 
                            ha='center', va='center', fontsize=14, fontweight='bold')
                elif i == 1:
                    ax2.text(x + cell_size/2, y + cell_size/2, r'$\frac{\omega}{2}$', 
                            ha='center', va='center', fontsize=14, fontweight='bold')
                else:
                    ax2.text(x + cell_size/2, y + cell_size/2, r'$\frac{\omega^2}{2}$', 
                            ha='center', va='center', fontsize=14, fontweight='bold')
            else:
                # Off-diagonal
                rect = plt.Rectangle((x, y), cell_size, cell_size, 
                                     facecolor='white', edgecolor='black', linewidth=1)
                ax2.add_patch(rect)
                ax2.text(x + cell_size/2, y + cell_size/2, '0', 
                        ha='center', va='center', fontsize=12, color='gray')
    
    # Matrix brackets
    ax2.plot([-0.1, -0.1], [-0.1, 3*cell_size + 0.1], 'k-', linewidth=3)
    ax2.plot([-0.1, 0.1], [-0.1, -0.1], 'k-', linewidth=3)
    ax2.plot([-0.1, 0.1], [3*cell_size + 0.1, 3*cell_size + 0.1], 'k-', linewidth=3)
    
    ax2.plot([3*cell_size + 0.1, 3*cell_size + 0.1], [-0.1, 3*cell_size + 0.1], 'k-', linewidth=3)
    ax2.plot([3*cell_size - 0.1, 3*cell_size + 0.1], [-0.1, -0.1], 'k-', linewidth=3)
    ax2.plot([3*cell_size - 0.1, 3*cell_size + 0.1], [3*cell_size + 0.1, 3*cell_size + 0.1], 'k-', linewidth=3)
    
    ax2.text(1.5*cell_size, -0.6, r'$\hat{\Omega} = \frac{1}{2}\,\mathrm{diag}(1, \omega, \omega^2)$', 
            ha='center', fontsize=14, fontweight='bold')
    
    ax2.set_xlim(-0.5, 4)
    ax2.set_ylim(-1, 4)
    ax2.set_aspect('equal')
    ax2.set_title(r'Diagonal matrix representation', fontsize=12, fontweight='bold')
    
    plt.tight_layout(rect=[0, 0, 1, 0.94])
    
    # Save figure
    output_path = output_dir / "eigenvalues_triangle"
    save_figure(fig, output_path, verbose=verbose)
    
    # Cleanup
    plt.close(fig)
    
    if verbose:
        print("  ✓ Eigenvalues and triangle figure generated")

