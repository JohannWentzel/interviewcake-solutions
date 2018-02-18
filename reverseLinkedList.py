class LinkedListNode:

	def __init__(self, value):
		self.value = value
		self.next  = None

	def print(self):
		current = self
		while current != None:
			print(current.value)
			current = current.next

	def reverse(self):
		if self.next == None:
			return self

		currentNode = self
		previousNode = None
		twoBack = None

		while currentNode != None:
			if previousNode != None:
				previousNode.next = twoBack

			twoBack = previousNode
			previousNode = currentNode
			currentNode = currentNode.next

		previousNode.next = twoBack
		return previousNode




if __name__ == '__main__':
	a = LinkedListNode("A")
	b = LinkedListNode("B")
	c = LinkedListNode("C")

	a.next = b
	b.next = c

	print("NORMAL:")
	a.print()

	reversedHead = a.reverse()

	print("REVERSED:")
	reversedHead.print()


