#!/usr/local/python2.7.9/bin/python
#coding:utf-8

""" 
Made by pel for reboot task
https://github.com/51reboot/homework-arch-4/blob/master/2/Reboot%E8%BF%90%E7%BB%B4%E5%BC%80%E5%8F%91%E6%9E%B6%E6%9E%84%E5%B8%88%E7%8F%AD-%E4%BD%9C%E4%B8%9A-2.pdf
Auto_seekMM v0.1
Des: 使用urllib2、正则表达式、ftp
"""
import urllib
import urllib2
import os
import shutil
import time
import re
from ftplib import FTP

if __name__ == "__main__":
  # Set the configura
  page = 0
  mm_Number = 1
  dir_name = "dbmeizi_" + time.strftime("%y%m%d_%H%M")
  user_agent = "Mozilla/5.0 (Windows NT 5.1)"
  headers = { 'User_Agent': user_agent}
  
  if os.path.isdir(dir_name) is True:
    print "The dir is exist, Delet the old and make new!"
    shutil.rmtree(dir_name)    
  os.mkdir(dir_name,0744)
  os.chdir(dir_name)
  print "Make dir success: %s." %(dir_name)
  
  # Get the URL
  while (page < 5):
    url = "http://www.dbmeizi.com/?p=" + str(page)
    request = urllib2.Request( url, None, headers )
    try:
      response = urllib2.urlopen(request)
      content = response.read()
    except:
      print "Error downLoading name: %s ." %(url)
      continue

    # print content

    # image_name = re.findall(r'<img\sclass=.*data-src="(.*)"\salt',content)
    # title_name = re.findall(r'<img\sclass=.*data-title="(.*)"\sdata-url',content)
    image_name = re.findall(r'<img\sclass=.*data-src="(.*)"\salt.*data-title="(.*)"\sdata-url',content)
    
    # print image_name
    for url_title in image_name:
      #print i[0],i[1]
      img_url = url_title[0]
      img_name = str(mm_Number) + "_" +url_title[1] + '.jpg'
      print img_name
      try:
        #urllib.urlretrieve(img_url,img_name)
        img_head = urllib.urlopen(img_url)
        f = open(img_name, 'wb')
        while True:
          s = img_head.read(1024*32)
          if len(s) == 0:
            break
          f.write(s)
        mm_Number += 1
      except IOError:
        print "Error downloading name: %s ." %(img_name) 
      #if mm_Numuber >= 5:
      #  break
    page += 1
  
  # put pic into ftp server
  ftp_IP = "172.18.216.168"
  ftp_username = "xxxxxx"
  ftp_passwd = "xxxxxxx"
  ftp_url = "./ftp/=D= 影音娱乐/豆瓣妹子"
  
  ftp = FTP(ftp_IP)
  ftp.login(ftp_username,ftp_passwd)
  ftp.cwd(ftp_url)
  ftp.retrlines('LIST')
  
  # upload the images to ftp
  ftp.mkd(dir_name)
  ftp.cwd(dir_name)
  files = os.listdir("./")
  for f in files:
    fh = open(f, 'rb')
    ftp.storbinary('STOR %s' % f, fh)
    fh.close()
  ftp.quit()
      


