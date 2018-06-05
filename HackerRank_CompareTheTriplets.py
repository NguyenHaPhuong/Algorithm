# Challenge 2:
# Compare the scores of Bob and Alice. The input is the scores of Alice and Bob. 
# If score of Alice is higher than score of Bob, Alice gets 1 point and vice versa. If score of Alice is equal Bob's one then neither person receives a point. 
# Input "a0" "a1" "a2" are the scores of Alice and "b0" "b1" "b2" are the scores of Bob
# The output is the points of Alice and Bob. 


def solve(a0, a1, a2, b0, b1, b2):
 
		alice = 0
		bob = 0
		a=[a0,a1,a2]
		b=[b0,b1,b2]
		for i in range(len(a)):
			if a[i] >b[i]:
				alice+=1
			elif a[i]<b[i]:
				bob +=1
		
		return(alice, bob)
						
print(solve(5,6,7,3,6,10))
