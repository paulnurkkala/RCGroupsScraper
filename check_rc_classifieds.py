from bs4 import BeautifulSoup
import requests
import json

#url = raw_input("")
class RCGItem(object): 

    def __init__(self, *args, **kwargs):
        self.attributes  = ['title', 'description', 'price', 'url', 'status', 'is_new']

        #loop through attributes and set them based on what's passed in 
        for attr in self.attributes:
            setattr(self, attr, kwargs.get(attr))

    def to_array(self):
        results = []
        for attr in self.attributes:
            results.append(getattr(self, attr))

        return results

    def is_sold(self): 
        return self.status.lower() == 'sold'

    def is_wanted(self): 
        return self.status.lower() == 'wanted'

    def is_for_sale(self):
        return self.status.lower() == 'for sale'

class ForumRunner(object): 

    def __init__(self, *args, **kwargs):
        """
            Saves the strings
        """
        self.base_url       = "http://www.rcgroups.com/"

        self.search_strings = kwargs.get('search_strings')
        self.url            = kwargs.get('url')

    def run(self):
        """
            Runs the script, getting the information out of the forum 
        """
        #get the page, get the text from the page, and then make a beautiful soup object, which will help parse this whole beast
        r  = requests.get(self.base_url + self.url)
        data = r.text
        soup = BeautifulSoup(data)
        
        #get the main table and then get every row within it 
        body = soup.find('table', {'class': 'tborder-rcgplus'})
        rows = body.find_all('tr')
        
        #this will contain all results for the page that we hit
        items = []
        
        #loop through every row that was found in the search using beutiful soup 
        for row in rows: 
        
            #initiate some empty variables that will be saved back to the RCGItem
            price       = 0
            title       = ''
            description = ''
            url         = ''
            status      = ''
        
            #find LINK information, including the URL and text 
            for link in row.find_all('a', {"class": "fsw-title"}):
                title       = link.text.strip()
                url         = self.base_url + link.attrs['href'].strip()
                description = link.attrs.get('data-tip').strip()
        
            #find FOR SALE STATUS 
            for link in row.find_all('div', {"class": "fsw-category"}):
                status = link.find('span').text.strip()
        
            #find price 
            for link in row.find_all('div', {"class": "fsw-price-text"}):
                price = link.text.strip()
        
            result = RCGItem(
                title       = title, 
                url         = url, 
                description = description, 
                price       = price, 
                status      = status,
                is_new      = False
            )
        
            #the first element is often blank
            if result.title: 
                items.append(result)

        self.results = items
        return items

    def search(self, search_strings):
        """
            given an array of strings to search for, search them against the things found on the front page of RCClassifieds
        """     
        search_results = []

        #loop through the strings, because that will give us the lowest number of loops 
        for sstring in search_strings:

            #loop through items in self.results
            for item in self.results: 
                if item.is_for_sale():
        
                    #check to see if the search string is in this particular item 
                    if sstring.lower() in item.title.lower():

                        #if we find a result, stick it on to the total results
                        search_results.append(item)

        #since we may have found duplicates, pull the duplicates out 
        search_results = list(set(search_results))

        #send the search results back to the home page 
        for result in search_results: 
            is_new = self.save_search(result.url)
            result.is_new = is_new

        return search_results

    def save_search(self, url):
        """
            This records which things have already been searched for. It saves all new things over so that notifications aren't sent to you over and over agian. 
        """
        all_urls = []
        urls = None
        is_new = False 

        #open the local json file containing the list of URLS that have already been located 
        with open('urls.json') as data_file:
            urls = []

            #try to load in json list
            try:
                urls = json.load(data_file)

            #this essentially assumes that the json list is blank/empty and just overrides it all with a default 
            except ValueError:
                urls = {'urls': []}

            #if there are urls to grab, grab then 
            json_urls = urls['urls']

            #check to see if the URL we are working with is already added. 
            #This will be the return value for the function 
            is_new = url not in json_urls

        #do this outside of the context of the file being open 
        if is_new: 

            #plop the new url down on the end of the array 
            #take the new array, remove any duplicates anywhere 
            json_urls.append(url)
            urls['urls'] = list(set(json_urls))
    
            #write the whole thing back into the file 
            with open('urls.json', 'w') as outfile:
                json.dump(urls, outfile)

        #return whether or not we added a new URL to the list     
        return is_new

