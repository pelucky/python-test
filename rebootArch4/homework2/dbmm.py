#!/usr/local/python2.7.9/bin/python
#coding:utf-8

""" 
Made by pel for reboot task
https://github.com/51reboot/homework-arch-4/blob/master/2/Reboot%E8%BF%90%E7%BB%B4%E5%BC%80%E5%8F%91%E6%9E%B6%E6%9E%84%E5%B8%88%E7%8F%AD-%E4%BD%9C%E4%B8%9A-2.pdf
Name: Auto_seekMM v0.3
Desc: run the python with multiProcessing of Pool
Auth: pel
Date: 2015.05.03
Useage:./dbmm.py begin_page end_page url regular dir_name ftp_ip ftp_username ftp_passwd ftp_url
Output: tiltle_name's image in the dir_name
"""

import time,sys,os
import myftp
from multiprocessing import Pool
import handle

if __name__ == "__main__":
  # Set the default value: include spider and ftp
  process_number = 5
  '''
  configure = { "begin_page" : 0,
      "end_page" : 1,
      "url" : "http://www.dbmeizi.com/?p=",
      "regular" : '<img\sclass=.*data-src="(.*)"\salt.*data-title="(.*)"\sdata-url',
      "dir_name" : "dbmeizi_" + time.strftime("%y%m%d_%H%M"),
      "ftp_ip" = "172.18.216.168",
      "ftp_username" = "xxx",
      "ftp_passwd" = "xxx",
      "ftp_url" = "./ftp/=D= 影音娱乐/豆瓣妹子"
      }
  '''
  config = [0,
      1,
      "http://www.dbmeizi.com/?p=",
      '<img\sclass=.*data-src="(.*)"\salt.*data-title="(.*)"\sdata-url',
      "dbmeizi_" + time.strftime("%y%m%d_%H%M"),
      "172.18.216.168",
      "xxx",
      "xxx",
      "./ftp/=D= 影音娱乐/豆瓣妹子"]
   
  print "Usage: ./dbmm.py begin_page end_page url regular dir_name ftp_ip ftp_username ftp_passwd ftp_url"
  print "The default begin = 0,the end = 1, spider dbmm' image and upload to ftp"

  begin_time = int(time.time())
  argv_length = len(sys.argv) - 1

  # Python 2.X doesn't support variable length value and default value together
  # It has 2 vales
  if argv_length >= 1:
    for i in range(argv_length):
      config[i] = sys.argv[i+1]
    if (int(config[0]) >= int(config[1])):
      print "The begin page must smaller than end page!"
      sys.exit(1)
    # page is little, use single process
    if (int(config[1]) - int(config[0]) < process_number):
      handle.handle(config)
    # Use multiProcessing
    else:
      pages = int(config[1]) - int(config[0])
      process_pages = pages / process_number
      print 'Parent process is %s.' %(os.getpid())
      # Use processs_number processes
      pool = Pool(processes=process_number)
      # Make a copy to config
      temp_config = list(config)
      # Have process_number jobs to do  
      for i in xrange(process_number):
        temp_config[0] = int(config[0]) + i * process_pages
        if (i != process_number - 1 ):
          temp_config[1] = int(config[0]) + (i+1) * process_pages
        else:
          temp_config[1] = int(config[1])
        # print "page %i-%i" %(temp_config[0], temp_config[1])
        # make sure temp_config is pass by value not reference, so use list()
        pool.apply_async(handle.handle, args=(list(temp_config),))
      print "Waiting for all subprocesses done..."
      pool.close()
      pool.join()
  # Use the default value cos no argv
  else:
    handle.handle(config)

  end_time = int(time.time())
  print "Task complete(Page %i-%i)! Totally used %is." %(int(config[0]), int(config[1]), end_time - begin_time)
