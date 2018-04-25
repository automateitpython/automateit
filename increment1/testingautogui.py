import os
import subprocess
import distro
import platform
import manjaro
import wind10
import automateitcommon



oscheck = platform.platform()
osversion = str(oscheck)



with open('distro.txt', 'w') as file:
    file.write(osversion)

with open('distro.txt') as f:
        found = False
        for line in f:
            if "Manjaro" in line: # Key line: check if `w` is in the line.
                manjaro.manjaro()
                found = True
            if "Windows-10" in line: # Key line: check if `w` is in the line.
                wind10.load()
                found = True


