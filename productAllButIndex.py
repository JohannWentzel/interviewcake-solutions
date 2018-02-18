def productAllButIndex(nums):

	ret = [None] * len(nums) 

	productSoFar = 1

	for i in range(len(nums)):
		ret[i] = productSoFar
		productSoFar *= nums[i]


	productSoFar = 1
	for i in range(len(nums) - 1, -1, -1):
		ret[i] *= productSoFar
		productSoFar *= nums[i]

	return ret

if __name__ == '__main__':
	print productAllButIndex([1,7,3,4])



# 1, 7, 3, 4
# 1*7*3*4, 1*1*3*4, 1*7*1*4, 1*7*3*1