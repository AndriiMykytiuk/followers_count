#importing the libraries
import requests
from bs4 import BeautifulSoup


#creating function to scrap information
def InstaScrap(user):
    #url.format(urlObj) is the built in API provided by uRL class,which takes an object or string and return a formatted string
    #derived from that object or string and if urlObj not found then it throws an error.
    url = "https://www.instagram.com/{}".format(user)

    # creating 'r' as an object that will hold the recieved data from http request.
    r = requests.get(url)
    #Code for Parsing the r.text to the BeautifulSoup and storing it into python object "bs".
    bs = BeautifulSoup(r.text ,"html.parser")
    #holding the title of bs
    title=bs.title
    #use of 'FIND' method to get the details.
    rep = bs.find('meta',property ='og:description').attrs["content"]
    #print the text content of 'title' element.
    #returning parse(rep)
    print(rep.split('Followers,'))

InstaScrap('stepanets_kir')