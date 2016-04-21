import pytest

from MiniTestFramework.GetUrlByRecuestLib import *


# Parameters for test. TODO In future may create config
cases = [
    ("w", "wikipedia.org"),
    ("imdb", "imdb.com"),
    ("g", "google.com"),
    ("so", "stackoverflow.com")
]

# Search query for tests
testQuery = 'test'


@pytest.mark.parametrize("bang_id, expected", cases)
def test_check_query(bang_id, expected):
    """This case check duckduckgo by using they api query."""

    # Header
    print '\n{separate}'.format(separate='='*60)
    print 'Check query'

    getUrlByQuery = GetUrlByQuery(bang_id, testQuery)
    url = getUrlByQuery.GetUrl()

    # Print to console current page URL
    print 'Url getted by query: {URL}'.format(URL=url)
    print 'Url parsed URL: {URL}'.format(URL=getUrlByQuery.GetDomainName())

    # Check expected result
    assert expected in getUrlByQuery.GetDomainName()

    print '{separate}'.format(separate='=' * 60)
