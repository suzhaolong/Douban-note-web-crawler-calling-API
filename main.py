#main.py
#coding=utf-8
import os
import sys
import urllib.request
from download_notes import *


url = input("Put the user's [Douban homepage] here:\n")

i = 0

note_count = 0

while True:
	note_page = get_note_page(url,1+i*10)

	page_title,note_list = exract_title_and_content(note_page)

	if note_list == {}:
		break
		# break the loop if all notes downloaded

	page_title = page_title.replace(" ","")
	
	if not os.path.exists(page_title):
		os.mkdir(page_title)

	download(note_list,page_title+'/'+'page '+str(i+1))

	if i == 0:
	# if the 1st note hasn't download, cover the original catalog(if exist) with 'w'
		file_object = open(page_title+'/'+'catalog.txt', 'w')
	else:
		file_object = open(page_title+'/'+'catalog.txt', 'a')

	file_object.write('* page '+str(i+1)+'\n\n')
	for title in note_list:
		file_object.write('--' + title+'\n')
		note_count += 1

	file_object.write('\n\n\n')
	file_object.close()
	i += 1
print('Done downloading, '+str(note_count)+' notes in total')


