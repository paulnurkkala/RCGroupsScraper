from bs4 import BeautifulSoup
import requests

#url = raw_input("")
class RCGItem(object): 

	def __init__(self, *args, **kwargs):
		self.attributes  = ['title', 'description', 'price', 'url', 'status']


		#loop through attributes and set them based on what's passed in 
		for attr in self.attributes:
			setattr(self, attr, kwargs.get(attr))

	def to_array(self):
		results = []
		for attr in self.attributes:
			results.append(getattr(self, attr))

		return results


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
				status      = status
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

				#check to see if the search string is in this particular item 
				if sstring.lower() in item.title.lower():

					#if we find a result, stick it on to the total results
					search_results.append(item)

		#since we may have found duplicates, pull the duplicates out 
		search_results = set(search_results)

		#send the search results back to the home page 
		return search_results


		
