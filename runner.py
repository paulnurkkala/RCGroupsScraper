from check_rc_classifieds import * 


def rgc_runner_run(forum_url, search_strings): 
	fr = ForumRunner(url=forum_url)

	results = fr.run()

	search_results = fr.search(search_strings)
	for res in search_results: 
		if res.is_new: 
			print "%s (%s) new?%s" % (res.title, res.price, res.is_new)