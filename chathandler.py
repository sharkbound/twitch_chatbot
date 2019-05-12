import irc.bot
import requests
import config
import commands


class TwitchBot(irc.bot.SingleServerIRCBot):
    def __init__(self, username, client_id, token, channel):
        self.client_id = client_id
        self.token = token
        self.channel = '#' + channel
        self.channel_id = config.user_id

        #create the IRC bot
        server = 'irc.chat.twitch.tv'
        port = 6667
        print(f'Connecting to {server} on {port}')
        irc.bot.SingleServerIRCBot.__init__(self,
                [(server, port, token)], username, username)


    def get_channel_id(self, channel):
        url = 'https://api.twitch.tv/kraken/users?login='+channel
        headers = {'Client-ID': self.client_id,
                'Accept': 'application/vnd.twitchtv.v5+json'}
        r = requests.get(url, headers=headers).json()
        return r['users'][0]['_id']

    def on_welcome(self, c, e):
        print(f'Joining {self.channel}')

        #kinda unsure what this is
        c.cap('REQ', ':twitch.tv/membership')
        c.cap('REQ', ':twtich.tv/tags')
        c.cap('REQ', ':twitch.tv/commands')
        c.join(self.channel)

    def on_pubmsg(self, c, e):
        if e.arguments[0][:1] == '!':
            #split args on whitespace
            name = ""
            s_list = e.arguments[0].split(' ')
            if len(s_list) == 2:
                name = s_list[1]
            cmd = str(e.arguments[0]).split(' ')[0][1:]
            print(f'Rececived command: {cmd}')
            self.do_command(e, cmd, name)
        return

    def do_command(self, e, cmd, name):
        c = self.connection

        cmd_list = commands.cmd_list
        if cmd == 'atick':
            c.privmsg(self.channel, commands.atick_resp())
        elif cmd == 'insult':
            c.privmsg(self.channel, commands.insult_resp(name))
        elif cmd == 'fucks':
            c.privmsg(self.channel, commands.fucks_resp(name))
        elif cmd == 'holy':
            c.privmsg(self.channel, commands.holy_resp(name))    
        else:
            for item in cmd_list:
                if cmd == item['cmd']:
                    c.privmsg(self.channel, item['resp'])
                    break
            else:
                pass

if __name__ == '__main__':
    bot = TwitchBot(config.username, config.client_id,
            config.token, config.channel)
    bot.start()
