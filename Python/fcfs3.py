def calculate_completion_time(num_processes, arrival_time, burst_time):

    completion_time = [0] * num_processes
    
    # The first process's completion time is its burst time plus its arrival time.
    completion_time[0] = arrival_time[0] + burst_time[0]
    
    # Loop through the rest of the processes to calculate their completion times.
    for i in range(1, num_processes):
        # The completion time is the maximum of the previous process's completion time
        # and the current process's arrival time, plus its own burst time.
        completion_time[i] = max(completion_time[i - 1], arrival_time[i]) + burst_time[i]
    
    return completion_time

def calculate_tat_and_wt(num_processes, arrival_time, burst_time, completion_time):

    turnaround_time = [0] * num_processes
    waiting_time = [0] * num_processes
    
    for i in range(num_processes):
        # Turnaround Time (TAT) = Completion Time - Arrival Time
        turnaround_time[i] = completion_time[i] - arrival_time[i]
        
        # Waiting Time (WT) = Turnaround Time - Burst Time
        waiting_time[i] = turnaround_time[i] - burst_time[i]
        
    return turnaround_time, waiting_time

def print_results(processes, arrival_time, burst_time, completion_time, turnaround_time, waiting_time):

    print("--- FCFS Scheduling Results ---")
    print("Process\tAT\tBT\tCT\tTAT\tWT")
    
    total_wt = 0
    total_tat = 0
    
    for i in range(len(processes)):
        total_wt += waiting_time[i]
        total_tat += turnaround_time[i]
        print(f"{processes[i]}\t{arrival_time[i]}\t{burst_time[i]}\t{completion_time[i]}\t{turnaround_time[i]}\t{waiting_time[i]}")

    print(f"\nAverage Waiting Time = {total_wt / len(processes):.2f}")
    print(f"Average Turnaround Time = {total_tat / len(processes):.2f}")

# --- Main Program Execution ---
if __name__ == "__main__":
    # Given data
    num_processes = 4
    processes = [f"P{i}" for i in range(num_processes)]
    arrival_time = [0, 1, 2, 3]
    burst_time = [5, 3, 8, 6]

    # Call functions to perform calculations
    completion_time = calculate_completion_time(num_processes, arrival_time, burst_time)
    turnaround_time, waiting_time = calculate_tat_and_wt(num_processes, arrival_time, burst_time, completion_time)
    
    # Print the final results
    print_results(processes, arrival_time, burst_time, completion_time, turnaround_time, waiting_time)

