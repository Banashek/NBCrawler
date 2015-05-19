import urllib.request, requests, json
from bs4 import BeautifulSoup
from Models.GoogleResult import GoogleResult

# url = "http://www.google.ca/search?hl=en&q=nbc+universal&btnG=Google+Search&meta="
# url = "https://duckduckgo.com/?q=nbc"

# Parameters
num_results = 20
search_query = "nbc+universal"

search_terms = search_query.split(' ')

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
    gres = GoogleResult(search_query, link_title, link_href, link_subtext)
    results_array.append(gres)


for gr in results_array:
    print("Search term: " + gr.searchterm)
    print("Title: " + gr.title)
    print("Link: " + gr.link)
    print("Subtext: " + gr.subtext)
    print()
