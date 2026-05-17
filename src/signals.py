"""Signal generation utilities."""

import numpy as np


def sine_wave(freq, duration, fs, amplitude=1.0, phase=0.0):
    """Generate a sine wave.

    Args:
        freq: Frequency in Hz
        duration: Duration in seconds
        fs: Sample rate in Hz
        amplitude: Peak amplitude
        phase: Initial phase in radians
    Returns:
        t: Time array
        y: Signal array
    """
    t = np.arange(0, duration, 1 / fs)
    y = amplitude * np.sin(2 * np.pi * freq * t + phase)
    return t, y


def sweep_chirp(f0, f1, duration, fs, method="linear"):
    """Generate a swept-frequency chirp signal.

    Args:
        f0: Start frequency in Hz
        f1: End frequency in Hz
        duration: Duration in seconds
        fs: Sample rate in Hz
        method: 'linear' or 'log'
    Returns:
        t: Time array
        y: Signal array
    """
    t = np.arange(0, duration, 1 / fs)
    if method == "linear":
        k = (f1 - f0) / duration
        phase = 2 * np.pi * (f0 * t + 0.5 * k * t**2)
    elif method == "log":
        phase = 2 * np.pi * f0 * ((f1 / f0) ** (t / duration) - 1) * duration / np.log(f1 / f0)
    else:
        raise ValueError(f"Unknown method: {method}")
    y = np.sin(phase)
    return t, y


def white_noise(duration, fs, sigma=1.0):
    """Generate white Gaussian noise.

    Args:
        duration: Duration in seconds
        fs: Sample rate in Hz
        sigma: Standard deviation
    Returns:
        t: Time array
        y: Noise array
    """
    n_samples = int(duration * fs)
    t = np.arange(n_samples) / fs
    y = np.random.default_rng().normal(0, sigma, n_samples)
    return t, y


def step_signal(onset_time, duration, fs, amplitude=1.0):
    """Generate a step function (0 before onset, amplitude after).

    Args:
        onset_time: Time when step occurs in seconds
        duration: Total duration in seconds
        fs: Sample rate in Hz
        amplitude: Step amplitude
    Returns:
        t: Time array
        y: Step signal array
    """
    n_samples = int(duration * fs)
    t = np.arange(n_samples) / fs
    y = np.where(t >= onset_time, amplitude, 0.0)
    return t, y


def impulse_signal(impulse_time, duration, fs, amplitude=1.0):
    """Generate a unit impulse (approximated as a single sample spike).

    Args:
        impulse_time: Time of the impulse in seconds
        duration: Total duration in seconds
        fs: Sample rate in Hz
        amplitude: Impulse amplitude
    Returns:
        t: Time array
        y: Impulse signal array
    """
    n_samples = int(duration * fs)
    t = np.arange(n_samples) / fs
    y = np.zeros(n_samples)
    idx = int(impulse_time * fs)
    if 0 <= idx < n_samples:
        y[idx] = amplitude
    return t, y
