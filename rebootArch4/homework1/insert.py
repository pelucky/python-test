#!/usr/local/python2.7.9/bin/python
#coding:utf-8

""" 
Made by pel for reboot task
https://github.com/51reboot/homework-arch-4/blob/master/1/Reboot%E8%BF%90%E7%BB%B4%E5%BC%80%E5%8F%91%E6%9E%B6%E6%9E%84%E5%B8%88%E7%8F%AD-%E4%BD%9C%E4%B8%9A-1.pdf
"""

import sys
import os

def insert_file(file_name,ins_pos,ins_str):
  length = len(ins_str)
  seek_length = length * 3
  f = open(file_name,"r+")
  f.seek(-length,2)
  while (f.tell() > int(ins_pos)):
    temp_str = f.read(length)
    # print temp_str
    f.write(temp_str)
    # print f.tell()
    if (f.tell() - seek_length >= int(ins_pos)):
      f.seek(-seek_length,1)
    else:
      break
    
  # print f.tell()
  if f.tell() != int(ins_pos):
    temp_pos = f.tell()  
    f.seek(int(ins_pos),0)
    temp_length = temp_pos -2*length -int(ins_pos)
    #print temp_length
    temp_last_string = f.read(temp_length)
  else:
    temp_last_string = f.read(length)
  f.seek(int(ins_pos)+length,0)
  f.write(temp_last_string)
  f.seek(int(ins_pos),0)
  f.write(ins_str)  
  f.close()

if __name__ == "__main__":
  if len(sys.argv) < 4:
    print "参数少于三个！"
    sys.exit()
  else:
    filename = sys.argv[1]
    insert_pos = sys.argv[2]
    insert_str = sys.argv[3]
    if os.path.exists(filename) is False:
      print "文件不存在，请创建"
      sys.exit()
    else:
      insert_file(filename,insert_pos,insert_str)
