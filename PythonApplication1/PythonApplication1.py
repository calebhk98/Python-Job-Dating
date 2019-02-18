import time
start = time.clock()
import string
import random
import math
import datetime

if True:
	employees=[]#keeps track of the employees
	employers=[]#keeps track of the employers
	numOfFakeEmployees=0#This is for testing. It creates this many fake employees.
	numOfFakeEmployers=0#This is for testing. It creates this many fake employers.
	advDebugging=False
	#AdvDebugging - This shows all the variables as they are changing. Probably should only be turned on if something has freaked out. 
	Debugging=True
	#Debugging - This shows some basic variables. Turn this off for users, but just for debugging, is quite useful.
	"multiline for minization"
	#All the Variable

'''
Change Log
12/28/18
Started, Have mostly just variable and stuff
12/29/18
Have the employers done
12/30/18
Have the employees done
1/2/19
Some Debugging
1/3/19
Have the combination Done
1/4/19
More Debugging
1/5/19
Change Log Created
starting to add in actual traits for employees
Stuck in a repeated asking
Fixed, problem was being asked 2x
Fixed the so many parameters
Added addreess,	phoneNumber, email,skills, experience, education, languages, hobbies, interest, certifications, awards, projects
Need to change Address to a maps
Need to make Phone Number better
Need to ensure email is valid
Need to fix experience to show years and what they did
need to fix education to show years, location, degree, and GPA
Need to make languages shown how proficient you are
Need to learn what certifications, awards, and projects need
Should turn age into a DOB
Should allow a Sallary
1/7/19
Added all the functions for employee to create an employee function
Added birthdate function to employee, should allow to remove age
Fixed a bunch of bugs, if the user didn't follow some things





'''
class experience:
	startDate=string
	EndDate=string
	currentJob=bool

class employee:
	age=int
	gender=string
	wantedpay=float
	wantedHours=int
	workFromHome=bool
	birthDate=datetime

	addreess=string
	phoneNumber=int
	email=string
	skills=[]
	experience=[]
	education=[]
	languages=[]
	hobbies=[]
	interest=[]
	certifications=[]
	awards=[]
	projects=[]
	
	def __init__(self, name):
		self.name=name
		self.employerImportancte=[]
		self.bestChoice=float
		employees.append(self) #my attempt to allow multiple calls appears to do nothing

	def __init__(self, name,age=18, gender='M', wantedpay=7.25, wantedHours=40, workFromHome=False):
		self.name=name
		self.age=age
		self.gender=gender
		self.wantedpay=wantedpay
		self.wantedHours=wantedHours
		self.workFromHome=workFromHome
		self.employerImportancte=[]
		self.bestChoice=float
		employees.append(self)#_init_ this runs whenever you call the class to create a new person


	def Age(self):
		self.age=int(input('How old are you?'))
		if(self.age<=0):
			print("Your age has to be older than 0. Please age up before looking for a job.")
			employee.Age(self)
		print("You are", self.age, "years old")

	def Gender(self):
		self.gender=(input('What gender are you? M/F'))
		if(self.gender=='M' or self.gender == 'F'):
			self.gender=self.gender

		else:
			print("Sorry, that is not a gender. Please press F for Female or M for Male.")
			employee.Gender(self)
		print("Your gender is ", self.gender)

	def WantedPay(self):
		self.wantedpay=int(input('How much do you want to be paid per hour?'))
		if(self.wantedpay<=0):
			print("Sorry, you have to be paid more than $0 per hour")
			employee.WantedPay(self)
		print("You want to be paid $", self.wantedpay, "per hour.")
		
	def WantedHour(self):
		self.wantedHours=int(input('How many hours do you want per week?'))
		if(self.wantedHours<=0):
			print("You have to work more than 0 hours.")
			employee.WantedHour(self)
		if(self.wantedHours>168):
			print("There are only 168 hours in a week. Please choose less than 168.")
			employee.wantedHours(self)
		print("You want ", self.wantedHours, " hours per week.")

	def workFromHome(self):
		workFromHome=input('Do you want to work from Home? T/F')
		if(workFromHome=='T'):
			self.workFromHome=True
			print("You want to work from home")
		elif (workFromHome=='F'):
			self.workFromHome=False
			print("You do not want to work from home")
		else:
			print("Your Response is not acceptable. It needs to be 'T' for True, or 'F' for False")
			employee.workFromHome(self)
			
	def address(self):
		self.addreess=input('What is your address?')
		print("Your address is ", self.addreess)

	def PhoneNumber(self):
		self.phoneNumber=(input('What is your phone number?'))
		print("Your phone number is ", self.phoneNumber)

	def Email(self):
		self.email=input('What is your email?')
		print("Your email is ", self.email)

	def Skills(self):
		skill=input("What skills do you have?")
		self.skills.append(skill)
		print("You have added ", skill, "to your skills")
		moreSkills=input("Do you have more skills? Y/N ")
		if(moreSkills=='Y'):
			employee.Skills(self)
		print("Your total skills is ", self.skills)

	def Experience(self):
		experience=input("What work Experience do you have?")
		self.experience.append(experience)
		print("You have added ", experience, "to your experience")
		moreExperience=input("Do you have more experience? Y/N ")
		if(moreExperience=='Y'):
			employee.Experience(self)
		print("Your total experience is ", self.experience)

	def Education(self):
		education=input("What education do you have?")
		self.education.append(education)
		print("You have added ", education, "to your education")
		moreEducation=input("Do you have more education? Y/N ")
		if(moreEducation=='Y'):
			employee.Education(self)
		print("Your total education is ", self.education)

	def Languages(self):
		languages=input("What languages do you know?")
		self.languages.append(languages)
		print("You have added ", languages, "to your languages")
		moreLanguages=input("Do you know more languages? Y/N ")
		if(moreLanguages=='Y'):
			employee.Languages(self)
		print("Your total education is ", self.languages)

	def Hobbies(self):
		hobbies=input("What hobbies do you have?")
		self.hobbies.append(hobbies)
		print("You have added ", hobbies, "to your hobbies")
		moreHobbies=input("Do you have more hobbies? Y/N ")
		if(moreHobbies=='Y'):
			employee.Hobbies(self)
		print("Your total hobbies is ", self.hobbies)

	def Interest(self):
		interest=input("What interest do you have?")
		self.interest.append(interest)
		print("You have added ", interest, "to your interest")
		moreInterest=input("Do you have more interest? Y/N ")
		if(moreInterest=='Y'):
			employee.Interest(self)
		print("Your total interest is ", self.interest)

	def Certifications(self):
		certifications=input("What certifications do you have?")
		self.certifications.append(certifications)
		print("You have added ", certifications, "to your certifications")
		moreCertifications=input("Do you have more certifications? Y/N ")
		if(moreCertifications=='Y'):
			employee.Certifications(self)
		print("Your total certifications is ", self.certifications)

	def Awards(self):
		awards=input("What awards do you have?")
		self.awards.append(awards)
		print("You have added ", awards, "to your awards")
		moreAwards=input("Do you have more awards? Y/N ")
		if(moreAwards=='Y'):
			employee.Awards(self)
		print("Your total awards is ", self.awards)

	def Projects(self):
		projects=input("What projects do you have?")
		self.projects.append(projects)
		print("You have added ", projects, "to your projects")
		moreProjects=input("Do you have more projects? Y/N ")
		if(moreProjects=='Y'):
			employee.Projects(self)
		print("Your total projects is ", self.projects)

	def BirthDate(self):
		print("Please do your birthday in the following order: Year, Month, Day .")
		year = int(input("Please put the year you were born. Ex: 1985 or 2010 "))
		month=int(input("Please put the month of your birth. Ex: 01 or 12 "))
		day=int(input("Please put the date of the month you were born. Ex: 01 or 28 "))
		while year<32:#This is more to prevent accidentally putting the month or day in for the year. 
			print("Sorry, the year has to be greater than that. ")
			year = int(input("Please put the year you were born. Ex: 1985 or 2010"))
		while month>12 or month<=0:
			print("Sorry, the month has to be between 1 and 12")
			month=int(input("Please put the month of your birth. Ex: 01 or 12"))
		while day>32 or day <= 0:
			print("Sorry, the date has to be between 1 and 31. ")
			day=int(input("Please put the date of the month you were born. Ex: 01 or 28"))
		self.birthDate=datetime.date(year, month,day)
		print("Thank you, your birth date is ", self.birthDate)





	
class employer:
	def __init__(self, name, pay,wantedage, wantedgender,Hours, workFromHome):
		self.name=name
		self.pay=pay
		self.Hours=Hours
		self.workFromHome=workFromHome
		self.wantedage=wantedage
		self.wantedgender=wantedgender
		self.employeeImportancte=[]
		self.bestChoice=float
		employers.append(self)

if(True):

	Caleb = employee("Caleb", 20, 'M', 8,  40, False)
	Piper = employee("Piper", 15, 'F', 7,  10, False)
	Mom   = employee("Shely", 40, 'F', 10, 15, True)
	Dad   = employee("Mark",  45, 'M', 12, 40, False)
	Cryst = employee("Cryst", 25, 'F', 9,  35, True)
	OCaleb = employee("OCaleb", 20, 'M', 15,  40, False)
	PCaleb = employee("PCaleb", 20, 'M', 5,  40, False)#This is all the workers
for  i in range(0,numOfFakeEmployees) :
	name = ''.join(random.choices(string.ascii_uppercase, k=5))
	age = random.randint(1,100)
	sex= random.randint(1,2)
	if(sex==1):
		sex='M'
	else:
		sex='F'
	pay=random.randint(1,30)
	hours = random.randint(1,60)
	WFH= random.randint(1,2)
	if(WFH==1):
		WFH=True
	else:
		WFH=False
	Guest = employee(name,age,sex,pay,hours,WFH)
	
	i+=1#This creates fake employees for testing

def CreateWorker():
	
	MyName=(input('What is your name?'))
	Guest = employee(MyName)
	
	#Guest = employee(MyName,MyAge, MyGender, MyWantedPay, MywantedHours, MyWorkFromHome)
	
	employee.Age(Guest)
	employee.Gender(Guest)
	employee.WantedPay(Guest)
	employee.WantedHour(Guest)
	employee.workFromHome(Guest)
	employee.address(Guest)
	employee.PhoneNumber(Guest)
	employee.Email(Guest)
	employee.Skills(Guest)
	employee.Experience(Guest)
	employee.Education(Guest)
	employee.Languages(Guest)
	employee.Hobbies(Guest)
	employee.Interest(Guest)
	employee.Certifications(Guest)
	employee.Awards(Guest)
	employee.Projects(Guest)
	employee.BirthDate(Guest)
	
	

MakeNewWorker=input('Do you want to make a new person? T/F\n')
if(MakeNewWorker=='T'):
	CreateWorker()




if(True):

	Babysitter = employer("Babysitting",  15,  5, 'F', 10, True)
	Factory    = employer("Factory",     8,  25, 'M', 45, False)
	Librarian  = employer("Librarian",   10, 37, 'M', 20, False)
	FastFood   = employer("McDonald'",   7, 18, 'F',  30, False)
	Gastatio   = employer("Gassy",       7, 23, 'M',  25, False)
	OFactory   = employer("OFactory",   15,  25, 'M', 45, False)
	PFactory   = employer("PFactory",    5,  20, 'M', 40, False)#This is all of the jobs
for  i in range(0,numOfFakeEmployers) :
	name = ''.join(random.choices(string.ascii_uppercase, k=5))
	pay = random.randint(1,30)
	wantedage=random.randint(1,100)
	sex= random.randint(1,2)
	if(sex==1):
		sex='M'
	else:
		sex='F'
	
	hours = random.randint(1,60)
	WFH= random.randint(1,2)
	if(WFH==1):
		WFH=True
	else:
		WFH=False
	Boss = employer(name,pay,wantedage,sex,hours,WFH)
	
	i+=1#This creates fake jobs for testing


for employeres in (employers):
	print(employeres.name)
	for employeees in (employees):
		#for advDebugging, read note at top
		if(advDebugging):
			print(employeees.name)
			"multiline for minization"
		#This finds the difference between the what the employer and the employee wants
		paydifference = abs(employeres.pay-employeees.wantedpay)
		agedifference = abs(employeres.wantedage-employeees.age)
		sexDifference = employeres.wantedgender==employeees.gender
		HoursDifference = abs(employeres.Hours - employeees.wantedHours)
		workFromHomeDifference = (employeres.workFromHome==employeees.workFromHome)

		if(advDebugging):
			print("Pay Difference: ",paydifference, " Age Difference: ", agedifference, "Sex Difference: ", sexDifference)#for advDebugging, read note at top
			"multiline for minization"
		
		#this turns each of these into a relationship, so they can be directly compared
		if(sexDifference==True):
			sexDifference=0
			"multiline for minization"
		else:
			sexDifference=1
			"multiline for minization"
		if(workFromHomeDifference==True):
			workFromHomeDifference=0
			"multiline for minization"
		else:
			workFromHomeDifference=1
			"multiline for minization"
		paydifference = paydifference/employeres.pay
		agedifference = agedifference/employeres.wantedage

		if(advDebugging):
			print("Pay Difference: ",paydifference, " Age Difference: ", agedifference, "Sex Difference: ", sexDifference)#for advDebugging, read note at top
			"multiline for minization"
		employeres.employeeImportancte.append(abs(sexDifference+paydifference+agedifference))
		#This adds the sum of the relations to the employers set of possible employees, to therefore know how all 
		#employees relate to each other
		
	if(Debugging):#For Debugging, look at top
			print(employeres.employeeImportancte)#This is for employers
			"This is to allow minization"
	"This is to break up the debugging from the above part. Do not delete, unless you fix the minimization"
	#This adds the sum of the relations to the employers set of possible employees, to therefore know how all 
		#employees relate to each other
			
if(Debugging):
	print()	
	print("Round 2")
	print()

for employee in (employees):
	for employer in (employers):
		
		paydifference = abs(employee.wantedpay - employer.pay)
		agedifference = abs(employee.age - employer.wantedage)
		sexDifference = employer.wantedgender==employee.gender
		HoursDifference = abs(employee.wantedHours - employer.Hours)
		workFromHomeDifference = (employer.workFromHome==employee.workFromHome)
		if(sexDifference==True):
			sexDifference=0
			"multiline for minization"
		else:
			sexDifference=1
			"multiline for minization"
		if(workFromHomeDifference==True):
			workFromHomeDifference=0
			"multiline for minization"
		else:
			workFromHomeDifference=1
			"multiline for minization"

		paydifference = paydifference/employee.wantedpay
		agedifference = agedifference/employee.age
		#importance.append(abs(sexDifference+paydifference+agedifference))
		employee.employerImportancte.append(abs(sexDifference+paydifference+agedifference))
	#print(employer.name)
	print(employee.employerImportancte)
#this is for the employees

for employersindex, employeer in enumerate(employers):
	employeer.bestChoice = min(employeer.employeeImportancte)
	worstChoice=max(employeer.employeeImportancte)
	bestChoice=min(employeer.employeeImportancte)
	LiklihoodOfGoodMatch=(round(((1-bestChoice/worstChoice)*100),2))

	for employeeImportancteindex, employeeImportancte in enumerate(employeer.employeeImportancte):
		if(employeer.bestChoice==employeer.employeeImportancte[employeeImportancteindex]):

			employeer.bestChoice=employeeImportancteindex
	print("The best choice for ", employeer.name, " is ", employees[employeer.bestChoice].name, "at a likihood of ", LiklihoodOfGoodMatch,"%")#Finding the best choice numbers

print("")

for employee in employees:
	employee.bestChoice= min(employee.employerImportancte)
	worstChoice=max(employee.employerImportancte)
	bestChoice=min(employee.employerImportancte)
	LiklihoodOfGoodMatch=(round(((1-bestChoice/worstChoice)*100),2))
	#print("The best choice is ", employee.bestChoice)
	i=0
	while i < len(employee.employerImportancte):
		if(employee.bestChoice==employee.employerImportancte[i]):

			employee.bestChoice=i
			#print("That choice is option ", i, "Which should be equal to ",employee.bestChoice)
			
			break
		i=i+1
	print("The best choice for ", employee.name, " is ", employers[employee.bestChoice].name, "at a likihood of ", LiklihoodOfGoodMatch,"%")
	#This finds the best employee for the employer
#print(Babysitter.employeeImportancte)


Combination = []
firstRound = []
comparison = float

for employeeindex, employe in enumerate(employees):
	print(employeeindex)
	for employeerindex, employeer in enumerate(employers):
		print("		",employeerindex)
		#print("			",employe.employerImportancte[employeerindex])
		#print("			",employeer.employeeImportancte[employeeindex])
		comparison = employe.employerImportancte[employeerindex]*employeer.employeeImportancte[employeeindex]
		comparison  = math.sqrt(comparison)
		print("				", comparison)
		firstRound.append(comparison)
	Combination.append(firstRound)
	firstRound=[]
	

end = time.clock()
print ("Number of employees is ",len(employees))
print ("Number of employers is ",len(employers))
print("Time: ",end - start," Sec")