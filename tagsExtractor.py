import yt_dlp
import datetime
from os import chdir, system, listdir
import json
import sys

link = sys.argv[1]

folderName = str(datetime.datetime.today()).replace(" ", "")
system(f"mkdir {folderName}")
chdir(folderName)

ydl_opts = {"skip_download": True,
			"writeinfojson": True,
            "no_warnings": True,
            # "overwrites": False,
            "nooverwrites": True,
            "ignoreerrors" : True
 }

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])

for file in listdir():
    if file.endswith(".json"):
        try:
            with open(file) as f:
                data = json.load(f)
                
            oneVideoData = data["tags"]

            print(type(oneVideoData))
            print(",".join(oneVideoData))
        

        except Exception as e:
            print(str(e))