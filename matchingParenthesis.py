def matchingParenthesis(string, parenIndex):

	openParensInFront = 0

	if string[parenIndex] != '(':
		raise ValueError("Index didn't point to an open paren.")

	index = parenIndex + 1
	while index < len(string):
		if string[index] == '(':
			openParensInFront += 1

		elif string[index] == ')' and openParensInFront == 0:
			return index

		elif string[index] == ')':
			openParensInFront -= 1

		index += 1
	return -1



if __name__ == '__main__':
	string = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."
	print(matchingParenthesis(string,10))