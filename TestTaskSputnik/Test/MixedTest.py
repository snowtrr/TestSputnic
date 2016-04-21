import pytest

from selenium import webdriver
from MiniTestFramework.GetUrlByDdgApi import *
from MiniTestFramework.GetUrlByQuery import *
from MiniTestFramework.PageObject import *


# Parameters for test. TODO In future may create config
cases = [
    ("w", "wikipedia.org"),
    ("imdb", "imdb.com"),
    ("g", "google.com"),
    ("so", "stackoverflow.com")
]

# Search query for tests
testQuery = 'test'


@pytest.yield_fixture
def driver():
    """Fixture for open browser and close after test."""
    _driver = webdriver.Firefox()
    yield _driver
    _driver.close()


@pytest.mark.parametrize("bang_id, expected", cases)
def test_check_ddg_api(driver, bang_id, expected):
    """This case check duckduckgo by their library."""

    # Header TODO In future may use logger
    print '\n{separate}'.format(separate='='*60)
    print 'Check DDG API'

    getUrlByDdgApi = GetUrlByDdgApi(bang_id, testQuery)
    url = getUrlByDdgApi.GetUrl()

    driver.get(url)

    # Print to console current page URL
    print 'Url getted by Api: {URL}'.format(URL=url)
    print 'Url parsed URL: {URL}'.format(URL=getUrlByDdgApi.GetDomainName())

    # Check expected result
    assert expected in getUrlByDdgApi.GetDomainName()

    # Check search results
    assert PageObject(driver).CheckQuery(testQuery)

    print '{separate}'.format(separate='=' * 60)


@pytest.mark.parametrize("bang_id, expected", cases)
def test_check_query(driver, bang_id, expected):
    """This case check duckduckgo by using they api query."""

    # Header
    print '\n{separate}'.format(separate='='*60)
    print 'Check query'

    getUrlByQuery = GetUrlByQuery(bang_id, testQuery)
    url = getUrlByQuery.GetUrl()
    driver.get(url)

    # Print to console current page URL
    print 'Url getted by query: {URL}'.format(URL=url)
    print 'Url parsed URL: {URL}'.format(URL=getUrlByQuery.GetDomainName())

    # Check expected result
    assert expected in getUrlByQuery.GetDomainName()

    # Check search results
    assert PageObject(driver).CheckQuery(testQuery)

    print '{separate}'.format(separate='=' * 60)
