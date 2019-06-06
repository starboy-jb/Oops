class Employee:
	increment = 3
	totalEmp = 0
	def __init__(self, firstName, secondName, salary):
		self.firstName = firstName
		self.secondName = secondName
		self.salary = int(salary)
		Employee.totalEmp += 1

	def increase(self):
		self.salary = int(self.salary * Employee.increment)

	@property
	def email(self):
		if (self.firstName == None):
			return "No email is found"
		return self.firstName + "." + self.secondName + "@gmail.com"

	@email.setter
	def email(self, given_email):
		name_list = given_email.split('@')[0].split('.')
		self.firstName = name_list[0]
		self.secondName = name_list[1]

	@email.deleter
	def email(self):
		self.firstName = None
		self.secondName = None
		
	@classmethod
	def change_increment(cls, rate):
		cls.increment = rate

	@classmethod
	def from_str(cls, emp_string):
		firstName, secondName, salary = emp_string.split('-')
		return cls(firstName, secondName, salary)

	@staticmethod
	def isOpen(day):
		if day == 'sunday':
			return False
		else:
			return True
	def __add__(self, other):
		return self.salary + other.salary

	def __repr__(self):
		return 'Employee({}, {}, {})'.format(self.firstName, self.secondName, self.salary)

	def __str__(self):
		return 'Employee name is {} {}'.format(self.firstName, self.secondName)


# class Programmar(Employee):
# 	"""docstring for Programmar"""
# 	def __init__(self, firstName, secondName, salary, pLang, exp):
# 		super().__init__(firstName, secondName, salary)
# 		self.pLang = pLang
# 		self.exp = str(exp) + ' yrs'

# starboy = Programmar('Jyotish', 'Bhaskar', 3, 'C++', 2)
# print(starboy.firstName, starboy.secondName, starboy.pLang, starboy.exp, sep='\n')		

# print(Employee.isOpen('sunday'))
# fastboot = Employee('Pranjal', 'Mishra', 3)
# lowjack = Employee.from_str('Harshit-Gupta-3')
# print(lowjack.firstName, lowjack.secondName, lowjack.salary, lowjack.email)
# print(fastboot.firstName, fastboot.secondName, fastboot.salary, fastboot.email)
# fastboot.email = "anything.Mishra@gmail.com"
# print(fastboot.firstName, fastboot.secondName, fastboot.salary, fastboot.email)
# print(fastboot.firstName, fastboot.secondName, fastboot.salary, fastboot.email)
# print(lowjack + fastboot)
# print(repr(fastboot))
# print(str(fastboot))
# print(starboy.firstName, starboy.secondName, starboy.salary)
# Employee.change_increment(10)
# starboy.increase()
# print(starboy.firstName, starboy.secondName, starboy.salary)

# print(Employee.__dict__)
