def fibonacci_topDown(target, cache):
	if target in cache:
		return cache[target]

	if target == 2: 
		return 2
	if target == 1:
		return 1
	
	result = fibonacci_topDown(target - 1, cache) + fibonacci_topDown(target - 2, cache)
	cache[target] = result

	return result

def fibonacci_bottomUp(target):

	if target < 0:
		return
	
	if target in [0,1]:
		return target

	twoBack = 0
	oneBack = 1

	for i in range(target - 1):
		result = twoBack + oneBack

		twoBack = oneBack
		oneBack = result

	return result

def fibonacci_naive(target):

	if target == 2: 
		return 2
	if target == 1:
		return 1
	
	result = fibonacci_naive(target - 1) + fibonacci_naive(target - 2)

	return result

if __name__ == '__main__':
	# print(fibonacci_topDown(500, {}))
	print(fibonacci_bottomUp(5))
	# print(fibonacci_naive(500))