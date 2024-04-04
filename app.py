from flask import Flask, request, url_for, session, redirect
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.secret_key = "fehw9r3829hr3298eFSEWw3G3FpJC3D8"
app.config['SESSION_COOKIE_NAME'] = 'Chris Cookie'

@app.route('/')
def login():
    sp_oauth = create_spotify_oauth()
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

@app.route('/redirect')
def redirectPage():
    return 'redirect'

@app.route('/getTracks')
def getTracks():
    return 'Some drake songs or something'


def create_spotify_oauth():
    return SpotifyOAuth(
        client_id=os.getenv('CLIENT_ID'),
        client_secret=os.getenv('CLIENT_SECRET'),
        redirect_uri=url_for('redirectPage', _external=True),
        scope="user-library-read")
