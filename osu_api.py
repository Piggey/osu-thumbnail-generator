# doing this because all other wrappers doesnt seem to work for me :<

import json, requests

base = 'https://osu.ppy.sh/api'

class OsuApi(object):
    def __init__(self, api_key):
        self.api_key = api_key
    
    def get_beatmaps(self, creator):
        params = {
            'k': self.api_key,
            'u': creator,
            'type': 'string',
            'm': 0,
            'a': 0
        }
        r = requests.get(base + '/get_beatmaps', params=params)
        return json.loads(r.text)

    def get_user(self, username):
        params = {
            'k': self.api_key,
            'u': username,
            'm': 0,
            'type': 'string'
        }
        r = requests.get(base + '/get_user', params=params)
        return json.loads(r.text)