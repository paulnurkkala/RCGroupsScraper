from check_rc_classifieds import * 

forum_url      = "fpv-equipment-fs-w-710/"
search_strings = ['dominator', 'dominators']

fr = ForumRunner(
	url = forum_url
)

results = fr.run()

search_results = fr.search(search_strings)
for res in search_results: 
	print "%s (%s)" % (res.title, res.price)