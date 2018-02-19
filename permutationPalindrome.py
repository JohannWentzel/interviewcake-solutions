def permIsPalindrome(string):
	unmatched = set()

	for c in string:
		if c.lower() in unmatched:
			unmatched.remove(c.lower())
		else:
			unmatched.add(c.lower())

	return len(unmatched) <= 1

if __name__ == '__main__':
	string1 = "civic"
	string2 = "ivicc"
	string3 = "civil"
	string4 = "livci"

	print(permIsPalindrome(string1))
	print(permIsPalindrome(string2))
	print(permIsPalindrome(string3))
	print(permIsPalindrome(string4))
