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
        
        '''
        Output: Running program should display 
        the average wait for the shortest job first and running 
        them in the order (B, C, D, E, A) in a user-friendly form.
        '''
        #Shortest Job First (SJF)
        SJF_AWT = SJF(jobs)
        print(f"\nAverage wait time for the Shortest Job First: {SJF_AWT:.2f}")

        #Defined Order
        definedOrder_AWT = definedOrder(jobs)
        print(f"Average wait time for the defined order (B,C,D,E,A) : {definedOrder_AWT:.2f}")

        #RandomOrder
        randomOder_AWT = randomApproach(jobs)
        print(f"\nAverage wait time for a random order: {randomOder_AWT:.2f}")

    except ValueError:
        print("Invalid input. Please enter a valid number.")



   



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


        #checks if CPU is idle before a new job arrive, if so, time = arrival
        if currentTime < arrivalTime:
            currentTime = arrivalTime

        # wait time = current time - arrival time

        waitTime = currentTime - arrivalTime
        totalWaitTime += waitTime
        currentTime += runtime

    averageWaitTime = totalWaitTime / len(jobs)
    return averageWaitTime

'''
    Next, using the Shortest Job First Approach (SJF)
    will be performing it on a copy of the original list 
    in order to prevent mistakes or alteration of the original list during sorting

    '''
#a) function to implement average wait time the Shortest Job First (SJF) Algorithm

def SJF(jobs):

    #sorting the jobs by arrival time since we need to start from the shortest

    sortedJobs = sorted(jobs, key=lambda x: x['runtime'])
    return awt(sortedJobs)

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