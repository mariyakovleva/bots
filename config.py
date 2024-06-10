
import requests
import json 


TOKEN = '6878391788:AAHhuJhcdXu6NqOjAl5A2VczyXjWcYvNIMs'  
URL = f'https://api.telegram.org/bot{TOKEN}'
print(requests.get(URL + '/getUpdates').json()) 

