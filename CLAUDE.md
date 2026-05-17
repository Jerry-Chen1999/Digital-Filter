# Digital Filter Learning Repository

## Background

Author is an automotive embedded software engineer working extensively with digital signal processing (DSP) in automotive microcontrollers. The representative peripheral is **DSADC (Delta-Sigma Analog-to-Digital Converter)**. To correctly configure and use these chip peripherals, a solid understanding of the underlying theory is required:

- **Control theory** (自动控制原理) — transfer functions, stability, feedback systems
- **Time/frequency domain transforms** — Laplace, Z-transform, Fourier, DFT/FFT
- **Frequency-domain analysis** — Bode plots, Nyquist plots, pole-zero analysis
- **Digital filter design** — FIR, IIR, window functions, filter structures (Direct Form I/II, cascaded, etc.)

This repository uses **Python + Jupyter notebooks** as a learning-by-debugging platform to re-learn these concepts through hands-on experimentation.

## Repository Structure

```
notebooks/          Jupyter notebooks — each experiment is self-contained
src/                Reusable Python modules (signal generation, filter impl, plotting)
data/               Sample data files (CSV, NPZ, etc.)
tests/              Unit tests for src/ modules
requirements.txt    Python dependencies (pip install -r requirements.txt)
```

## Workflow

- **Notebooks** are the primary workspace — each notebook tackles one topic (e.g., "Bode plot of a 2nd-order RC filter", "FIR window method comparison")
- **src/** holds reusable code extracted from notebooks — don't duplicate, import
- When a notebook matures, relevant utilities graduate to src/

## Python Environment

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
jupyter notebook
```

## Key Dependencies

- `numpy`, `scipy` — numerical computation, signal processing toolbox
- `matplotlib` — all plotting (time domain, frequency domain, Bode, Nyquist)
- `control` — Python Control Systems Library (transfer functions, Bode/Nyquist helpers)

## Conventions

- Notebooks are numbered (e.g., `01_basic_sine.ipynb`) for rough progression order
- Notebook filenames use English with underscores
- Plot settings use Chinese-compatible fonts where possible
- All new functionality starts in a notebook; only extract to src/ when reused by 2+ notebooks
