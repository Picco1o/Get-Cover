import sys
import os
import json
import argparse
from urllib import request

parser = argparse.ArgumentParser(description='some args')
parser.add_argument('-i', '--id', required=True, help='bilibili bvid')
args = parser.parse_args()
BVID = args.id
PATH = 'cover'


def main():
    if not os.path.isdir(PATH):
        os.mkdir(PATH)
    print('...')
    cid_url = 'https://api.bilibili.com/x/player/pagelist?bvid={}'.format(BVID)
    r = json.loads(request.urlopen(cid_url).read())
    try:
        cid = r['data'][0]['cid']
    except:
        print('检查输入的bvid')
        sys.exit()
    interface_url = 'https://api.bilibili.com/x/web-interface/view?cid={}&bvid={}'.format(cid, BVID)
    r = json.loads(request.urlopen(interface_url).read())
    pic_url = r['data']['pic']
    filename = '{}/{}'.format(PATH, pic_url.split('/')[-1])
    request.urlretrieve(pic_url, filename)
    print('success')
    print(filename)


if __name__ == "__main__":
    main()
