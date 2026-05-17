# Digital Filter Learning

Python + Jupyter 实验仓库，用于学习数字滤波器与信号处理。

## 学习路线

- **时频域变换** — Fourier, Laplace, Z-transform, DFT/FFT
- **滤波器设计** — FIR (窗函数法), IIR (Butterworth, Chebyshev)
- **频域分析** — Bode 图, Nyquist 图, 零极点分析
- **应用场景** — DSADC 数字滤波器配置、去噪、抽取滤波

## 环境配置

```bash
python -m venv .venv
source .venv/bin/activate        # Linux/Mac
.venv\Scripts\activate           # Windows
pip install -r requirements.txt
jupyter notebook
```

## 目录结构

| 目录 | 用途 |
|------|------|
| `notebooks/` | Jupyter 实验笔记 |
| `src/` | 可复用 Python 模块 |
| `data/` | 数据文件 |
| `tests/` | 单元测试 |

## 运行测试

```bash
python -m pytest tests/ -v
```
