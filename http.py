#-*- coding:utf-8 -*-

import sys, os, re
import urllib, urllib2, cookielib, json
from lxml import etree
from lxml.html import fromstring



class http_hack:
  def __init__(self):
    self.user_agent = ('User-Agent:', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36')
    self.agent = ('Agent:', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')
    self.accept_encoding = ('Accept-Encoding:', 'gzip,deflate,sdch')
    self.accept_language = ('Accept-Language:', 'zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4')
    self.connection = ('Connection:', 'keep-alive')
    self.host = ''
    self.Client_IP = ''
    self.X_Forwarded_For = ''
    self.X_Requested_With = ''

  class http_code:
    def __init__(self):
      self.url = ''
      self.tag = ''
      self.tagRule = ''
      self.page = ''

    def get_html(self, hd):
      h = urllib2.HTTPHandler()
      urlOpener = urllib2.build_opener(h)
      headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
     
      req = urllib2.Request(self.url, headers = headers)
      #soup = urllib2.urlopen(req).read()
      soup = urlOpener.open(req).read()
    
      return soup

    def linksearch(self, headers = {}):
      
      #headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
      #print headers
      req = urllib2.Request(self.url, headers = headers)
      page = urllib2.urlopen(req).read()
      

      doc = fromstring(page)
      return doc
    
def add_handler(self):
  hd = []
  for h in self.user_agent, self.agent, self.accept_encoding, self.accept_language, \
                 self.connection, self.host, self.Client_IP, \
		 self.X_Forwarded_For, self.X_Requested_With:
    if not h == '' :
      hd.append(h)

  return hd



