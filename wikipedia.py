import json
import urllib
import sys
import webbrowser

	#Imported the JSON so we can extract JSON data and convert it to extractable data for the program.
	#Imported theurllibrary so we could download the URL contents of the wiki pages.
	#Imported system for various functions, including exit.
	#Imported webbrowser to open up the new URL.

def getjsonData():
    url = "http://en.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&rnlimit=10&format=json"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    return data

	#We make this function to download and translate the JSON data.  We get the url from wikipedia's API that generates
	#random articles 10 at a time (url).  We then utilize the urllib to open the url and download the content.
	#json.loads deserializes a str or unicode instance containing a JSON document to a Python object, we then download 
	#the content into the variable data.

def generateURL(jsonid):
    baseUrl = "http://en.wikipedia.org/?curid="   
    newURL = baseUrl + str(jsonid)
    return newURL

 	#We create a function to generate the new URL with the JSON id.  We place jsonid we pulled from the jsonData function
 	#into the argument.  We create a variable called baseurl, which is the baseurl that utilizes page id and forwards it 
 	#to the corresponding webpage.  We add the baseurl to whatever id is in the jsonid variable, and this returns a new 
 	#URL of the combination of the web address and page id. We then create a new variable to store new value, called 
 	#new URL.

def webpage(newURL):
    webbrowser.open_new_tab(newURL)

	#We create a function to open the new URL a separate window in a web browser, by utilizing the webbrowser module.    


def link(data):
    for temp in data['query']['random']:
            title =  temp['title']
            jsonid =  temp['id']
            print  "Would you like to view " + temp['title'] + "?"
            newURL =  generateURL(jsonid)
            user_input = str(raw_input("> "))
            if user_input == 'Yes' or user_input == 'yes' or user_input == 'Y' or user_input == 'y':
                webpage(newURL)
            elif user_input == 'N' or user_input == 'n' or user_input == 'No' or user_input == 'no':
                print("WikiBot will find another article.")
                jsonData = getjsonData()
                link(jsonData)
            elif user_input == ("EXIT"):
                sys.exit()
            else:
                print("Error 404, WikiBot doesn't understand. :c  Please type yes or no.")

    #We read the parts of JSON translated into Python objects, we create a function called link to extract the title and ID, 
	#and we print it for the user to view the content in a readable form.  We create a "for statement", creating the variable 
	#temp to store content from data.  In the for argument of data, we request information blocks from query and random.  
	#Within query and random  we draw the title and id, and print them for the user.  Query stores 10 different article 
	#blocks, and random selects any of the 10 blocks.  In random, there are 3 variables: title, corresponding id, and 
	#corresponding namespace. We Create a variable to store id (jsonid), and we create the variable title to store the 
	#title.

	#We prompt the user if this is an article that they wish to read.  If they agree to it, we call the function that
	#opens the window to the address.  If the user says no, the Wikibot generates another article.  If the user types EXIT
	#the program shuts down.  We also leave room if there is anything outside of yes or no.



print "Welcome to the WikiBot.  This cute bot will generate a random article for you to read anywhere in Wikipedia."
print "To exit, please type EXIT."
print "Would you like to generate an article to read?"

	#We introduce the Wikipedia prgram to the user, instruct the user how to navigate the program.  We also prompt the user
	#to generate an article or to exit.

while(True):
	user_input = raw_input("> ")

	if user_input == 'Yes' or user_input == 'yes' or user_input == 'Y' or user_input == 'y':
		print "WikiBot is generating your article...."
		data = getjsonData()
		link(data)
	elif user_input == 'N' or user_input == 'n' or user_input == 'No' or user_input == 'no':
		print "WikiBot is shutting down.  Have a nice day!"
		sys.exit()
	elif user_input == ("EXIT"):
		sys.exit()
	else:
		print "Error 404, WikiBot doesn't understand. :c  Please type yes or no."

	#We create options for the user.  Anything starting with y will call the function to generate the random article.
	#Anything with n will close the program.  Anything outside of y or n will cause the program to error, loop back, 
	#and ask again.


