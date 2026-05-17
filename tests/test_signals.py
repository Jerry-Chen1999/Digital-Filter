"""Tests for signals module."""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from src.signals import sine_wave, step_signal, impulse_signal, sweep_chirp
from src.plotting import plot_time_domain

_interactive = matplotlib.get_backend().lower() not in ('agg', 'template')


def _show():
    """Call _show() only when using an interactive backend."""
    if _interactive:
        plt.show()


def test_sine_wave():
    t, y = sine_wave(freq=10, duration=1.0, fs=1000)
    assert len(t) == 1000
    assert len(y) == 1000
    assert np.abs(np.max(y) - 1.0) < 0.01
    plot_time_domain(t, y, title="Sine Wave (10 Hz, fs=1000)")
    _show()


def test_step_signal():
    t, y = step_signal(onset_time=0.5, duration=1.0, fs=1000)
    assert y[0] == 0.0
    assert y[-1] == 1.0
    assert np.all(y[:400] == 0.0)
    assert np.all(y[600:] == 1.0)
    plot_time_domain(t, y, title="Step Signal (onset=0.5s)")
    _show()


def test_impulse_signal():
    t, y = impulse_signal(impulse_time=0.5, duration=1.0, fs=1000)
    assert np.sum(y) == 1.0
    assert y[500] == 1.0
    fig, ax = plot_time_domain(t, y, title="Impulse Signal (at t=0.5s)")
    ax.stem(t[480:520], y[480:520], linefmt='r-', markerfmt='ro', basefmt='k-')
    _show()


def test_sweep_chirp():
    t, y = sweep_chirp(f0=10, f1=100, duration=1.0, fs=1000)
    assert len(t) == 1000
    assert np.abs(np.max(y) - 1.0) < 0.01
    plot_time_domain(t[:1000], y[:1000], title="Sweep Chirp (10→100 Hz, first 200 samples)")
    _show()

# %%
test_sine_wave()
# %%
test_step_signal()
# %%
test_impulse_signal()
# %%
test_sweep_chirp()

# %%
