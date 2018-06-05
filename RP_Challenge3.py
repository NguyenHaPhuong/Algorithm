
# writing a code to generate passwords. Essentially each generated password consists of a combination of random letters and numbers. 

#new password for Technical Support Staff: 
#(randomly pick a password from a given list of passwords ["passOne", "TwoPass", "3PassWord"]

#new password for Other Employees, with the following conditions:
#All passwords must consist of a combination of random lower and/or uppercase alphabets, with a random number at the end
#The random number must be 2 digits long

#new password for Upper Management Staff
#The password is 10 characters long
#The password starts with a random combination of lower and/or uppercase alphabets
#The password continues with an English word (at most six letters long) randomly selected from a given list of words between four to six letters
#The password must end with 1 digit at the back


import random 
import string

def functionP (password):
    n = len(password)
    g = random.randint(0, n-1)
    strPassword = password[g]
    return strPassword

def functionH(length):
    strNewPassword =''
    intNumAlpha = length - 2
    Alpha = string.ascii_letters
    strRanNum1 = str(random.randint(0,9))
    strRanNum2 = str(random.randint(0,9))
    
    for i in range(intNumAlpha):
        intIndex = random.randint(0,51)
        strNewPassword += Alpha[intIndex]
    strNewPassword += strRanNum1 + strRanNum2
    return strNewPassword

def functionU(EngWord):
    strNewUPpassword =''
    u = random.randint(0, len(EngWord) -1)
    strEngWord= EngWord[u]
    intNumAlpha = 10 - len(strEngWord) - 1
    strRanNum = str(random.randint(0,9))   
    Alpha = string.ascii_letters
    for i in range(intNumAlpha):
        intIndex1 = random.randint(0,51)
        strNewUPpassword += Alpha[intIndex1]
    strNewUPpassword += strEngWord + strRanNum
    return strNewUPpassword

    
Choice = ''
while Choice != '-1': 
    print ('enter 1 to generate new password for Technical Support Staff')
    print ('enter 2 to generate new password for Other Employees')
    print ('enter 3 to generate new password for Upper Management Staff')
    print ('enter -1 to Quit')
    print ('#'*50)

    Choice = input('Enter choices:')

    if Choice == '1':
            listPass =['passOne','passTwo','3passWord','pass4']
            print (functionP(listPass))
        
    elif Choice == '2':
        print (functionH(6))
        print (functionH(8))
        print (functionH(10))
        
    elif Choice == '3':
                listWord= [ 'Pizza', 'Coffe','Space', 'Sky', 'World', 'Country']
                print ('The new password is' , functionU(listWord))
