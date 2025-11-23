

import matplotlib.pyplot as plt
import matplotlib

from pimpmyplot.utils import setupax

from typing import Tuple


@setupax
def legend(*args, 
           shadow: bool = True, 
           frameon: bool = True,
           loc: str = 'upper center',
           bbox_to_anchor: Tuple = (.5, -.1),
           edgecolor: str = 'k',
           ax: matplotlib.axes.Axes = None,
           ncol: int = None,
           **kwargs) -> matplotlib.legend.Legend:
    '''
    Customize legend
    '''

    # Deduce number labels in legend
    if ncol is None:
        legend_handles = [line for line in ax.get_lines() if line.get_label() != '_nolegend_']
        ncol = len(legend_handles)

    # Call standard legend
    l = ax.legend(*args, 
                  shadow=shadow, 
                  frameon=frameon, 
                  loc=loc, 
                  bbox_to_anchor=bbox_to_anchor, 
                  edgecolor=edgecolor, 
                  ncol=ncol,
                  **kwargs)
    
    # Shadow style
    l._shadow_props = {'ox': 3, 'oy': -3, 'color': 'black', 'shade': 1., 'alpha': 1.}

    return l






