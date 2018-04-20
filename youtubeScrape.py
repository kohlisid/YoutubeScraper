import requests
import json
userid = input("Enter channel id\n")
url1='https://www.googleapis.com/youtube/v3/channels?part=contentDetails&id={}&maxResults=10&key=AIzaSyDHln1QFJLallOIhlhuRJsvy3mGe_xcAc8'.format(userid)
req=requests.get(url1)
#print(req.json())
obj = json.loads(req.text)
print(obj['items'][0]['contentDetails']['relatedPlaylists']['uploads'])
upid=obj['items'][0]['contentDetails']['relatedPlaylists']['uploads']
# print(obj[1])
url='https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&playlistId={}&key=AIzaSyDHln1QFJLallOIhlhuRJsvy3mGe_xcAc8'.format(upid)

req2=requests.get(url)
obj2=json.loads(req2.text)
for x in obj2['items']:
	print('*********\n')
	print('video name\n')
	print(x['snippet']['title']+'\n')
	vidid=x['snippet']['resourceId']['videoId']
	url3='https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=10&relatedToVideoId={}&type=video&key=AIzaSyDHln1QFJLallOIhlhuRJsvy3mGe_xcAc8'.format(vidid)
	req3=requests.get(url3)
	obj3=json.loads(req3.text)
	print('Similar Vids\n')
	for y in obj3['items']:
		print(y['snippet']['title']+'\n')
	print('***********\n')
