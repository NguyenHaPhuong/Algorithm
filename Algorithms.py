

# Challenge 2:
def solve(a0, a1, a2, b0, b1, b2):
 
		alice = 0
		bob = 0
		a=[a0,a1,a2]
		b=[b0,b1,b2]
		for i in range(len(a)):
			if a[i] >b[i]:
				alice+=1
			elif a[i]<b[i]:
				bob +=1
		
		return(alice, bob)
						
print(solve(5,6,7,3,6,10))


# Challenge 3:
def aVeryBigSum(n, ar):
	a=0
	for i in list(range(n)):
		a= a+ar[i]
	
	return a
		
print (aVeryBigSum(5,[1000000001, 1000000002, 1000000003, 1000000004, 1000000005]))



# Challenge 4:
def diagonalDifference(a):
	e=0
	b=0
	for i in range(len(a)):
		e= e+a[i][i]
		b= b+a[i][-(i+1)]
		d= abs(e-b)
	return d
	
print (diagonalDifference([[11,2,4],[4,5,6],[10,8,-12]]))



# Challenge 5:			
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



# Challenge 5:
def staircase(n):
	for i in range(n+1):
		if i != 0:
			a= " "*(n-i)+"#"*i
			print (a)
		
staircase(5)


# Challenge 6:
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
	
a=[[4,8,2],[4,5,7],[6,1,6]]


def sum_arr(arr):
	list_arr=[]
	for i in range(len(arr)):
		
		b=0
		for e in range(len(arr[i])):
			b+=arr[i][e]
		list_arr.append(b)
	return (list_arr)
	
list_sum=[]	
def diagonalDifference(a):
	e=0
	b=0
	list_dia=[]
	for i in range(len(a)):
		e= e+a[i][i]
		b= b+a[i][-(i+1)]
	
	if e!= b:
		list_sum.append(e)
		list_sum.append(b)
	else:
		list_sum.append(e)
	
	
def sum_col(list):
	list_col=[]
	for i in range(len(list[0])):
		d=0
		for e in range(len(list)):
			d+=list[e][i]
		list_col.append(d)
	return(list_col)

list_list=[]
	
list_list.append(sum_arr(a))
list_list.append(sum_col(a))



for i in range(len(list_list)):
	for x in range(len(list_list[i])):
		if list_list[i][x] not in list_sum:
			list_sum.append(list_list[i][x])


d=0
for i in list_sum:
	c= abs(15-i)
	d+=c
print (list_sum)

print(list_list)	
print (d)

#Challenge 7:

scores= [100,100,50,40,40,20,10]
alice= [5,25,50,120]

new_score=[]
for a in scores:
	if a not in new_score:
		new_score.append(a)
print (new_score)

for i in (alice):
	for x in range(len(new_score)):
		if i < new_score[x]:
			c=x+2
		elif i == new_score[x]:
			c=x+1
		elif i>new_score[0]:
			c=1
	print (c)
	

#Challenge 8:
def birthdayCakeCandles(n, ar):
	a= ar[0]
	for i in range(n):
		if a<ar[i]:
			a=ar[i]
			
	count=0
	for x in ar:
		if a == x:
			count+=1
			
	return (count)
	
	
print (birthdayCakeCandles(7,[8,5,6,8, 2, 1, 8]))

#Challenge 9:
def timeConversion(s):
	if s[-2:]=="PM":
		if s[:2]=='12':
			b=s.strip('PM')
		else:
			c= int(s[:2])+12
			b= str(c)+s[2:8]
	else:
		if s[:2]!='12':
			b=s.strip('AM')
		else:
			b= '00'+s[2:8]
			
	return (b)
	
	
print(timeConversion('12:05:45AM'))
		
		
#Challenge 10:
def gradingStudents(grades):
	for i in grades:
		if i >=38:
			if i%5 >2:
				i=i+ (5- i%5)
		
		print (i)
		
				
a=gradingStudents([73,67,38,33])



#Challenge 11:

def countApplesAndOranges(s, t, a, b, apples, oranges):
	count1=0
	count2=0
	for i in apples:
		c= a + i
		if c in range(s,t+1):
			count1+=1
	
	for x in oranges:
		d= b+ x
		if d in range(s,t+1):
			count2+=1
			
	print(count1)
	print(count2)
				
countApplesAndOranges(7, 11, 5, 15, [-2,2,1], [5,-6])

#Challenge 12:

def kangaroo(x1, v1, x2, v2):
	if v2>= v1:
		return ("NO")
		
	else:
		c= x1
		d= x2
		b=0
		for i in range(10):
			c+=v1
			d+=v2
			if d == c:
				b+=1
			
		if b!= 0:
			return("YES")
			
		else:
			return("NO")
				
a= kangaroo(0,6,5,2)
print(a)





##########################################################################


#Q1:

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

#Q3:
def right_sum(m,n,s):
	a=0
	for i in range(m+1):
		a+=i
	b=s-a	
	for x in range(n):
		
#Q7:

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


#Q8:



#Part b)
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


#Q9:
	
		
import itertools

m = int(input("Enter the number of test: "))

bits = []

for _ in range(m):
	bits.append(list(map(int, input().rstrip().split())))

def main(n):
	a= itertools.product([0, 1], repeat=n)
	b= list(a)
	for i in b:
		c=''
		for x in range(n):
			c+= str(i[x])
		
		print (c)

for i in bits:
	for x in i:
		main(x)

	
