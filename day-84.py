import argparse
import requests
def DownloadFile(url, local_filename):
    r = requests.get(url)
    f = open(local_filename, 'wb')
    for chunk in r.iter_content(chunk_size=512 * 1024):
        if chunk: # filter out keep-alive new chunks
            f.write(chunk)
    f.close()
    return

parser = argparse.ArgumentParser()

parser.add_argument("url", help="URL of the file")
parser.add_argument("Filename", help="The filename of the file")

args = parser.parse_args()
DownloadFile(args.url, args.Filename)

#python3 day-84.py https://imagej.net/images/8-connected-pixel.gif harry.jpg
#This will download the file