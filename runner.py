from check_rc_classifieds import * 
from pushbullet import Pushbullet

def rgc_runner_run(forum_url, search_strings, pb_key): 
	fr = ForumRunner(url=forum_url)

	results = fr.run()

	search_results = fr.search(search_strings)
	for res in search_results: 
		if res.is_new: 
			print "%s (%s) new?%s" % (res.title, res.price, res.is_new)

			#if the pushbullet key is set, send a link to pushbullet containing the information and URL that we found
			if pb_key: 
				pb = Pushbullet(pb_key)
				found_text = 'RCGBot -- Match Found: %s %s' % (res.title, res.price)
				push = pb.push_link(found_text, res.url)