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
  def __init__(self,config):
    '''Set the configure'''
    self.ftp_ip = config[0]
    self.ftp_username = config[1]
    self.ftp_passwd = config[2]
    self.ftp_url = config[3]
  
  def login_ftp(self):
    self.ftp = FTP(self.ftp_ip)
    self.ftp.login(self.ftp_username, self.ftp_passwd)
    self.ftp.cwd(self.ftp_url)
    # self.ftp.retrlines('LIST')
    
  def upload_file(self, dir_name, sub_dir_name):
    try:
      self.ftp.mkd(dir_name)
    except:
      print "The dir is exists!"
    finally:
      self.ftp.cwd(dir_name)
    
    try:
      self.ftp.mkd(sub_dir_name)
    except:
      print "The sub dir is exists!"
    finally:
      self.ftp.cwd(sub_dir_name)
    files = os.listdir("./")
    for f in files:
      fh = open(f, 'rb')
      self.ftp.storbinary('STOR %s' % f, fh)
      fh.close()
    self.ftp.cwd("../../")
  
  def download_file(self):
    pass

  def logout_ftp(self):
    self.ftp.quit()
