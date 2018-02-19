def validateBrackets(inputString):
	openers = "{[("
	closers = "}])"

	openersUsed = []

	mapping = {
		"}": "{",
		"]": "[",
		")": "("
	}

	for char in inputString:
		if char in openers:
			openersUsed.append(char)

		elif char in closers:
			if len(openersUsed) == 0:
				return False

			lastOpener = openersUsed.pop()
			if mapping[char] != lastOpener:
				return False

	return len(openersUsed) == 0



if __name__ == '__main__':
	test1 = "{ [ ] ( ) }"
	test2 = "{ [ ( ] ) }" 
	test3 = "{ [ }"

	print(validateBrackets(test1))
	print(validateBrackets(test2))
	print(validateBrackets(test3))