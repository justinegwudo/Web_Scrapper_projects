import requests
from urllib.parse import urlencode
import json
from random import randint

search_term = 'nollywood'

url = 'https://api.giphy.com/v1/gifs/search?'
params = { 'api_key' : 'csZ55ha5aY5t5MiWNbeAVNu8rYJmaRKC', 
		   'q'       : search_term, 
		   'lang'    : 'en' }

url += urlencode( params )
r = requests.get( url )
result = r.json()

i = randint( 0, len( result[ 'data' ] ) - 1 )

rand_result = result[ 'data' ][ i ]
url = rand_result[ 'images' ][ 'original' ][ 'url' ]

print( url )
