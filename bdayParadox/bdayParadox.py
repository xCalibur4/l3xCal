from random import randint

success = 0

def main():
	N = int(raw_input("Enter number of people: "))
	T = int(raw_input("Enter number of trials to perform: "))
	# Perform T trials
	for i in range(T):
		perform_simulation(N,i+1)
	ans = math_bday_par(N)
	print "\n\nTotal trials conducted = %d" %T
	print "Successful trials = %d" %success
	print "Probability 2 or more persons have the same bday (Using simulation) = %f %%" %((success/float(T)) * 100.0)
	print "\nExpected probability (Using the mathematical formula) = %f %% \n\n" %ans


# P(N) = 1 - permute(365,N)/pow(365,N)
def math_bday_par(N):
	num = 1
	for i in range(365 - N + 1, 366):
		num *= i
	for i in range(N):
		num = num/365.0
	return (1.0 - num) * 100



def perform_simulation(N,t):
	global success
	# Generate a list of N random numbers between 1 and 365 denoting random bdays of different people
	bday_list = []
	unique_bdays = True
	for i in range(N):
		bday_list.append(randint(1,365))
	print bday_list
	# Check if more than 2 people have the same bdays
	for bday in bday_list:
		if bday_list.count(bday) > 1 :
			success += 1
			unique_bdays = False
			break
	if unique_bdays == False:
		print "Trial %d : Success" %t
	else:
		print "Trial %d : Failure" %t

if __name__ == '__main__':
	main()