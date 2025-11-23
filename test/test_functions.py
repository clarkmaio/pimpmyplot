



import matplotlib.pyplot as plt
import numpy as np
import pimpmyplot as pmp


def demoplot():
    x = np.linspace(0, 10, 100)
    plt.plot(x, np.sin(x), label='A')

def demosubplot():
    x = np.linspace(0, 10, 100)
    fig, ax = plt.subplots(1, 2)

    ax[0].plot(x, np.sin(x), label='A')
    ax[1].plot(x, np.cos(x), label='B')
    return fig, ax




def test_remove_axis():
    demoplot()
    pmp.remove_axis()

    fig, ax = demosubplot()
    pmp.remove_axis(ax=ax[1])


def test_remove_ticks():
    demoplot()
    pmp.remove_ticks()

    fig, ax = demosubplot()
    pmp.remove_ticks(ax=ax[1])


def test_legend():
    demoplot()
    pmp.legend()

    fig, ax = demosubplot()
    pmp.legend(ax=ax[1])


def test_bullet_grid():
    demoplot()
    pmp.bullet_grid()

    fig, ax = demosubplot()
    pmp.bullet_grid(ax=ax[1])


    