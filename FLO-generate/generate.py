variables_table = {}

class DependencyTree: 
	def __init__(s):
		self.root = Root("is")
		self.subject = Expression("every student at STU")
		self.predicative = Expression("smart")

	def generate():
		if self.subject.isUniversal():
			self.subject.generateUniversal()
			print("\\Rightarrow")
			# self.

class Expression: 
	def __init__(s):
		self.text = s

class Universal(Expression):
	def __init__(s):
		self.text = s
		self.type = "Universal"
		self.noun = "student"
		self.attributes = ["at STU"]

	def generate():
		print("\\forall")
		t = len(variables_table)
		variables_table[noun] = "x_%d"%t
		self.attributes.generate()

s = str(input())
tree = DependencyTree(s)
tree.generate()

class Term(Expression): 
	def __init__(s):
		self.type = "Term"
		self.text = s

class Constant(Term): 
	def generate():
		print(self.text)

class Variable(Term): 
	def addName():
		t = len(variables_table)
		variables_table[self.text] = "x_%d"%t
		return

	def generate():
		print(variables_table[self.text])
		return

class Function(Term): 
	def __init__(s, terms):
		self.terms = terms
		self.type = "Term"
		self.text = s

	def generate():
		outputSymbol(self.text)
		print("(")
		for term in self.terms[: -1]:
			term.generate()
			print(", ")
		term.generate()
		print(")")

class Formula(Expression): 
	# def __init__(s):
	# 	self.type = "Formula"
	# 	self.text = s
	pass

class Predicate(Formula): 
	def __init__(s, terms):
		self.text = s
		self.terms = terms
		self.type = "Predicate"

	def generate():
		outputSymbol(self.text)
		print("(")
		for term in self.terms[: -1]:
			term.generate()
			print(", ")
		term.generate()
		print(")")
		return

class Equality(Formula): 