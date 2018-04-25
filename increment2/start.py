import os
import subprocess
import distro
import platform
import linux
import windows
import logging
import automateitcommon



oscheck = platform.platform()
osversion = str(oscheck)
logging.basicConfig(filename='bootlog.txt', level=logging.INFO, format='%(asctime)s %(message)s')


with open('distro.txt', 'w') as file:
    file.write(osversion)

with open('distro.txt') as f:
        found = False
        for line in f:
            if "Linux" in line: # Key line: check if `w` is in the line.
                linux.load()
                found = True
                logging.info('Linux was found as your OS, loading Linux GUI');
            if "Windows" in line: # Key line: check if `w` is in the line.
                windows.load()
                found = True
                logging.info('Windows was found as your OS, loading Windows GUI');


