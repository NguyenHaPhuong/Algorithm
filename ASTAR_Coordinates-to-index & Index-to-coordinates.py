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