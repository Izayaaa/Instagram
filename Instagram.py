import requests
import re
import datetime
import os
from random import randint
import msvcrt


def get_link_image():
    input_data = input('Instagram Link: ')
    resp = requests.get(input_data, stream=True)
    print('Checking link...')
    if resp.status_code == 200:
        print('Access link success, getting link image ...', end='')
        html_link = resp.text
        find_link = re.search(
            r'<meta property="og:image"\ content="(.*?)" />', html_link
            )
    else:
        print('Link error, try another link.')
    if find_link:
        image_link = find_link.group(1)
    fileName = datetime.datetime.now().strftime(
        '%Y-%m-%d_') + str(randint(0, 10000)) + '.jpg'
    return image_link, fileName


def get_link_video():
    input_data = input('Instagram Video Link: ')
    resp = requests.get(input_data, stream=True)
    print('Checking link ...')
    if resp.status_code == 200:
        print('Access link success, getting link image ...')

        html_link = resp.text
        find_link = re.search(
            r'<meta property="og:video" content="(.*?)" />', html_link)
    else:
        print('Link error, try another link.')
    if find_link:
        image_link = find_link.group(1)
    fileName = datetime.datetime.now().strftime(
        '%Y-%m-%d_') + str(randint(0, 10000)) + '.mp4'
    return image_link, fileName


def download(input_data):
    currentFolder = os.getcwd()
    req = requests.get(input_data[0], stream=True)
    with open(input_data[1], 'wb') as f:
        for chunk in req.iter_content(50000):
            f.write(chunk)
    report = 'Your image saved as ' + currentFolder + \
     ' with name ' + input_data[1]
    return print(report)

# download_image(get_link_video())


def run_script():
    print('Image or Video ? (Input the number.)')
    print('1. Image.\n2. Video.\n Control C for exit.')
    number = input('> ')
    if number == str(1):
        download(get_link_image())
    elif number == str(2):
        download(get_link_video())
    else:
        print('Input number, please.')
        msvcrt.getch()
        run_script()


run_script()
print('\nPress any key to exit...')
msvcrt.getch()
