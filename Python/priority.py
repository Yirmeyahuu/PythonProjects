# A program to simulate the non-preemptive Priority Scheduling algorithm.
# This algorithm schedules processes based on their assigned priority, with a lower
# number typically indicating a higher priority.

def find_waiting_time(processes, n, burst_time, wt):
    """
    Calculates the waiting time for each process in Priority Scheduling.
    The waiting time for the first process is 0. For others, it's the sum of the
    burst times of all preceding, higher-priority processes.
    
    Args:
        processes (list): A list of process IDs, sorted by priority.
        n (int): The number of processes.
        burst_time (list): The burst time for each process, sorted to match the processes.
        wt (list): An empty list to store the calculated waiting times.
    """
    wt[0] = 0

    # Calculate waiting time for subsequent processes.
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

def find_average_time(processes, n, burst_time, priority):
    """
    Orchestrates the calculation and printing of average waiting and turnaround times.
    This function first sorts the processes by their priority, which is the core
    logic of the Priority Scheduling algorithm.
    
    Args:
        processes (list): A list of process IDs.
        n (int): The number of processes.
        burst_time (list): The burst time for each process.
        priority (list): The priority for each process.
    """
    # Combine processes, burst times, and priorities into a list of tuples for easy sorting.
    process_data = list(zip(processes, burst_time, priority))

    # Sort processes based on priority in ascending order (lower number = higher priority).
    # The lambda function specifies that the sorting key is the third element of the tuple (priority).
    process_data.sort(key=lambda x: x[2])

    # Unzip the sorted tuples back into separate lists.
    sorted_processes, sorted_burst_time, sorted_priority = zip(*process_data)
    
    # Initialize lists to store waiting time and turnaround time.
    wt = [0] * n
    tat = [0] * n

    # Find waiting time of all processes based on the sorted order.
    find_waiting_time(list(sorted_processes), n, list(sorted_burst_time), wt)

    # Find turnaround time of all processes.
    find_turn_around_time(list(sorted_processes), n, list(sorted_burst_time), wt, tat)

    # Display results in a clear table format.
    print("Processes\tBurst Time\tPriority\tWaiting Time\tTurn-Around Time")
    total_wt = 0
    total_tat = 0
    for i in range(n):
        total_wt += wt[i]
        total_tat += tat[i]
        print(f"P{sorted_processes[i]}\t\t{sorted_burst_time[i]}\t\t{sorted_priority[i]}\t\t{wt[i]}\t\t{tat[i]}")

    print(f"\nAverage Waiting Time = {total_wt / n:.2f}")
    print(f"Average Turn-Around Time = {total_tat / n:.2f}")

# Main part of the program to run the Priority Scheduling algorithm with sample data.
if __name__ == "__main__":
    # Define a list of processes.
    processes = [1, 2, 3, 4, 5]
    n = len(processes)

    # Define the CPU burst times for each process.
    burst_time = [10, 1, 2, 1, 5]

    # Define the priorities for each process (lower number = higher priority).
    priority = [3, 1, 4, 5, 2]

    # Call the main function to perform the calculations and display the results.
    find_average_time(processes, n, burst_time, priority)
