

# Challenge 2:
# Compare the scores of Bob and Alice. The input is the scores of Alice and Bob. 
# If score of Alice is higher than score of Bob, Alice gets 1 point and vice versa. If score of Alice is equal Bob's one then neither person receives a point. 
# Input "a0" "a1" "a2" are the scores of Alice and "b0" "b1" "b2" are the scores of Bob
# The output is the points of Alice and Bob. 


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
# This function is used to caculate the sum of the numbers that are in list. 
# Input: "n" is the integer, that is the number of numbers in list
#        "ar" is the list of numbers


def aVeryBigSum(n, ar):
	a=0
	for i in list(range(n)):
		a= a+ar[i]
	
	return a
		
print (aVeryBigSum(5,[1000000001, 1000000002, 1000000003, 1000000004, 1000000005]))



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



# Challenge 5: a function prints a staircase of size.
#Input Format: integer "n' denoting the size of the staircase.
# Output Format: Print a staircase of size n, using '#' symbols and spaces.
def staircase(n):
	for i in range(n+1):
		if i != 0:
			a= " "*(n-i)+"#"*i
			print (a)
		
staircase(5)


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
	


#Challenge 7:
#Alice is playing an arcade game and wants to climb to the top of the leaderboard.
#leaderboard works like this:
#1. The player with the highest score is ranked number 1 on the leaderboard.
#2. Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number.
#Input: 'scores' is the list of scores in leaderboard, and  'alice' is the list of scores of Alice after playing. 
def climbingLeaderboard(scores,alice):

	new_score=[]
	for a in scores:
		if a not in new_score:
			new_score.append(a)
	

	for i in (alice):
		for x in range(len(new_score)):
			if i < new_score[x]:
				c=x+2
			elif i == new_score[x]:
				c=x+1
			elif i>new_score[0]:
				c=1
		print (c)
	
climbingLeaderboard([100,100,55,50,45,40,40,20,10], [5,25,50,120])

#Explaination
#After Alice finishes 1st time, her score is 5 and her ranking is 8
#After Alice finishes 2nd time, her score is 25  and her ranking is 6......
#The out put is her rank after playing.
	


#Challenge 8:
#Alice is in-charge of the cake for her niece'sbirthday and have to decided the cake will have one candle for each year of her total age. When her niece blows out the candles, she’ll only be able to blow out the tallest ones. 
#So we need to find out how many candles she can successfully blow out.
#For example, if her niece is turning 4 years old, and the cake will have 4 candles of height 3,2 ,1 ,3 , she will be able to blow out 2 candles successfully, since the tallest candle is of height 3 and there are 2 such candles.
#Input: 'n' is the number of the candles and 'ar' is the array of height of candles.
#Output is the number of the candles she blow out successfully.
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
#Given a time in 12-hour AM/PM format, and we need to convert it to military (24-hour) time.
#Input: 's' is the a single string containing a time in 12-hour clock format (i.e.: hh:mm:ssAM or hh:mm:ssPM ), 
#where 01 =< hh =<12 and 00 =<mm,ss=<59.
#Output: print the given time in 24-hour format, where 00 =< hh =< 23.
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
#This function is used to round each student's  according to these rules:
#If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5 .
#If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade. Any grade less than 40 is a failing grade.
#Input is the list of grades.
#Output is rounded grade, that is printed line by line.
def gradingStudents(grades):
	for i in grades:
		if i >=38:
			if i%5 >2:
				i=i+ (5- i%5)
		
		print (i)
		
				
a=gradingStudents([73,67,38,33])



#Challenge 11:
# This function is used to determine how many apples and oranges will fall on Sam's house.
#s is Starting point of Sam's house location. 
#t is Ending location of Sam's house location. 
#a is Location of the Apple tree. 
#b is Location of the Orange tree. 
#"apples" is Distance at which each apple falls from the tree. 
#"oranges" is Distance at which each orange falls from the tree.
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

#The first apple falls at position 5-2=3. 
#The second apple falls at position 5+2=7. 
#The third apple falls at position 5+1=6. 
#The first orange falls at position 15+5=20. 
#The second orange falls at position 15-6=9. 
#Only one fruit (the second apple) falls within the region between 7 and 11, so we print 1 as our first line of output. 
#Only the second orange falls within the region between 7 and 11, so we print 1 as our second line of output.


