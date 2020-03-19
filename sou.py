import os
import subprocess
import getpass
import time
import datetime

#stdout, stderr = process.communicate()
#print("out", stdout)
#print("err", stderr)
f = "sou.py"
os.system('dos2unix ' + f)

#pro = subprocess.Popen(["dos2unix", "sou.py"], stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)
#pro, err = pro.communicate()
#print(pro)

#print(getpass.getuser())
#now = time.strftime("%c")

'''
def printLog(info):
  date = datetime.datetime.now()
  print(date.strftime("[%s]~[%Y-%m-%d %H:%M:%S IST]~") + info)
printLog("Hi") 
'''
'''
with open("inp.txt", "r") as fp:
  lines = [l.strip() for l in fp]

con = []
with open("modem.txt") as f:
  for line2 in f:
    for line1 in lines:
      if line1 in line2:
        con.append(line2.strip())

with open("out.txt", "w") as ofp:
  for field in con:
    val = field.split('~')
    ofp.write(val[0] + '~'+ val[1] + '~' + val[2] + '~' + val[4] + '~' + val[6] + '~' + val[9] + '\n')
'''

