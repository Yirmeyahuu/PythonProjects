# A program to simulate the non-preemptive Shortest Job First (SJF) CPU scheduling algorithm.
# This algorithm schedules processes based on their burst time, giving priority to the shortest jobs.

def find_waiting_time(processes, n, burst_time, wt):
    """
    Calculates the waiting time for each process in SJF.
    The waiting time for the first process is 0. For others, it's the sum of the
    burst times of all preceding processes.
    
    Args:
        processes (list): A list of process IDs, sorted by burst time.
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

def find_average_time(processes, n, burst_time):
    """
    Orchestrates the calculation and printing of average waiting and turnaround times.
    This function first sorts the processes by their burst time, which is the core
    logic of the SJF algorithm.
    
    Args:
        processes (list): A list of process IDs.
        n (int): The number of processes.
        burst_time (list): The burst time for each process.
    """
    # Combine processes and burst times into a list of tuples for easy sorting.
    process_data = list(zip(processes, burst_time))

    # Sort processes based on burst time in ascending order.
    # The lambda function specifies that the sorting key is the second element of the tuple (burst time).
    process_data.sort(key=lambda x: x[1])

    # Unzip the sorted tuples back into separate lists.
    sorted_processes, sorted_burst_time = zip(*process_data)
    
    # Initialize lists to store waiting time and turnaround time.
    wt = [0] * n
    tat = [0] * n

    # Find waiting time of all processes based on the sorted order.
    find_waiting_time(list(sorted_processes), n, list(sorted_burst_time), wt)

    # Find turnaround time of all processes.
    find_turn_around_time(list(sorted_processes), n, list(sorted_burst_time), wt, tat)

    # Display results in a clear table format.
    print("Processes\tBurst Time\tWaiting Time\tTurn-Around Time")
    total_wt = 0
    total_tat = 0
    for i in range(n):
        total_wt += wt[i]
        total_tat += tat[i]
        print(f"P{sorted_processes[i]}\t\t{sorted_burst_time[i]}\t\t{wt[i]}\t\t{tat[i]}")

    print(f"\nAverage Waiting Time = {total_wt / n:.2f}")
    print(f"Average Turn-Around Time = {total_tat / n:.2f}")

# Main part of the program to run the SJF algorithm with sample data.
if __name__ == "__main__":
    # Define a list of processes.
    processes = [1, 2, 3, 4]
    n = len(processes)

    # Define the CPU burst times for each process.
    burst_time = [5, 3, 8, 6]

    # Call the main function to perform the calculations and display the results.
    find_average_time(processes, n, burst_time)
