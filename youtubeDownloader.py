#!/usr/bin/env python3

import os 
import platform
import subprocess

youtubeCmd = "youtube-dl"
cmd = "where" if platform.system() == "Windows" else "which"
try: 
        subprocess.call([cmd, youtubeCmd])
        link = input('insert the link of the youtube video: ')
        print(link)
        subprocess.call([youtubeCmd, link])

except: 
        print("No executable")
        exit()

