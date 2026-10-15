import os
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Set aesthetic style matching pa2_spec.pdf (Pages 6 & 7)
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Helvetica']
plt.rcParams['axes.edgecolor'] = 'black'
plt.rcParams['axes.linewidth'] = 1.0
plt.rcParams['axes.grid'] = False
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['axes.facecolor'] = 'white'

os.makedirs('plots/task2a', exist_ok=True)
os.makedirs('plots/task2b', exist_ok=True)
os.makedirs('plots/task3', exist_ok=True)

# Common definitions
traces = ['Trace 1', 'Trace 2', 'Trace 3']
x_traces = np.arange(len(traces))
width2 = 0.32
width3 = 0.24
width_single = 0.45

# PDF Color Palette
c_coral = '#eb7d75'   # Baseline
c_sky = '#7fc2df'     # Intermediate / Metric
c_green = '#98d89e'   # Optimized Policy
c_slate = '#6a82bc'
c_crimson = '#c95374' # 1.0 dashed line

# Baseline LRU Data across Traces 1, 2, 3
lru_ipc = [0.2321, 0.2500, 0.3819]
lru_impki = [10.367, 19.844, 1.127]
lru_dmpki = [7.359, 8.706, 2.835]
lru_totmpki = [17.725, 28.550, 3.961]

# ==============================================================================
# TASK 2A PLOTS (Saved to plots/task2a/)
# ==============================================================================

irrip_ipc = [0.2316, 0.2589, 0.3825]
irrip_spd = [0.9979, 1.0357, 1.0016]
irrip_impki = [9.204, 9.993, 0.788]
irrip_dmpki = [9.589, 11.074, 3.152]
irrip_totmpki = [18.793, 21.067, 3.940]

# --- Plot 2A-1: IPC ---
fig, ax = plt.subplots(figsize=(6.5, 4.8), dpi=300)
ax.bar(x_traces - width2/2, lru_ipc, width2, label='Baseline (LRU)', color=c_coral, edgecolor='black', linewidth=0.8)
ax.bar(x_traces + width2/2, irrip_ipc, width2, label='I-RRIP', color=c_green, edgecolor='black', linewidth=0.8)
ax.set_title('Task 2A: Instructions Per Cycle (IPC)', fontsize=11, pad=10)
ax.set_ylabel('IPC', fontsize=10)
ax.set_xlabel('Benchmark Traces', fontsize=10)
ax.set_xticks(x_traces)
ax.set_xticklabels(traces)
ax.set_ylim(0, 0.45)
ax.legend(loc='upper left', frameon=True, edgecolor='black', fontsize=9, framealpha=1.0)
plt.tight_layout()
plt.savefig('plots/task2a/task2a_ipc.png')
plt.close()

# --- Plot 2A-2: Speedup ---
fig, ax = plt.subplots(figsize=(6.5, 4.8), dpi=300)
ax.bar(x_traces, irrip_spd, 0.45, label='I-RRIP Speedup', color=c_sky, edgecolor='black', linewidth=0.8)
ax.axhline(1.0, color=c_crimson, linestyle='--', linewidth=1.2, label='Baseline (LRU = 1.0)')
ax.set_title('Task 2A: Speedup over Baseline (LRU)', fontsize=11, pad=10)
ax.set_ylabel('Speedup (Normalized to LRU)', fontsize=10)
ax.set_xlabel('Benchmark Traces', fontsize=10)
ax.set_xticks(x_traces)
ax.set_xticklabels(traces)
ax.set_ylim(0.96, 1.05)
for i, v in enumerate(irrip_spd):
    diff = (v - 1.0) * 100
    sign = '+' if diff >= 0 else ''
    ax.text(i, v + 0.002, f'{sign}{diff:.2f}%', ha='center', va='bottom', fontsize=9, fontweight='bold')
ax.legend(loc='upper right', frameon=True, edgecolor='black', fontsize=9, framealpha=1.0)
plt.tight_layout()
plt.savefig('plots/task2a/task2a_speedup.png')
plt.close()

# --- Plot 2A-3: L2 Instruction Load MPKI ---
fig, ax = plt.subplots(figsize=(6.5, 4.8), dpi=300)
ax.bar(x_traces - width2/2, lru_impki, width2, label='Baseline (LRU)', color=c_coral, edgecolor='black', linewidth=0.8)
ax.bar(x_traces + width2/2, irrip_impki, width2, label='I-RRIP', color=c_green, edgecolor='black', linewidth=0.8)
ax.set_title('Task 2A: L2 Instruction Load MPKI', fontsize=11, pad=10)
ax.set_ylabel('L2 Instruction MPKI', fontsize=10)
ax.set_xlabel('Benchmark Traces', fontsize=10)
ax.set_xticks(x_traces)
ax.set_xticklabels(traces)
ax.set_ylim(0, 22)
ax.legend(loc='upper right', frameon=True, edgecolor='black', fontsize=9, framealpha=1.0)
plt.tight_layout()
plt.savefig('plots/task2a/task2a_instruction_mpki.png')
plt.close()

# --- Plot 2A-4: L2 Data Load MPKI ---
fig, ax = plt.subplots(figsize=(6.5, 4.8), dpi=300)
ax.bar(x_traces - width2/2, lru_dmpki, width2, label='Baseline (LRU)', color=c_coral, edgecolor='black', linewidth=0.8)
ax.bar(x_traces + width2/2, irrip_dmpki, width2, label='I-RRIP', color=c_sky, edgecolor='black', linewidth=0.8)
ax.set_title('Task 2A: L2 Data Load MPKI', fontsize=11, pad=10)
ax.set_ylabel('L2 Data MPKI', fontsize=10)
ax.set_xlabel('Benchmark Traces', fontsize=10)
ax.set_xticks(x_traces)
ax.set_xticklabels(traces)
ax.set_ylim(0, 14)
ax.legend(loc='upper right', frameon=True, edgecolor='black', fontsize=9, framealpha=1.0)
plt.tight_layout()
plt.savefig('plots/task2a/task2a_data_mpki.png')
plt.close()

# --- Plot 2A-5: Total L2C Load MPKI ---
fig, ax = plt.subplots(figsize=(6.5, 4.8), dpi=300)
ax.bar(x_traces - width2/2, lru_totmpki, width2, label='Baseline (LRU)', color=c_coral, edgecolor='black', linewidth=0.8)
ax.bar(x_traces + width2/2, irrip_totmpki, width2, label='I-RRIP', color=c_green, edgecolor='black', linewidth=0.8)
ax.set_title('Task 2A: Total L2C Load MPKI', fontsize=11, pad=10)
ax.set_ylabel('L2C Total MPKI', fontsize=10)
ax.set_xlabel('Benchmark Traces', fontsize=10)
ax.set_xticks(x_traces)
ax.set_xticklabels(traces)
ax.set_ylim(0, 32)
ax.legend(loc='upper right', frameon=True, edgecolor='black', fontsize=9, framealpha=1.0)
plt.tight_layout()
plt.savefig('plots/task2a/task2a_total_mpki.png')
plt.close()

# ==============================================================================
# TASK 2B PLOTS (Saved to plots/task2b/)
# ==============================================================================

thresholds = ['0.15', '0.20', '0.25\n(Default)', '0.30', '0.35']
x_th = np.arange(len(thresholds))

spds_t1 = [0.9980, 0.9979, 0.9984, 0.9984, 0.9975]
spds_t2 = [1.0346, 1.0346, 1.0346, 1.0346, 1.0304]
spds_t3 = [1.0016, 1.0017, 1.0018, 1.0017, 0.9987]

# --- Parameter Tuning Plot: Speedup across 5 Thresholds (All Traces) ---
fig, ax = plt.subplots(figsize=(7.0, 4.8), dpi=300)
ax.bar(x_th - width3, spds_t1, width3, label='Trace 1', color=c_coral, edgecolor='black', linewidth=0.8)
ax.bar(x_th, spds_t2, width3, label='Trace 2', color=c_sky, edgecolor='black', linewidth=0.8)
ax.bar(x_th + width3, spds_t3, width3, label='Trace 3', color=c_green, edgecolor='black', linewidth=0.8)
ax.axhline(1.0, color=c_crimson, linestyle='--', linewidth=1.2, label='Baseline (LRU = 1.0)')
ax.set_title('Task 2B Parameter Tuning: Speedup vs. Decision Threshold (All Traces)', fontsize=11, pad=10)
ax.set_ylabel('Speedup over Baseline', fontsize=10)
ax.set_xlabel('Decision Threshold', fontsize=10)
ax.set_xticks(x_th)
ax.set_xticklabels(thresholds)
ax.set_ylim(0.97, 1.055)
ax.legend(loc='upper right', frameon=True, edgecolor='black', fontsize=9, framealpha=1.0)
plt.tight_layout()
plt.savefig('plots/task2b/task2b_threshold_speedup.png')
plt.close()

# --- Leader Sets Tuning Plot: Speedup across Leader Set Allocations (All Traces) ---
leader_configs = ['16 Leaders\n(Stride 64)', '32 Leaders\n(Stride 32)', '64 Leaders\n(Stride 16, Default)']
x_ld = np.arange(len(leader_configs))

ld_spd_t1 = [0.9979, 0.9984, 0.9978]
ld_spd_t2 = [1.0334, 1.0346, 1.0352]
ld_spd_t3 = [1.0017, 1.0018, 1.0017]

fig, ax = plt.subplots(figsize=(7.0, 4.8), dpi=300)
ax.bar(x_ld - width3, ld_spd_t1, width3, label='Trace 1', color=c_coral, edgecolor='black', linewidth=0.8)
ax.bar(x_ld, ld_spd_t2, width3, label='Trace 2', color=c_sky, edgecolor='black', linewidth=0.8)
ax.bar(x_ld + width3, ld_spd_t3, width3, label='Trace 3', color=c_green, edgecolor='black', linewidth=0.8)
ax.axhline(1.0, color=c_crimson, linestyle='--', linewidth=1.2, label='Baseline (LRU = 1.0)')
ax.set_title('Task 2B: Speedup across Leader Set Allocations (All Traces)', fontsize=11, pad=10)
ax.set_ylabel('Speedup over Baseline', fontsize=10)
ax.set_xlabel('Leader Set Configurations', fontsize=10)
ax.set_xticks(x_ld)
ax.set_xticklabels(leader_configs)
ax.set_ylim(0.97, 1.055)
ax.legend(loc='upper right', frameon=True, edgecolor='black', fontsize=9, framealpha=1.0)
plt.tight_layout()
plt.savefig('plots/task2b/task2b_leaders_sensitivity.png')
plt.close()

# --- Tuned Dynamic I-RRIP vs. Baseline (LRU) ---
dyn_ipc = [0.2316, 0.2588, 0.3826]
dyn_spd = [0.9978, 1.0352, 1.0017]
dyn_impki = [9.193, 10.115, 0.790]
dyn_dmpki = [9.540, 10.996, 3.143]
dyn_totmpki = [18.734, 21.111, 3.934]

# --- Plot 2B Tuned vs LRU 1: IPC ---
fig, ax = plt.subplots(figsize=(6.5, 4.8), dpi=300)
ax.bar(x_traces - width2/2, lru_ipc, width2, label='Baseline (LRU)', color=c_coral, edgecolor='black', linewidth=0.8)
ax.bar(x_traces + width2/2, dyn_ipc, width2, label='Dynamic I-RRIP (Tuned)', color=c_green, edgecolor='black', linewidth=0.8)
ax.set_title('Task 2B: Instructions Per Cycle (IPC) - Tuned vs. LRU', fontsize=11, pad=10)
ax.set_ylabel('IPC', fontsize=10)
ax.set_xlabel('Benchmark Traces', fontsize=10)
ax.set_xticks(x_traces)
ax.set_xticklabels(traces)
ax.set_ylim(0, 0.45)
ax.legend(loc='upper left', frameon=True, edgecolor='black', fontsize=9, framealpha=1.0)
plt.tight_layout()
plt.savefig('plots/task2b/task2b_ipc.png')
plt.close()

# --- Plot 2B Tuned vs LRU 2: Speedup ---
fig, ax = plt.subplots(figsize=(6.5, 4.8), dpi=300)
ax.bar(x_traces, dyn_spd, 0.45, label='Dynamic I-RRIP Speedup', color=c_sky, edgecolor='black', linewidth=0.8)
ax.axhline(1.0, color=c_crimson, linestyle='--', linewidth=1.2, label='Baseline (LRU = 1.0)')
ax.set_title('Task 2B: Speedup over Baseline (LRU) - Tuned Design', fontsize=11, pad=10)
ax.set_ylabel('Speedup (Normalized to LRU)', fontsize=10)
ax.set_xlabel('Benchmark Traces', fontsize=10)
ax.set_xticks(x_traces)
ax.set_xticklabels(traces)
ax.set_ylim(0.96, 1.05)
for i, v in enumerate(dyn_spd):
    diff = (v - 1.0) * 100
    sign = '+' if diff >= 0 else ''
    ax.text(i, v + 0.002, f'{sign}{diff:.2f}%', ha='center', va='bottom', fontsize=9, fontweight='bold')
ax.legend(loc='upper right', frameon=True, edgecolor='black', fontsize=9, framealpha=1.0)
plt.tight_layout()
plt.savefig('plots/task2b/task2b_speedup.png')
plt.close()

# --- Plot 2B Tuned vs LRU 3: L2 Instruction Load MPKI ---
fig, ax = plt.subplots(figsize=(6.5, 4.8), dpi=300)
ax.bar(x_traces - width2/2, lru_impki, width2, label='Baseline (LRU)', color=c_coral, edgecolor='black', linewidth=0.8)
ax.bar(x_traces + width2/2, dyn_impki, width2, label='Dynamic I-RRIP (Tuned)', color=c_green, edgecolor='black', linewidth=0.8)
ax.set_title('Task 2B: L2 Instruction Load MPKI - Tuned vs. LRU', fontsize=11, pad=10)
ax.set_ylabel('L2 Instruction MPKI', fontsize=10)
ax.set_xlabel('Benchmark Traces', fontsize=10)
ax.set_xticks(x_traces)
ax.set_xticklabels(traces)
ax.set_ylim(0, 22)
ax.legend(loc='upper right', frameon=True, edgecolor='black', fontsize=9, framealpha=1.0)
plt.tight_layout()
plt.savefig('plots/task2b/task2b_instruction_mpki.png')
plt.close()

# --- Plot 2B Tuned vs LRU 4: L2 Data Load MPKI ---
fig, ax = plt.subplots(figsize=(6.5, 4.8), dpi=300)
ax.bar(x_traces - width2/2, lru_dmpki, width2, label='Baseline (LRU)', color=c_coral, edgecolor='black', linewidth=0.8)
ax.bar(x_traces + width2/2, dyn_dmpki, width2, label='Dynamic I-RRIP (Tuned)', color=c_sky, edgecolor='black', linewidth=0.8)
ax.set_title('Task 2B: L2 Data Load MPKI - Tuned vs. LRU', fontsize=11, pad=10)
ax.set_ylabel('L2 Data MPKI', fontsize=10)
ax.set_xlabel('Benchmark Traces', fontsize=10)
ax.set_xticks(x_traces)
ax.set_xticklabels(traces)
ax.set_ylim(0, 14)
ax.legend(loc='upper right', frameon=True, edgecolor='black', fontsize=9, framealpha=1.0)
plt.tight_layout()
plt.savefig('plots/task2b/task2b_data_mpki.png')
plt.close()

# --- Plot 2B Tuned vs LRU 5: Total L2C Load MPKI ---
fig, ax = plt.subplots(figsize=(6.5, 4.8), dpi=300)
ax.bar(x_traces - width2/2, lru_totmpki, width2, label='Baseline (LRU)', color=c_coral, edgecolor='black', linewidth=0.8)
ax.bar(x_traces + width2/2, dyn_totmpki, width2, label='Dynamic I-RRIP (Tuned)', color=c_green, edgecolor='black', linewidth=0.8)
ax.set_title('Task 2B: Total L2C Load MPKI - Tuned vs. LRU', fontsize=11, pad=10)
ax.set_ylabel('L2C Total MPKI', fontsize=10)
ax.set_xlabel('Benchmark Traces', fontsize=10)
ax.set_xticks(x_traces)
ax.set_xticklabels(traces)
ax.set_ylim(0, 32)
ax.legend(loc='upper right', frameon=True, edgecolor='black', fontsize=9, framealpha=1.0)
plt.tight_layout()
plt.savefig('plots/task2b/task2b_total_mpki.png')
plt.close()

# ==============================================================================
# TASK 3 PLOTS (Saved to plots/task3/)
# ==============================================================================

t3_ipc = [0.2340, 0.2630, 0.3948]
t3_spd = [1.0080, 1.0519, 1.0339]
t3_acc = [49.81, 48.43, 44.19]
t3_cov = [12.03, 5.13, 23.41]

lru_l1d = [10.679, 13.537, 3.404]
t3_l1d = [9.394, 12.843, 2.607]

lru_l2_t3 = [17.725, 28.550, 3.961]
t3_l2c = [17.391, 20.508, 2.952]

lru_l2_inst_t3 = [10.367, 19.844, 1.127]
t3_l2_inst = [9.282, 10.367, 0.814]

lru_l2_data_t3 = [7.359, 8.706, 2.835]
t3_l2_data = [8.109, 10.141, 2.138]

# --- Task 3 Plot 1: IPC ---
fig, ax = plt.subplots(figsize=(6.5, 4.8), dpi=300)
ax.bar(x_traces - width2/2, lru_ipc, width2, label='Baseline (LRU)', color=c_coral, edgecolor='black', linewidth=0.8)
ax.bar(x_traces + width2/2, t3_ipc, width2, label='Task 3 (SPP + Dyn I-RRIP)', color=c_green, edgecolor='black', linewidth=0.8)
ax.set_title('Task 3: Instructions Per Cycle (IPC)', fontsize=11, pad=10)
ax.set_ylabel('IPC', fontsize=10)
ax.set_xlabel('Benchmark Traces', fontsize=10)
ax.set_xticks(x_traces)
ax.set_xticklabels(traces)
ax.set_ylim(0, 0.48)
ax.legend(loc='upper left', frameon=True, edgecolor='black', fontsize=9, framealpha=1.0)
plt.tight_layout()
plt.savefig('plots/task3/task3_ipc.png')
plt.close()

# --- Task 3 Plot 2: Speedup (PDF Page 6 Top Style) ---
fig, ax = plt.subplots(figsize=(6.5, 4.8), dpi=300)
ax.bar(x_traces, t3_spd, width_single, label='Task 3 Speedup', color=c_sky, edgecolor='black', linewidth=0.8)
ax.axhline(1.0, color=c_crimson, linestyle='--', linewidth=1.2, label='Baseline (LRU = 1.0)')
ax.set_title('Task 3: Speedup over Baseline', fontsize=11, pad=10)
ax.set_ylabel('Speedup (Normalized to LRU)', fontsize=10)
ax.set_xlabel('Benchmark Traces', fontsize=10)
ax.set_xticks(x_traces)
ax.set_xticklabels(traces)
ax.set_ylim(0.97, 1.075)
for i, v in enumerate(t3_spd):
    diff = (v - 1.0) * 100
    sign = '+' if diff >= 0 else ''
    ax.text(i, v + 0.002, f'{sign}{diff:.2f}%', ha='center', va='bottom', fontsize=9, fontweight='bold')
ax.legend(loc='upper right', frameon=True, edgecolor='black', fontsize=9, framealpha=1.0)
plt.tight_layout()
plt.savefig('plots/task3/task3_speedup.png')
plt.close()

# --- Task 3 Plot 3: Prefetch Accuracy (PDF Page 7 Top Style) ---
fig, ax = plt.subplots(figsize=(6.5, 4.8), dpi=300)
ax.bar(x_traces, t3_acc, width_single, label='SPP Prefetch Accuracy', color=c_slate, edgecolor='black', linewidth=0.8)
ax.set_title('Task 3: L1D Prefetch Accuracy', fontsize=11, pad=10)
ax.set_ylabel('Accuracy (%)', fontsize=10)
ax.set_xlabel('Benchmark Traces', fontsize=10)
ax.set_xticks(x_traces)
ax.set_xticklabels(traces)
ax.set_ylim(0, 55)
for i, v in enumerate(t3_acc):
    ax.text(i, v + 1.0, f'{v:.2f}%', ha='center', va='bottom', fontsize=9, fontweight='bold')
ax.legend(loc='upper right', frameon=True, edgecolor='black', fontsize=9, framealpha=1.0)
plt.tight_layout()
plt.savefig('plots/task3/task3_accuracy.png')
plt.close()

# --- Task 3 Plot 4: L1D Coverage (PDF Page 7 Bottom Style) ---
fig, ax = plt.subplots(figsize=(6.5, 4.8), dpi=300)
ax.bar(x_traces, t3_cov, width_single, label='L1D Prefetch Coverage', color=c_green, edgecolor='black', linewidth=0.8)
ax.set_title('Task 3: L1D Cache Miss Coverage', fontsize=11, pad=10)
ax.set_ylabel('Coverage (%)', fontsize=10)
ax.set_xlabel('Benchmark Traces', fontsize=10)
ax.set_xticks(x_traces)
ax.set_xticklabels(traces)
ax.set_ylim(0, 32)
for i, v in enumerate(t3_cov):
    ax.text(i, v + 0.6, f'{v:.2f}%', ha='center', va='bottom', fontsize=9, fontweight='bold')
ax.legend(loc='upper right', frameon=True, edgecolor='black', fontsize=9, framealpha=1.0)
plt.tight_layout()
plt.savefig('plots/task3/task3_coverage.png')
plt.close()

# --- Task 3 Plot 5: L1D Load MPKI ---
fig, ax = plt.subplots(figsize=(6.5, 4.8), dpi=300)
ax.bar(x_traces - width2/2, lru_l1d, width2, label='Baseline (LRU)', color=c_coral, edgecolor='black', linewidth=0.8)
ax.bar(x_traces + width2/2, t3_l1d, width2, label='Task 3 (SPP + Dyn I-RRIP)', color=c_green, edgecolor='black', linewidth=0.8)
ax.set_title('Task 3: L1D Load MPKI Reduction', fontsize=11, pad=10)
ax.set_ylabel('L1D Load MPKI', fontsize=10)
ax.set_xlabel('Benchmark Traces', fontsize=10)
ax.set_xticks(x_traces)
ax.set_xticklabels(traces)
ax.set_ylim(0, 16)
ax.legend(loc='upper right', frameon=True, edgecolor='black', fontsize=9, framealpha=1.0)
plt.tight_layout()
plt.savefig('plots/task3/task3_l1d_mpki.png')
plt.close()

# --- Task 3 Plot 6: L2C Total Load MPKI ---
fig, ax = plt.subplots(figsize=(6.5, 4.8), dpi=300)
ax.bar(x_traces - width2/2, lru_l2_t3, width2, label='Baseline (LRU)', color=c_coral, edgecolor='black', linewidth=0.8)
ax.bar(x_traces + width2/2, t3_l2c, width2, label='Task 3 (SPP + Dyn I-RRIP)', color=c_green, edgecolor='black', linewidth=0.8)
ax.set_title('Task 3: Total L2C Load MPKI Reduction', fontsize=11, pad=10)
ax.set_ylabel('L2C Total MPKI', fontsize=10)
ax.set_xlabel('Benchmark Traces', fontsize=10)
ax.set_xticks(x_traces)
ax.set_xticklabels(traces)
ax.set_ylim(0, 32)
ax.legend(loc='upper right', frameon=True, edgecolor='black', fontsize=9, framealpha=1.0)
plt.tight_layout()
plt.savefig('plots/task3/task3_l2c_total_mpki.png')
plt.close()

# --- Task 3 Plot 7: L2 Instruction Load MPKI ---
fig, ax = plt.subplots(figsize=(6.5, 4.8), dpi=300)
ax.bar(x_traces - width2/2, lru_l2_inst_t3, width2, label='Baseline (LRU)', color=c_coral, edgecolor='black', linewidth=0.8)
ax.bar(x_traces + width2/2, t3_l2_inst, width2, label='Task 3 (SPP + Dyn I-RRIP)', color=c_green, edgecolor='black', linewidth=0.8)
ax.set_title('Task 3: L2 Instruction Load MPKI Reduction', fontsize=11, pad=10)
ax.set_ylabel('L2 Instruction MPKI', fontsize=10)
ax.set_xlabel('Benchmark Traces', fontsize=10)
ax.set_xticks(x_traces)
ax.set_xticklabels(traces)
ax.set_ylim(0, 22)
ax.legend(loc='upper right', frameon=True, edgecolor='black', fontsize=9, framealpha=1.0)
plt.tight_layout()
plt.savefig('plots/task3/task3_l2c_instruction_mpki.png')
plt.close()

# --- Task 3 Plot 8: L2 Data Load MPKI ---
fig, ax = plt.subplots(figsize=(6.5, 4.8), dpi=300)
ax.bar(x_traces - width2/2, lru_l2_data_t3, width2, label='Baseline (LRU)', color=c_coral, edgecolor='black', linewidth=0.8)
ax.bar(x_traces + width2/2, t3_l2_data, width2, label='Task 3 (SPP + Dyn I-RRIP)', color=c_sky, edgecolor='black', linewidth=0.8)
ax.set_title('Task 3: L2 Data Load MPKI', fontsize=11, pad=10)
ax.set_ylabel('L2 Data MPKI', fontsize=10)
ax.set_xlabel('Benchmark Traces', fontsize=10)
ax.set_xticks(x_traces)
ax.set_xticklabels(traces)
ax.set_ylim(0, 14)
ax.legend(loc='upper right', frameon=True, edgecolor='black', fontsize=9, framealpha=1.0)
plt.tight_layout()
plt.savefig('plots/task3/task3_l2c_data_mpki.png')
plt.close()

print('Successfully generated all Task 2A, Task 2B, and Task 3 plots in their respective subfolders!')
