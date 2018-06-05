
# You are given the following Python list of integers. By looping through the list, write code to determine and display the number of integers in the list which are less than 25.

listNum = [23,34,15,22,46,27,18]
count = 0
for i in listNum:
    if i < 25:
        print (i)
        count = count +1
print (count) 
