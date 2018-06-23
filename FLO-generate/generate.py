variables_table = {}
stack = []

class DependencyTree: 
	def __init__(self, s):
		self.root = Root("is")
		self.subject = Expression("every student at STU")
		self.predicative = Expression("smart")

	def generate(self):
		if self.subject.isUniversal():
			self.subject.generateUniversal()
			print("\\Rightarrow")
			# self.

class Expression: 
	def __init__(self, s):
		self.text = s

class Universal(Expression):
	def __init__(self, s):
		self.text = s
		self.type = "Universal"
		self.noun = "student"
		self.attributes = ["at STU"]

	def generate(self):
		print("\\forall")
		t = len(variables_table)
		variables_table[noun] = "x_%d"%t
		self.attributes.generate()

# s = str(input())
# tree = DependencyTree(s)
# tree.generate()

class Term(Expression): 
	def __init__(self, s):
		self.type = "Term"
		self.text = s

class Constant(Term): 
	def generate(self):
		print(self.text)

class Variable(Term): 
	def __init__(self, s):
		self.type = "Term"
		self.text = s
		self.addName()

	def addName(self):
		t = len(variables_table)
		name = "x_%d"%t
		variables_table[self.text] = name
		stack.append(name)
		return

	def generate(self):
		# try:
		# 	print(variables_table[self.text])
		# except:
		# 	self.addName()
		print(variables_table[self.text])
		return

class Function(Term): 
	def __init__(self, s, terms):
		self.terms = terms
		self.type = "Term"
		self.text = s

	def generate(self):
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
	def __init__(self, s, terms):
		self.text = s
		self.terms = terms
		self.type = "Predicate"

	def generate(self):
		outputSymbol(self.text)
		print("(")
		for term in self.terms[: -1]:
			term.generate()
			print(", ")
		a = self.terms[-1]
		a.generate()
		print(")")
		return

class Equality(Formula): 
	def __init__(self, s, t1, t2):
		self.text = s
		self.t1 = t1
		self.t2 = t2

	def generate(self):
		t1.generate()
		print(" = ")
		t2.generate()

class Negation(Formula): 
	def __init__(self, f):
		self.f = f

	def generate(self):
		print("\\neg ")
		formula = self.f
		formula.generate()

class Quantifier(Formula): 
	def __init__(self, type1, f):
		# self.text = s
		self.type = type1
		self.f = f

	def generate(self):
		if self.type == "Universal":
			print("\\forall")
		else:
			print("\\exists")
		variable = stack[-1]
		print(variable)
		f = self.f
		f.generate()
		return

class BinaryConnective(Formula): 
	def __init__(self, s, type1, f1, f2):
		self.text = s
		self.type = type1
		self.f1 = f1
		self.f2 = f2

	def generate(self):
		f1.generate()
		print(type)
		f2.generate()
		return

def outputSymbol(s):
	print("\\text{" , s, "}")
	return

f = Quantifier("Universal", Predicate("Smart", [Variable("student")]))
f.generate()