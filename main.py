import twitter
import credentials
import time 

api = twitter.Api(
    consumer_key=credentials.consumer_key,
    consumer_secret=credentials.consumer_secret,
    access_token_key=credentials.access_token_key,
    access_token_secret=credentials.access_token_secret
)

text = '💧 Stay Hydrated.'
waitTime = 60 * 180

running = True 

while running:
    api.PostUpdate(text)
    print('Posted new tweet!')
    time.sleep(waitTime)