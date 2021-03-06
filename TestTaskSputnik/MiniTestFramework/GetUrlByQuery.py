import os
import urllib

from xml.dom.minidom import *
from urlparse import *
from urllib2 import urlopen
from datetime import datetime


class GetUrlByQuery:

    def __init__(self, bang_id, search_query='', query_format='xml', redirect='1'):
        # Configure query
        query_args = {'q': '!{bangId} {searchQuery}'.format(bangId=bang_id, searchQuery=search_query),
                      'format': '{format}'.format(format=query_format),
                      'no_redirect': '{redirect}'.format(redirect=redirect)}
        encoded_args = urllib.urlencode(query_args)
        url = 'http://api.duckduckgo.com/?' + encoded_args

        self._url = urlopen(url)
        self._redirectUrl = ''

    def GetUrl(self):
        """Gets the URL by creating query."""

        # Get source xml
        url = self._url
        bytecode = url.read()
        xml_str = bytecode.decode()
        url.close()

        _tempName = 'tmp_{date}'.format(
                date=datetime.strftime(datetime.now(), "%Y%m%d%H%M%S"))

        # Write xml to temp file
        with open(_tempName, 'w') as f:
            f.write(xml_str)

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
