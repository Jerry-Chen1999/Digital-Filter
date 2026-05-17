"""Tests for filters module."""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from src.filters import fir_lowpass, iir_lowpass, apply_filter, freq_response
from src.signals import sine_wave
from src.plotting import plot_time_domain, plot_freq_response, plot_bode, plot_spectrum

_interactive = matplotlib.get_backend().lower() not in ('agg', 'template')


def _show():
    """Call _show() only when using an interactive backend."""
    if _interactive:
        plt.show()


def test_fir_lowpass():
    b = fir_lowpass(cutoff=100, fs=1000, numtaps=31)
    assert len(b) == 31
    assert np.isfinite(b).all()
    # Time domain: impulse response (FIR coefficients)
    t = np.arange(len(b)) / 1000
    plot_time_domain(t, b, title="FIR Lowpass — Impulse Response (31 taps)")
    _show()
    # Frequency response
    plot_bode(b, [1.0], fs=1000, title="FIR Lowpass — Bode Plot (fc=100 Hz)")
    _show()


def test_iir_lowpass():
    b, a = iir_lowpass(cutoff=100, fs=1000, order=4)
    assert len(b) == 5  # order 4 → 5 coefficients
    assert np.isfinite(b).all()
    assert np.isfinite(a).all()
    plot_bode(b, a, fs=1000, title="IIR Lowpass (Butterworth 4th-order, fc=100 Hz)")
    _show()


def test_apply_filter():
    t, x = sine_wave(freq=10, duration=1.0, fs=1000)
    _, noise = sine_wave(freq=400, duration=1.0, fs=1000, amplitude=0.5)
    x_noisy = x + noise

    b = fir_lowpass(cutoff=100, fs=1000, numtaps=31)
    y = apply_filter(b, [1.0], x_noisy)
    assert len(y) == len(x_noisy)
    np.testing.assert_array_less(np.std(y), np.std(x_noisy) + 0.1)
    # Show before/after filtering
    plot_time_domain(
        t[:200], [x_noisy[:200], y[:200]],
        labels=["Noisy (10 Hz + 400 Hz)", "Filtered"],
        title="FIR Lowpass — Filtering Effect (first 200 samples)"
    )
    _show()
    # Spectrum comparison
    plot_spectrum(x_noisy, fs=1000, title="Noisy Signal Spectrum")
    _show()
    plot_spectrum(y, fs=1000, title="Filtered Signal Spectrum")
    _show()


def test_freq_response():
    b = fir_lowpass(cutoff=100, fs=1000, numtaps=15)
    freq, mag, phase = freq_response(b, a=1.0, fs=1000)
    assert len(freq) == 1024
    assert np.all(mag >= 0)
    idx = np.argmin(np.abs(freq - 100))
    mag_db = 20 * np.log10(mag[idx] + 1e-15)
    assert -8 < mag_db < -2
    plot_freq_response(freq, mag, phase, title="FIR Lowpass — Frequency Response (fc=100 Hz)")
    _show()
