import re
import urllib.request
def get_page(url):
    return urllib.request.urlopen(url).read()


def get_note_page(url,page_number):
	#http://www.douban.com/people/audreyang/
	pat     = r'http://www.douban.com/people/(.*?)/'
	pattern = re.compile(pat)
	ID      =  pattern.findall(str(url))
	#link = 'http://api.douban.com/people/audreyang/notes?start-index=1&max-results=20'
	return 'http://api.douban.com/people/'+ID[0]+'/notes?start-index=1&max-results='+str(page_number)

def exract_title_and_content(url):
	content = get_page(url)
	pat = r'<title>(.*?)</title>(.*?)<content>(.*?)</content>'
	pattern = re.compile(pat)
	useful = pattern.findall(str(content))
	#return useful
	title_and_link = {}
	for note in useful:
		title_and_link[note[0]] = note[2]
	return title_and_link





