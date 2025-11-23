

import matplotlib.pyplot as plt
import matplotlib
from typing import List

from pimpmyplot.utils import setupax



@setupax
def remove_axis(*spines: str, ax: matplotlib.axes.Axes = None) -> None:
    '''
    Make axis not visible.

    Params
    -------
    *sides : str
        Options: 'top', 'bottom', 'left', 'right'. 
        If nothing is passed all axis will be removed
    
    ax : plt.axis
        Apply styling to this axis
    '''

    spines = ['top', 'bottom', 'left', 'right'] if len(spines) == 0 else spines
    for s in spines:
        ax.spines[s].set_visible(False)


def remove_ticks(*spines: str, ax: plt.axis = None) -> None:

    if not ax:
        ax = plt.gca()

    spines = ['top', 'bottom', 'left', 'right'] if len(spines) == 0 else spines
    tickkwargs = {s: False for s in spines}
    labelkwargs = {f'label{s}': False for s in spines}
    ax.tick_params(
        **tickkwargs,
        **labelkwargs
    )

