"""
This module provides methods for building up a figure which is for scientific publication and presentation.
    1. It supports subplots.
    2. It is mainly for plotting lines.
    3. It also serves as an example based on which the users can freely adapt for their own usage.
"""

from matplotlib import rc
from matplotlib.figure import Figure as MatFig
from matplotlib.axes import Axes
import matplotlib.pyplot as plt


# Settings for latex and font style
rc('text', usetex=True)
font = {
    'family': 'serif',
    'serif': 'Times'
}
rc('font', **font)


def new_plot(figsize: tuple) -> MatFig:
    """
    Makes a new figure.
    Args:
        figsize: tuple. The same input as directly using matplotlib.pyplot.

    Returns:
        fig: matplotlib.figure.Figure. It returns an instance of this type.
    """
    fig = plt.figure(figsize=figsize)
    return fig


def add_subplot(fig: MatFig, pos=211) -> Axes:
    """
    Adds a subplot to an existing fig.
    Args:
        fig: matplotlib.figure.Figure.
        pos: position of the subplot. The same input as directly using matplotlib.pyplot.

    Returns:
        ax: matplotlib.axes.Axes. It returns an instance of this type.

    """
    ax = fig.add_subplot(pos)
    return ax


def add_a_line(ax: Axes, x, y, line_width, line_style, line_color, marker, label) -> Axes:
    """
    Adds a line to an existing ax. The explanation of the arguments can be found in matplotlib.
    Args:
        ax: matplotlib.axes.Axes.
        x: list or np.ndarray of float. Data for horizontal axis.
        y: list or np.ndarray of float. Data for vertical axis.
        line_width: float.
        line_style: str.
        line_color: list of rgb values.
        marker: str.
        label: str.

    Returns:
        ax: matplotlib.axes.Axes. It returns an instance of this type.
    """
    ax.plot(x, y, linewidth=line_width, linestyle=line_style, color=line_color, marker=marker, label=label)
    return ax


def add_legend(ax: Axes, ncol: int) -> Axes:
    """
    Adds legend to an existing ax. The explanation of the arguments can be found in matplotlib.

    Args:
        ax: matplotlib.axes.Axes.
        ncol: int. Number of columns in the legend box.

    Returns:
        ax: matplotlib.axes.Axes. It returns an instance of this type.
    """
    ax.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left', ncol=ncol, mode="expand", borderaxespad=0.,
              fontsize=16)
    return ax


def set_axes(ax: Axes, xlim: list, ylim: list, fontsize: int = 20, show_grid: bool = True) -> Axes:
    """
    Sets axes to an existing ax. The explanation of the arguments can be found in matplotlib.
    Args:
        ax: matplotlib.axes.Axes.
        xlim: [float, float]. Sets the range of x-axis.
        ylim: [float, float]. Sets the range of y-axis.
        fontsize: int. The font size of ticker labels.
        show_grid: bool. Show grid or not.

    Returns:
        ax: matplotlib.axes.Axes. It returns an instance of this type.
    """
    ax.set_xlim(xlim[0], xlim[1])
    ax.set_ylim(ylim[0], ylim[1])
    ax.tick_params(labelsize=fontsize)

    if show_grid:
        ax.grid(True, linestyle='--')  # choose a linestyle between '-' | '--' | ':' | '-.'

    return ax


def add_axes_labels(ax: Axes, xlabel: str, ylabel: str, fontsize: int = 20) -> Axes:
    """
    Adds axes labels to an existing ax. The explanation of the arguments can be found in matplotlib.
    Args:
        ax: matplotlib.axes.Axes.
        xlabel: str.
        ylabel: str.
        fontsize: int.

    Returns:
        ax: matplotlib.axes.Axes. It returns an instance of this type.
    """
    ax.set_xlabel(xlabel=xlabel, fontsize=fontsize)
    ax.set_ylabel(ylabel=ylabel, fontsize=fontsize)
    return ax


def save(fig: MatFig, dpi: int = 300, file_name: str, file_extension: str = 'pdf', file_directory: str = ''):
    """
    Saves the fig into a specified location with specified extension.
    Args:
        fig: matplotlib.figure.Figure.
        dpi: int. For good quality, choose at least 300.
        file_name: str. File name without extension.
        file_extension: str. File extension
        file_directory: str. File directory. It includes the last directory separator. It differs in operating systems.
    """
    if file_directory:
        fig.savefig(f'{file_directory}{file_name}.{file_extension}', dpi=dpi)
    else:
        fig.savefig(f'{file_name}.{file_extension}', dpi=dpi)
