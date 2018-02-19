def listDuplicate(given_nums):
	slow = given_nums[-2]
	fast = slow

	slow = given_nums[slow - 1]
	fast = given_nums[given_nums[fast - 1] - 1]

	print("Slow =",slow,", fast =",fast)

	while slow != fast:
		

		slow = given_nums[slow - 1]
		fast = given_nums[given_nums[fast - 1] - 1]
		print("Slow =",slow,", fast =",fast)

	return slow

if __name__ == '__main__':
	nums = [3,5,2,1,4,5]
	print(listDuplicate(nums))