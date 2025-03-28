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
