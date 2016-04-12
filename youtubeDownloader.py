#!/usr/bin/env python

import os 
import platform
import subprocess

youtubeCmd = "youtube-dl"
cmd = "where" if platform.system() == "Windows" else "which"
try: 
        subprocess.call([cmd, youtubeCmd])
        subprocess.call([youtubeCmd, "https://www.youtube.com/watch?v=hS5CfP8n_js"])
except: 
        print "No executable"
        exit()

