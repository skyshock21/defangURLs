#!/usr/bin/python3
#
# defangURLs.py
# A script to read URLs from a text file, sort in
# ascending order, remote duplicates, defang URLs, 
# and output a file containing that list 

import sys,argparse
from defang import defang

# Function Defs

def defangURLs():
    url_list = args.file.readlines()
    uniq = list(set(url_list))
    urls = sorted(line.strip() for line in uniq)
    urlsorted = '\n'.join(map(str, urls))
    urlsanitized = defang(urlsorted, all_dots=True)
    with open('cleanURLs.txt', 'w') as f:
        print(urlsanitized, file=f)

# CLI arguments & arg parser
ex = '''example:
python3 defangURLs.py file.txt
'''
parser = argparse.ArgumentParser(prog='defangURLs',
                                description='''Outputs a list of defanged URLs''',
                                epilog=ex,
                                formatter_class=argparse.RawDescriptionHelpFormatter,
                                )
parser.add_argument('file', type=argparse.FileType('r'))
parser.set_defaults(func=defangURLs)
args = parser.parse_args()

def main():
    args.func()

if __name__ == "__main__":
    sys.exit( main() )
