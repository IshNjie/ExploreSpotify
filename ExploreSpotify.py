

import requests
import pandas as pd
from spot_secrets import *



class exploreSpotify:
    def __init__(self, playlistToken, playlistEndpoint, trackToken, trackEndpoint):
        self.playlistToken = playlistToken
        self.playlistEndpoint = playlistEndpoint
        self.trackToken = trackToken
        self.trackEndpoint = trackEndpoint
        
    def getPlaylists(self):
        token_headers = {'Authorization':f"Bearer {self.playlistToken}"}
        auth_response = requests.get(self.playlistEndpoint,headers = token_headers)
        print('Status Code: ' + str(auth_response.status_code))
        auth_response_data = auth_response.json()
        print('Number of Playlists: '+ str(len(auth_response_data['items'])))
        
        playlists = []
        playlist_owner = []
        playlist_id = []
    
        for i in range(len(auth_response_data['items'])):
            playlists.append(auth_response_data['items'][i]['name'])
            playlist_owner.append(auth_response_data['items'][i]['owner']['id'])
            playlist_id.append(auth_response_data['items'][i]['id'])
        
        d = {'id':playlist_id, 'playlists':playlists,'owner':playlist_owner}
        df = pd.DataFrame(data = d)
        # hides actual names of owners
        df['owner'] = df['owner'].astype('category').cat.codes
        
        return df
    
    def getTracks(self,playlistName):
        listPlay = self.getPlaylists()
        playlist_df_id = listPlay[listPlay['playlists'] == playlistName]['id'].index[0]
        playlistId = listPlay[listPlay['playlists'] == playlistName]['id'].values[0]
        endpoint = self.trackEndpoint.format(playlistId)
        Track_token_headers = {'Authorization':f"Bearer {self.trackToken}"}
        track_auth_response = requests.get(endpoint,headers = Track_token_headers)
        print('Status Code: ' + str(track_auth_response.status_code))
        track_auth_response_data = track_auth_response.json()
        print('Number of Tracks (capped at 100): '+ str(len(track_auth_response_data['items'])))
        
        
        tracks = []
        artists = []
        playlist_name = listPlay['playlists'][playlist_df_id]
        playlist_id = listPlay['id'][playlist_df_id]
        
        
        for i in range(len(track_auth_response_data['items'])):
            tracks.append(track_auth_response_data['items'][i]['track']['name'])
            artists.append(track_auth_response_data['items'][i]['track']['artists'][0]['name'])
            
        d = {'tracks':tracks,'artists':artists, 'Playlist':playlist_name,'id':playlist_id}
        df_tracks = pd.DataFrame(data = d)
        
        return df_tracks

        
