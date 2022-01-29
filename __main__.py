from zipfile import ZipFile
from sys import argv
from time import sleep
def zip_cracker(src=None, pass_list=None) -> .0:   
  if(src != None):
    if(pass_list != None):
      try:zip, passwd = ZipFile(str(r'%s'%src)) , open(r'%s'%pass_list,'r+').readlines()
      except:quit("Error -> opening_file")
      for passwords in passwd:
        password = passwords.strip('\n')
        sleep(.02)
        try:
          zip.extractall(pwd=bytes(password, 'utf-8'))
          print('\r\n  [*] Password Found -> %s'%password)
          break
        except:print('\r\n  [!] PassWord Not Found -> %s'%password)
      print()
    else:
      try:
        ZipFile(str(r'%s'%src)).extractall()
        print('\r\n  [*] Password Found -> (None)\n')
      except:quit("Error -> extracting")
  else:quit("Error -> params")

try:zip_file, password_list = argv[1:3]
except ValueError:
  try:zip_file, password_list = argv[1], ''
  except ValueError:quit("Error -> argv")

zip_cracker(\
  src= zip_file ,
  pass_list= password_list
)