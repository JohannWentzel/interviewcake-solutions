def reverse_words(message):
	message = message.split(' ')
	leftIndex = 0
	rightIndex = len(message) - 1

	while leftIndex < rightIndex:
		message[leftIndex], message[rightIndex] = message[rightIndex], message[leftIndex]
		leftIndex += 1
		rightIndex -= 1

	return " ".join(message)

def reverse_words_nopython(message):
	# the solution they intended, since Python is basically cheating at code.

	charSet = list(message)
	charSet = reverseCharacters(charSet, 0, len(message) - 1)

	wordStartIndex = 0
	wordEndIndex = 0

	while wordEndIndex <= len(charSet):
		if wordEndIndex == len(charSet) or charSet[wordEndIndex] == " ":
			charSet = reverseCharacters(charSet,wordStartIndex, wordEndIndex - 1)
			wordStartIndex = wordEndIndex + 1

		wordEndIndex += 1

	return ''.join(charSet)

def reverseCharacters(charSet, start, end):

	while start < end:

		temp = charSet[start]
		charSet[start] = charSet[end]
		charSet[end] = temp

		start += 1
		end -= 1

	return charSet

if __name__ == '__main__':
	message = 'find you will pain only go you recordings security the into if'
	print(reverse_words_nopython(message))