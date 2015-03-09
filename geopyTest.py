from geopy.geocoders import Nominatim
from geonamescache.mappers import country
import geonamescache
import pycountry

#!/usr/bin/python
# -*- coding: UTF-8 -*-

# mapper = country(from_key='name', to_key='official_name')

# iso3 = mapper('Spain') # iso3 is assigned ESP

# print iso3

geolocator = Nominatim()
# location = geolocator.geocode("175 5th Avenue NYC")

# To geolocate a query to an address and coordinates:

# print (location.address)
# print ((location.latitude, location.longitude))
# print (location.raw)

# To find the address corresponding to a set of coordinates:

# location = geolocator.reverse("52.509669, 13.376294")

# print (location.address)
# print ((location.latitude, location.longitude))
# print (location.raw)

# location = geolocator.geocode("Mace Blvd, Davis")

# print location.address

# location = geolocator.geocode("Tokyo")

# print location.address

# location = geolocator.geocode("Japan")

# print location.address

# location = geolocator.geocode("Bangkok, Thailand")

# print location.address

# location = geolocator.geocode("San Francisco Bay Area, US")

# print location.address

# location = geolocator.geocode("Iceland")

# print location.address

# try:
# 	location = geolocator.geocode("Coyhaique Alto, Aisen Del General Carlos Ibanez Del Campo, Chile")
# 	print location.address
# except Exception:
# 	print "fuuuuuck"

# try:
# 	location = geolocator.geocode("Innri Njar\xc3\xb0v\xc3\xadk, Gullbringusysla, Iceland")
# 	print location.address
# except Exception:
# 	print "fuuuuuck"


################################################################################################################################



gc = geonamescache.GeonamesCache()
countries = gc.get_countries_by_names()
print countries
print
for country in countries:
	if country == "United States":
		print countries[country]
		print country
		print countries[country].get("geonameid")
		print countries[country].get("neighbours")

print 

cities = gc.get_cities_by_name('New York City')

print cities

# print cities

# cities = gc.get_cities_by_name("Taipei")

# print cities[0].get("1668341").get("name")

# print countries 
# for city in cities:
# 	print city















	# print cities[city]


# print location.address

# location = geolocator.geocode("Aisen Del General Carlos Ibanez Del Campo, Chile")

# print location.address
# try:
# location = geolocator.geocode("Aisen Del General Carlos Ibanez Del Campo, Chile") #"Coyhaique Alto, Chile")
# print location.address


# except Exception:
	# print "BLA"


# print pycountry.countries.get(official_name = "Bangalore, India").name

