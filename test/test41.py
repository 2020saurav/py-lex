import facebook
import requests

TOKEN = 'CAACE'
graph = facebook.GraphAPI(TOKEN)
posts = graph.get_connections('me','home')

while True:
	try:
		items = posts['data']
		for item in items:
			print item['story']
		posts = requests.get(posts['paging']['next']).json()
		if(len(posts)==0):
			break
	except KeyError:
		posts = requests.get(posts['paging']['next']).json()
		if(len(posts)==0):
			break