def makeWordCloud(inputString):
	alphabet = "qwertyuiopasdfghjklzxcvbnm-"
	wordData = {}

	#not gonna use .split() since we need to parse out punctuation

	wordStartIndex = 0

	for i in range(len(inputString)):
		if inputString[i].lower() not in alphabet or i == len(inputString):
			word = ''.join(inputString[wordStartIndex:i]).lower()

			if len(word) > 0:
				if word in wordData:
					wordData[word] += 1
				else:
					wordData[word] = 1

			wordStartIndex = i + 1

	return wordData

if __name__ == '__main__':
	string = 'We came, we saw, we conquered...then we ate Bill\'s (Mille-Feuille) cake.'
	print(makeWordCloud(string))