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