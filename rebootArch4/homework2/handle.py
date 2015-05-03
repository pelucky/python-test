#!/usr/local/python2.7.9/bin/python
#coding:utf-8

""" 
Made by pel for reboot task
https://github.com/51reboot/homework-arch-4/blob/master/2/Reboot%E8%BF%90%E7%BB%B4%E5%BC%80%E5%8F%91%E6%9E%B6%E6%9E%84%E5%B8%88%E7%8F%AD-%E4%BD%9C%E4%B8%9A-2.pdf
Name: Auto_seekMM v0.3
Desc: Handle the spider and upload to ftp
Auth: pel
Date: 2015.05.02
"""

import time,os
import myftp
import spider

def handle(config):
  print "Start! Pid %s is running to grep Page %s-%s." %(os.getpid(), str(config[0]), str(config[1]))
  begin_time = time.time()
  dbmm_spider = spider.Spider(config[:5])
  dbmm_spider.start()
  end_time = time.time()
  print "Pid %s Download used %is.(page %s-%s)" %(os.getpid(), end_time - begin_time, str(config[0]), str(config[1]))

  ftp = myftp.Myftp(config[5:])
  ftp.login_ftp()
  ftp.upload_file(dbmm_spider.dir_name, str(config[0])+"-"+str(config[1]))
  ftp.logout_ftp()
  ftp_end_time = time.time()
  print "Finish! Pid %s Upload to ftp used %ss.(page %s-%s)" %(os.getpid(), round(ftp_end_time - end_time, 2), str(config[0]), str(config[1]))
