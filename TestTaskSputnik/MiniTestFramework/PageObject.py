class PageObject:

    def __init__(self, driver):
        self._driver = driver

    def GetTitle(self, url):
        """Get page title."""

        driver = self._driver
        driver.get(url)

        return driver.title

    def CheckQuery(self, query):
        """Check query."""
        driver = self._driver

        if 'google.com' in driver.current_url:
            return query in driver.title

        if 'wikipedia.org' in driver.current_url:
            return query.lower() in driver.title.lower()

        if 'imdb.com' in driver.current_url:
            return query in driver.find_element_by_class_name('findSearchTerm').text

        if 'stackoverflow.com' in driver.current_url:
            return query.lower() in driver.title.lower()
