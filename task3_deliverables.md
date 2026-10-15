# Task 3 Deliverables

## 1. Performance Metrics Table
Report of IPC, Speedup, Prefetch Accuracy, Coverage, and Load MPKI across L1D, L2C, L2 Instruction, and L2 Data for Baseline (LRU) vs. Task 3 (SPP L1D Prefetcher + Prefetch-Aware Dynamic I-RRIP L2 Replacement Policy):

| Configuration | Trace | IPC | Speedup vs LRU | L1D Load MPKI | Prefetch Accuracy | L1D Coverage | L2C Load MPKI | L2 Instruction MPKI | L2 Data MPKI |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Baseline (LRU)** | Trace 1 | 0.2321 | 1.0000 (0.00%) | 10.679 | - | - | 17.725 | 10.367 | 7.359 |
| **Task 3 (SPP + Dyn I-RRIP)** | Trace 1 | 0.2340 | **1.0080 (+0.80%)** | **9.394** | **49.81%** | **+12.03%** | **17.391 (-1.88%)** | **9.282 (-10.46%)** | 8.109 |
| **Baseline (LRU)** | Trace 2 | 0.2500 | 1.0000 (0.00%) | 13.537 | - | - | 28.550 | 19.844 | 8.706 |
| **Task 3 (SPP + Dyn I-RRIP)** | Trace 2 | 0.2630 | **1.0519 (+5.19%)** | **12.843** | **48.43%** | **+5.13%** | **20.508 (-28.17%)** | **10.367 (-47.76%)** | 10.141 |
| **Baseline (LRU)** | Trace 3 | 0.3819 | 1.0000 (0.00%) | 3.404 | - | - | 3.961 | 1.127 | 2.835 |
| **Task 3 (SPP + Dyn I-RRIP)** | Trace 3 | 0.3948 | **1.0339 (+3.39%)** | **2.607** | **44.19%** | **+23.41%** | **2.952 (-25.47%)** | **0.814 (-27.79%)** | 2.138 |

$$\text{Speedup} = \frac{\text{IPC}_{\text{Task 3}}}{\text{IPC}_{\text{Baseline (LRU)}}}$$

$$\text{L1D Coverage} = \frac{\text{L1D Load Misses}_{\text{Baseline}} - \text{L1D Load Misses}_{\text{Task 3}}}{\text{L1D Load Misses}_{\text{Baseline}}}$$

*Generated Plots for Task 3 (matching PDF Pages 6 & 7 theme in `plots/task3/`):*
- `plots/task3/task3_ipc.png`: Instructions Per Cycle (IPC) across Traces 1, 2, 3
- `plots/task3/task3_speedup.png`: Speedup over Baseline across Traces 1, 2, 3 (with 1.0 reference line)
- `plots/task3/task3_accuracy.png`: SPP L1D Prefetch Accuracy across Traces 1, 2, 3
- `plots/task3/task3_coverage.png`: L1D Cache Miss Coverage across Traces 1, 2, 3
- `plots/task3/task3_l1d_mpki.png`: L1D Load MPKI Reduction across Traces 1, 2, 3
- `plots/task3/task3_l2c_total_mpki.png`: Total L2C Load MPKI Reduction across Traces 1, 2, 3
- `plots/task3/task3_l2c_instruction_mpki.png`: L2 Instruction Load MPKI across Traces 1, 2, 3
- `plots/task3/task3_l2c_data_mpki.png`: L2 Data Load MPKI across Traces 1, 2, 3

---

## 2. Rationale Behind Handling the Prefetch Packet by the Replacement Policy

### 1. Exclusion of Prefetch Packets from Leader Set Counters
- **Mechanism:** In the set-dueling sampling logic, access and miss counters only update when `type != PREFETCH`.
- **Rationale:** The set-dueling threshold evaluates workload instruction intensity:
  $$\text{Ratio} = \frac{\text{instr\_accesses} + \text{instr\_misses}}{\text{total\_accesses} + \text{total\_misses}}$$
  Because SPP generates aggressive prefetch streams, prefetch packets have non-instruction tags (`isInstruction == 0`). If prefetch packets were counted, they would artificially inflate `data_acc` and `data_miss`, diluting the ratio below the 0.25 threshold. This would trick follower sets into turning off instruction prioritization during severe frontend starvation. Excluding prefetch traffic ensures that dynamic dueling measures genuine demand memory pressure.

### 2. Deprioritizing Speculative Prefetches on Cache Insertion (Miss Fills)
- **Mechanism:** Unprefetched demand lines insert at high or intermediate priority (instructions at $\text{RRPV} = 1$, demand data at $\text{RRPV} = 2$), while incoming prefetch lines insert at the lowest priority ($\text{RRPV} = \text{maxRRPV} = 3$).
- **Rationale:** Stride pattern prefetching is speculative. SPP operates at ~44–50% accuracy, meaning about half of issued prefetches may never experience demand reuse. Inserting speculative prefetch blocks at $\text{RRPV} = 3$ guarantees that if a prefetch is inaccurate, it becomes the immediate next candidate for replacement without displacing critical demand instructions or live data working sets.

### 3. Controlled Promotion on Cache Hits
- **Mechanism:** When a prefetch block already resident in the L2 cache experiences a hit from a subsequent prefetch request, it is promoted only to $\text{RRPV} = \text{maxRRPV} - 1 = 2$, whereas demand hits promote to $\text{RRPV} = 0$ (instructions) or $\text{RRPV} = 1$ (demand data).
- **Rationale:** Restricting prefetch hits to $\text{RRPV} = 2$ prevents repetitive speculative prefetch bursts from acquiring eviction immunity over demand instructions and demand data blocks. A line only attains top priority ($\text{RRPV} \le 1$) when an actual demand access validates its utility.

### 4. Asymmetric Miss Latency & Two-Tier Eviction Synergy
- **Rationale:** Frontend instruction stalls completely halt pipeline decode and issue stages, whereas data misses can be partially overlapped by Out-of-Order execution windows and MSHRs. By combining SPP prefetching with prefetch-aware Two-Tier eviction, inaccurate prefetches are evicted first at $\text{RRPV} = 3$, protecting instruction lines and achieving a **+5.19% speedup** on Trace 2 and **+3.39% speedup** on Trace 3 over baseline LRU.
