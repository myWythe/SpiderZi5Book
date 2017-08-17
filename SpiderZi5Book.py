#!/usr/bin/python
#-*- coding: utf-8 -*-
#encoding=utf-8

import urllib2
import os
import re
from bs4 import BeautifulSoup
import time


# 下载文件
def downloadBook(bookLink):
    
    req = urllib2.Request(bookLink)
    req.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36')
    response = urllib2.urlopen(req)
    return response.read()

# 解析书籍下载链接
def parseBookDownloadLink(bookPageLink):

    html = urllib2.urlopen(bookPageLink).read()
    soup = BeautifulSoup(html,"html.parser")
    downloadTag = soup.findAll('a',attrs={"class":"download-link"})

    downloadlinks = []
    for item in downloadTag:
    	downloadlinks.append(item.get('href'))


    # return [epubDownloadLink,mobiDownloadLink]
    return downloadlinks

# 解析书名
def parseBookName(bookPageLink):

    html = urllib2.urlopen(bookPageLink).read()
    
    soup = BeautifulSoup(html,"html.parser")

    titleTag = soup.findAll('div',attrs={"class":"h1-wrapper"})[0]
    title = titleTag.text

    print "Book Name:"+title
    return title

# 保存书籍文件
def saveFile(bookPageLink, bookFolder):

    bookName = parseBookName(bookPageLink)

    #因为要创建文件夹，故而等去除空格等
    detailFolder = bookFolder + "_".join(bookName.split())
    os.chdir(bookFolder)

    isExists=os.path.exists(detailFolder)
    if not isExists:
        os.mkdir(detailFolder)
    os.chdir(detailFolder)

    # 解析出下载链接
    downloadlinks = parseBookDownloadLink(bookPageLink)
    # print downloadlinks

    for link in downloadlinks:

    	# 拼接出完成的文件名
        filetype = link.split('.')[-1]
        filename = bookName + "." + filetype

        downloadFile = downloadBook(link)
        with open(filename, 'wb') as f:
            f.write(downloadFile)
            f.close()

# 解析出书页链接
def parseBookPageLink(bookListPageLink):

	html = urllib2.urlopen(bookListPageLink).read()
	soup = BeautifulSoup(html,"html.parser")
	bookTag = soup.findAll('div',attrs={"class":"thumb-holder"})

	bookLinks=[]
	for item in bookTag:
		bookLinkTag = item.a
		bookpageLink = bookLinkTag.get('href')
		bookLinks.append(bookpageLink)

	return bookLinks


# 下载子乌书简的书，希望下到的读者不要下的次数太多，对他们的服务器造成困扰
def downloadZi5Book():

	filesavepath = '/WytheData/Book/'
	basePageListLink =  "http://book.zi5.me/page/"

	for page in range(1,51):

		listPageLink = basePageListLink + str(page)
		print listPageLink
		bookLinks = parseBookPageLink(listPageLink)
		for book in bookLinks:
			print "Page " + str(page)
			saveFile(book, filesavepath)
		print "Wait a while"
		# 等待一会，避免造成太大的压力，同时也避免被封
		time.sleep(5)

	print "Download all finish"


if __name__ == '__main__':
    downloadZi5Book()