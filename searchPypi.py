#! python3
# searchPypi.py - Opens several search results.

import requests, sys, webbrowser, bs4
res = requests.get("https://pypi.org/search/?q=" + sys.argv[1])
res.raise_for_status()

# Retrieve search result links.
soup = bs4.BeautifulSoup(res.text, "html.parser")
# Open a browser tab for each result.
linkElems = soup.select(".package-snippet")
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    urlToOpen = "https://pypi.org" + linkElems[i].get("href")
    print(f"Opening {urlToOpen}...")
    webbrowser.open(urlToOpen)