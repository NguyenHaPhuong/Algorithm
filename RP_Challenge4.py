# Write the code to find the MRT codes that starts with NS or EW or CC and has 1 or 2 digit(s). 

import re
listStrMRTCodes = ['NS15','EW4', 'NS234', 'CC8', 'D101', 'XY27', 'C400', 'EW32']
for i in listStrMRTCodes:
	result = re.search("^(NS|EW|CC)\d{1,2}$", i)
	if result != None:
		print (i)