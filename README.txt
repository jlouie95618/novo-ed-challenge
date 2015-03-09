Task Chosen:

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

Directions:
	This is a Python implementation of a student location based search.
		The user is able to provide a comma separated file (CSV format),
		to use as the program run's database. If no file is provided, the
		program will not run and provide a message to the user. Once the
		program begins to run, the user will be asked whether they want
		to conduct a student search. If yes, they will have to specify
		what particular parameter they want to use to search students by 
		(countries, which utilize the flag "C", cities, which utilize the 
		flag "c", or regions, which utilize the flag "r"). Location strings
		inputted by the user must match that of the locations in the database,
		otherwise no result will be found. The location search by category 
		will run until the user enters a location that is present in the database
		(or they terminate the program with control-C). The user is able to
		search students as many times as they wish. Termination occurs when any
		string other than "yes" or "y" is provided to prompt to initiate a search.
		The program runs will take on the following form:
		
			The database you provided has ____ students and it took ___ seconds to load
			Would you like to look up students by country, city or region (yes or no)?: ___
			Please specify with either C (countries), c (cities) or r: ____
			Please note that locations are proper nouns and must be capitalized accordingly for results.
			Please enter a region: ___________
			Here are your search results:
				Student Name: ___ _____
				Student Name: ___ _____
					...
				Student Name: ___ _____
			There are a total of ___ students in this __(location)__.

Assumptions:
 - Functionality of this program depends on access to geonamescache;
 	this allows for the ability to stratify/filter the database location
 	information.
 - Currently all locations are only defined as the user has provided
 	in their database (i.e. a student who only provides "Prague", can
 	only be found with the city search query of "Prague").
 - Location parameters/details that are not defined as a country, city,
 	or state within the US, is assumed to be a generally defined "region"
 	(i.e. "Stanford" is a "region" because it is neither a state or city, 
 	just as the "San Francisco Bay Area" is also a "region").
 - The only information provided to the user on a student search is the
 	student's name