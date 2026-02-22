# Core Features

Pimp My Plot provides several functions that make it incredibly easy to style your plots without the typical matplotlib boilerplate code. Here are the most important features and their inputs.

## `pimpmyplot.bullet_grid`

Builds a grid similar to a dotted bullet journal by scattering small points uniformly across the axis.

```python
import pimpmyplot as pmp
pmp.bullet_grid(ax=None, stepinch=0.5, scatter_kwargs={})
```

- `ax`: The matplotlib axis to apply the grid to. If `None`, the current axis is used.
- `stepinch` *(float)*: Data-independent distance between dots, measured in inches. Default is `0.5`.
- `scatter_kwargs` *(dict)*: Additional keyword arguments passed to `ax.scatter` to customize the appearance of the dots (default: `s=2`, `color='#cccccc'`, `alpha=0.8`).

![Bullet Grid Plot](assets/bullet_grid_plot.png)

## `pimpmyplot.remove_axis`

Quickly removes the specified spines (borders) from your plot.

```python
pmp.remove_axis('top', 'right', ax=None)
```

- `*spines` *(str)*: A sequence of spine names to remove. Valid options are `'top'`, `'bottom'`, `'left'`, and `'right'`. If no arguments are passed, it removes all spines.
- `ax`: The axis to modify.

![Remove Axis Plot](assets/remove_axis_plot.png)

## `pimpmyplot.remove_ticks`

Removes the ticks and their labels from the specified sides of the plot.

```python
pmp.remove_ticks('top', 'right', ax=None)
```

- `*spines` *(str)*: A sequence of spine names to remove the ticks from. Same as `remove_axis`.
- `ax`: The axis to modify.

![Remove Ticks Plot](assets/remove_ticks_plot.png)

## `pimpmyplot.legend`

A wrapper around the standard matplotlib legend but with better styling defaults (such as a nice shadow) and horizontal layout. Especifically designed to easily locate the legend completely outside the plot area using the `'ext'` prefix in the `loc` parameter.

```python
pmp.legend(loc='ext lower center', ncol=None, ax=None, shadow=True, edgecolor='k')
```

- `loc` *(str)*: Legend location. You can place the legend completely outside the plot by prefixing standard positions with `'ext '`. For example:
    - `'ext lower center'` (Below the plot, centered)
    - `'ext lower right'`
    - `'ext upper left'`
    - `'ext side upper right'` (Outside the plot on the right side)
- `ncol` *(int)*: Number of columns for the legend. By default, it dynamically infers the number of rows/columns depending on the location to flatten the legend horizontally.
- `ax`, `shadow`, `edgecolor`: Used to further style the legend exactly like standard matplotlib.

![Legend Plot](assets/legend_plot.png)

## `pimpmyplot.annotation_legend`

An extremely clean alternative to the traditional legend. Instead of using a dedicated box, it places the label of each line directly next to the end of the line on the plot.

```python
pmp.annotation_legend(ax=None, offset=None, ha='left', color=None, fontweight=None, size=None)
```

- `offset` *(tuple)*: Tuple specifying a custom offset in points for the labels.
- `ha` *(str)*: Horizontal alignment of the text (e.g. `'left'`).
- `color` *(str)*: Forces all labels to use this color. If `None`, each label automatically inherits the color of its corresponding line.

![Annotation Legend Plot](assets/annotation_legend_plot.png)
