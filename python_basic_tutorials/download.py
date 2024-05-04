import argparse
import requests


def download_file(url, file_name):
    if file_name is None:
        file_name = url.split('/')[-1]
    r = requests.get(url)
    f = open(file_name, 'wb')
    for chunk in r.iter_content(chunk_size=512 * 1024):
        if chunk:  # filter out keep-alive new chunks
            f.write(chunk)
    f.close()
    return


parser = argparse.ArgumentParser()

parser.add_argument("url", help='Url of the file ')
parser.add_argument('-o', '--output', help='name or path\\name of the file you want to download')

args = parser.parse_args()

download_file(args.url, args.output)
