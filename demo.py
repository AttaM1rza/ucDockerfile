#!/usr/bin/python3
import logging
import subprocess
import time
import undetected_chromedriver as uc

sleepTime = 5
url = "https://nowsecure.nl/#relax"
url = "https://www.zara.com/de/de/jacke-aus-kunstleder-p08281450.html?v1=222756772"
VERSION_MAIN = 108

def getCompatibleChromeVersion():
  str1 = driver.capabilities['browserVersion']
  str2 = driver.capabilities['chrome']['chromedriverVersion'].split(' ')[0]
  print("++++++++++++++++++", str1)
  print("++++++++++++++++++", str2)
  print(str1[0:2])
  print(str2[0:2])
  if str1[0:2] != str2[0:2]: 
    print("please download correct chromedriver version")
  
logging.basicConfig(level=10)
logging.getLogger("parso").setLevel(100)

#o = uc.ChromeOptions()
#o.arguments.extend(["--no-sandbox", "--disable-setuid-sandbox"])  # these are needed to run chrome as root
driver = uc.Chrome(advanced_elements=True, version_main = VERSION_MAIN)  # driver = uc.Chrome( version_main = 108 )
driver.get(url)

logging.getLogger().info(f'sleeping {sleepTime} seconds to give site a chance to load')
time.sleep(sleepTime) # this is only for the timing of the screenshot
logging.getLogger().setLevel(20)
driver.save_screenshot("/data/nowsecure.png")
subprocess.run(["catimg", "/data/nowsecure.png"])
logging.getLogger().info('screenshot saved to /data/nowsecure.png')
input("press a key to quit")
exit()
