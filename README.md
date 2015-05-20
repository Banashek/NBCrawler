NBCrawler is a simple google crawler built for an interview

It uses flask for some rest routing, mongodb for the database, requests for web requests, and beautifulsoup to parse html.

Pre-requisites:
- [Python 3.4]("https://www.python.org/downloads/")
- [MongoDB]("https://www.mongodb.org/")
- [Requests]("http://docs.python-requests.org/en/latest/")
- [BeautifulSoup4]("http://www.crummy.com/software/BeautifulSoup/bs4/doc/")
- [PyMongo]("http://api.mongodb.org/python/current/")
- [Flask]("http://flask.pocoo.org/")

How to run:
- Ensure mongo is up and running on the default port
- Change into the main directory and run ```python3 flaskApp.py```
- Browse to [http://localhost:5000](http://localhost:5000) to see the index page and type in your search query, then hit scrap

Things not included (but definitely would be high on the todo list):
- Tests (nothing is tested, since this was made in a few hours)
- Error Handling (")
- Something more robust than requests and beautifulsoup smashed into one file (perhaps something more modular)
- Better UI/UX (maybe a small crud site)
