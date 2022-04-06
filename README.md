Explore Spotify
===

Having fun with the Spotify API - A simple script that allows the user to view their current playlists and gets the tracks for a specified playlist

## Setup 

1. Navigate to Spotify for Developers and go to the [Console Tab](https://developer.spotify.com/console/)
The Console will have multiple endpoints you can use to connect to the Spotify Web API. Here is where we will retrieve the endpoint and OAuth Token for each Console type.

2. For the playlists endpoints, go to the Playlists dropdown. The endpoints we used were:
* [Current user's playlist](https://developer.spotify.com/console/get-current-user-playlists/) 
* [Get Playlist Items](https://developer.spotify.com/console/get-playlist-tracks/)

3. Create a spot_secrets.py file and assign the endpoints and OAuth Token's to relevant variables

4. 
  * Call the *getPlaylists* method to get a list of all of the playlists
  * Call the *getTracks* method to get a list of the tracks in a playlist (capped at 100)

