def mergeSortedLists(list1, list2):

	list1Current = 0
	list2Current = 0
	mergedListsCurrent = 0

	mergedLists = [None] * (len(list1) + len(list2))

	while mergedListsCurrent < len(mergedLists):
		if list1Current < len(list1) and list2Current < len(list2):
			if list1[list1Current] <= list2[list2Current]:
				mergedLists[mergedListsCurrent] = list1[list1Current]
				list1Current += 1
				mergedListsCurrent += 1
			else:
				mergedLists[mergedListsCurrent] = list2[list2Current]
				list2Current += 1
				mergedListsCurrent += 1

		elif list1Current < len(list1):
			mergedLists[mergedListsCurrent] = list1[list1Current]
			list1Current += 1
			mergedListsCurrent += 1

		else:
			mergedLists[mergedListsCurrent] = list2[list2Current]
			mergedListsCurrent += 1
			list2Current += 1

	return mergedLists

if __name__ == '__main__':
	my_list     = [3, 4, 6, 10, 11, 15]
	alices_list = [1, 5, 8, 12, 14, 19]

	print(mergeSortedLists(my_list, alices_list))
	# prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19