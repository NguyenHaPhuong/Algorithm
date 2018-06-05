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