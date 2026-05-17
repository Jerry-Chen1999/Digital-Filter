"""Tests for signals module."""

import numpy as np
from src.signals import sine_wave, step_signal, impulse_signal, sweep_chirp


def test_sine_wave():
    t, y = sine_wave(freq=10, duration=1.0, fs=1000)
    assert len(t) == 1000
    assert len(y) == 1000
    assert np.abs(np.max(y) - 1.0) < 0.01


def test_step_signal():
    t, y = step_signal(onset_time=0.5, duration=1.0, fs=1000)
    assert y[0] == 0.0
    assert y[-1] == 1.0
    assert np.all(y[:400] == 0.0)
    assert np.all(y[600:] == 1.0)


def test_impulse_signal():
    t, y = impulse_signal(impulse_time=0.5, duration=1.0, fs=1000)
    assert np.sum(y) == 1.0
    assert y[500] == 1.0


def test_sweep_chirp():
    t, y = sweep_chirp(f0=10, f1=100, duration=1.0, fs=1000)
    assert len(t) == 1000
    assert np.abs(np.max(y) - 1.0) < 0.01
