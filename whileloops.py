

def count_down(beginning):
	while beginning < 11 and beginning > -1:
		print beginning
		beginning -= 1


def counter(x):
	if x > 0:
		while x > 0:
			print x
			x -= 1
	
	elif x < 0:
		while x < 0:
			print x
			x += 1

#def addup(x):
#	while x


def countFrom(beginning, end):
	if beginning > end:
		while beginning > end:
			print beginning
			beginning -= 1
	
	elif beginning < end:
		while beginning < end:
			print beginning
			beginning += 1

def sumOfOdds(x):
	total = 0
	if x > 0:
		while x > 0:
			if not x % 2 == 0:
				total += x
			else:
				pass
			x -= 1
	
	elif x < 0:
		while x < 0:
			if not x % 2 == 0:
				total += x
			else:
				pass
			x += 1
	

	print total


		

			


	


def main():
#	count_down(10)
#	counter(5)
	sumOfOdds(9)

main()
