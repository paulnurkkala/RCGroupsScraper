from bs4 import BeautifulSoup
import requests

#url = raw_input("")
r  = requests.get("http://www.rcgroups.com/fpv-equipment-fs-w-710/")

search_strings = ['dominator', 'dominators']

data = r.text
soup = BeautifulSoup(data)

matches = []

for string in search_strings: 
    string = string.lower()

    for link in soup.find_all('a', {'class': 'fsw-title'}):
        link_text = link.text.lower()         
    
        if string in link_text: 
            matches.append(link)


matches = set(matches)

for match in matches: 
    print match.text
