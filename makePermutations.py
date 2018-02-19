def makePermutations(string):
	if len(string) <= 1:
		return set([string])

	allCharsExceptLast = string[:-1]
	last = string[-1]

	permsOfAllButLast = makePermutations(allCharsExceptLast)

	perms = set()

	for perm in permsOfAllButLast:
		for position in range(len(allCharsExceptLast) + 1):
			permToAdd = perm[:position] + last + perm[position:]
			perms.add(permToAdd)


	return perms

if __name__ == '__main__':
	string = "abcd"
	
	print(makePermutations(string))