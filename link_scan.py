from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def get_links(url):
    """Find all links on page at the given url.

    Returns:
        a list of all unique hyperlinks on the page,
        without page fragments or query parameters.
    """
    browser = webdriver.Chrome('chromedriver.exe')
    browser.get(url)
