import os
from xml.dom.minidom import *
from urllib2 import urlopen
from datetime import datetime


class GetUrlByQuery:

    def __init__(self, bang_id, search_query=''):
        # Configure query
        self.url = urlopen(
            'http://api.duckduckgo.com/?q=!{bangId}+{searchQuery}&format=xml&no_redirect=1'.format(
                bangId=bang_id,
                searchQuery=search_query))

    def GetUrl(self):
        """Gets the URL by creating query."""

        # Get source xml
        url = self.url
        bytecode = url.read()
        xml_str = bytecode.decode()

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

        return name[0].childNodes[0].nodeValue
