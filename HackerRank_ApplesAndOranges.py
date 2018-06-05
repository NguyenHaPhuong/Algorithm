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


