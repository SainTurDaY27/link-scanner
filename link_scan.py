import sys
from typing import List
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests


def get_links(given_url):
    """Find all links on page at the given url.

    Returns:
        a list of all unique hyperlinks on the page,
        without page fragments or query parameters.
    """
    browser = webdriver.Chrome()
    browser.get(given_url)
    input_url = browser.find_elements(By.TAG_NAME, 'a')
    hyperlink_list = []
    for each_url in input_url:
        each_url = each_url.get_attribute('href')
        if each_url is not None:
            if ("?" in each_url) or ("#" in each_url):
                # remove query string from url.
                each_url = each_url.split("?")[0].split("#")[0]
            hyperlink_list.append(each_url)
    return list(set(hyperlink_list))


def is_valid_url(given_url: str):
    """Check that given url is valid.
    """
    return requests.head(given_url).ok


def invalid_urls(url_list: List[str]) -> List[str]:
    """Validate the urls in url_list and return a new list containing
    the invalid or unreachable urls.
    """
    bad_url = []
    for each_url in url_list:
        if is_valid_url(each_url) is False:
            bad_url.append(each_url)
    return bad_url


if __name__ == '__main__':
    # test url from running this file.
    # url = "https://cpske.github.io/ISP/"

    url = sys.argv[1]
    links = get_links(url)
    print()

    # display all link.
    print("All links found on the page: ")
    for link in links:
        print(link)
    print()

    # display all bad link.
    print("All bad links: ")
    for bad_link in invalid_urls(links):
        print(bad_link)
    print()
