from random import randint
import requests

INSULTS = [
    "dumbass"
    "stupid"
    "stoopid"
    "monkey ass"
]

SUBJECTS = [
    "J", 
    "MK", 
    "Mike", 
    "Michael", 
    "Mike J", 
    "Michael J", 
    "Mike McIntire", 
    "Michael McIntire", 
    "Mike J McIntire", 
    "Michael J McIntire"
]

REACTIONS = [
    "a tick ?", 
    "that's not a tick!", 
    "OMG No!", 
    "WTF No!", 
    "LOL Focus!", 
    "Look at The Clock", 
    "Are you blind or what ?", 
    "even the clock are laughing at you.", 
    "what in the hell is wrong with ya?", 
    "YEEHAW"
    "OH COME ON!"
]

def get_reaction():
    return REACTIONS[randint(0, len(REACTIONS)-1)].replace("\n", "") + " "

def get_subject():
    return SUBJECTS[randint(0, len(SUBJECTS)-1)].replace("\n", "") + " "

def get_insult():
    return INSULTS[randint(0, len(INSULTS)-1)].replace("\n", "") + " "


def get_user_id(client_id, channel):
    url = 'https://api.twitch.tv/kraken/users?login='+channel
    headers = {'Client-ID': client_id,
            'Accept': 'application/vnd.twitchtv.v5+json'}
    r = requests.get(url, headers=headers).json()
    return r['users'][0]['_id']