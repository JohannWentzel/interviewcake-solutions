class TempTracker(object):
	"""docstring for TempTracker"""
	def __init__(self):
		super(TempTracker, self).__init__()
		self.recorded = [0] * 111
		self.mean = 0
		self.max = -999
		self.min = 999
		self.mode = 0
		self.entries = 0

	def insert(self,newTemp):
		# update hashmap
		self.recorded[newTemp] += 1

		if self.mode == None or self.recorded[newTemp] >= self.recorded[self.mode]:
			self.mode = newTemp


		# update mean
		self.entries += 1
		self.mean += ((newTemp - self.mean) / self.entries)

		# update max
		if newTemp > self.max:
			self.max = newTemp

		# update min

		if newTemp < self.min:
			self.min = newTemp

		

	def getMax(self):
		return self.max	

	def getMin(self):
		return self.min

	def getMean(self):
		return self.mean

	def getMode(self):
		return self.mode


if __name__ == '__main__':
	tracker = TempTracker()
	tracker.insert(2)
	tracker.insert(4)
	tracker.insert(4)
	tracker.insert(6)
	tracker.insert(10)
	tracker.insert(69)
	tracker.insert(69)

	print("Mean:", tracker.getMean())
	print("Mode: ", tracker.getMode())
	print("Max: ", tracker.getMax())
	print("Min:", tracker.getMin())
		