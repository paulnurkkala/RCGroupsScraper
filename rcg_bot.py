"""
	Simply call: rcg_bot.py() with the two arguments, forum_url and search_strings (an array) to run the bot and check a page for a string 

	forum_url      = "fpv-equipment-fs-w-710/"
	search_strings = ['fatshark', 'dominator']

                             ___________________  
                             \______   \_   ___ \ 
                              |       _/    \  \/ 
                              |    |   \     \____
                              |____|_  /\______  /
                                     \/        \/ 
           __________________ ________   ____ _____________  _________
          /  _____/\______   \\_____  \ |    |   \______   \/   _____/
         /   \  ___ |       _/ /   |   \|    |   /|     ___/\_____  \ 
         \    \_\  \|    |   \/    |    \    |  / |    |    /        \
          \______  /|____|_  /\_______  /______/  |____|   /_______  /
                 \/        \/         \/                           \/ 
      ____________________________    _____ _______________________________ 
     /   _____/\_   ___ \______   \  /  _  \\______   \_   _____/\______   \
     \_____  \ /    \  \/|       _/ /  /_\  \|     ___/|    __)_  |       _/
     /        \\     \___|    |   \/    |    \    |    |        \ |    |   \
    /_______  / \______  /____|_  /\____|__  /____|   /_______  / |____|_  /
            \/         \/       \/         \/                 \/         \/ 	

"""

from runner import * 
import time

forum_url       = "fpv-equipment-fs-w-710/"    #the last bit of the URL on an RC groups forum page 
search_strings  = ['fatshark', 'dominator', 'fat shark']    #the OR string to serach for (returns all results matching these values, checking against their name on RC groups)
repeat_interval = 60                           #time to repeat in seconds 
pushbullet_key  = "PUSHBULLET KEY HERE"        #set to null if you aren't going to use pushbullet


def run_the_runner():
    #code here
    print "Starting Execution Loop"

    rgc_runner_run( forum_url, search_strings, pushbullet_key)

    #run this thing every x seconds 
    time.sleep(repeat_interval)

while True:
    run_the_runner()