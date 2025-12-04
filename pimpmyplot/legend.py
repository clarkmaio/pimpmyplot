

import matplotlib.pyplot as plt
import matplotlib

from pimpmyplot.utils import setupax

from typing import Tuple




EXT_LOC_MAP = {
    'ext lower center': ('upper center', (.5, -0.1)),
    'ext lower right': ('lower left', (1., 0.)),
    'ext lower left': ('lower right', (-0.01, 0.)), 
    'ext upper right': ('upper left', (1, 1.03)),
    'ext upper left': ('upper right', (-0.01, 1.03)),
    'ext upper center': ('lower center', (.5, 1.03)),
}


@setupax
def legend(*args, 
           shadow: bool = True, 
           frameon: bool = True,
           loc: str = 'ext lower center',
           bbox_to_anchor: Tuple = None,
           edgecolor: str = 'k',
           ax: matplotlib.axes.Axes = None,
           ncol: int = None,
           **kwargs) -> matplotlib.legend.Legend:
    """
    Just a wrap of standard legend with additional features and style.
    Can handle external legend location

    Params
    -------
    loc: str
        legend location. One can locate the legend at the exterior of plot prefix "ext" (a.e. "ext upper center")
    ncol: int
        number of legend columns. Default is the number of labels to make legend flat. Set 1 for classical vertical legend

    """

    if loc.startswith('ext'):
        # To display legend at the exterior you need a new loc and the associated bboc_to_anchor for offset
        loc, bbox_to_anchor = EXT_LOC_MAP[loc]


    # Deduce number labels in legend
    if ncol is None:
        handles, labels = ax.get_legend_handles_labels()
        ncol = len(labels)

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




@setupax
def annotation_legend(ax: matplotlib.axes.Axes = None, 
                line_color: bool = False, 
                offset: Tuple = (5, -2), 
                fontweight: str = None, 
                size: str = None,
                ha: str = 'left', 
                color: str = 'black'):
    """
    Create a legend printing labels next to last value on the right.
    
    Params
    -------
        ax: matplotlib.axes.Axes
            axis the legend willbe applied to
        line_color: bool 
            True to apply to labels same color of curves
        offset:
            Tuple to apply custom offset on labels
        color:
            Make all labels with this color. Ignored if line_color is True
        
    """

    for line in ax.get_lines():        
        x_coord, y_coord, label = extract_line_info(line=line)
        c = line.get_color() if line_color else color

        ax.annotate(
            text=label,
            xy=(x_coord, y_coord),
            textcoords='offset points',
            xytext=offset,
            color=c,
            ha=ha,
            size=size,
            fontweight=fontweight
        )


def extract_line_info(line):
    x_coord = line.get_xdata()[-1]
    y_coord = line.get_ydata()[-1]
    label = line.get_label() 
    return x_coord, y_coord, label
