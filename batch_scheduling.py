'''
Author: Grace Julius
Class: Operating System
Assignment: Individual_Assignment_Batch_Scheduling
Date: 10/04/2025



approach:
1) Get user's input for number of the job, then get each runtimes and arrival times
2) Implementation of wait time(Turn Around Time - Burst Time)
3) Implementation of Shortest Job First (SJF)
4) Implementation of Fixed Order (B,C,D,E,A)

key terms:
SJF: Shortest Job First
AWT/awt: Average Wait Time
'''''

#This section aims to get the user's input and output the result
#going to use a copy so as to prevent working on the main input so I don't affect other calculations
import copy
def main():
    print("Welcome to the Batch Scheduling Program Assignment!")
    print("This program will calculate average wait times for different scheduling algorithms(Shortest Job First, Defined Order, Randomized Order)")
    #adding the ability for users to be able to correct their input incase there is an error
    try:
        numberOfJobs = int(input("Please enter the number of jobs to be executed: "))
        
        jobs = [] #an array to store the jobs

    
        #Getting the job details... e.g: name of the job,runtimes, and arrival time

        for num in range(numberOfJobs):
            job_confirmation =False
            while not job_confirmation:
                try:
        
                    jobName = input(" Enter the job name for job : ")
                    jobRunTime = int(input(f" Enter runtime for job {jobName}: "))
                    jobArrivalTime = int(input(f" Enter the arrival time for job {jobName}: "))

                    print(f"\nYou entered: Job Name: {jobName}, Runtime: {jobRunTime}, Arrival Time: {jobArrivalTime}")
                    confirm = input("Is this information correct? (Yes/No): ").lower()
                    
                    if confirm =="yes":
                        jobs.append({"name": jobName, "runtime": jobRunTime, "arrival": jobArrivalTime})
                        job_confirmation = True

                    else: 
                        print("Please re-enter the job details carefully.")
                
                except ValueError:
                    print("Your input is invalid. Please enter a valid number for runtime and arrival time.")
        if len(jobs) != numberOfJobs or numberOfJobs == 0:
            print("Job input was incomplete or empty")
            return
        
        '''
        Output: Running program should display 
        the average wait for the shortest job first and running 
        them in the order (B, C, D, E, A) in a user-friendly form.
        '''
        #Shortest Job First (SJF)
        SJF_AWT = SJF(jobs)
        print(f"\nAverage wait time for the Shortest Job First: {SJF_AWT:.2f}")

        #Defined Order
        #made some updates here
        if numberOfJobs == 5 and all(job['name'] in ['A', 'B', 'C', 'D', 'E'] for job in jobs):
            definedOrder_AWT = definedOrder(jobs)
            print(f"Average wait time for the defined order (B,C,D,E,A) : {definedOrder_AWT:.2f}")
        else:
            print("\nSkipping Defined Order (B,C,D,E,A) calculation as input jobs do not match the expected 5 jobs (A, B, C, D, E).")
        
        #RandomOrder
        randomOder_AWT = randomApproach(jobs)
        print(f"\nAverage wait time for a random order: {randomOder_AWT:.2f}")

    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except KeyError as e:
        print(f"Error: Could not find job name {e} needed for the defined order calculation. Ensure you entered jobs A, B, C, D, and E.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



   



# function to calculate the average wait time (awt)

def awt(jobs):
    currentTime = 0 #track all current CPU time
    totalWaitTime = 0 #sum of wait times for all the jobs

    #incase there are no jobs, return 0
    if not jobs:
        return 0
    #loop through the jobs
    for job in jobs:
        arrivalTime = job['arrival']
        runtime = job['runtime']


        #start time = max of current time and arrival time
        jobStartTime = max(currentTime, arrivalTime)
        # wait time = start time - arrival time

        waitTime = jobStartTime - arrivalTime
        totalWaitTime += waitTime
        #updates current time to job's completion time
        currentTime = jobStartTime + runtime

    averageWaitTime = totalWaitTime / len(jobs)
    return averageWaitTime

'''
    Next, using the Shortest Job First Approach (SJF)
    will be performing it on a copy of the original list 
    in order to prevent mistakes or alteration of the original list during sorting

    '''
#a) function to implement average wait time the Shortest Job First (SJF) Algorithm

def SJF(jobs):

    #create a copy of the job
    jobsCopy = copy.deepcopy(jobs)
    #sorting the jobs by arrival time since we need to start from the shortest
    #after some research and external assistant from google and perplexity and chatgpt, I realized I did not create a copy which made get wrong answers
    # as I was working on the original input
    
    jobsCopy.sort(key=lambda x: (x['arrival'], x['runtime']))
    currentTime = 0
    totalWaitTIme = 0
    #readyQueue: keeps jobs that have arrived and are waiting
    readyQueue = []
    
    #jobsLeft: jobs that have not arrived
    jobsLeft = jobsCopy[:]
    numJobs = len(jobs)

    #looping till every job is processed
    while jobsLeft or readyQueue:
        i = 0
        while i < len(jobsLeft) and jobsLeft[i]['arrival'] <= currentTime:
            readyQueue.append(jobsLeft.pop(i))
        if not readyQueue:
            if jobsLeft:
                currentTime = jobsLeft[0]['arrival']
                continue
            else:
                break
        
        #SJF selection
        readyQueue.sort(key=lambda x: x['runtime'])
        jobsToRun = readyQueue.pop(0)

        jobStartTime = currentTime

        #waitTime
        waitTime = jobStartTime - jobsToRun['arrival']
        totalWaitTIme+= waitTime

        currentTime += jobsToRun['runtime']

    #fianl calculation
    averageWaitTime = totalWaitTIme/numJobs
    return averageWaitTime
        
    #return awt(sortedJobs)

#b) function to implement average wait time by running them in a defined order (BCDEA)


def definedOrder(jobs):
    '''
    have to sort the jobs into the defined order which is B,C,D,E,A and calculate the average wait time
    
    '''

    #a dictionary for easy and quick lookups of jobs to prevent nested loops in case of a large data

    jobDict = {job['name']: job for job in jobs}
    # A list of the given defined orders
    definedOrderNames = ['B','C','D','E','A']
    

    orderedJobs = [jobDict[jobName] for jobName in definedOrderNames]
    return awt(orderedJobs)

'''
extra point: Running program should display the average wait for the shortest job first
 and running them in an order generated randomly.
'''

import random

def randomApproach(jobs):
   #slicing helps create a shallow copy (a new object that contains reference to the elements of the original object)
   randomJobs = jobs[:] 
   random.shuffle(randomJobs)

   #printing the random order so, users can have an idea incase they want to cross check the output
   print(f"\nRandomized order of jobs: {[job['name'] for job in randomJobs]}")
   return awt(randomJobs)


#calling the main function in order to run the program

if __name__ =='__main__':
    main()