#!/usr/bin/python3
from flask import Flask, render_template
import mympd
import mpd

app = Flask(__name__)


@app.route("/")
def status(client=None):
    client = mympd.Client()
    return render_template('index.html', client=client)

@app.route("/p")
def p():
    client = mpd.MPDClient()
    client.connect("localhost", 6600)
    client.pause()
    state = client.status()
    client.disconnect()
    return state['state']

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 80, debug = False)
