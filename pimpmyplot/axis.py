

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


@setupax
def remove_ticks(*spines: str, ax: matplotlib.axes.Axes = None) -> None:

    if not ax:
        ax = plt.gca()

    spines = ['top', 'bottom', 'left', 'right'] if len(spines) == 0 else spines
    tickkwargs = {s: False for s in spines}
    labelkwargs = {f'label{s}': False for s in spines}
    ax.tick_params(
        **tickkwargs,
        **labelkwargs
    )


@setupax
def display_ticks(n: int = None, every: int = None, values: List = None, ax: matplotlib.axes.Axes = None) -> None:
    """
    Handle axis ticks display. Control how many ticks or which ones to show

    Params
    -------
    n: int
        Absolute number of ticks to display
    every: int
        Disiplay subset of ticks among default ones adopting the frequency defined by this parameter
    values: List
        Use this values as ticks
    """

    assert n | every | values, "One between n, every and values parameters must be not None"
    
    if n:
        pass

    elif every:
        pass

    elif values:
        pass



