

import matplotlib.pyplot as plt
import matplotlib

from pimpmyplot.utils import setupax

from typing import Tuple




POSITION_SETUP = {
    'upper': (),
    'lower': ('upper center', (.5, -.1)),
    'right': ('upper left', (1, 1.03)),
    'left': ('upper right', ())
}


@setupax
def legend(*args, 
           shadow: bool = True, 
           frameon: bool = True,
           loc: str = 'upper center',
           bbox_to_anchor: Tuple = (.5, -.1),
           edgecolor: str = 'k',
           ax: matplotlib.axes.Axes = None,
           ncol: int = None,
           position: str = None,
           **kwargs) -> matplotlib.legend.Legend:
    
    if position:
        loc = None
        bbox_to_anchor = None


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
