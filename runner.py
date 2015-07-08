from check_rc_classifieds import * 

forum_url      = "fpv-equipment-fs-w-710/"
#forum_url      = "aircraft-electric-batteries-and-chargers-fs-w-284/"
search_strings = ['fatshark', 'dominator']

fr = ForumRunner(url=forum_url)

results = fr.run()

search_results = fr.search(search_strings)
for res in search_results: 
	if res.is_new: 
		print "%s (%s) new?%s" % (res.title, res.price, res.is_new)