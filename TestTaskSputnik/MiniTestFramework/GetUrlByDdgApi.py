import duckduckgo


class GetUrlByDdgApi:

    def __init__(self, bang_id, search_query=''):
        self.query = duckduckgo.query('!{bangId} {searchQuery}'.format(bangId=bang_id, searchQuery=search_query))

    def GetUrl(self):
        """Gets the URL by duckduckgo library."""

        return self.query.redirect.url
