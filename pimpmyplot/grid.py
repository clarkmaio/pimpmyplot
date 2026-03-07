

import matplotlib
from typing import Dict, Tuple
import numpy as np
from pimpmyplot.utils import setupax


def build_uniform_meshgrid(ax: matplotlib.axes.Axes, stepinch: float = .5) -> Tuple[np.ndarray, np.ndarray]:
    """
    Create an equispaced meshgrid where the distance between points is uniform in physical units (inches).

    This function calculates the necessary steps in data coordinates to ensure that the
    grid points are separated by a fixed physical distance, regardless of the axis 
    limits or aspect ratio.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The matplotlib axis object for which to generate the meshgrid.
    stepinch : float, optional
        The physical distance between grid points in inches, by default 0.5.

    Returns
    -------
    Tuple[np.ndarray, np.ndarray]
        A tuple containing (X, Y) coordinate matrices for the meshgrid.
    """

    # Deduce axis step to make mesh uniform
    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()
    xrange, yrange = xmax - xmin, ymax - ymin
    xinch, yinch = ax.figure.get_size_inches()
    axwidth, axheight = ax.get_position().width, ax.get_position().height
    xstep = xrange / (xinch * axwidth) * stepinch
    ystep = yrange / (yinch * axheight) * stepinch

    xpoints = np.arange(xmin, xmax + xstep/2, xstep)
    ypoints = np.arange(ymin, ymax + ystep/2, ystep)
    X, Y = np.meshgrid(xpoints, ypoints)
    return X, Y



@setupax
def bullet_grid(ax: matplotlib.axes.Axes = None, stepinch: float = .5,
                s: int = 2, 
                color: str = '#cccccc', 
                marker: str = 'o', 
                alpha: float = 0.8, 
                zorder: int = -100, 
                **kwargs):
    """
    Render a grid of dots similar to a dotted bullet journal.

    The grid is uniform in physical space (inches), ensuring that dots are equally spaced
    visually even if the data scales differ significantly between X and Y axes.

    Parameters
    ----------
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on. If None, uses the current axis (via @setupax).
    stepinch : float, optional
        The physical distance between dots in inches, by default 0.5.
    s : int, optional
        The size of the dots in points^2, by default 2.
    color : str, optional
        The color of the dots, by default '#cccccc' (light gray).
    marker : str, optional
        The marker style to use, by default 'o' (circle).
    alpha : float, optional
        The transparency of the dots, by default 0.8.
    zorder : int, optional
        The drawing order of the grid, by default -100 (drawn behind most elements).
    **kwargs : dict
        Additional keyword arguments passed to `ax.scatter`.
    """
    X, Y = build_uniform_meshgrid(ax=ax, stepinch=stepinch)
    ax.scatter(X, Y,
                s=s,
                color=color,
                marker=marker,
                alpha=alpha,
                zorder=zorder,
                **kwargs)
    