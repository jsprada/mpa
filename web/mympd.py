import mpd

class Client(object):
    def __init__(self, host='localhost', port='6600'):
        self.host = host
        self.port = port
        self.client = mpd.MPDClient()
        self.connect_status = self._try_connect()
        self.status = self._status()
        self.current_song = self._current_song()
        self.track = self.current_song['title']
        self.artist = self.current_song['artist']

        self.state = self._get_state()
        self.state_action = self._state_action()
        self.state_inverse = self._state_inverse()
        self.playlists = self._get_playlists()
        self.current_playlist = self._get_playlist()


    def _try_connect(self):
        try:
            self.client.connect(self.host, self.port)
            return True
        except:
            return False

    def _disconnect(self):
        self.client.disconnect()

    def _status(self):
        return self.client.status()

    def play(self):
        pass

    def _current_song(self):
        try:
    	    return self.client.currentsong()
        except:
            return {'title': "na", 'artist': "na"}
    def _get_state(self):
        if self.status['state'] == 'play':
            return 'Play'
        elif self.status['state'] == 'pause':
            return 'Pause'
        else:
            return 'unknown'

    def _state_action(self):
        if self.state == 'Play':
            return 'Playing'
        elif self.state == 'Pause':
            return 'Paused'
        else:
            return "Unknown"

    def _state_inverse(self):
        if self.state == 'Play':
            return 'Pause'
        elif self.state == 'Pause':
            return 'Play'
        else:
            return "Unknown"

    def _get_playlists(self):
        return self.client.listplaylists()

    def _get_playlist(self):
        return self.client.stats()



#obj = Client()
#print(obj.track)
