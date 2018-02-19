def reverseStringInPlace(myStr):
	charSet = list(myStr)
	start = 0
	end = len(charSet) - 1

	while start <= end:

		temp = charSet[start]
		charSet[start] = charSet[end]
		charSet[end] = temp

		start += 1
		end -= 1

	return "".join(charSet)

if __name__ == '__main__':
	string = "Johann"
	print(reverseStringInPlace(string))
