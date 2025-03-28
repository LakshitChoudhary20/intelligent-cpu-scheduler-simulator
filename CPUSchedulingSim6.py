import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
import random
from sklearn.linear_model import LinearRegression

# Stage 1: Basic FCFS Scheduler
def fcfs_scheduling(processes):
    processes.sort(key=lambda x: x[1])  # Sort by arrival time
    time = 0
    schedule = []
    results = []
    for pid, arrival, burst in processes:
        start = max(time, arrival)
        end = start + burst
        schedule.append((pid, start, end))
        completion_time = end
        turnaround_time = completion_time - arrival
        waiting_time = turnaround_time - burst
        response_time = start - arrival
        results.append((pid, completion_time, turnaround_time, waiting_time, response_time))
        time = end
    return schedule, results

# Stage 2: Add SJF, Priority, and Round Robin

def sjf_scheduling(processes):
    processes.sort(key=lambda x: (x[1], x[2]))  # Sort by arrival time then burst time
    time, schedule, results = 0, [], []
    while processes:
        available = [p for p in processes if p[1] <= time]
        if available:
            available.sort(key=lambda x: x[2])
            pid, arrival, burst = available.pop(0)
            start, end = time, time + burst
            schedule.append((pid, start, end))
            completion_time = end
            turnaround_time = completion_time - arrival
            waiting_time = turnaround_time - burst
            response_time = start - arrival
            results.append((pid, completion_time, turnaround_time, waiting_time, response_time))
            time = end
            processes.remove((pid, arrival, burst))
        else:
            time += 1
    return schedule, results

# Updated Priority Scheduling to ensure priority values are only required for Priority Scheduling
def priority_scheduling(processes):
    processes.sort(key=lambda x: (x[1], x[3]))  # Sort by arrival time then priority
    time, schedule, results = 0, [], []
    while processes:
        available = [p for p in processes if p[1] <= time]
        if available:
            available.sort(key=lambda x: x[3])
            pid, arrival, burst, priority = available.pop(0)
            start, end = time, time + burst
            schedule.append((pid, start, end))
            completion_time = end
            turnaround_time = completion_time - arrival
            waiting_time = turnaround_time - burst
            response_time = start - arrival
            results.append((pid, completion_time, turnaround_time, waiting_time, response_time))
            time = end
            processes.remove((pid, arrival, burst, priority))
        else:
            time += 1
    return schedule, results

def round_robin_scheduling(processes, quantum=2):
    queue = sorted(processes, key=lambda x: x[1])
    time, schedule, results = 0, [], {}
    remaining_burst = {p[0]: p[2] for p in processes}
    while queue:
        pid, arrival, burst = queue.pop(0)
        start = max(time, arrival)
        execute = min(remaining_burst[pid], quantum)
        end = start + execute
        schedule.append((pid, start, end))
        remaining_burst[pid] -= execute
        if pid not in results:
            results[pid] = [arrival, start, 0, 0, 0]
        if remaining_burst[pid] == 0:
            completion_time = end
            turnaround_time = completion_time - arrival
            waiting_time = turnaround_time - burst
            response_time = results[pid][1] - arrival
            results[pid] = [pid, completion_time, turnaround_time, waiting_time, response_time]
        else:
            queue.append((pid, end, remaining_burst[pid]))
        time = end
    return schedule, list(results.values())

# Stage 4: Basic GUI
def create_gui():
    root = tk.Tk()
    root.title("CPU Scheduling Simulator")
    
    tk.Label(root, text="Process ID").grid(row=0, column=0)
    tk.Label(root, text="Arrival Time").grid(row=0, column=1)
    tk.Label(root, text="Burst Time").grid(row=0, column=2)
    tk.Label(root, text="Priority").grid(row=0, column=3)
    
    process_entries = []
    for i in range(5):
        pid_entry = tk.Entry(root)
        at_entry = tk.Entry(root)
        bt_entry = tk.Entry(root)
        pr_entry = tk.Entry(root)
        pid_entry.grid(row=i+1, column=0)
        at_entry.grid(row=i+1, column=1)
        bt_entry.grid(row=i+1, column=2)
        pr_entry.grid(row=i+1, column=3)
        process_entries.append((pid_entry, at_entry, bt_entry, pr_entry))
    
    def run_scheduler():
        processes = []
        selected_algorithm = algorithm_var.get()
        for p in process_entries:
            if p[0].get():
                pid = int(p[0].get())
                arrival = int(p[1].get())
                burst = int(p[2].get())
                if selected_algorithm == "Priority":
                    priority = int(p[3].get()) if p[3].get() else 0
                    processes.append((pid, arrival, burst, priority))
                else:
                    processes.append((pid, arrival, burst))

        if selected_algorithm == "FCFS":
            schedule, results = fcfs_scheduling(processes)
        elif selected_algorithm == "SJF":
            schedule, results = sjf_scheduling(processes)
        elif selected_algorithm == "Priority":
            schedule, results = priority_scheduling(processes)
        elif selected_algorithm == "Round Robin":
            schedule, results = round_robin_scheduling(processes)
        else:
            return
        
        visualize_schedule(schedule)
        display_results(results)
        
    def visualize_schedule(schedule):
        fig, ax = plt.subplots()
        for pid, start, end in schedule:
            ax.barh(pid, end - start, left=start)
        plt.xlabel("Time")
        plt.ylabel("Process ID")
        plt.title("Gantt Chart for CPU Scheduling")
        plt.show()