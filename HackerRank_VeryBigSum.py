# Challenge 3:
# This function is used to caculate the sum of the numbers that are in list. 
# Input: "n" is the integer, that is the number of numbers in list
#        "ar" is the list of numbers


def aVeryBigSum(n, ar):
	a=0
	for i in list(range(n)):
		a= a+ar[i]
	
	return a
		
print (aVeryBigSum(5,[1000000001, 1000000002, 1000000003, 1000000004, 1000000005]))

