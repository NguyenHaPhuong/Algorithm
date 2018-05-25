

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


#Q2:
#Given a sequence of points that form a polygon, we are required to tell if a list of points are either inside or
#outside the polygon.
# Example: Given a sequence of points for polygon: (1,1),(1,5),(10,5),(10,1). The following is the outcome of
#points tested.
# (3,2) Inside
# (7,5) Inside
# (5,6) Outside

#input_question: polygon"
#1st column: x cartesian coordinate
#2nd column: y cartesian coordinate


#input_question points"
#1st column: x cartesian coordinate
#2nd column: y cartesian coordinate

#Output:

#1st column: x cartesian coordinate
#2nd column: y cartesian coordinate
#3rd column: answer as either "inside" or "outside"


n = int(input("Enter the number of points forming polygon: "))

a = []
points=[]
arr1=[]
arr2=[]

for _ in range(n):
	a.append(list(map(int, input().rstrip().split())))
	
	
m= int(input("Enter the number of points: "))
for _ in range(m):
	points.append(list(map(int, input().rstrip().split())))
	
for i in a:
	arr1.append(i[0])
	arr2.append(i[1])
	
def min(arr1):
	min=arr1[0]
	for i in arr1:
		if min>i:
			min= i
			
	return (min)
	
def max(arr1):
	max=arr1[0]
	for i in arr1:
		if max<i:
			max= i
			
	return (max)
	
	
def polygon(a,b,c):
	n1= min(a)
	x1= max(a)
	
	n2= min(b)
	x2= max(b)
	
	for i in c:
		if i[0] in range(n1,x1+1) and i[1] in range(n2,x2+1):
			print (i[0], i[1], "inside")
			
		else:
			print (i[0], i[1], "outside")
			
			
polygon(arr1, arr2, points)



#Q3:

# For two dimensional grid, indexing the cells is done by 2-dimensional raster scan 
# For example, a 2-dimensional grid with sizes (L1, L2)=(4, 3) (it means there are 4 columns and 3 rows)
# In this grid, coordinates (x1, x2)=(2, 1) corresponds to index I = 6, and vice versa.


# Given 2-dimensional grid with sizes (L1, L2) = (50, 57)
# part a)
# Write a code to convert given coordinates to index (i.e. given x1 and x2, find index I)
# Input: 1st column: x1
#        2nd column: x2
# Output: 1st column: index

n = int(input("Enter the number of coordinates: "))

a = []

for _ in range(n):
	a.append(list(map(int, input().rstrip().split())))
	
	
	
def coor_2index(a):
	print (" ********* results *********")
	print ("index")
	for i in a:
		index= i[0] + (i[1]*50)
		print(index)
coor_2index(a)

#Part 2
#Write a code to convert given index to coordinates (i.e. given I, find coordinates x1 and x2)
#Input : 1st column: index
#Output: 1st column: x1
#        2nd column: x2


m = int(input("Enter the number of indexes: "))

b = []

for _ in range(m):
	b.append(int(input()))

def index_2coor(a):
	print (" ********* results *********")
	print ('x1', 'x2')
	for i in a:
		x1= i % 50
		x2= int(i/50)
		print (x1, x2)
	
	

index_2coor(b)




	
