import re
import urllib.request
def get_page(url):
    return urllib.request.urlopen(url).read()

def get_note_links_from_page(url):
    content = get_page(url)

    pat = r'<id>http://api.douban.com/note/(.*?)</id>\\n\\t\\t<title>(.*?)</title>'

    pattern = re.compile(pat)

    ID_and_title = pattern.findall(str(content))

    result = {}
    for entry in ID_and_title:
    	link = ID_to_links(entry[0])
    	result[entry[1]] = link
    return result



def ID_to_links(note_id):
	return 'https://api.douban.com/v2/note/'+note_id