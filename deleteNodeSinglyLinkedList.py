class LinkedListNode:

	def __init__(self, value):
	    self.value = value
	    self.next  = None

def delete_node(node):

	if node.next != None:
		node.value = b.next.value
		node.next = b.next.next

def printLinkedList(node):
	while node != None:
		print(node.value)
		node = node.next


if __name__ == '__main__':
	a = LinkedListNode('A')
	b = LinkedListNode('B')
	c = LinkedListNode('C')

	a.next = b
	b.next = c

	delete_node(b)
	printLinkedList(a)