variables_table = []

class DependencyTree: 
	def __init__(s):
		self.root = "is"

	def generate():
		if self.subject.isUniversal():
			outputUniversal()

class Sentence: 
	def __init__(subject, verb, predicative):
		self.subject = subject
		self.verb = verb
		self.predicative = predicative

	def generate():
		if subject.isUniversal():
			print("\\forall")

class Quantifier: 
	def __init__(name, formula, root):
		self.name = name
		self.formula = formula
		self.root = root

	def getName():
		return self.name

	def lpn():

	def generate():
		noun = self.lpn()
		variables = variables_table[noun]
		name = self.getName()
		output(name)
		output(formula)

class Term: 