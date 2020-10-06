
'''
===============================================================================
ENGR 133 Fa 2020

Assignment Information
	Assignment:     e.g. Py4 Task 1
	Author:         Matthew Kane, kane83@purdue.edu
	Team ID:        LC5-005
	
Contributors:   Matthew Kane, kane83@purdue.edu

	My contributor(s) helped me:	
	[ ] understand the assignment expectations without
		telling me how they will approach it.
	[ ] understand different ways to think about a solution
		without helping me plan my solution.
	[ ] think through the meaning of a specific error or
		bug present in my code without looking at my code.
	Note that if you helped somebody else with their code, you
	have to list that person as a contributor here as well.
===============================================================================
'''
lastName = input("Enter your last name:\n")
firstName = input("Enter your first name:\n")
age = int(input("Enter your age in whole years:\n"))
days = int(input("Enter the days elapsed since your last birthday:\n"))

ageYears = str(age + (days/365.242199))
ageSec = str(float(ageYears)*365.242199*24*60*60)

file = open('Py4_Task1_output.txt','w')
file.write(f"{firstName} {lastName}\n")
file.write(f"You are {ageYears} years old.\n")
file.write(f"You are {ageSec} seconds old.\n")
file.close()

'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''

