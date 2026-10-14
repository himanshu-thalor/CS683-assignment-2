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

os.makedirs('plots', exist_ok=True)

# Common definitions
traces = ['Trace 1', 'Trace 2', 'Trace 3']
x_traces = np.arange(len(traces))
width2 = 0.32
width3 = 0.24

# PDF Color Palette
c_coral = '#eb7d75'   # Trace 1 / Baseline
c_sky = '#7fc2df'     # Trace 2 / Intermediate
c_green = '#98d89e'   # Trace 3 / Tuned Policy
c_slate = '#6a82bc'
c_crimson = '#c95374'

# Baseline LRU Data across Traces 1, 2, 3
lru_ipc = [0.2321, 0.2500, 0.3819]
lru_impki = [10.367, 19.844, 1.127]
lru_dmpki = [7.359, 8.706, 2.835]
lru_totmpki = [17.725, 28.550, 3.961]

# ==============================================================================
# TASK 2A PLOTS: Baseline (LRU) vs. I-RRIP across all 3 Traces
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
plt.savefig('plots/task2a_ipc.png')
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
plt.savefig('plots/task2a_speedup.png')
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
plt.savefig('plots/task2a_instruction_mpki.png')
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
plt.savefig('plots/task2a_data_mpki.png')
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
plt.savefig('plots/task2a_total_mpki.png')
plt.close()

# ==============================================================================
# TASK 2B PARAMETER TUNING: 1 Graph for Threshold Tuning + 1 for Leader Sets
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
plt.savefig('plots/task2b_threshold_speedup.png')
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
plt.savefig('plots/task2b_leaders_sensitivity.png')
plt.close()

# ==============================================================================
# TASK 2B TUNED PARAMS VS. LRU PLOTS: Dynamic I-RRIP (Tuned) vs. Baseline (LRU)
# ==============================================================================

# Tuned Dynamic I-RRIP (64 Leader Sets, Threshold 0.25)
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
plt.savefig('plots/task2b_ipc.png')
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
plt.savefig('plots/task2b_speedup.png')
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
plt.savefig('plots/task2b_instruction_mpki.png')
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
plt.savefig('plots/task2b_data_mpki.png')
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
plt.savefig('plots/task2b_total_mpki.png')
plt.close()

print('Successfully generated all Task 2A and 2B plots (1 graph for parameter tuning, full suite for tuned vs LRU)!')
