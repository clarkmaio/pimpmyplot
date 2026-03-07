

import matplotlib.pyplot as plt
import matplotlib
from typing import List

from pimpmyplot.utils import setupax



@setupax
def remove_axis(*spines: str, ax: matplotlib.axes.Axes = None) -> None:
    """
    Make specified axis spines not visible.

    Parameters
    ----------
    *spines : str
        The spines to remove. Options: 'top', 'bottom', 'left', 'right'.
        If no spines are provided, all four spines will be removed.
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis object to modify. If None, uses the current axis (via @setupax).
    """

    spines = ['top', 'bottom', 'left', 'right'] if len(spines) == 0 else spines
    for s in spines:
        ax.spines[s].set_visible(False)


@setupax
def remove_ticks(*spines: str, ax: matplotlib.axes.Axes = None) -> None:
    """
    Remove ticks and labels from specified axis sides.

    Parameters
    ----------
    *spines : str
        The sides from which to remove ticks and labels. Options: 'top', 'bottom', 'left', 'right'.
        If no sides are provided, ticks/labels from all four sides will be removed.
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis object to modify. If None, uses the current axis (via @setupax).
    """

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
    Control how many ticks or which specific ones to display on the axis.

    Parameters
    ----------
    n : int, optional
        The absolute number of ticks to display.
    every : int, optional
        Display a subset of ticks, keeping only every N-th tick.
    values : List, optional
        A list of specific values to use as ticks.
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis object to modify. If None, uses the current axis (via @setupax).
    """
    
    assert n | every | values, "One between n, every and values parameters must be not None"
    
    if n:
        pass

    elif every:
        pass

    elif values:
        pass



