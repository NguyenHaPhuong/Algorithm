#Q1:
#Write a recursive function to evaluate yn, x is of type double.
# yn(x) = x^n + x^(n-1) +........+ x^2 + x^1 + 1
# Input: 1st column: n
#        2nd column: x

#Output: 1st column: n
#        2nd column: x
#        3rd column: answer (that is 'yn(x)')

n = int(input("Enter the number of pairs: "))

a = []

for _ in range(n):
	a.append(list(map(int, input().rstrip().split())))
	
def recursive(n):
	
	for i in n:
		y=0
		for x in range(i[0]+1):
			y+=(i[1]**x)
		
		print (i[0],i[1],y)
	
	
recursive(a)