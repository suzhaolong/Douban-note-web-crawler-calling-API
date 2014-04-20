#coding=utf-8
import os
import urllib.request
from download_notes import *
#name = audreyang

url = 'http://www.douban.com/people/audreyang/'


for i in range(0,3):
	note_page = get_note_page(url,1+i*10)
	#note_page_list.append(get_note_page(url,i*10))

	page_title,note_list = exract_title_and_content(note_page)

	page_title = page_title.replace(" ","")
	
	if not os.path.exists(page_title):
		os.mkdir(page_title)

	download(note_list,page_title+'/'+'page '+str(i+1))

	file_object = open(page_title+'/'+'catalog.txt', 'a')
	file_object.write('* page '+str(i+1)+'\n\n')
	for title in note_list:
		file_object.write('--' + title+'\n')

	file_object.write('\n\n\n')
	file_object.close()



