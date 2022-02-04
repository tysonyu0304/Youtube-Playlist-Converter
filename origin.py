import requests
YOUTUBE_API_KEY = "AIzaSyCdoVRTwGmjcRkai11FtT6onb8G6alUmCA"

def main():
    start = yt_playlist_to_URL(YOUTUBE_API_KEY)
    playlist=input()
    if 'https' in playlist:
        playlistid = playlist[-34:]
    elif len(playlist) != 34:
        print('error')
    print(start.playlist_to_URL(playlistid))

class yt_playlist_to_URL():
    def __init__(self,api_key):
        self.base_url = "https://www.googleapis.com/youtube/v3/"
        self.api_key = api_key

    def get_html_to_json(self, path):
        api_url = f"{self.base_url}{path}&key={self.api_key}"
        r = requests.get(api_url)
        print(api_url)
        if r.status_code == requests.codes.ok:
            print('yes')
            data = r.json()
        else:
            print('no')
            data = None
        return data

    def playlist_to_URL(self, playlistID, part='contentDetails', max_results=50):
        path = f'playlistItems?part={part}&playlistId={playlistID}&maxResults={max_results}'
        print('path =',path)
        data = self.get_html_to_json(path)
        if not data:
            return []

        video_ids = []
        for data_item in data['items']:
            video_ids.append(data_item['contentDetails']['videoId'])
        video_ids = list(video_ids)
        URL=[]
        for i in video_ids:
            URL.append(f"https://www.youtube.com/watch?v={i}")
            #print(f"https://www.youtube.com/watch?v={i}")
        return list(URL)
        

if __name__ == '__main__':
    main()