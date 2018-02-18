def stealCakes(cakes, capacity):

	maxValueAtCapacity = [0] * (capacity + 1)

	for i in range(0, capacity + 1):
		for cakeWeight, cakeValue in cakes:
			if (cakeWeight <= i):
			# print("checking",i)
				maxValueAtCapacity[i] = max(maxValueAtCapacity[i], maxValueAtCapacity[i - cakeWeight] + cakeValue)

	return maxValueAtCapacity[capacity]
	

if __name__ == '__main__':
	cakes = [(3, 40), (5, 70)]
	capacity = 9
	print(stealCakes(cakes,capacity))