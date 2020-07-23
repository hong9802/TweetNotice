from PIL import Image
import requests
import os

def get_profile(profile):
    imgname = profile.rsplit("/", 1)[1]
    r = requests.get(profile, stream = True)
    if(r.status_code == 200):
        with open(imgname, "wb") as f:
            for chunk in r.iter_content(1024):
                f.write(chunk)
        img = Image.open(imgname)
        img.save("profile.ico")
        os.remove(imgname)