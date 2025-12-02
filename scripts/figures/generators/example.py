"""
Example figure generator.

This is a template showing how to create a generator.
It can be deleted or used as a reference.
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
from utils import setup_figure, save_figure


@register("example")
def generate_example(output_dir: Path, verbose: bool = False) -> None:
    """
    Generate an example figure.
    
    This is a template demonstrating:
    - How to register a generator
    - How to use plotting utilities
    - How to save the figure
    
    Args:
        output_dir: Directory where to save the figure
        verbose: If True, show additional information
    """
    if verbose:
        print("  Generating example figure...")
    
    # Create figure with standard configuration
    fig, ax = setup_figure(width=6.0, height=4.0)
    
    # Generate example data
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x)
    
    # Plot
    ax.plot(x, y, label="sin(x)")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Example Figure")
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # Save
    output_path = output_dir / "example"
    save_figure(fig, output_path, verbose=verbose)
    
    # Cleanup
    plt.close(fig)
    
    if verbose:
        print("  ✓ Example figure generated")

