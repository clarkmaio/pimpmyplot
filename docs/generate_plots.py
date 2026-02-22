import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import matplotlib.pyplot as plt
import numpy as np
import pimpmyplot as pmp

def generate_quickstart_plot():
    x = np.linspace(0, 10, 100)

    plt.figure(figsize=(8, 3))
    plt.plot(x, np.sin(x), label='sin(x)')
    plt.plot(x, np.sin(2*x), label='sin(2x)')
    plt.plot(x, np.sin(3*x), label='sin(3x)')

    pmp.bullet_grid(stepinch=.3)
    pmp.remove_axis('top', 'right')
    pmp.remove_ticks()
    pmp.legend(loc='ext lower center', title='Legend title')
    plt.title('Plot title')

    # Save logic
    static_dir = os.path.join(os.path.dirname(__file__), '_static')
    os.makedirs(static_dir, exist_ok=True)
    out_path = os.path.join(static_dir, 'quickstart_plot.png')
    plt.savefig(out_path, bbox_inches='tight', dpi=150)
    print(f"Saved {out_path}")

if __name__ == "__main__":
    generate_quickstart_plot()
