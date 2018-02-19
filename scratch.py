def setsThatAddTo(target, given_nums, i, chosen_nums):

	if target == 0:
	 	sets.append(chosen_nums)
	 	return 1

	elif target < 0:
		return 0

	elif i < 0:
		return 0

	elif target < given_nums[i]:
		return setsThatAddTo(target, given_nums, i - 1, chosen_nums)

	else:
		return setsThatAddTo(target - given_nums[i], given_nums, i - 1, chosen_nums + [given_nums[i]]) + setsThatAddTo(target, given_nums, i - 1, chosen_nums)



if __name__ == '__main__':
	nums = [2,4,6,10]
	target = 16
	sets = []
	print(setsThatAddTo(target, nums, len(nums) - 1, []))
	print(sets)