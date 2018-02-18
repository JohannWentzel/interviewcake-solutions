def rotationPoint(words):
	low = 0
	high = len(words) - 1
	index = (low + high) // 2

	while low <= high:
		index = (low + high) // 2

		if words[index] < words[index - 1]:
			return index

		if words[index] < words[low]:
			high = index
		else: 
			low = index

	return index

if __name__ == '__main__':
	words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote',  # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
	]

	print(rotationPoint(words))