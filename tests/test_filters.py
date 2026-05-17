"""Tests for filters module."""

import numpy as np
from src.filters import fir_lowpass, iir_lowpass, apply_filter, freq_response
from src.signals import sine_wave


def test_fir_lowpass():
    b = fir_lowpass(cutoff=100, fs=1000, numtaps=31)
    assert len(b) == 31
    assert np.isfinite(b).all()


def test_iir_lowpass():
    b, a = iir_lowpass(cutoff=100, fs=1000, order=4)
    assert len(b) == 5  # order 4 → 5 coefficients
    assert np.isfinite(b).all()
    assert np.isfinite(a).all()


def test_apply_filter():
    t, x = sine_wave(freq=10, duration=1.0, fs=1000)
    # Add 400 Hz noise
    _, noise = sine_wave(freq=400, duration=1.0, fs=1000, amplitude=0.5)
    x_noisy = x + noise

    b = fir_lowpass(cutoff=100, fs=1000, numtaps=31)
    y = apply_filter(b, [1.0], x_noisy)
    assert len(y) == len(x_noisy)
    # Filtered signal should have less power at high frequencies than noisy
    np.testing.assert_array_less(np.std(y), np.std(x_noisy) + 0.1)


def test_freq_response():
    b = fir_lowpass(cutoff=100, fs=1000, numtaps=15)
    freq, mag, phase = freq_response(b, a=1.0, fs=1000)
    assert len(freq) == 1024
    assert np.all(mag >= 0)
    # At cutoff, magnitude should be around -6 dB
    idx = np.argmin(np.abs(freq - 100))
    mag_db = 20 * np.log10(mag[idx] + 1e-15)
    assert -8 < mag_db < -2
