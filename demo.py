#!/usr/bin/python3
import logging
import subprocess
import time
import undetected_chromedriver as uc


logging.basicConfig(level=10)
logging.getLogger("parso").setLevel(100) # i hate damn parso

#o = uc.ChromeOptions()
#o.arguments.extend(["--no-sandbox", "--disable-setuid-sandbox"])  # these are needed to run chrome as root
driver = uc.Chrome(advanced_elements=True, version_main = 95)  # driver = uc.Chrome( version_main = 95 )
driver.get("https://nowsecure.nl/#relax")

logging.getLogger().info('sleeping 5 seconds to give site a chance to load')
time.sleep(5) # this is only for the timing of the screenshot
logging.getLogger().setLevel(20)
driver.save_screenshot("/data/nowsecure.png")
subprocess.run(["catimg", "/data/nowsecure.png"])
logging.getLogger().info('screenshot saved to /data/nowsecure.png')
input("press a key to quit")
exit()
