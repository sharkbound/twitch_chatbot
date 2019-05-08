import requests
import config
import dateutil.parser
import datetime


def cmds_resp():
    return "Avaliable Commands: !cmds !uptime !title !setup !editor !emacs"

def uptime_resp():
    headers = {'Client-ID': config.client_id}
    r = requests.get(f'{config.helix_base}/streams?user_id={config.user_id}',
            headers=headers).json()['data'][0]
    today = datetime.datetime.now()
    s_time = dateutil.parser.parse(r['started_at'])
    tzone_adjust = 6
    live_hour = (today.hour+tzone_adjust - s_time.hour)
    live_min = (today.minute - s_time.minute)
    return f"{r['user_name']} has been live for {live_hour} hours and {live_min} minutes"

def title_resp():
    headers = {'Client-ID': config.client_id}
    r = requests.get(f'{config.helix_base}/streams?user_id={config.user_id}',
            headers=headers).json()['data'][0]
    return f"Current Title: {r['title']}"

def setup_resp():
    comp = 'Intel i7 w/ GTX 980 Ti'
    os = 'Ubuntu 16.04 w/ i3-Gaps'
    mbp = '15" MacBook Pro w/ i7'
    per = 'Gigabyte Keyboard w/ MX-Blues and a Logitech Mouse'
    return f'Comps: {comp} running {os} and a {mbp} ---- Peripherals: {per}'

def editor_resp():
    return 'VIM ----- THERE IS NO OTHER EDITOR ----- https://www.vim.org/'

def emacs_resp():
    return '%s/emacs/vim/g'


cmd_list = [
        {'cmd': 'cmds', 'resp': cmds_resp()},
        {'cmd': 'uptime', 'resp': uptime_resp()},
        {'cmd': 'title', 'resp': title_resp()},
        {'cmd': 'setup', 'resp': setup_resp()},
        {'cmd': 'editor', 'resp': editor_resp()},
        {'cmd': 'emacs', 'resp': emacs_resp()},]
#print([x['resp'] for x in cmd_list if x['cmd'] == 'uptime'])
