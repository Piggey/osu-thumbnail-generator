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
            'type': 'string'
        }
        r = requests.get(base + '/get_beatmaps', params=params)
        return json.loads(r.text)

    def get_user(self, username):
        params = {
            'k': self.api_key,
            'u': username,
            'type': 'string'
        }
        r = requests.get(base + '/get_user', params=params)
        return json.loads(r.text)

    def get_scores(self, beatmapID, username):
        params = {
            'k': self.api_key,
            'b': beatmapID,
            'u': username,
            'type': 'string',
            'limit': 100
        }
        r = requests.get(base + '/get_scores', params=params)
        return json.loads(r.text)

    def get_replay(self, beatmapID, userID):
        params = {
            'k': self.api_key,
            'b': beatmapID,
            'type': 'id',
            'u': userID
        }
        r = requests.get(base + '/get_replay', params=params)
        return json.loads(r.text)