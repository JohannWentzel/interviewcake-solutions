def sort_scores(unsorted_scores, highestPossible):
	scoreStorage = [0] * (highestPossible + 1)
	finalScores = []

	for score in unsorted_scores:
		scoreStorage[score] += 1

	for i in range(len(scoreStorage)-1, -1, -1):
		if scoreStorage[i] > 0:
			for time in range(scoreStorage[i]):
				finalScores.append(i)

	return finalScores



if __name__ == '__main__':
	unsorted_scores = [37, 89, 41, 65, 91, 53, 41]
	HIGHEST_POSSIBLE_SCORE = 100

	sortedScores = sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE)
	print(sortedScores)
# returns [91, 89, 65, 53, 41, 37]