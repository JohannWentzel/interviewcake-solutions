def isSingleRiffle(shuffled_deck, half1, half2):

	deckIndex = 0
	half1Index = 0
	half2Index = 0

	while deckIndex < len(shuffled_deck):
		if half1Index < len(half1) and shuffled_deck[deckIndex] == half1[half1Index]:
			half1Index += 1
			deckIndex += 1	
		elif half2Index < len(half2) and shuffled_deck[deckIndex] == half2[half2Index]:
			half2Index += 1
			deckIndex += 1
		else:
			return False 

	return True


if __name__ == '__main__':
	half1 = [1,5,26,31,44,7,2]
	half2 = [3,7,46,52,31,2,6]

	shuffled_deck = [1,5,26,31,44,7,2,3,7,46,52,31,2,6]

	print(isSingleRiffle(shuffled_deck,half1,half2))