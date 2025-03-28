Intelligent CPU Scheduling Simulator

 Project purpose
Intelligent CPU Scheduling Simulator is a Python-based application designed to simulate and analyze various CPU scheduling algorithms. It offers users an interactive graphical user interface (GUI) to imagine the input process details and scheduling results. The project helps to understand and compare scheduling strategies based on their performance matrix.

Features
- Several schedueling supports algorithms:
  -First-Come, first-served (FCFS)
  - The smallest job first (SJF)
  - priority assessment
  - Round Robin (RR) over quantum time
- Graphical User Interface (GUI):
  - Easy input of process data (process ID, arrival time, burst time, priority)
  - Dropdown menu to select Scheduling Algorithm
  - Interactive Result Performance
- Gant Chart Visualization:
  - The process performance sequence for better understanding
- Performance metrics:
  - Completion time
  - Turn Around Time
  - waiting time
  - Response time

 Instructions to run simulator
 Required conditions
Make sure you have a python installed (Python 3.X recommended). Establish the required dependence using the use:
`` `
PIP installed Nompi matplotlib scit-lan
,

 Running simulator
1. Download or clone the repository.
2. Navigate in the project directory.
3. Run using the script:
   `` `
   Pythan <script_name> .py
   ,
4. Enter the process details in the GUI.
5. Select the desired scheduling algorithm.
6. Click on "Run Scheduler" to execute and imagine the results.

 Use examples
- Enter the process details in the text field.
- Select an algorithm (eg, FCFS, SJF, priority, or round robin).
- Click on the run scheduler button.
- See Gant Chart and Table Results.

 Future Improvements
-Implement additional scheduling algorithms.
-Enhance GUI with more interactive features.
-Support for real-time scheduling analysis.
