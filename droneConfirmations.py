def returnNonDuplicate(nums):
	unique = 0

	for num in nums:
		# ^= is a XOR operator. Because we know we're going to cancel out each integer by XORing it,
		# the only one left will be the one that only appears once!
		unique ^= num

	return unique

if __name__ == '__main__':
	delivery_id_confirmations = [3,2,5,7,2,5,7]
	print(returnNonDuplicate(delivery_id_confirmations))