import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import matplotlib.pyplot as plt
import numpy as np
import pimpmyplot as pmp

def _save(name):
    static_dir = os.path.join(os.path.dirname(__file__), '_static')
    os.makedirs(static_dir, exist_ok=True)
    out_path = os.path.join(static_dir, f'{name}.png')
    plt.savefig(out_path, bbox_inches='tight', dpi=150)
    print(f"Saved {out_path}")
    plt.close()

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
    _save('quickstart_plot')

def generate_bullet_grid_plot():
    np.random.seed(42)
    x = np.random.randn(50)
    y = x * 1.5 + np.random.randn(50)
    plt.figure(figsize=(6, 4))
    plt.scatter(x, y, color='tab:blue', alpha=0.7)
    pmp.bullet_grid()
    plt.title('Bullet Grid')
    _save('bullet_grid_plot')

def generate_remove_axis_plot():
    x = np.linspace(0, 5, 50)
    y = np.exp(x)
    plt.figure(figsize=(6, 4))
    plt.plot(x, y, color='tab:orange', lw=2)
    pmp.remove_axis('top', 'right')
    plt.title('Remove Axis (top, right)')
    _save('remove_axis_plot')

def generate_remove_ticks_plot():
    categories = ['A', 'B', 'C', 'D']
    values = [10, 15, 7, 12]
    plt.figure(figsize=(6, 4))
    plt.bar(categories, values, color='tab:green', alpha=0.8)
    pmp.remove_axis('top', 'right', 'left')
    pmp.remove_ticks('left', 'bottom', 'top', 'right')
    plt.title('Remove Ticks (all sides)')
    _save('remove_ticks_plot')

def generate_legend_plot():
    x = np.linspace(0, 10, 100)
    plt.figure(figsize=(6, 3))
    plt.plot(x, np.sin(x), label='Model A')
    plt.plot(x, np.cos(x), label='Model B')
    plt.plot(x, np.sin(x)*np.cos(x), label='Model C')
    pmp.remove_axis('top', 'right')
    pmp.legend(loc='ext side upper right', title='Models')
    _save('legend_plot')

def generate_annotation_legend_plot():
    x = np.linspace(0, 10, 100)
    plt.figure(figsize=(6, 4))
    plt.plot(x, x**1.5, label='Fast Growth', lw=2)
    plt.plot(x, x*5, label='Linear', lw=2)
    plt.plot(x, 20*np.log(x+1), label='Slow Growth', lw=2)
    pmp.remove_axis('top', 'right')
    pmp.annotation_legend()
    _save('annotation_legend_plot')

if __name__ == "__main__":
    generate_quickstart_plot()
    generate_bullet_grid_plot()
    generate_remove_axis_plot()
    generate_remove_ticks_plot()
    generate_legend_plot()
    generate_annotation_legend_plot()
