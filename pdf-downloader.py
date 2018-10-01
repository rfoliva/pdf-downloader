#!/usr/bin/env python3


import requests
import sys


""" Downlaod
"""
def download_files(path, urls_to_download):
    """ Function expects to receive list composed of URLs of files to be
    downloaded.

    param urls_to_download: list
    returns: 
    """
    downloaded_files = []
    for url in urls_to_download:
        if url.find('/'):
            filename = url.rsplit('/', 1)[1]
        try:
            print("\n" + "Downloading " + filename + " ...")
            r = requests.get(url, allow_redirects=True)
            open(path + filename, 'wb').write(r.content)
        except requests.exceptions.RequestException as err:
            print(err)
            sys.exit(1)
        downloaded_files.append(path + filename)
        print(filename + " has been downloaded successful!")
    print()
    return downloaded_files

def pdf_merge(parameter_list):
    pass

def main():
    files_to_download = ['http://google.com/favicon.ico', 'http://aviaryan.in/images/profile.png']
    print(download_files('/tmp/', files_to_download))
    

if __name__ == '__main__':
    main()
