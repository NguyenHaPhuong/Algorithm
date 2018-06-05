# Challenge 4:
# Input "a" is the list of rows of the matrix. 
#Output Format: Print the absolute difference between the sums of the matrix's two diagonals as a single integer.
def diagonalDifference(a):
	e=0
	b=0
	for i in range(len(a)):
		e= e+a[i][i]
		b= b+a[i][-(i+1)]
		d= abs(e-b)
	return d
	
print (diagonalDifference([[11,2,4],[4,5,6],[10,8,-12]]))
