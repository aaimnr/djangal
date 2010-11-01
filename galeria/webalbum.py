#!/usr/bin/env python
# encoding: utf-8
"""
webalbum.py

Created by Am on 2010-10-31.
Copyright (c) 2010. All rights reserved.
"""

import sys
import os
import gdata.photos.service
import gdata.media
import gdata.geo

def textOrEmpty(x):
	return x if x is not None else ""

def getPhotosHtml():
	client = getAuthClient()
	photos = getPhotos(client)
	out = ""
	for photo in photos.entry:
		out+= "<a href='%s'><img src='%s'/></a><span>%s</span>\n" % (photo.content.src, photo.media.thumbnail[0].url, textOrEmpty(photo.summary.text))
	return out
		

def getAuthClient():
	gd_client = gdata.photos.service.PhotosService()
	gd_client.email = 'ha5en1@gmail.com'
	gd_client.password = 'Yasgma62'
	#gd_client.source = 'exampleCo-exampleApp-1'
	gd_client.ProgrammaticLogin()
	return	gd_client
	
def getPhotos(gd_client):
	album = gd_client.GetUserFeed().entry[0]
	photos = gd_client.GetFeed('/data/feed/api/user/default/albumid/%s?kind=photo' % (album.gphoto_id.text))
	return photos

def main():
	gd_client = gdata.photos.service.PhotosService()
	gd_client.email = 'ha5en1@gmail.com'
	gd_client.password = 'Yasgma62'
	#gd_client.source = 'exampleCo-exampleApp-1'
	gd_client.ProgrammaticLogin()
	
	albums = gd_client.GetUserFeed()
	for album in albums.entry:
	  print 'Album: %s (%s)' % (album.title.text, album.numphotos.text)

	  photos = gd_client.GetFeed('/data/feed/api/user/default/albumid/%s?kind=photo' % (album.gphoto_id.text))
	  for photo in photos.entry:
	    print '  Photo:', photo.title.text

	    tags = gd_client.GetFeed('/data/feed/api/user/default/albumid/%s/photoid/%s?kind=tag' % (album.gphoto_id.text, photo.gphoto_id.text))
	    for tag in tags.entry:
	      print '    Tag:', tag.title.text

	    comments = gd_client.GetFeed('/data/feed/api/user/default/albumid/%s/photoid/%s?kind=comment' % (album.gphoto_id.text, photo.gphoto_id.text))
	    for comment in comments.entry:
	      print '    Comment:', comment.content.text


if __name__ == '__main__':
	main()

