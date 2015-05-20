import urllib.request, requests, json
from bs4 import BeautifulSoup
from Models.GoogleResult import GoogleResult
from pymongo import MongoClient


# Parameters
num_results = 20
# search_query = "nbc+universal"
search_query = "nbc"

# Set up the database
try:
    client = MongoClient()
except Exception as e:
    print("Unable to connect to the database. Is Mongo running and bound to port 27017?")
    raise e

try:
    db = client.nbcrawler
except Exception as e:
    print("Unable to open the nbcrawler database. Check mongo output for errors.")
    raise e

# First check if we already have the query in the database
cursor = db.googleResults.find({"searchQuery": search_query})

if cursor.count() > 1:
    print("found results in database")
else:
    # Build the url
    url_base = "http://www.google.ca/search?" 
    hl_param = "hl=en" 
    query_param = "&q=" + search_query
    btng_param = "&btnG=Google+Search"
    meta_param = "&meta="
    num_results_param = "&num=" + num_results.__repr__()
    url = url_base + hl_param + query_param + btng_param + meta_param + num_results_param

    headers = { 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36' }

    # Create request object with url and custom headers
    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.text)
    results_array = []

    # Create GoogleResult objects from resulting page
    for result in soup.find_all('li', class_="g"):
        link = result.find('a')
        link_title = link.get_text()
        # Filter out image and ad results that have a blank title
        if not link_title:
            continue
        link_href = link.get('href')
        # Check if subtext is there
        if result.find('span', class_='st') is not None:
            link_subtext = result.find("span", class_="st").get_text()
        else:
            link_subtext = "No subtext for this node"
        search_terms = search_query.split(' ')
        gres = GoogleResult(search_query, link_title, link_href, link_subtext, ["test", "test2", "test3"])
        gres.save(db)
        results_array.append(gres)
