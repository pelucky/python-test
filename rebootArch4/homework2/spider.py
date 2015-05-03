#!/usr/local/python2.7.9/bin/python
#coding:utf-8

""" 
Made by pel for reboot task
https://github.com/51reboot/homework-arch-4/blob/master/2/Reboot%E8%BF%90%E7%BB%B4%E5%BC%80%E5%8F%91%E6%9E%B6%E6%9E%84%E5%B8%88%E7%8F%AD-%E4%BD%9C%E4%B8%9A-2.pdf
Name: spider.py
Desc: 使用urllib2、正则表达式 修改为类的结构
Auth: pel
Date: 2015.04.30
Useage:./spider.py 
"""
import urllib
import urllib2
import shutil
import time,sys,os
import re

# spider
class Spider:
  '''Spide's class for curl web'''
  def __init__(self, config):
    '''Set the configure'''
    self.page = int(config[0])
    self.end_page = int(config[1])
    self.url = config[2]
    self.regular = config[3]
    self.dir_name = config[4]
    
    self.mm_pic = 1
    self.user_agent = "Mozilla/5.0 (Windows NT 5.1)"
    self.headers = { 'User_Agent': self.user_agent }
            
  def get_page(self, current_page):
    url = self.url + str(current_page)
    request = urllib2.Request( url, None, self.headers )
    try:
      # Timeout is 4s
      response = urllib2.urlopen(request, None, 4)
      content = response.read()
      self.load_page(content)
    except:
      print "Error get page: %s ." %(url)
      
  def load_page(self, current_content):
    url_name_list = re.findall(self.regular, current_content)
    for url_name in url_name_list:
      img_url = url_name[0]
      img_name = str(self.mm_pic) + '_' + url_name[1] + '.jpg'
      print img_name + ' FROM ' + img_url
      self.download_data(img_url, img_name)

  def download_data(self, current_img_url, current_img_name):
    '''Enable get big data'''
    try:
      # Timeout is 4s
      img_head = urllib2.urlopen(current_img_url, None, 4)
      f = open(current_img_name, 'wb')
      while True:
        data = img_head.read(1024*16)
        if len(data) == 0:
          break
        f.write(data)
      f.close() 
      self.mm_pic += 1
    except IOError:
      print "Error downloading file: %s ." %(current_img_name) 

  def start(self):
    if os.path.isdir(self.dir_name) is False:
      #print "The dir is exist, Delet the old and make new!"
      #shutil.rmtree(self.dir_name)    
      os.mkdir(self.dir_name, 0744)
    os.chdir(self.dir_name)
    sub_dir = str(self.page) + "-" + str(self.end_page)
    os.mkdir(sub_dir, 0744)
    os.chdir(sub_dir)
    print r"Make dir success: ./%s/%s " %(self.dir_name, sub_dir)
    while(self.page < self.end_page):
      self.get_page(self.page)
      self.page += 1
