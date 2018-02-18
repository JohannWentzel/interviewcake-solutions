def makeDenominations(amount, denoms):
	
	waysToCreate = [0] * (amount + 1)
	waysToCreate[0] = 1

	for coin in denoms:
		# print("Working with coin value ", coin)
		for higherAmount in range(coin,amount + 1):
			# print("higherAmount = ", higherAmount)
			# print("adding to index", higherAmount, "with waysToCreate[", (higherAmount-coin),"] = ", waysToCreate[higherAmount-coin])
			waysToCreate[higherAmount] += waysToCreate[higherAmount - coin]
	
	return waysToCreate


		
	
if __name__ == '__main__':
	amount = 4
	answer = makeDenominations(amount, [1,2,3])
	print(answer)
	print("Final answer: ", answer[amount])



