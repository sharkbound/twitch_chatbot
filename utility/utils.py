from random import choice
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


def rand_reaction():
    return choice(REACTIONS)


def rand_subject():
    return choice(SUBJECTS)


def rand_insult():
    return choice(INSULTS)


def get_user_id(client_id, channel):
    url = f'https://api.twitch.tv/kraken/users?login={channel}'
    headers = {'Client-ID': client_id,
               'Accept': 'application/vnd.twitchtv.v5+json'}
    r = requests.get(url, headers=headers).json()
    return r['users'][0]['_id']


def find_commands(items: dict):
    # loop over globals passed as `items`
    for name, item in items.items():
        # check if it is a function and it is not private, and ends with `resp`
        if callable(item) and not name.startswith('_') and name.endswith('resp'):
            # separate the cmd name out of the key
            cmd = name.split('_')[0]
            # yield it in in command form
            yield f'!{cmd}'
