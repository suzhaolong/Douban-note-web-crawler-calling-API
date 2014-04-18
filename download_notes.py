import re
import os
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
	note_list = {}
	for note in useful:
		note_list[note[0]] = note[2]
	return note_list


def download(note_list,dir):
	if not os.path.exists(dir):
		os.mkdir(dir)
		#print('nothing')
	for note_title in note_list:
		file_object = open(dir + '/' + note_title.replace('/','|') + '.html', 'w')
        # '/' is not allowed to use in a filename under HFS+(OS X)

		file_object.write(note_list[note_title])
	file_object.close()
