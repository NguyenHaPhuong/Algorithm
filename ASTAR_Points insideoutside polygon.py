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