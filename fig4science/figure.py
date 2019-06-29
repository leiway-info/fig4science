from matplotlib import rc
from matplotlib.figure import Figure as MatFig
from matplotlib.axes import Axes
import matplotlib.pyplot as plt

rc('text', usetex=True)
font = {
    'family': 'serif',
    'serif': 'Times'
}
rc('font', **font)


def new_plot(figsize: tuple) -> MatFig:

    fig = plt.figure(figsize=figsize)
    return fig


def add_subplot(fig: MatFig, pos=211) -> Axes:
    ax = fig.add_subplot(pos)
    return ax


def add_line_property(ax: Axes, x, y, line_width, line_style, line_color, marker, label) -> Axes:
    ax.plot(x, y, linewidth=line_width, linestyle=line_style, color=line_color, marker=marker, label=label)
    return ax


def add_legend(ax: Axes, ncol: int) -> Axes:
    ax.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left', ncol=ncol, mode="expand", borderaxespad=0.,
              fontsize=16)
    return ax


def set_axes(ax: Axes, xlim: list, ylim: list, fontsize: int = 20, show_grid: bool = True) -> Axes:
    ax.set_xlim(xlim[0], xlim[1])
    ax.set_ylim(ylim[0], ylim[1])
    ax.tick_params(labelsize=fontsize)

    if show_grid:
        ax.grid(True, linestyle='--')  # choose a linestyle between '-' | '--' | ':' | '-.'

    return ax


def add_axes_labels(ax: Axes, xlabel: str, ylabel: str, fontsize: int = 20) -> Axes:
    ax.set_xlabel(xlabel=xlabel, fontsize=fontsize)
    ax.set_ylabel(ylabel=ylabel, fontsize=fontsize)
    return ax


def save(fig: MatFig, file_name: str, file_extention: str, file_directory: str = None):
    if file_directory:
        fig.savefig(f'{file_directory}{file_name}.{file_extention}')
    else:
        fig.savefig(f'{file_name}.{file_extention}')
