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