import os
import sys
import shutil
import requests

if len(sys.argv) < 2:
    exit("Day required as first argument")

day = sys.argv[1]
directory = f'day{day}'
if not os.path.exists(directory):
    os.mkdir(directory)
    print(f'Created directory {directory}')

inputUrl = f'https://adventofcode.com/2024/day/{day}/input'
inputPath = f'{directory}/input.txt'

if not os.path.exists(inputPath):
    print(f'Downloading {inputUrl}')

    aocCookiePath = "../../.aoccookie"
    if not os.path.exists(aocCookiePath):
        exit(f'Advent of code cookie file missing "{aocCookieFile}"')

    with open(aocCookiePath, 'r') as cookieFile:
        cookie = cookieFile.read().strip()

    inputRequest = requests.get(inputUrl, cookies={'session': cookie})

    if inputRequest.status_code == 400:
        exit("AOC session cookie either missing or invalid")
    elif inputRequest.status_code == 404:
        exit(f'Day {day} not available yet')
    elif inputRequest.status_code != 200:
        exit("Uknown error fetching input: " + inputRequest.text)

    with open(inputPath, 'w') as inputFile:
        inputFile.write(inputRequest.text)
    print(f'Created file {inputPath}') 


partPath = f'{directory}/part1.py'
tmplPath = 'part.py.tmpl'
if not os.path.exists(partPath):
    shutil.copyfile(tmplPath, partPath)
    print(f'Copied file {tmplPath} to {partPath}')

