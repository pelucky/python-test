#!/usr/local/python2.7.9/bin/python
#coding:utf-8

""" 
Des: Use for ftp upload
"""
import os
from ftplib import FTP

# my ftp client to upload data
class Myftp:
  '''My ftp'''
  def __init__(self, ftp_ip = "172.18.216.168", ftp_username = "zigbee", ftp_passwd = "zigbee2014"):
    '''Set the configure'''
    self.ftp_ip = ftp_ip
    self.ftp_username = ftp_username
    self.ftp_passwd = ftp_passwd
    self.url = "./ftp/=D= 影音娱乐/豆瓣妹子"
    self.ftp = FTP(self.ftp_ip)
  
  def login_ftp(self):
    self.ftp.login(self.ftp_username, self.ftp_passwd)
    self.ftp.cwd(self.url)
    self.ftp.retrlines('LIST')
    
  def upload_file(self, dir_name):
    self.ftp.mkd(dir_name)
    self.ftp.cwd(dir_name)
    files = os.listdir("./")
    for f in files:
      fh = open(f, 'rb')
      self.ftp.storbinary('STOR %s' % f, fh)
      fh.close()
    self.ftp.cwd("../")
  
  def download_file(self):
    pass

  def logout_ftp(self):
    self.ftp.quit()

if __name__ == "__main__":
  ftp = Myftp()
