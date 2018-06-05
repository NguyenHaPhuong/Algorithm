# Challenge 5:	
#Given an array of integers, calculate the fractions of its elements that are positive, negative, and are zeros. 
#The function will print the decimal value of each fraction on a new line.		
#Input Format: "arr" is an array of numbers .

# Output Format: 

#1. A decimal representing of the fraction of positive numbers in the array compared to its size.
#2. A decimal representing of the fraction of negative numbers in the array compared to its size.
#3. A decimal representing of the fraction of zeros in the array compared to its size.

def plusMinus(arr):
	a=0
	b=0
	c=0
	for i in range(len(arr)):
		if arr[i]>0:
			a+=1
		elif arr[i]<0:
			b+=1
		else:
			c+=1
	e= format((a/len(arr)),'.6f')
	f= format((b/len(arr)),'.6f')
	g= format((c/len(arr)),'.6f')
	
	print (e +"\n"+f+"\n"+g)
	
		
plusMinus([-4, 3, -9, 0, 4, 1])