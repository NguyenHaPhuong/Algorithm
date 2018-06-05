import random
import string
# Write the code to pick randomly the word which is in list 'List'
List = [ 'asg', 'asgdrte', 'asgetg']
u = random.randint(0,2)
print (List[u])

# Write the function named "getEmail" with two arguments which is user name and server nameto create the email. Write the code to test your function in which username is your student id, the server name is myrp.edu.sg
def getEmail(user, server):
    return str(user)+ "@" + str(server)
print (getEmail('15015824', 'myrp.edu.sg'))

#Use while loop to print the input if the input not equal 'q', if input equal 'q' print "Bye!"
a= ''

while a!='q':
	print (a)
	a = input("Enter input: ")
print ("Bye!")