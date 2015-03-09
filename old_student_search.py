import sys, time, geonamescache
from geopy.geocoders import Nominatim
from geopy.distance import great_circle


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

gc = geonamescache.GeonamesCache()
countries_dict = gc.get_countries_by_names()
countries = countries_dict.keys()
cities_dict = gc.get_cities()
# print cities_dict

class Student(object):
	"""docstring for Student"""
	def __init__(self, first_name = None, last_name = None, location = None):
		self.first_name = first_name
		self.last_name = last_name
		self.location_name = location #self.processLocation(location)
		self.neighbors = set()

	def addNeighbor(self, neighbor):
		(self.neighbors).add(neighbor)

	def getNeighbors(self):
		return self.neighbors

	def getFirstName(self):
		return self.first_name

	def getLastName(self):
		return self.last_name

	def getLocation(self):
		return self.location_name

class Location(object):
	"""docstring for Location"""
	def __init__(self, location = None):
		self.location_string = location
		self.location_data = None
		self.location_lat = None
		self.location_long = None
		self.location_country = None
		self.location_city = None
		self.location_region = None
		self.students = set()

	def setLocationString(self, location_str):
		self.location_string = location_str

	def setLongLat(self, lon, lat):
		self.location_long = lon
		self.location_lat = lat

	def setCountry(self, country):
		self.location_country = country
		
	def setCity(self, city):
		self.location_city = city

	def setRegion(self, region):
		self.location_region = region
		
	def addStudent(self, student):
		(self.students).add(student)

	def getLocationString(self):
		return self.location_str

	def getLongLat(self):
		return (self.location_long, self.location_lat)

	def getCountry(self):
		return self.location_country
		
	def getCity(self):
		return self.location_city

	def getRegion(self):
		return self.location_region
		
	def getStudentSet(self):
		return self.students

	def isStudentIn(self, student):
		return (student in self.students)


class LocationDatabase(object):
	"""docstring for LocationDatabase"""
	def __init__(self):
		self.location_by_country = dict() # dict to with countries as keys, with student set as values
		self.location_by_city = dict() # dict to with cities as keys, with student set as values
		self.students = set() # all students in database

	def addLocation(self, country, city):
		pass

	def addStudent(self):
		pass

	def getLocations(self):
		pass
		
	def getStudents(self):
		pass

	def locationExists(self):
		pass

	def studentExists(self):
		pass

def main(args):
	if args > 1:
		database = retrieveLines(args[1])
	else:
		print "No database file provided"

def retrieveLines(file_name):
	database = LocationDatabase()
	geolocator = Nominatim()
	unique_locations = list()
	total = 0
	while True: # Exiting out of this method requires a proper file be provided
		try:
			# utilize "with ... as ...:" syntax to take care of file closing
			with open(file_name, 'r') as data_file: 
				counter = 0 #remove later
				for line in data_file:
					if counter == 100: break ### REMOVE LATER!!! ###
					info_arr = line.split(',')
					(first, last, loc_index) = findName(info_arr)
					location_name = reconstructLocation(info_arr[loc_index:])
					location = Location(location_name)
					student = Student(first, last, location_name)

					###################################

					# split = location.split(", ")
					
					check = False

					for elem in info_arr[loc_index:]:
						if unicode(elem, "UTF-8") in countries:
							check = True
						for city in cities_dict:
							if unicode(elem, "UTF-8") == cities_dict[city].get("name"):
								check = True

								# print elem
					if check:
						counter += 1
					else: unique_locations.append(location)

					total += 1

					# print split


			for location in unique_locations:
				print location
			print len(unique_locations)
			print counter
			print total
			return database


		except IOError as e:
			# Catches whether the file is incorrectly opened or not; if incorrect,
			#	asks user to specify a correct file name. (this pertains to both
			#	correct dictionary files and input test files)
			print "You have not correctly specified a file name. Please try again."
			file_name = str(raw_input("Please specify a file name: "))

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




"""


	# location = processLocation()

	# if counter < 20 or loc_index == 1:
	# 	print first
	# 	print last
	# 	print loc_index
	
	# counter += 1

	# try:

	# 	location = reconstructLocation(info_arr[2:])
	# 	geocode_loc = geolocator.geocode(location)
	# 	loc_address = geocode_loc.address

	# 	student = Student(info_arr[0], info_arr[1], reconstructLocation(info_arr[2:]))

	# except Exception, e:
	# 	print "exception %i found with: %s, %s" % (counter, info_arr[0], info_arr[1])
	# 	counter += 1


"""


