import requests

username = ''
client_id = ''
token = ''
channel = ''

helix_base = 'https://api.twitch.tv/helix'

def get_user_id(client_id):
    url = 'https://api.twitch.tv/kraken/users?login='+channel
    headers = {'Client-ID': client_id,
            'Accept': 'application/vnd.twitchtv.v5+json'}
    r = requests.get(url, headers=headers).json()
    return r['users'][0]['_id']

user_id = get_user_id(client_id)



