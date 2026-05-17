"""Plotting utilities for DSP visualization."""

import numpy as np
import matplotlib.pyplot as plt


def set_style():
    """Apply consistent plot style."""
    plt.rcParams.update({
        "figure.figsize": (10, 5),
        "figure.dpi": 100,
        "grid.alpha": 0.3,
        "axes.grid": True,
    })


def plot_time_domain(t, signals, labels=None, title="Time Domain"):
    """Plot one or more signals vs time.

    Args:
        t: Time array
        signals: Single array or list of arrays
        labels: Single label or list of labels
        title: Plot title
    """
    set_style()
    if isinstance(signals, np.ndarray):
        signals = [signals]
    if labels is None:
        labels = [f"Signal {i}" for i in range(len(signals))]
    elif isinstance(labels, str):
        labels = [labels]

    fig, ax = plt.subplots()
    for y, lbl in zip(signals, labels):
        ax.plot(t, y, label=lbl)
    ax.set_xlabel("Time [s]")
    ax.set_ylabel("Amplitude")
    ax.set_title(title)
    ax.legend()
    fig.tight_layout()
    return fig, ax


def plot_freq_response(freq, mag, phase=None, title="Frequency Response"):
    """Plot magnitude and optionally phase response.

    Args:
        freq: Frequency array
        mag: Magnitude (linear)
        phase: Phase array in radians (optional)
        title: Plot title
    """
    set_style()
    if phase is not None:
        fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(10, 7))
    else:
        fig, ax1 = plt.subplots()
        ax2 = None

    mag_db = 20 * np.log10(mag + 1e-15)
    ax1.semilogx(freq, mag_db)
    ax1.set_ylabel("Magnitude [dB]")
    ax1.set_title(title)

    if ax2 is not None and phase is not None:
        phase_deg = np.rad2deg(phase)
        ax2.semilogx(freq, phase_deg)
        ax2.set_xlabel("Frequency [Hz]")
        ax2.set_ylabel("Phase [deg]")

    fig.tight_layout()
    return fig, (ax1, ax2)


def plot_bode(b, a, fs=1.0, title="Bode Plot"):
    """Plot Bode diagram (magnitude + phase) for a filter.

    Args:
        b, a: Filter coefficients
        fs: Sample rate in Hz
        title: Plot title
    """
    from scipy import signal as scipy_signal

    set_style()
    w, mag, phase = scipy_signal.bode((b, a), n=2000)
    freq = w * fs / (2 * np.pi)

    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(10, 7))
    ax1.semilogx(freq, mag)
    ax1.set_ylabel("Magnitude [dB]")
    ax1.set_title(title)
    ax1.grid(which="both", alpha=0.3)

    ax2.semilogx(freq, phase)
    ax2.set_xlabel("Frequency [Hz]")
    ax2.set_ylabel("Phase [deg]")
    ax2.grid(which="both", alpha=0.3)

    fig.tight_layout()
    return fig, (ax1, ax2)


def plot_spectrum(x, fs, title="Power Spectrum", nperseg=256):
    """Plot power spectral density using Welch's method.

    Args:
        x: Input signal
        fs: Sample rate in Hz
        title: Plot title
        nperseg: Samples per segment
    """
    from scipy import signal as scipy_signal

    set_style()
    freq, psd = scipy_signal.welch(x, fs, nperseg=nperseg)

    fig, ax = plt.subplots()
    ax.semilogy(freq, psd)
    ax.set_xlabel("Frequency [Hz]")
    ax.set_ylabel("PSD [V²/Hz]")
    ax.set_title(title)
    fig.tight_layout()
    return fig, ax
