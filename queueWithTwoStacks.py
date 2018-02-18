class QueueWithTwoStacks(object):
	"""docstring for queueWithTwoStacks"""
	def __init__(self):
		super(QueueWithTwoStacks, self).__init__()
		self.normalStack = []
		self.flipStack = []
		
	def enqueue(self, number):
		self.normalStack.append(number)

	def dequeue(self):
		if len(self.flipStack) == 0:
			self.shiftToFlipStack()
		return self.flipStack.pop()

	def shiftToFlipStack(self):
		while len(self.normalStack) > 0:
			self.flipStack.append(self.normalStack.pop())

if __name__ == '__main__':
	stack = QueueWithTwoStacks()
	stack.enqueue(1)
	stack.enqueue(2)
	stack.enqueue(3)
	stack.enqueue(4)
	print(stack.dequeue())
	print(stack.dequeue())
	print(stack.dequeue())
	stack.enqueue(5)
	stack.enqueue(6)
	print(stack.dequeue())
	stack.enqueue(7)
	print(stack.dequeue())
	print(stack.dequeue())
	print(stack.dequeue())

