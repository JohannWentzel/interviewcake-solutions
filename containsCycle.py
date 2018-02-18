class LinkedListNode:

	def __init__(self, value):
	    self.value = value
	    self.next  = None

def containsCycle_pointers(head):

	# O(1) space!
	
	dummy = LinkedListNode(None)
	dummy.next = head
	if dummy.next == None or dummy.next.next == None:
		return False

	slow = dummy.next
	fast = dummy.next.next

	while fast.next != None:
		if slow.value == fast.value:
			return True

		slow = slow.next
		fast = fast.next.next

	return False


def containsCycle_dict(head):
	# O(n) space
	nodesSeen = set()

	current = head

	while current != None:
		if current.value in nodesSeen:
			return True
		nodesSeen.add(current.value)
		current = current.next

	return False

if __name__ == '__main__':
	a = LinkedListNode("A")
	b = LinkedListNode("B")
	c = LinkedListNode("C")
	d = LinkedListNode("D")
	a.next = b
	b.next = c
	c.next = d
	d.next = b
	# d.next = c

	print("Check using a set:", containsCycle_dict(a))
	print("Check using pointers:", containsCycle_pointers(a))