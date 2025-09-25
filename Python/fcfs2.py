# A basic program to simulate the First-Come, First-Served (FCFS) CPU scheduling algorithm
# with arrival times. This version keeps all the logic in one place without functions.

# --- Process Data ---
# The number of processes (P0 to P3).
num_processes = 4
processes = [f"P{i}" for i in range(num_processes)]

# Given arrival times for each process.
arrival_time = [0, 1, 2, 3]

# Given burst times for each process.
burst_time = [5, 3, 8, 6]

# --- Calculation of Metrics ---
# Initialize lists to store the results.
completion_time = [0] * num_processes
turnaround_time = [0] * num_processes
waiting_time = [0] * num_processes

# The completion time of the first process is its burst time plus its arrival time.
# This is a key part of handling arrival times.
completion_time[0] = arrival_time[0] + burst_time[0]

# Calculate completion time for subsequent processes.
for i in range(1, num_processes):
    # The completion time of the current process is the maximum of:
    # 1) The completion time of the previous process.
    # 2) The arrival time of the current process.
    # We take the maximum to ensure the CPU is not busy before a process arrives.
    completion_time[i] = max(completion_time[i - 1], arrival_time[i]) + burst_time[i]

# Calculate turnaround time and waiting time for all processes.
for i in range(num_processes):
    # Turnaround Time (TAT) = Completion Time - Arrival Time
    turnaround_time[i] = completion_time[i] - arrival_time[i]
    
    # Waiting Time (WT) = Turnaround Time - Burst Time
    waiting_time[i] = turnaround_time[i] - burst_time[i]

# --- Display Results ---
print("--- FCFS Scheduling Results ---")
print("Process\tAT\tBT\tCT\tTAT\tWT")

total_wt = 0
total_tat = 0

for i in range(num_processes):
    total_wt += waiting_time[i]
    total_tat += turnaround_time[i]
    print(f"{processes[i]}\t{arrival_time[i]}\t{burst_time[i]}\t{completion_time[i]}\t{turnaround_time[i]}\t{waiting_time[i]}")

# --- Final Average Calculation ---
print(f"\nAverage Waiting Time = {total_wt / num_processes:.2f}")
print(f"Average Turnaround Time = {total_tat / num_processes:.2f}")

