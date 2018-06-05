# Challenge 6:
# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. 
# Then print the respective minimum and maximum values as a single line of two space-separated long integers.
# Input: "arr" is the array of numbers
# Output is the minimum value and maximum value. 

def miniMaxSum(arr):
	a=0
	list=[]
	for i in range(len(arr)):
		a=a+arr[i]
		
	for e in arr:
		b=a-e
		list.append(b)
	
	c=list[0]
	d=list[0]
	for m in range(len(list)):
		if c>list[m]:
			c=list[m]
		elif d< list[m]:
			d=list[m]
	print (c,d)

miniMaxSum([1,2,3,4,5])	



#Explaination
#If we sum everything except 1,our sum is 2+3+4+5= 14 .
#If we sum everything except 2, our sum is 13.
#If we sum everything except 3, our sum is 12.
#If we sum everything except 4, our sum is 11.
#If we sum everything except 5, our sum is 10.
# The minimum value is 10 and the maximum value is 10
	

