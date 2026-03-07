

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
    """
    Extract coordinate and label information from a matplotlib Line2D object.

    Parameters
    ----------
    line : matplotlib.lines.Line2D
        The line object to extract information from.

    Returns
    -------
    Tuple[float, float, str]
        A tuple containing (last_x_coord, last_y_coord, label).
    """
    x_coord = line.get_xdata()[-1]
    y_coord = line.get_ydata()[-1]
    label = line.get_label() 
    return x_coord, y_coord, label


def get_number_labels(ax) -> int:
    """
    Count the number of labeled handles in the axis.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The axis to inspect.

    Returns
    -------
    int
        The number of legend labels found.
    """
    _, labels = ax.get_legend_handles_labels()
    return len(labels)


def infer_ncol(ncol: int, ax, loc: str):
    """
    Determine the appropriate number of columns for the legend if not explicitly provided.

    Parameters
    ----------
    ncol : int
        The requested number of columns.
    ax : matplotlib.axes.Axes
        The axis object.
    loc : str
        The location string for the legend.

    Returns
    -------
    int
        The inferred number of columns.
    """
    if ncol == -1:
        ncol = get_number_labels(ax=ax)
    elif ncol is None:
        ncol = 1
        if not loc.startswith('ext side'):
            ncol = get_number_labels(ax=ax)
    return ncol


def get_tick_labels_shape(ax) -> Tuple:
    """
    Calculate the maximum width and height of x and y tick labels.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The axis object.

    Returns
    -------
    Tuple[Tuple[float, float], Tuple[float, float]]
        ((max_x_width, max_x_height), (max_y_width, max_y_height)) in points.
    """
    x_width = max(*[l.get_window_extent().width for l in ax.get_xticklabels()])
    x_height = max(*[l.get_window_extent().height for l in ax.get_xticklabels()])

    y_width = max(*[l.get_window_extent().width for l in ax.get_yticklabels()])
    y_height = max(*[l.get_window_extent().height for l in ax.get_yticklabels()])

    return (x_width, x_height), (y_width, y_height)
    


def _build_ext_bbox_to_anchor(loc: str, ax) -> Tuple:
    """
    Calculate the bounding box to anchor (bbox_to_anchor) for external legend locations.

    Parameters
    ----------
    loc : str
        The external location string (starts with 'ext').
    ax : matplotlib.axes.Axes
        The axis object.

    Returns
    -------
    Tuple[str, Tuple[float, float]]
        A tuple of (standardized_loc, bbox_to_anchor_coordinates).
    """

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
    Enhanced matplotlib legend with support for external positioning and custom styling.

    Parameters
    ----------
    *args :
        Arguments passed to the standard `ax.legend`.
    shadow : bool, optional
        Whether to draw a shadow behind the legend, by default True.
    frameon : bool, optional
        Whether to draw a frame around the legend, by default True.
    loc : str, optional
        The legend location. Supports standard matplotlib locations and 'ext' prefixed 
        locations (e.g., 'ext lower center' or 'ext side upper left'), by default 'ext lower center'.
    bbox_to_anchor : Tuple, optional
        The bounding box to anchor the legend to, by default None.
    edgecolor : str, optional
        The color of the legend frame edge, by default 'k' (black).
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to add the legend to. If None, uses the current axis (via @setupax).
    ncol : int, optional
        Number of columns. If -1, sets to the number of labels. If None, it is inferred.
    **kwargs :
        Additional keyword arguments passed to `ax.legend`.

    Returns
    -------
    matplotlib.legend.Legend
        The created legend object.
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
    Create an annotation-style legend where labels are printed directly next to the lines.

    Labels are placed at the end of each line on the right side of the plot.

    Parameters
    ----------
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to apply annotations to. If None, uses the current axis (via @setupax).
    offset : Tuple, optional
        Offset in points for the labels (dx, dy), by default derived from `ha`.
    fontweight : str, optional
        The font weight for the labels (e.g., 'bold').
    size : str or float, optional
        The font size for the labels.
    ha : str, optional
        Horizontal alignment of the labels, by default 'left'.
    color : str, optional
        Color for all labels. If None, each label uses the color of its corresponding line.
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


