
Individual Assignment: Batch Scheduling
Author: Grace Julius
Class: Operating Systems
Date: 10/04/2025
Language: Python 3


1. OVERVIEW
------------------------------------------------------------
This program calculates the Average Waiting Time (AWT) for a set of jobs
based on three different CPU scheduling approaches:

   1. Shortest Job First (SJF)
   2. Defined Order (B, C, D, E, A)
   3. Randomized Order (For Extra Credit)

The goal of this assignment is to help visualize how scheduling algorithms affect the average
waiting time of multiple processes with different arrival and runtime values.

------------------------------------------------------------
2. HOW THE PROGRAM WORKS (HIGH LEVEL STEPS)
------------------------------------------------------------
1. The user is prompted to enter:
      - The total number of jobs
      - Each job’s name (A, B, C, D, E, etc.)
      - Runtime (burst time)
      - Arrival time

2. After entering the information, the program confirms the details to allow
   the user to correct any mistakes before proceeding.

3. Once all job data is collected, the program performs:
      - Shortest Job First (SJF) scheduling
      - Defined order scheduling in (B, C, D, E, A)
      - Randomized order scheduling (extra credit)

4. For each scheduling approach, the program calls the appropriate function
   to compute the average waiting time and displays the result in a clear,
   user-friendly format.

5. The calculations are done using the same helper function “awt()” which
   computes the average wait time from the job list.

------------------------------------------------------------
3. KEY FUNCTIONS AND WHAT THEY DO
------------------------------------------------------------
- **main()**  
  Handles all user input, confirmation, and printing results.

- **awt(jobs)**  
  Calculates the average waiting time for a given list of jobs.

- **SJF(jobs)**  
  Implements the Shortest Job First algorithm by sorting jobs based on runtime.

- **definedOrder(jobs)**  
  Runs jobs in the predefined order (B, C, D, E, A) using a dictionary for
  fast job lookups.

- **randomApproach(jobs)**  
  Randomly shuffles the job list to calculate average waiting time for a
  random execution order.

------------------------------------------------------------
4. EDGE CASES CONSIDERED
------------------------------------------------------------
The program includes several checks and handling mechanisms to ensure smooth
execution even under unusual input conditions:

1. **Invalid input handling:**  
   If a user's input is invalid (e.g a non-numeric runtime or arrival time), an error message
   is shown and they are re-prompted for correct input.

2. **User correction option:**  
   After each job’s details are entered, the program asks for confirmation
   ("Is this information correct?") so users can fix mistakes before continuing 
   this prevents the stress of having to start over after realizing the got a wrong output.
   It is really helpful in the case of a large dataset as it helps to ensure accuracy.

3. **Empty job list:**  
   If no jobs are entered, the program safely returns an average wait time of 0
   instead of crashing or dividing by zero.

4. **CPU idle time handling:**  
   If the CPU is idle before a job arrives, the current time is advanced to
   the next job’s arrival time.

5. **Data preservation:**  
   Copies of the job list are made before sorting or shuffling to prevent
   changes to the original user input.

6. **Random order stability:**  
   The random order is displayed to the user for transparency and cross-checking.

**Possible improvements (if extended):**
- Add checks in case the defined order (B, C, D, E, A) contains jobs not entered by the user.
- Handle tie-breaking when multiple jobs have the same arrival and runtime.

------------------------------------------------------------
5. HOW TO RUN
------------------------------------------------------------
**Follow these steps for successful execution of the program and accurate display of scheduling results:**

1. Save the file as: `batch_scheduling.py`
2. Run the program using:
       python batch_scheduling.py
3. Enter the job details as prompted:
       - Number of jobs
       - Each job’s name, runtime, and arrival time
4. Confirm each entry when asked.
5. View the calculated average waiting times for:
       - Shortest Job First (SJF)
       - Defined Order (B, C, D, E, A)
       - Randomized Order.
       
------------------------------------------------------------
6. SAMPLE OUTPUT
------------------------------------------------------------
Welcome to the Batch Scheduling Program Assignment!
This assignment will calculate average wait times 
for different scheduling algorithms(Shortest Job First, Defined Order, Randomized Order)

Please enter the number of jobs to be executed: 
Average wait time for the Shortest Job First: 3.60
Average wait time for the defined order (B,C,D,E,A): 3.40
Randomized order of jobs: ['E', 'A', 'C', 'D', 'B']
Average wait time for a random order: 3.40


