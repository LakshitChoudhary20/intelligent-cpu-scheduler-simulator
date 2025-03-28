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
