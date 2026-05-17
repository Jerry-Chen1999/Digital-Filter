"""Digital filter implementations."""

import numpy as np
from scipy import signal as scipy_signal


def fir_lowpass(cutoff, fs, numtaps):
    """Design a FIR lowpass filter using a Hamming window.

    Args:
        cutoff: Cutoff frequency in Hz (-3 dB)
        fs: Sample rate in Hz
        numtaps: Filter order + 1 (must be odd for best results)
    Returns:
        b: Numerator coefficients (FIR taps)
    """
    nyquist = fs / 2
    b = scipy_signal.firwin(numtaps, cutoff / nyquist, window="hamming")
    return b


def iir_lowpass(cutoff, fs, order=2):
    """Design a Butterworth IIR lowpass filter.

    Args:
        cutoff: Cutoff frequency in Hz (-3 dB)
        fs: Sample rate in Hz
        order: Filter order
    Returns:
        b, a: Numerator and denominator coefficients
    """
    nyquist = fs / 2
    b, a = scipy_signal.butter(order, cutoff / nyquist, btype="low")
    return b, a


def apply_filter(b, a, x):
    """Apply a filter (forward-backward for zero phase).

    Args:
        b: Numerator coefficients
        a: Denominator coefficients (use [1.0] for FIR)
        x: Input signal
    Returns:
        y: Filtered signal
    """
    return scipy_signal.lfilter(b, a, x)


def apply_filter_zerophase(b, a, x):
    """Apply a filter with zero-phase (forward-backward filtering).

    Args:
        b: Numerator coefficients
        a: Denominator coefficients (use [1.0] for FIR)
        x: Input signal
    Returns:
        y: Filtered signal
    """
    return scipy_signal.filtfilt(b, a, x)


def freq_response(b, a=1.0, fs=1.0, nfft=1024):
    """Compute frequency response (magnitude and phase).

    Args:
        b: Numerator coefficients
        a: Denominator coefficients
        fs: Sample rate for correct frequency axis
        nfft: Number of FFT points
    Returns:
        freq: Frequency array in Hz
        mag: Magnitude (linear)
        phase: Phase in radians
    """
    freq, h = scipy_signal.freqz(b, a, worN=nfft, fs=fs)
    mag = np.abs(h)
    phase = np.angle(h)
    return freq, mag, phase


def group_delay(b, a, fs=1.0, nfft=1024):
    """Compute group delay of a filter.

    Args:
        b, a: Filter coefficients
        fs: Sample rate
        nfft: Number of FFT points
    Returns:
        freq: Frequency array in Hz
        gd: Group delay in samples
    """
    w = np.linspace(0, np.pi, nfft)
    _, gd = scipy_signal.group_delay((b, a), w=w)
    freq = w * fs / (2 * np.pi)
    return freq, gd
