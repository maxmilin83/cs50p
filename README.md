# Syncify
#### Description:

I had a few ideas to implement this project, it was a windows 10 app , a discord bot, or a website
ultimately I went with the website as I have the most experience in that from
CS50

My project is called Syncify, it is a web application, where you input a URL to a youtube playlist, and it
converts that playlist to a Spotify playlist. As this is a personal project and I didn't plan on making this
fully functional, the web app will only work for me (or anyone that knows how to use it) because you have to manually
input credentials from the spotify web api so that it can communicate with my program. I could make it so the user is asked
for their credentials using a form in the future though!

I made my project on flask , using html,css,jinja,SQL and of course python, I didnt use javascript for this project
as a lot of it was backend, and 80% of my time was spent doing the python coding which would communicate with the spotify api,
there wasn't really a lot I could think of where could integrated into my web app. Of course it could make the front end look a little
bit nicer and more interactive but the focus of this project was the back end part in my opinion, thats where all the energy went into, and
it what made this project possible at the end of the day. You can have a nice front end website but if it not fully functioning theres not much of a point.

Spotify api : The spotify api was tough to work with, I had to read through the documentation many times
and read many forums. I got it working in the end using the Authorization Code Flow. I used the client credentials method
before that, but I realised I cant use that method if I want to "create" stuff, I can only use it to read stuff from the spotify api,which quickly became
a problem. The Authorization Code Flow prompts the user to log in into spotify in a browser, and press accept, you are then redirect to a different URI which
has a code at the end of it that you copy and put into the python program. I wish I knew a way to do this automatically as having to paste the authorization code manually into my python program is tedious and non-intuitive.

Lets go through each of the files in my project
In the static folder, I have some images for my website and an external css file.

In my templates folder are all the html files that make up my website, along with a apology file for any errors.

In app.py , is where all my flask and logic is.
At the start of app.py I import some functions from my other python files so that I can use them for the logic in my code.
On line 17 I link app.py with my SQLite database, then I configure a session.
I have an errorhandler that returns an epology whenever a 500 server error occurs.
After that I have 3 routes

The first rirst route is just the starting page,

The playlist route returns to the home page if its accesses with GET, because you need to input a playlist URL before you can choose a name
If its reached by POST,we get the YT playlist URL, from the form and we use the returnList function to get each of the songs from that playlist, we then insert these songs to a database so they can be used in other parts of the code.
After that we go to playlist.html

The success route indicates we have successfully created a playlist
First we have a list of songs, I convert them from a dictionary to a list so I dont have to do anymore notation in the future. Then we get the name of the playlist that the user inputted to the form, and we do some basic validation.

Then we get the ID's of all the spotify songs from our list of song names using the getIds function, and finally we create the playlist and add songs to it.

In get_songs.py I used the pytube python module.The function ,takes one argument, a youtube playlist URL, and it returns a list of song names from that playlist

In getSongID.py I used the spotipy python module. The function takes one argument, a list of song names, and returns a list of Spotify ID's of them songs
while prepending 'spotify:track:' before the song ID so it can be recognized by the spotify API

In history.db we just have our SQLITE database that has one table,songsList
which is just one column. I was planning to use SQLite to have a history table on the website but I realised I can just do that with jinja and python.

In test.py is all the python code that talks to the spotify API, its pretty complicated. At the bottom I made the createPlaylist function
and addSongs function.

That was my project, thanks for reading!




