class Experience:
	type_ = "experience"
	options = ["1-5 years",
				"6-10 years",
				"11-15 years",
				"16-20 years",
				"20-25 years",
				"26+ years"
				]
	def __init__(self, exp):
		if exp != '':
			self.value = int(exp)
		else:
			self.value = None

	def getActive(self):
		return [self.readable()]

	def __eq__(self, other):
		return self.value == other.value

	def __str__(self):
		return "<Experience object>: %s" % self.readable()

	def readable(self):
		return Experience.options[self.value-1]