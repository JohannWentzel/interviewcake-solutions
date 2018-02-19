import random

def shuffleInPlace(inputList):
	firstIndexInNonShuffledList = 0

	while firstIndexInNonShuffledList < len(inputList):

		randomIndex = random.randint(firstIndexInNonShuffledList,len(inputList) - 1)

		inputList[firstIndexInNonShuffledList], inputList[randomIndex] = inputList[randomIndex], inputList[firstIndexInNonShuffledList]

		firstIndexInNonShuffledList += 1

	return inputList


if __name__ == '__main__':
	inputList = [1,2,3]
	print(shuffleInPlace(inputList))