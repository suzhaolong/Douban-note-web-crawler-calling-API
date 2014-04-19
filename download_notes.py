import re
import os
import urllib.request
def get_page(url):
    return urllib.request.urlopen(url).read().decode('utf-8', 'ignore')


def get_note_page(url,page_number):
	#http://www.douban.com/people/audreyang/
	pat     = r'http://www.douban.com/people/(.*?)/'
	pattern = re.compile(pat)
	ID      =  pattern.findall(str(url))
	#link = 'http://api.douban.com/people/audreyang/notes?start-index=1&max-results=20'
	return 'http://api.douban.com/people/'+ID[0]+'/notes?start-index=1&max-results='+str(page_number)

def exract_title_and_content(url):
	page_content = get_page(url)
	pat_title = r'<title>(.*?)</title>'
	pattern_title = re.compile(pat_title)
	note_title = pattern_title.findall(str(page_content))

	#(.*?)<content>(.*?)</content>

	pat_content = r'<content>(.*?)</content>'
	pattern_content = re.compile(pat_content)
	note_content = pattern_content.findall(str(page_content))
	note_list = {}

	for i in range(0,len(note_title)-1):
		note_list[note_title[i]] = note_content[i]
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
		#print(note_title)
