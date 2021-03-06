import datetime

class GoogleResult:

    """
        The GoogleResult class is a model of how the google search results are stored in the database.
        Takes as parameters:
            - searchterm: the search term used to find the result. Stored to prevent duplicate lookups.
            - title: the title of the result
            - link: the href link for the result
            - subtext: the subtext partial definition for the result
    """

    def __init__(self, query, title, link, subtext, searchterms, scripts):
        """Creates a new GoogleResult object"""
        self.search_query = query
        self.title = title
        self.link = link
        self.subtext = subtext
        self.searchterms = searchterms
        self.link_scripts = scripts
	
    def save(self, db):
        """Saves the GoogleResult to mongo"""
        db.googleResults.insert_one(
            {
                    "searchQuery": self.search_query,
                    "title": self.title,
                    "link": self.link,
                    "subtext": self.subtext,
                    "searchterms" : self.searchterms, # array
                    "queryTime": datetime.datetime.now(),
                    "details": self.link_scripts
            }
        )
