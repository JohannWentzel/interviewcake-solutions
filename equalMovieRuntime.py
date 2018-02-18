def sumPair(movies,flightLength):
	complements = {}
	for movieLength in movies:
		if movieLength in complements:
			return True
		else:
			complements[flightLength - movieLength] = movieLength

	return False

if __name__ == '__main__':

	movies = [120,60,80,90,200,50,70]
	flightLength = 260
	print(sumPair(movies,flightLength))