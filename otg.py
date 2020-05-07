from os.path import exists
from os import remove
from sys import argv
from text_recognition import Recognizer
from osu_api import OsuApi
import cv2, requests
from photo_edition import editPhoto

# beatmap cover size: 900x250

def downloadImgFromLink(URL, new_filepath):
    with open(new_filepath, 'wb') as handle:
        response = requests.get(URL, stream=True)
        if not response.ok:
            print(response)
        for block in response.iter_content(1024):
            if not block:
                break
            handle.write(block)
    return new_filepath

def fetchBeatmapCover(_artist, _title, _mapper):
    checked = []
    response = api.get_beatmaps(_mapper)
    for beatmap in response:
        artist = beatmap['artist']
        title = beatmap['title']

        if(artist+title in checked):
            pass
        checked.append(artist+title)

        if(_artist == artist and _title == title):
            bg_id = beatmap['beatmapset_id']
            bg_url = f'https://assets.ppy.sh/beatmaps/{bg_id}/covers/cover.jpg'
            return downloadImgFromLink(bg_url, 'cover.jpg')
    return '[*] BACKGROUND NOT FOUND'

# API key check
print('[*] getting the API key')
if(not exists('API_KEY')):
    API = input('Please paste your osu! api key (): ')
    f = open('API_KEY', 'w')
    f.write(API)
    f.close()
    print('API key saved successfully')
else:
    API = open('API_KEY').read()
    print('[*] successfully got API key (doesnt mean its viable)')
    
try:
    print('[*] downloading the screenshot image from ' + argv[1])
    ss_url = argv[1]
    ss = downloadImgFromLink(ss_url, 'temp.jpg')
    ss = cv2.imread(ss)
    height, width = ss.shape[:2]
    cropped_ss = ss[0:height//8, 0:width]
    remove('temp.jpg')
    print('[*] successfully downloaded the screenshot')
except IndexError:
    print('[*] WARNING: to use the generator please use "otg.py [screenshot link]"')

Recon = Recognizer()
api = OsuApi(API)

print('[*] finding metadata')
artist = Recon.getArtist(cropped_ss)
title = Recon.getTitle(cropped_ss)
mapper_name = Recon.getMapper(cropped_ss)
player_name = Recon.getPlayer(cropped_ss)

print(f'[*] FOUND: {artist} - {title} ({mapper_name}) played by {player_name}')

res = input('[!] Please check whether the metadata is correct (type "y" if yes or correct metadata manually)\nFORMAT: artist;title;mapper;player\n')
if(res.lower() != 'y'):
    res = res.split(';')
    arist, title, mapper_name, player_name = res
    print(f'[*] corrected to: {artist} - {title} ({mapper_name}) played by {player_name}')

print('[*] downloading player avatar')
player_id = api.get_user(player_name)[0]['user_id']
player_avatar = downloadImgFromLink(f'http://s.ppy.sh/a/{player_id}', 'player_avatar.jpg')

print('[*] downloading the beatmap cover')
map_cover = fetchBeatmapCover(artist, title, mapper_name)