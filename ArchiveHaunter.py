from argparse import *
from zipfile import *
import time
import py7zr
import sys

sys.setrecursionlimit(999999999)

def cracksz():
    count = 0
    f = open(dictionary, 'r')
    lines = f.read().splitlines()
    f.close()
    start_time = time.time()
    for line in lines:
        try:
            with py7zr.SevenZipFile(filename, mode='r', password=line) as z:
                z.extractall(output)
                print("===========================================")
                print("Status: Cracked")
                print(f'Password: {line}')
                print(f"Time: {time.time() - start_time} seconds")
                print(f'{count} passwords are checked')
                print("===========================================")
                break
        except:
            count += 1
            continue

def crackzip():
    count = 0
    f = open(dictionary, 'r')
    lines = f.read().splitlines()
    f.close()
    start_time = time.time()
    for line in lines:
        try:
            zip = ZipFile(filename)
            zip.setpassword(line.encode("utf-8"))
            zip.extractall(output)
            zip.close()
            print("===========================================")
            print("Status: Cracked")
            print(f'Password: {line}')
            print(f"Time: {time.time() - start_time} seconds")
            print(f'{count} passwords are checked')
            print("===========================================")
        except:
            count += 1
            continue

def check():
    if str(filename).endswith(".7z"):
        cracksz()
    elif str(filename).endswith('.zip'):
        crackzip()

def choice():
    global filename, dictionary, output, extension
    filename = args.archive
    dictionary = args.dictionary
    output = args.output

def options():
    global args
    parser = ArgumentParser()
    parser.add_argument('-a', '--archive', dest='archive', metavar='<archive>', required=True, type=str, help='path to archive')
    parser.add_argument('-d', '--dictionary', dest='dictionary', metavar='<dictionaty>', type=str, help='path to password dictionary file')
    parser.add_argument('-o', '--output', dest='output', type=str, help='path to output file')
    args = parser.parse_args()

if __name__ == '__main__':
    options()
    choice()
    check()