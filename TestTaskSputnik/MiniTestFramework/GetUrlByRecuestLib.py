import requests
import os

from xml.dom.minidom import *
from datetime import datetime
from urlparse import *


class GetUrlByQuery:

    def __init__(self, bang_id, search_query='', query_format='xml', redirect='1'):
        # Configure query
        query_args = {'q': '!{bangId} {searchQuery}'.format(bangId=bang_id, searchQuery=search_query),
                      'format': '{format}'.format(format=query_format),
                      'no_redirect': '{redirect}'.format(redirect=redirect)}

        url = requests.get('http://api.duckduckgo.com/?', params=query_args)

        self._url = url
        self._redirectUrl = ''

    def GetUrl(self):
        """Gets the URL by creating query."""

        _tempName = 'tmp_{date}'.format(
                date=datetime.strftime(datetime.now(), "%Y%m%d%H%M%S"))

        # Write xml to temp file
        with open(_tempName, 'w') as f:
            f.write(self._url.content)

        # Get Redirect element from file
        xml_file = parse(_tempName)
        name = xml_file.getElementsByTagName('Redirect')

        # Remove temp file
        os.remove(_tempName)
        self._redirectUrl = name[0].childNodes[0].nodeValue

        return self._redirectUrl

    def GetDomainName(self):
        """Gets the domain URL name"""
        return urlparse(self._redirectUrl).netloc