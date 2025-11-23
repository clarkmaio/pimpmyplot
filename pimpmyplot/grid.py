

import matplotlib
from typing import Dict, Tuple
import numpy as np
from pimpmyplot.utils import setupax


_DEFAULT_SCATTER_KWARGS = {
    's': 2,
    'color': '#cccccc',
    'marker': 'o',
    'alpha': .8,
    'zorder': -100
}



def build_uniform_meshgrid(ax: matplotlib.axes.Axes, stepinch: float = .5) -> Tuple[np.array, np.array]:
    """Create equispaced meshgrid relative to axis scale"""

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
def bullet_grid(ax: matplotlib.axes.Axes = None, stepinch: float = .5, scatter_kwargs: Dict = {}):
    '''
    Build grid similar to dotted bullet journals
    '''
    X, Y = build_uniform_meshgrid(ax=ax, stepinch=stepinch)

    scatter_kwargs.update(_DEFAULT_SCATTER_KWARGS)
    ax.scatter(X, Y, **scatter_kwargs)
    