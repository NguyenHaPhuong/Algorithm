# Challenge 5: a function prints a staircase of size.
#Input Format: integer "n' denoting the size of the staircase.
# Output Format: Print a staircase of size n, using '#' symbols and spaces.
def staircase(n):
	for i in range(n+1):
		if i != 0:
			a= " "*(n-i)+"#"*i
			print (a)
		
staircase(5)