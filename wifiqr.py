import configparser
import pyqrcode
import glob
import os
import sys

if not os.geteuid() == 0:
    sys.exit('Script must be run as root')

config = configparser.ConfigParser()
def getinfo(file):
 config.read(file)
 name=config['wifi']['ssid']
 security="nopass"
 try:
  if "wpa" in config['wifi-security']['key-mgmt']:
   security="WPA"
  else:
   security="WEP"
  password=config['wifi-security']['psk']
 except:
  security="nopass"
 qrmsg="WIFI:T:"+security+";S:"+name+";P:"+password+";;"
 return qrmsg
num=0
ntarr=[]
print("Select Wifi")
for wifi in glob.glob('/etc/NetworkManager/system-connections/*'):
 ntarr.append(wifi)
 print(str(num) + ":" + wifi)
 num +=1
wifino = int(input("Select Wifi: "))
wifi = pyqrcode.create(getinfo(ntarr[wifino]))
fn = input("Please Imput the Name for the file: ")
wifi.svg(fn + ".svg")
