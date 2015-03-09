import sys, time, geonamescache
from geopy.geocoders import Nominatim # currently unused
from geopy.distance import great_circle # currently unused

#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Task:

	Find A Classmate To Work with!!

	On NovoEd students from all over the world, form teams and work together on their classes. One of the ways students find each other is through using our search feature. Our students need to be able to search each other based on location, they might be looking for another student in a specific country, region/state and city. 

	We have created a mini version of NovoEd's location data from student profiles. This location data comes from different sources, so you are not going to see a consistent formatting in it.

	You are creating the first version of NovoEd's location search. In the basic version of the search app we want:

	 - students to be able to find everyone from a given country
	 - students to be able to find everyone from a given city
	 - students to be able to find everyone from a given region/state
	 - search results should be accurate, i.e. they should show all students from different locations

	Bonus: 
	How could a better version of this search work?
	Remember the goal is to help students find teams. 

	Bonus user story 1: Let's say a student lives in a city near the bay area; she wants to be able to meet her team members in person and work with them. How can she do that with your app? How can you make your app better?

	Bonus user story 2: Student lives in China, she can't find anyone from China in her class, she wants to find a remote team; and wants to have an easy time setting up meetings and working with her team. Is there anyways you can reframe the location search problem, use the location data, and help her find teammates?

	Data: 
	https://docs.google.com/a/novoed.com/spreadsheets/d/15mEigqCJxOcSiP-5VLHwUHt9vBGBQ7tY7ixiCUfcBwE
"""

######### Instance Variables #########

gc = geonamescache.GeonamesCache()
countries_dict = gc.get_countries_by_names()
countries = countries_dict.keys()
cities_dict = gc.get_cities()
cities = [cities_dict[city].get("name") for city in cities_dict]
states_dict = gc.get_us_states_by_names()
states = states_dict.keys()

######### Class Definitions #########

class Student(object):
	"""docstring for Student"""
	def __init__(self, first_name = "Unspecified", last_name = "Unspecified", country = "Unspecified", city = "Unspecified", state = "Unspecified", region = "Unspecified"):
		self.first_name = first_name
		self.last_name = last_name
		self.country = country
		self.city = city
		self.state = state
		self.region = region
		self.neighbors = set()

	###### Setter Functions ######

	def setCountry(self, country):
		self.country = country

	def setCity(self, city):
		self.city = city

	def setState(self, state):
		self.state = state

	def setRegion(self, region):
		self.region = region

	def addNeighbor(self, neighbor):
		(self.neighbors).add(neighbor)

	###### Getter Functions ######

	def getNeighbors(self):
		return self.neighbors

	def getFirstName(self):
		return self.first_name

	def getLastName(self):
		return self.last_name

	def getCountry(self):
		return self.country

	def getCity(self):
		return self.city

	def getRegion(self):
		return self.region

	def getState(self):
		return self.state

class LocationDatabase(object):
	"""docstring for LocationDatabase"""
	def __init__(self):
		self.location_by_country = dict() # dict to with countries as keys, with student set as values
		self.location_by_city = dict() # dict to with cities as keys, with student set as values
		self.location_by_region = dict() # dict to with regions as keys, with student set as values
		self.students = set() # all students in database

	def addStudent(self, student):
		if student not in self.students:
			self.addToDict(student, student.getCountry(), self.location_by_country)
			self.addToDict(student, student.getCity(), self.location_by_city)
			self.addToDict(student, student.getState(), self.location_by_region)
			self.addToDict(student, student.getRegion(), self.location_by_region)
			(self.students).add(student)
		else:
			print "Student already in database"

	def addToDict(self, student, attribute, location_dict):
		if attribute not in location_dict:
			student_set = set()
			student_set.add(student)
			location_dict[attribute] = student_set
		else:
			location_dict[attribute].add(student)

	def getCountries(self):
		return (self.location_by_country).keys()

	def getCities(self):
		return (self.location_by_city).keys()

	def getRegions(self):
		return (self.location_by_region).keys()
		
	def getStudents(self):
		return self.students

	def studentExists(self, student):
		return student in self.students

	def studentsFrom(self, location, category):
		if category == "country": return self.location_by_country[location]
		elif category == "city": return self.location_by_city[location]
		else: return self.location_by_region[location]

######### Main Program #########

def main(args):
	if args > 1:
		database = retrieveLines(args[1])
		countries_in_database = database.getCountries()
		cities_in_database = database.getCities()
		regions_in_database = database.getRegions()
		numStudents = len(database.getStudents())
		print "The database you provided has %i students and it took %s seconds to load" % (numStudents, time.time() - start_time)
		user_search(database, countries_in_database, cities_in_database, regions_in_database)
	else:
		print "No database file provided"

def user_search(database, countries_in_database, cities_in_database, regions_in_database):
	decision = str(raw_input("Would you like to look up students by country, city or region (yes or no)?: "))
	while decision.lower() == "yes" or decision.lower() == "y":
		flag = retrieveFlagFromUser()
		if flag == "C":
			searchDatabase(database, countries_in_database, "country")
		elif flag == "c":
			searchDatabase(database, cities_in_database, "city")
		else:
			searchDatabase(database, regions_in_database, "region")
		decision = str(raw_input("Would you like to search again (yes or no)?: "))

def retrieveFlagFromUser():
	flag = str(raw_input("Please specify with either C (countries), c (cities) or r: "))
	while True:
		if flag == "C" or flag == "c" or flag == "r": break
		flag = str(raw_input("Please try again: "))
	return flag

def searchDatabase(database, locations, category):
	inputted_word = str(raw_input("Please enter a " + category + ": "))
	while (inputted_word not in locations):
		inputted_word = str(raw_input("Please enter a valid " + category + ": "))
	student_set = database.studentsFrom(inputted_word, category)
	print "Here are your search results:"
	for student in student_set:
		print "\tStudent Name: %s %s" % (student.getFirstName(), student.getLastName())
	print "There are a total of %i students in this %s." % (len(student_set), category)

def retrieveLines(file_name):
	database = LocationDatabase()
	while True: # Exiting out of this method requires a proper file be provided
		try:
			# utilize "with ... as ...:" syntax to take care of file closing
			with open(file_name, 'r') as data_file: 
				for line in data_file:
					info_arr = line.split(',')
					(first, last, loc_index) = findName(info_arr)
					student = Student(first, last)
					location_info = clean(info_arr[loc_index:])
					
					################# ALL IMPORTANT PROCESSING BELOW ##################

					for elem in location_info:
						if unicode(elem, "UTF-8") in countries:
							student.setCountry(unicode(elem, "UTF-8"))
						elif unicode(elem, "UTF-8") in cities:
							student.setCity(unicode(elem, "UTF-8"))
						elif unicode(elem, "UTF-8") in states:
							student.setState(unicode(elem, "UTF-8"))
						else:
							student.setRegion(unicode(elem, "UTF-8"))
					database.addStudent(student)

			###############################################

			return database

		except IOError as e:
			# Catches whether the file is incorrectly opened or not; if incorrect,
			#	asks user to specify a correct file name. (this pertains to both
			#	correct dictionary files and input test files)
			print "You have not correctly specified a file name. Please try again."
			file_name = str(raw_input("Please specify a file name: "))

def clean(arr):
	for i in xrange(0, len(arr)):
		arr[i] = arr[i].strip("\",\n, ")
	return arr

def findName(info_arr):
	index = 0
	length = len(info_arr) - 1
	while (info_arr[index][0] != "\"" and index < length):
		index += 1
	if index > 1:
		return (info_arr[0], info_arr[1], index)
	elif index == 1:
		return (info_arr[0], None, index)
	else:
		return (info_arr[0], info_arr[1], 2)

def reconstructLocation(location_list):
	result = ""
	for elem in location_list:
		stripped = elem.lstrip("\"").rstrip("\",\n")
		result += (stripped + ",")
	return result.rstrip("\",\ ")

start_time = time.time()

main(sys.argv)

print ("--- %s seconds ---" % (time.time() - start_time))

