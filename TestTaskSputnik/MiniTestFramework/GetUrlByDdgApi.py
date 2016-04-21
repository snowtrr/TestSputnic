import duckduckgo

from urlparse import *


class GetUrlByDdgApi:

    def __init__(self, bang_id, search_query=''):
        self._query = duckduckgo.query('!{bangId} {searchQuery}'.format(bangId=bang_id, searchQuery=search_query))
        self._redirectUrl = ''

    def GetUrl(self):
        """Gets the URL by duckduckgo library."""
        self._redirectUrl = self._query.redirect.url
        return self._redirectUrl

    def GetDomainName(self):
        """Gets the domain URL name"""
        return urlparse(self._redirectUrl).netloc
