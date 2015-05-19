class GoogleResult:

    """
        The GoogleResult class is a model of how the google search results are stored in the database.
        Takes as parameters:
            - searchterm: the search term used to find the result. Stored to prevent duplicate lookups.
            - title: the title of the result
            - link: the href link for the result
            - subtext: the subtext partial definition for the result
    """

    def __init__(self, searchterm, title, link, subtext):
        """Creates a new GoogleResult object"""
        self.searchterm = searchterm
        self.title = title
        self.link = link
        self.subtext = subtext
