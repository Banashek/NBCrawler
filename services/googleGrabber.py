import urllib.request, requests, json
from bs4 import BeautifulSoup
from pymongo import MongoClient
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Models.GoogleResult import GoogleResult

def scrape_from_query(query="nbc"):
    """TODO: Docstring for scrape_from_query.

    :query: Search query to scrape for
    :returns: Array of GoogleResults

    """
    # Parameters
    num_results = 20
    # search_query = "nbc+universal"
    # search_query = "nbc"
    search_query = query

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
        results_array = []
        cursor = db.googleResults.find({"searchQuery": search_query})
        for result in cursor:
            results_array.append(result)
        return results_array
    else:
        # Build the url
        url_base = "http://www.google.com/search?" 
        hl_param = "hl=en" 
        query_param = "&q=" + search_query
        btng_param = "&btnG=Google+Search"
        meta_param = "&meta="
        num_results_param = "&num=" + num_results.__repr__()
        url = url_base + hl_param + query_param + btng_param + meta_param + num_results_param
        print(url)

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
        return results_array
