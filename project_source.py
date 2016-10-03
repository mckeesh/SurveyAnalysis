class ProjectSource:
	options = ["open source", "closed source", "both open and closed source", "Not Specified"]
	type_ = "Project Source Type"

	def __init__(self, source):
		self.value = ProjectSource.options[int(source)-1]

	def __eq__(self, other):
		return self.value == other.value

	def __str__(self):
		return self.value

	def getActive(self):
		return [str(self)]