import datetime
now = datetime.datetime.now()

from get_songs import returnList
from getSongID import getIds
from test import *

import os
from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

db = SQL("sqlite:///history.db")

#Configure session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.errorhandler(500)
def internal_error(error):

    return render_template("apology.html",d="Must enter valid youtube URL")



@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")



@app.route("/playlist", methods=["GET", "POST"])
def playlist():
    if request.method == "GET":

        return render_template("index.html")

    if request.method == "POST":
        db.execute("DELETE FROM songsList")
        session['ytPlaylist'] = request.form.get("ytplaylist")
        songs = returnList(session['ytPlaylist'])
        count = 0

        for i in songs:
            db.execute("INSERT INTO songsList (songs) VALUES (?)",songs[count])
            count+=1

        return render_template("playlist.html")


@app.route("/success", methods=["GET", "POST"])
def success():
    if request.method == "GET":
        return redirect("/playlist")

    if request.method == "POST":

        songs = []
        songs = db.execute("SELECT * FROM songsList")
        songs1=[]
        for i in songs:
            songs1.append(i['songs'])

        playlistname = request.form.get("playlistName")
        if not playlistname:
            return render_template("apology.html",d="Must enter valid playlist name")

        for i in playlistname:
            if i.isalpha() == False:
                return render_template("apology.html",d="Must enter valid playlist name")


        songIds = []
        songIds = getIds(songs1)
        playlistID = createPlaylist(playlistname)[1]
        print( addSongs(playlistID,songIds))

        return render_template("success.html",songs = songs1,name=playlistname)

