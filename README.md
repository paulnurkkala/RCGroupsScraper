# RCGroupsScraper
A python tool to scrape RC groups home page to do automated searching for you, and notifies you when something that you're searching for pops up.

My goal is to have this grab all of the useful information from RC groups -- price, location, etc. Allow the user to decide what they want to be notified about, how they want to get that notification, and then be able to define what exactly they want the notification to include (price, location, URL, description, etc)

Installation and First Run
 * virtualenv env
 * . env/bin/activate 
 * pip install -r requirements.txt
 * set up your settings in rcg_bot.py ( they are the first arguments of the file )
 * python rcg_bot.py ( and it will start running and keep running )

Next steps 
 * Add a way to do "ands" and "ors" on the search strings
 * add filters so that you can decide what kinds of results you want to see


More Details can be found at (http://paulnurkkala.com/rcg-groups-scraper/)[RCGroupsScraper]