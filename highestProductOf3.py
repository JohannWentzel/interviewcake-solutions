
def highestProductOf3_bruteforce(nums):
	maxProd = float("-inf")

	for i in range(len(nums)):
		for j in range(len(nums)):
			if j != i:
				for k in range(len(nums)):
					if k != j and k != i:
						maxProd = max(maxProd, nums[i] * nums[j] * nums[k])

	return maxProd

def highestProductOf3(nums):

	if len(nums) < 3:
		return

	highest = max(nums[0], nums[1])
	lowest = min(nums[0], nums[1])

	highestProd2 = nums[0] * nums[1]
	lowestProd2 = nums[0] * nums[1]

	highestProd3 = nums[0] * nums[1] * nums[2]

	for i in range(2, len(nums)):
		current = nums[i]

		highestProd3 = max(highestProd3, highestProd2 * nums[i], lowestProd2 * nums[i])

		# otherwise update vals for next iteration

		highestProd2 = max(highestProd2, current * highest, current * lowest)
		lowestProd2 = min(lowestProd2, current * highest, current * lowest)

		highest = max(highest, current)
		lowest = min(lowest, current)

	return highestProd3


if __name__ == '__main__':

	nums = [1,2,3,4,5,6]

	print "Iterative: ", highestProductOf3(nums)

	print "Brute force: ", highestProductOf3_bruteforce(nums)