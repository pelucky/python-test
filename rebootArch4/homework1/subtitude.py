#!/usr/local/python2.7.9/bin/python
#coding:utf-8

""" 
Made by pel for reboot task
https://github.com/51reboot/homework-arch-4/blob/master/1/Reboot%E8%BF%90%E7%BB%B4%E5%BC%80%E5%8F%91%E6%9E%B6%E6%9E%84%E5%B8%88%E7%8F%AD-%E4%BD%9C%E4%B8%9A-1.pdf
"""

import sys
import os

def replace_file(file_name,sea_str,rep_str):
  length = len(sea_str)
  read_bytes = 2*length
  f = open(file_name,'r+')
  temp_string = f.read(read_bytes)
  # print "temp_sting is " + temp_string
  while (temp_string != 0):
    position = f.tell()
    # print "position is %d" %(position)
    if(temp_string.find(sea_str) != -1):
      temp_string = temp_string.replace(sea_str,rep_str)
      # print "temp_string is %s" %(temp_string)
      f.seek(-read_bytes,1)
      f.write(temp_string)
    next_string = f.read(length)
    # print "next_string is %s" %(next_string)
    if ( len(next_string) != 0 ):
      temp_string = temp_string[length:] + next_string
      # print "The temp_string after is %s" %(temp_string)
    else:
      break;
  f.close()


if __name__ == "__main__":
  if len(sys.argv) < 4:
    print "参数少于三个！"
    sys.exit()
  else:
    filename = sys.argv[1]
    search_str = sys.argv[2]
    change_str = sys.argv[3]
    if os.path.exists(filename) is False:
      print "文件不存在，请创建"
      sys.exit()
    else:
      replace_file(filename,search_str,change_str)
