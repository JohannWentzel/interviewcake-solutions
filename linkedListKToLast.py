class LinkedListNode:
	def __init__(self, value):
		self.value = value
		self.next  = None

def getKtoLast_iterative(k,head):
	if k < 1:
		return None

	current = head
	length = 1
	while current != None:
		current = current.next
		length += 1
	pos = 1
	current = head
	while current != None:
		if length - k == pos:
			return current
		current = current.next
		pos += 1

	return None

def getKtoLast_pointers(k,head):

	if k < 1:
		return None

	slow = head
	fast = head

	for i in range(k - 1):
		if not fast.next:
			return None

		fast = fast.next

	while fast.next != None:
		fast = fast.next
		slow = slow.next

	return slow

def getKtoLast_recursive(k, head):

	if k < 1:
		return None

	# Uses O(n) space on call-stack
	if head == None:
		return (0, None)

	pos, node = getKtoLast_recursive(k, head.next)

	if pos + 1 == k:
		return (pos + 1, head)

	return (pos + 1, node)

if __name__ == '__main__':
	
	a = LinkedListNode("Angel Food")
	b = LinkedListNode("Bundt")
	c = LinkedListNode("Cheese")
	d = LinkedListNode("Devil's Food")
	e = LinkedListNode("Eccles")

	a.next = b
	b.next = c
	c.next = d
	d.next = e

	_, found = getKtoLast_recursive(5, a)
	if found:
		print("Recursive:", found.value)
	else:
		print("Recursive: no match found")

	found = getKtoLast_iterative(5,a)
	if found:
		print("Iterative:", found.value)
	else:
		print("Iterative: no match found")

	found = getKtoLast_pointers(1,a)
	if found:
		print("Pointers:", found.value)
	else:
		print("Pointers: no match found")