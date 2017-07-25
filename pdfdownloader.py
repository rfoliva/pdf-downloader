#!/usr/bin/env python
"""Script to scrape through provided URL, identify all of the PDF file links
available for download, with methods for downloading and merging them into a
single PDF.
"""

# TODO: Improve Docstrings and comments overall code.


import requests
from lxml import html


__version__ = "0.1"
__author__ = "Ricardo Oliva"


def request_url():
    """Function to request URL from user.

    :return: url
    """
    try:
        url = input("What is the URL to scrape for PDFs? ")
    except:
        print("Error while reading URL from user!")
        raise

    # FIXME: Remove hardcoded URL used for testing.
    # TODO: Implement means to get URL from user (CLI or input()).

    # return url
    return "http://epe.lac-bac.gc.ca/100/200/300/allan_publishing/history_personal_computer/index.html"

def get_pdflist(url):
    """Function to obtain list of links for PDFs on specific page.

    :return:
    """
    page = requests.get(url)
    html_content = html.fromstring(page.content)
    print(html_content.xpath('href'))


def main():
    target_url = request_url()
    print(get_pdflist(target_url))


if __name__ == '__main__':
    main()
