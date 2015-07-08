"""
	Simply call: rcg_bot.py() with the two arguments, forum_url and search_strings (an array) to run the bot and check a page for a string 

	forum_url      = "fpv-equipment-fs-w-710/"
	search_strings = ['fatshark', 'dominator']

"""

from runner import * 
import time

forum_url       = "fpv-equipment-fs-w-710/"    #the last bit of the URL on an RC groups forum page 
search_strings  = ['fatshark', 'dominator']    #the OR string to serach for (returns all results matching these values, checking against their name on RC groups)
repeat_interval = 10                           #time to repeat in seconds 


def run_the_runner():
    #code here
    print "Starting Execution Loop"

    rgc_runner_run( forum_url, search_strings)

    #run this thing every x seconds 
    time.sleep(repeat_interval)

while True:
    run_the_runner()