'''http='https://www.youtube.com/watch?v=qzUU5tfFAeA&list=RDqzUU5tfFAeA'
print(http.find('list='))
print(http[49:])


http='https://www.youtube.com/watch?v=zSOJk7ggJts&list=RDzSOJk7ggJts'
print(http.find('list='))
print(http.count())
'''
#print('''<a href='http://stackoverflow.com'>stackoverflow</a>''')

import requests

r = requests.get('https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId=PLNOqW9mLQsEqIs2dMqUkVR7DUARUDDuwA&maxResults=50&key=AIzaSyCdoVRTwGmjcRkai11FtT6onb8G6alUmCA')
if r.status_code == requests.codes.ok:
    data = r.json()
else:
    data = None
print(data['pageInfo']['totalResults'])