#!/usr/local/python2.7.9/bin/python
#coding:utf-8

""" 
Made by pel for test by using cookies
"""

import urllib
import urllib2
import cookielib

if __name__ == "__main__":
  filename = 'cookie.txt'
  cookie = cookielib.MozillaCookieJar(filename)
  opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
  loginurl = "http://ecampus.sysu.edu.cn/zsuyy/login_normal.jsp"
  user_agent = "Mozilla/5.0 (Windows NT 5.1)"
  headers = { 'User_Agent': user_agent}

  # geturl = url + "?" + data
  response = opener.open(loginurl,postdata)
  cookie.save(ignore_discard=True, ignore_expires=True)
  #gradeUrl =  'http://ecampus.sysu.edu.cn/zsuyy/yanyuan/xw/xwChaXunGeRenXueWeiDaBian.do?method=initEnter'
  #response = opener.open(gradeUrl)
  print response.read()


