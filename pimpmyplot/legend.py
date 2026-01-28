

import matplotlib.pyplot as plt
import matplotlib

from pimpmyplot.utils import setupax

from typing import Tuple




EXT_LOC_MAP = {
    'ext lower center': ('upper center', (.5, -0.1)),
    'ext lower right': ('upper right', (1., -0.1)),
    'ext lower left': ('upper left', (-0.01, -0.1)),
    'ext upper center': ('lower center', (.5, 1.03)), 
    'ext upper right': ('lower right', (1, 1.03)),
    'ext upper left': ('lower left', (-0.01, 1.03)),

    'ext side lower left': ('lower right', (None, -0.02)),
    'ext side upper left': ('upper right', (None, 1.02)),
    'ext side lower right': ('lower left', (1., -0.02)),
    'ext side upper right': ('upper left', (1., 1.02))
}


DEFAULT_OFFSET_ANNOTATION_LEGEND =  {
    'left': (5, 0),
    'center': (0, 5),
    'right': (-5, 0)
}


def extract_line_info(line):
    x_coord = line.get_xdata()[-1]
    y_coord = line.get_ydata()[-1]
    label = line.get_label() 
    return x_coord, y_coord, label


def get_number_labels(ax) -> int:
    _, labels = ax.get_legend_handles_labels()
    return len(labels)


def infer_ncol(ncol: int, ax, loc: str):
    if ncol == -1:
        ncol = get_number_labels(ax=ax)
    elif ncol is None:
        ncol = 1
        if not loc.startswith('ext side'):
            ncol = get_number_labels(ax=ax)
    return ncol


def get_tick_labels_shape(ax) -> Tuple:
    """
    Return max width of x and y ticks labels
    """
    x_width = max(*[l.get_window_extent().width for l in ax.get_xticklabels()])
    x_height = max(*[l.get_window_extent().height for l in ax.get_xticklabels()])

    y_width = max(*[l.get_window_extent().width for l in ax.get_yticklabels()])
    y_height = max(*[l.get_window_extent().height for l in ax.get_yticklabels()])

    return (x_width, x_height), (y_width, y_height)
    


def _build_ext_bbox_to_anchor(loc: str, ax) -> Tuple:
    '''
    In case of ext location return the loc and bbox to use to place legend
    '''

    _cases_dynamic_mapping = (loc.endswith('left') and loc.startswith('ext side'))
    loc, bbox_to_anchor = EXT_LOC_MAP[loc]
    if not _cases_dynamic_mapping:
        return loc, bbox_to_anchor

    # TODO Make MARGIN dynamic. Percentage of (max_width_labels) / (ax_width)?
    MARGIN = 0.05
    y_labels = ax.get_yticklabels()
    max_width_labels = max(*[l.get_window_extent().width for l in y_labels])
    ax_width = ax.get_position().transformed(plt.gca().transAxes.get_affine()).width
    L = (max_width_labels) / (ax_width) + MARGIN
    bbox_to_anchor = (-L, bbox_to_anchor[1])

    return loc, bbox_to_anchor




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

    original_loc = loc
    if loc.startswith('ext'):
        loc, bbox_to_anchor = _build_ext_bbox_to_anchor(loc=loc, ax=ax)

    ncol = infer_ncol(ncol=ncol, ax=ax, loc=original_loc)

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
                offset: Tuple = None, 
                fontweight: str = None, 
                size: str = None,
                ha: str = 'left', 
                color: str = None):
    """
    Create a legend printing labels next to last value on the right.
    
    Params
    -------
        ax: matplotlib.axes.Axes
            axis the legend willbe applied to
        offset:
            Tuple to apply custom offset on labels
        color:
            Make all labels with this color. If None use same color of associated plot
        
    """


    if offset is None:
        offset = DEFAULT_OFFSET_ANNOTATION_LEGEND[ha]


    for line in ax.get_lines():        
        x_coord, y_coord, label = extract_line_info(line=line)
        c = line.get_color() if color is None else color

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


