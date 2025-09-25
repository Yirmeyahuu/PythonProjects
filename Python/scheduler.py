import collections
import time

class Process:
    """Represents a single process in the OS."""
    def __init__(self, pid, arrival_time, burst_time, io_time=0):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time  # Total CPU time needed
        self.io_time = io_time # Time at which an I/O operation is triggered
        
        self.remaining_time = burst_time
        self.state = 'New'
        self.wait_time = 0
        self.turnaround_time = 0

def run_scheduler(processes):
    """
    Simulates a First-Come, First-Served (FCFS) process scheduler.
    """
    # Use a deque for efficient appends and pops from both ends
    ready_queue = collections.deque()
    io_queue = collections.deque()
    completed_processes = []
    
    current_time = 0
    cpu_busy = False
    
    # Sort processes by arrival time to handle them as they "arrive"
    processes.sort(key=lambda p: p.arrival_time)
    
    print("--- Process Scheduling Simulation (FCFS) ---")

    while processes or ready_queue or io_queue:
        # 1. Add newly arrived processes to the ready queue
        while processes and processes[0].arrival_time <= current_time:
            proc = processes.pop(0)
            proc.state = 'Ready'
            ready_queue.append(proc)
            print(f"Time {current_time:2d}: Process {proc.pid} has arrived and is now in the Ready Queue.")

        # 2. Check for processes that have finished I/O
        if io_queue and io_queue[0]['end_time'] <= current_time:
            proc = io_queue.popleft()['process']
            proc.state = 'Ready'
            ready_queue.append(proc)
            print(f"Time {current_time:2d}: Process {proc.pid} has finished I/O and is back in the Ready Queue.")

        # 3. If CPU is free and there are processes in the ready queue, dispatch one
        if not cpu_busy and ready_queue:
            running_process = ready_queue.popleft()
            running_process.state = 'Running'
            cpu_busy = True
            
            # Calculate wait time
            running_process.wait_time += current_time - running_process.arrival_time

            print(f"Time {current_time:2d}: Process {proc.pid} is now Running on the CPU.")

        # 4. Simulate process execution for one time unit
        if cpu_busy:
            running_process.remaining_time -= 1
            
            # Check for I/O request
            if running_process.io_time > 0 and (running_process.burst_time - running_process.remaining_time) == running_process.io_time:
                running_process.state = 'Waiting'
                io_queue.append({'process': running_process, 'end_time': current_time + 3}) # Assume I/O takes 3 time units
                print(f"Time {current_time:2d}: Process {running_process.pid} is now in the I/O Waiting Queue.")
                cpu_busy = False

            # Check for process completion
            elif running_process.remaining_time <= 0:
                running_process.state = 'Terminated'
                running_process.turnaround_time = current_time + 1 - running_process.arrival_time
                completed_processes.append(running_process)
                print(f"Time {current_time:2d}: Process {running_process.pid} has finished execution.")
                cpu_busy = False

        # 5. Increment time
        current_time += 1
        time.sleep(0.5) # Slow down the simulation to make it readable

    print("\n--- Simulation Complete ---")
    print(f"Total time taken: {current_time -1} units")
    
    # --- Print statistics ---
    total_wait_time = sum(p.wait_time for p in completed_processes)
    total_turnaround_time = sum(p.turnaround_time for p in completed_processes)
    avg_wait_time = total_wait_time / len(completed_processes)
    avg_turnaround_time = total_turnaround_time / len(completed_processes)
    
    print("\n--- Process Statistics ---")
    print("PID | Wait Time | Turnaround Time")
    for p in completed_processes:
        print(f"{p.pid:3d} | {p.wait_time:9d} | {p.turnaround_time:15d}")

    print(f"\nAverage Wait Time: {avg_wait_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")


if __name__ == "__main__":
    # Define a list of processes to simulate
    # Process(pid, arrival_time, burst_time, io_time=0)
    # io_time is the time *into* the process's execution that an I/O request occurs
    process_list = [
        Process(pid=1, arrival_time=0, burst_time=8),
        Process(pid=2, arrival_time=1, burst_time=4, io_time=2), # I/O request after 2s of execution
        Process(pid=3, arrival_time=2, burst_time=5),
        Process(pid=4, arrival_time=4, burst_time=2),
    ]
    
    run_scheduler(process_list)