"""
This file shows how to use the figure.py file to make high quality figures for publication and presentation.
"""

import matplotlib.pyplot as plt
import numpy as np

import figure as f4s


def one_subplot():
    t = np.arange(0, 0.04, 50e-6)
    ua = np.sin(2*np.pi*50*t)
    ub = np.sin(2*np.pi*50*t - 2/3*np.pi)
    uc = np.sin(2*np.pi*50*t + 2/3*np.pi)

    fig = f4s.new_plot(figsize=(8, 4))

    ax = f4s.add_subplot(fig=fig)
    f4s.add_a_line(ax=ax, x=t, y=ua, line_width=2, line_style='-', line_color=[1, 0, 0])
    f4s.add_a_line(ax=ax, x=t, y=ub, line_width=2, line_style='--', line_color=[0, 1, 0])
    f4s.add_a_line(ax=ax, x=t, y=uc, line_width=2, line_style='-.', line_color=[0, 0, 1])
    f4s.add_legend(ax=ax, legend=['$u_a$', '$u_b$', '$u_c$'], ncol=3)
    f4s.set_axes(ax=ax, xlim=(0, 0.04), ylim=(-1.1, 1.1))
    f4s.add_axes_labels(ax=ax, xlabel='Time [s]', ylabel='Voltage [kV]')

    f4s.use_tight_layout(fig=fig)

    f4s.save(fig=fig, file_name='one_subplot')

    plt.show()


def one_subplot_grey():
    t = np.arange(0, 0.04, 50e-6)
    ua = np.sin(2*np.pi*50*t)
    ub = np.sin(2*np.pi*50*t - 2/3*np.pi)
    uc = np.sin(2*np.pi*50*t + 2/3*np.pi)

    fig = f4s.new_plot(figsize=(8, 4))

    ax = f4s.add_subplot(fig=fig)
    f4s.add_a_line(ax=ax, x=t, y=ua, line_width=2, line_style='-', line_color=[0, 0, 0])
    f4s.add_a_line(ax=ax, x=t, y=ub, line_width=2, line_style='--', line_color=[0.3, 0.3, 0.3])
    f4s.add_a_line(ax=ax, x=t, y=uc, line_width=2, line_style='-.', line_color=[0.6, 0.6, 0.6])
    f4s.add_legend(ax=ax, legend=['$u_a$', '$u_b$', '$u_c$'], ncol=3)
    f4s.set_axes(ax=ax, xlim=(0, 0.04), ylim=(-1.1, 1.1))
    f4s.add_axes_labels(ax=ax, xlabel='Time [s]', ylabel='Voltage [kV]')

    f4s.use_tight_layout(fig=fig)

    f4s.save(fig=fig, file_name='one_subplot_grey')


def three_subplots_same_x():
    t = np.arange(0, 0.04, 50e-6)
    ua = np.sin(2*np.pi*50*t)
    ub = np.sin(2*np.pi*50*t - 2/3*np.pi)
    uc = np.sin(2*np.pi*50*t + 2/3*np.pi)

    errs = 0.005 * np.random.randn(3, t.shape[0]) + 0.01

    uam = ua + errs[0, :]
    ubm = ub + errs[1, :]
    ucm = uc + errs[2, :]

    fig = f4s.new_plot(figsize=(8, 8))
    ax = f4s.add_subplot(fig=fig, pos=311)
    f4s.add_a_line(ax=ax, x=t, y=ua, line_width=2, line_style='-', line_color=[1, 0, 0])
    f4s.add_a_line(ax=ax, x=t, y=uam, line_width=2, line_style='--', line_color=[0, 0, 1])
    f4s.add_legend(ax=ax, legend=['simulated', 'measured'], ncol=2)
    f4s.set_axes(ax=ax, xlim=(0, 0.04), ylim=(-1.1, 1.1), hide_xticklabels=True)
    f4s.add_axes_labels(ax=ax, ylabel='$u_a$ [kV]')

    ax = f4s.add_subplot(fig=fig, pos=312)
    f4s.add_a_line(ax=ax, x=t, y=ub, line_width=2, line_style='-', line_color=[1, 0, 0])
    f4s.add_a_line(ax=ax, x=t, y=ubm, line_width=2, line_style='--', line_color=[0, 0, 1])
    f4s.set_axes(ax=ax, xlim=(0, 0.04), ylim=(-1.1, 1.1), hide_xticklabels=True)
    f4s.add_axes_labels(ax=ax, ylabel='$u_b$ [kV]')

    ax = f4s.add_subplot(fig=fig, pos=313)
    f4s.add_a_line(ax=ax, x=t, y=uc, line_width=2, line_style='-', line_color=[1, 0, 0])
    f4s.add_a_line(ax=ax, x=t, y=ucm, line_width=2, line_style='--', line_color=[0, 0, 1])
    f4s.set_axes(ax=ax, xlim=(0, 0.04), ylim=(-1.1, 1.1))
    f4s.add_axes_labels(ax=ax, xlabel='Time [s]', ylabel='$u_c$ [kV]')

    f4s.use_tight_layout(fig=fig)
    f4s.save(fig=fig, file_name='three_subplots_same_x')


def two_subplots_log():
    f = np.linspace(0, 1e6, 20000)
    f[0] = 1e-6
    w = 2*np.pi*f
    z = 1 / (1/10 + 1/(1j*w*10e-3) + 1j*w*10e-9)

    fig = f4s.new_plot(figsize=(8, 6))

    ax = f4s.add_subplot(fig=fig, pos=211)
    f4s.add_a_line(ax=ax, x=f, y=np.abs(z), line_width=2, line_style='-', line_color=[0, 0, 1])
    f4s.set_axes(ax=ax, x_scale='log', xlim=(1, f[-1]), hide_xticklabels=True)
    f4s.add_axes_labels(ax=ax, ylabel=r'$|\underline{z}|$ [$\Omega$]')

    ax = f4s.add_subplot(fig=fig, pos=212)
    f4s.add_a_line(ax=ax, x=f, y=np.angle(z)/np.pi*180, line_width=2, line_style='-', line_color=[0, 0, 1])
    f4s.set_axes(ax=ax, x_scale='log', xlim=(1, f[-1]), ylim=(-95, 95))
    ax.set_yticks([-90, -45, 0, 45, 90])
    f4s.add_axes_labels(ax=ax, xlabel='Frequency [Hz]', ylabel=r'$\angle\, \underline{z}$ [$^\circ$]')

    f4s.use_tight_layout(fig=fig)
    f4s.save(fig=fig, file_name='two_subplots_log')


if __name__ == '__main__':
    one_subplot()
    one_subplot_grey()
    three_subplots_same_x()
    two_subplots_log()
