# A program to simulate the First-Come, First-Served (FCFS) CPU scheduling algorithm.
# This algorithm is non-preemptive and executes processes in the order they arrive.

def find_waiting_time(processes, n, burst_time, wt):
    """
    Calculates the waiting time for each process.
    The waiting time of a process is the sum of the burst times of all processes
    that came before it.
    
    Args:
        processes (list): A list of process IDs.
        n (int): The number of processes.
        burst_time (list): The burst time for each process.
        wt (list): An empty list to store the calculated waiting times.
    """
    # The waiting time for the first process is always 0.
    wt[0] = 0

    # Calculate waiting time for subsequent processes.
    # Waiting time of the current process is the waiting time of the previous
    # process plus the previous process's burst time.
    for i in range(1, n):
        wt[i] = burst_time[i - 1] + wt[i - 1]

def find_turn_around_time(processes, n, burst_time, wt, tat):
    """
    Calculates the turnaround time for each process.
    Turnaround time is the total time from arrival until completion.
    It is calculated as: burst_time + waiting_time.
    
    Args:
        processes (list): A list of process IDs.
        n (int): The number of processes.
        burst_time (list): The burst time for each process.
        wt (list): The list of waiting times.
        tat (list): An empty list to store the calculated turnaround times.
    """
    for i in range(n):
        tat[i] = burst_time[i] + wt[i]

def find_average_time(processes, n, burst_time):
    """
    Orchestrates the calculation and printing of average waiting and turnaround times.
    
    Args:
        processes (list): A list of process IDs.
        n (int): The number of processes.
        burst_time (list): The burst time for each process.
    """
    # Initialize lists to store waiting time and turnaround time.
    wt = [0] * n
    tat = [0] * n

    # Find waiting time of all processes.
    find_waiting_time(processes, n, burst_time, wt)

    # Find turnaround time of all processes.
    find_turn_around_time(processes, n, burst_time, wt, tat)

    # Display results in a clear table format.
    print("Processes\tBurst Time\tWaiting Time\tTurn-Around Time")
    total_wt = 0
    total_tat = 0
    for i in range(n):
        total_wt += wt[i]
        total_tat += tat[i]
        print(f"P{i+1}\t\t{burst_time[i]}\t\t{wt[i]}\t\t{tat[i]}")

    print(f"\nAverage Waiting Time = {total_wt / n:.1f}")
    print(f"Average Turn-Around Time = {total_tat / n:.1f}")

# Main part of the program to run the FCFS algorithm with sample data.
if __name__ == "__main__":
    # Define a list of processes (you can add more or change their order).
    processes = [1, 2, 3, 4]
    n = len(processes)

    # Define the CPU burst times for each process.
    # The order of burst times corresponds to the order of processes.
    burst_time = [5, 3, 8, 6]

    # Call the main function to perform the calculations and display the results.
    find_average_time(processes, n, burst_time)
