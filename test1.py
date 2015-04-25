#/usr/bin/env py
#coding:utf-8
"This is a test module"

import sys

'''
name = 'pel'

print
print 'Hello world!'
print
print 'hello %s' % name
print 'a' * 10

temp = "%r %r %r %r"
print temp % ("first' at", "s", "T", "s")
#age = raw_input()


#print 'The script\'s name is %s' % sys.argv[0]
#print 'The first argument is %s' % sys.argv[1]
#print 'The second argument is %s' % sys.argv[2]

1 + 2 * 4


i = 0
while i <= 10:
  print i
  i += 1

print

for a in range(11):
  print a

print ############
num = int(raw_input("please input a number"))
if num==0:
  print 'it is 0'
elif num<0:
  print 'it belows 0'
else:
  print 'it big than 0'


print
print '2-7:'
str = raw_input("please input a string:")
i = 0
while i < len(str):
  print str[i] 
  i += 1

for i in str:
  print i


print
print '2-8:'
print 'please input the 5 numbers and we will \
cacl the sum!:'

i = 0
sum = 0
list=[1,2,3,4,5]
while i<5:
  list[i] = int(raw_input('Please input the ' + str(i+1) + \
'the number: '))
  sum +=list[i]
  i += 1
print 'the sum of the numbers is: %d' %(sum)

sum = 0
forList = []
for i in range(5):
  temp = int(raw_input('Please input the %d the number by FOR \
' %(i+1)))
  forList.append(temp)
  sum += temp
print sum

print
print '2-9:'
print 'please input the 5 numbers and we will \
cacl the ave!:'

sum = 0
forList = []
for i in range(5):
  temp = int(raw_input('Please input the %d the number by FOR \
' %(i+1)))
  forList.append(temp)
  sum += temp
print 'the sum of the numbers is: %d.' %(sum)
ave = float(sum)/len(forList)
print 'the sum of the numbers is: %f.' %(ave)



print
print '2-10:'

num = int(raw_input('Please input a number: '))
if 1<=int(num)<=100:
  print "succese! exit!"
  exit

while num>100 or num <1:
  print "It is not between 1 and 100, input again!: "
  num = int(raw_input('Please input a number: '))
print 'finaly success'



print
print '2-11:'

i = True
while i:
  choose = raw_input("Please input the choose: 1 for sum; 2 for ave; \
X for exit: ")
  if choose == "1":
    print 'please input the 5 numbers and we will \
cacl the sum!:'

    i = 0
    sum = 0
    list=[1,2,3,4,5]
    while i<5:
      list[i] = int(raw_input('Please input the ' + str(i+1) + \
'the number: '))
      sum +=list[i]
      i += 1
    print 'the sum of the numbers is: %d' %(sum)



  elif choose == "2":
    print 'please input the 5 numbers and we will \
cacl the ave!:'

    sum = 0
    forList = []
    for i in range(5):
      temp = int(raw_input('Please input the %d the number by FOR \
' %(i+1)))
      forList.append(temp)
      sum += temp
    print 'the sum of the numbers is: %d.' %(sum)
    ave = float(sum)/len(forList)
    print 'the sum of the numbers is: %f.' %(ave)

  elif choose == "X":
    i = False

  else:
    print "Wrong input!"



print
print '2-15:'

fir = int(raw_input("input first: \n"))
sec = int(raw_input("input second: \n"))
thi = int(raw_input("input third: \n"))

if fir >= sec:
  high = fir
  mid = sec
  if sec >= thi:
    low = thi
  else:
    if thi >= fir:
      high = thi
      mid = fir
      low = sec
else:
  high = sec
  mid = fir
  if fir >= thi:
    low = thi
  else:
    if thi >=sec:
      high = thi
      mid = sec
      low = fir

print "From high to low is : %d %d %d " %(high,mid,low)
print "From low to high is : %d %d %d " %(low,mid,high)


print
print '2-16:'

fileHandle = file("t.py","aw+")
for i in fileHandle:
  print i,
  
fileHandle.close()



print
print '5-2:'

def mulit(a,b):
  return a * b

c = mulit(10,20)
print c


print
print '5-3:'

testGrade = int(raw_input("Please input the score you get: "))

if 90 <= testGrade <= 100:
  print "you get A"
elif 80 <= testGrade <= 89:
  print "you get B"
elif 70 <= testGrade <= 79:
  print "you get C"
elif 60 <= testGrade <= 69:
  print "you get D"
elif testGrade <  60:
  print "you get F"
else:
  print "Wrong Score"


print
print '5-4:'

year = int(raw_input("Please input a year: "))

if year % 4 == 0 and (year % 100 != 0 or year % 400 ==0):
  print "it's a leap year! '"
else:
  print "it's not a leap year! "


print
print '5-5:'

float_coin = float(raw_input("Please input the number in $: "))
dollor = float_coin*100
print dollor
(dol25,rest) = divmod(dollor,25)
print dol25
print rest
(dol10,rest1) = divmod(rest,10)
print dol10
print rest1
(dol5,rest2) = divmod(rest1,5)
print dol5
print rest2
print "it can divid into %d(s) 25C, %d(s) 10C, %d(s) 5C, %d(s) 1C"\
%(dol25,dol10,dol5,round(rest2))
print rest2


print
print '5-6:'

N1 = raw_input("Please input the N1: ")
N2 = raw_input("Please input the N2: ")
meth = raw_input("Please input the metheand: ")

if meth == "+":
  print float(N1)+float(N2)
elif meth == "-":
  print float(N1)-float(N2)
elif meth == "*":
  print float(N1)*float(N2)
elif meth == "/":
  print float(N1)/float(N2)
elif meth == "%":
  print float(N1)/float(N2)
elif meth == "**":
  print float(N1)**float(N2)
else:
  print "Error input!"



print
print '5-10:'

Ftemp = float(raw_input("Please input the F tempurature: "))
Ctemp = (Ftemp-32)*(5.0/9)
print "The C tempurate of %f is %f." %(round(Ftemp,2),round(Ctemp,2))




print
print '5-11:'

for i in range(21):
  if i % 2 == 1:
    print i

def firstModSecond(fir,sec):
  if fir% sec == 0:
    print True
  else:
    print False

firstNo = int(raw_input("Please input the first int: "))
secondNo = int(raw_input("Please input the second int: "))

firstModSecond(firstNo,secondNo)




print
print '5-13:'

def hour2min(hour,min):
  total = hour*60+min
  print "The minute is %d." %total

hourTime = int(raw_input("Please input the hours: "))
minuteTime = int(raw_input("Please input the minutes: "))

hour2min(hourTime,minuteTime)


print
print '5-14:'

money = float(raw_input("Please input the money you store in the bank: "))
rate = float(raw_input("Please input the rate of the bank: "))


for i in range(365):
  money = (money * (1+rate))

print money




print
print '5-17:'

import random
big_n = random.randint(1, 101)

list = range(big_n)

for i in range(big_n):
      list[i] = random.randint(-1, 2**31)
      
print big_n
print list
list.sort()
print list




print '------------------------------'
print '6-1:'
print '------------------------------'


temp = "Hello world, pel "
name = "pel"

print temp.find(name)
print name in temp



print '------------------------------'
print '6-2:'
print '------------------------------'

import string
import keyword

alphas = string.letters + '_'
nums = string.digits

print "Please unput test:"
myInput = raw_input("identifier to test: \n")

if myInput in  keyword.kwlist:
  print "the input is keword!"
else:
  if myInput[0] not in alphas:
    print "invalid: first symbol must be alphabtic"
  else:
    if len(myInput) > 1:
      for otherChar in myInput[1:]:
        if otherChar not in alphas + nums:
          print "invalid: have invalid words"
          break
      print "okay~"
    else:
      print 'okay'


print '------------------------------'
print '6-3:'
print '------------------------------'

num = str(raw_input("Please input the sequnece number it will sort: \n"))

print sorted(num,reverse=True)



print '------------------------------'
print '6-4:'
print '------------------------------'

print 'please input the 5 numbers and we will \
cacl the ave!:'

sum = 0
forList = []
for i in range(5):
  temp = int(raw_input('Please input the %d the number by FOR:  \
' %(i+1)))
  forList.append(temp)
  sum += temp
print 'the sum of the numbers is: %d.' %(sum)
ave = float(sum)/len(forList)
print 'the sum of the numbers is: %f.' %(ave)

if 90 <= ave <= 100:
  print "you get A"
elif 80 <= ave <= 89:
  print "you get B"
elif 70 <= ave <= 79:
  print "you get C"
elif 60 <= ave <= 69:
  print "you get D"
elif ave <  60:
  print "you get F"
else:
  print "Wrong Score"




print '------------------------------'
print '6-5:'
print '------------------------------'


print '(a)'
displayString = raw_input("Please input a string: ")
i = 0
while i < len(displayString):
  if i == 0:
    print displayString[0:2]
  else:
    print displayString[i-1:i+2]
  i += 1

print "(b)"
string1 = raw_input("Please input the first string: ")
string2 = raw_input("Please input the second string: ")

isMatch = True
if len(string1) != len(string2):
  print "Not match, the length is not same"
else:
  i = 0
  while i < len(string1):
    if string1[i] != string2[i]:
      print "Not match, the %s bits is not small" %(i+1)
      isMatch = False
      break
    i += 1
  if isMatch == True:
    print "Match!"

print "(d)"

getStr = raw_input("Please input a string, we will rev it: ")
revStr = getStr +  getStr[::-1]
print revStr




print '------------------------------'
print '6-9:'
print '------------------------------'

totalMin = int(raw_input("Please input the minutes : "))

(hour,min) = divmod(totalMin,60)
print "It is %i hour(s) and %i minute(s). "%(hour,min)
  


print '------------------------------'
print '6-10:'
print '------------------------------'

input_string = raw_input("Please input a string: ")
print input_string.swapcase()




print '------------------------------'
print '6-11:'
print '------------------------------'

num_string = int(raw_input("Please input a number: "))
(firstPart,rest) = divmod(num_string,256**3)
(secPart,rest) = divmod(rest,256**2)
(thirdPart,rest) = divmod(rest,256)
print "%i.%i.%i.%i" %(firstPart,secPart,thirdPart,rest)

ip_string = raw_input("Please input a IP: ")
ipList = ip_string.split(".")
total = int(ipList[0])*(256**3) + int(ipList[1])*(256**2) + int(ipList[2])*256 + int(ipList[3])
print total




print '------------------------------'
print '6-12:'
print '------------------------------'

def findchr(string, char):
 print 
 i = 0
 isfind = False;
 while i < len(string):
    if char == string[i]:
      print "Find! It's in %i bit." %(i+1)
      isfind = True;
      #break;
    i += 1
 if isfind == False:
    print "Not find!"

def rfindchr(string,char):
 print
 i = len(string)
 isfind = False;
 while i > 0:
    if char == string[i-1]:
      print "Find! It's in %i bit in last." %(i)
      isfind = True;
      break;
    i -= 1
 if isfind == False:
    print "Not find!"

def subchr(string,char,newchar):
 print
 i = 0
 isfind = False;
 while i < len(string):
    if char == string[i]:
      print "Find! It's in %i bit " %(i+1)
      newString = string.replace(char,newchar)
      isfind = True;
      #break;
    i += 1
 if isfind == False:
    print "Not find!"
 print newString

getStr = raw_input("Please input the string: ")
getChar = raw_input("Please input the char: ")
findchr(getStr, getChar)
rfindchr(getStr,getChar)
subchr(getStr,getChar,"*")




print '------------------------------'
print '6-17:'
print '------------------------------'


def myPop(mylist):
  mylist = mylist[0:len(mylist)-1]
  print mylist

listName = []
listName = list(raw_input("Please input a list: "))
print listName
myPop(listName)





print '------------------------------'
print '7-3:'
print '------------------------------'

dictTest = {"a":2,"b":4,"c":1,"d":3}
print dictTest

for i in sorted(dictTest.keys()):
  print "key = %s : values = %s " %(i,dictTest[i])




print '------------------------------'
print '7-4:'
print '------------------------------'

listKey = [1,2,3]
listValue = ["abc","def","ghi"]
print listKey
print listValue

#better way
dictA = {}
dictA = dict(zip(listKey,listValue))
print dictA

dictTest = {}
listLen = len(listKey)
i = 0
while i < listLen:
  dictTest[listKey[i]] = listValue[i]
  i += 1
print dictTest





print '------------------------------'
print '7-7:'
print '------------------------------'

dictTest = {"a":2,"b":4,"c":1,"d":3}
print dictTest

dictLen = len(dictTest)
dictNew = {}
for i,j in dictTest.items():
  dictNew[j] = i
  #print i,j

print dictNew





print '------------------------------'
print '7-8:'
print '------------------------------'

#listInput = raw_input("Please input the name and No. and spearate \
#by , e.g. pel:1,choidi:2,sysu:3...")
listInput = "pel:1,choidi:2,sysu:3"

listTemp = listInput.split(",")
print listTemp

dictNew = {}
for i in listTemp:
  dictNew[i.split(":")[0]] = i.split(":")[1]

print dictNew

for i in sorted(dictNew.keys()):
  print "name : %s , Number : %s " %(i,dictNew[i])


'''


print '------------------------------'
print '7-9:'
print '------------------------------'

def tr(srcstr, dststr, input_string):
  finalString = input_string.replace(srcstr,dststr)
  print finalString

tr("abc","mno","abcdef")

