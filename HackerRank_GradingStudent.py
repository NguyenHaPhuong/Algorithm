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