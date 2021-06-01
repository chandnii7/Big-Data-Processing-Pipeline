from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import KafkaProducer, KafkaClient
from time import sleep

class TwitterListener(StreamListener):
    
    def on_data(self, raw_data):
        temp = producer.send("covid-19", raw_data.encode('utf-8'))
        producer.flush()
		
        print(raw_data)		
        return True
    
    def on_error(self, status_code):
        print(status_code)
		
access_token = "1190761539571027970-0jteZBPfxk3J3KCKazmc5vrQEsx1jF"
access_token_secret = "yophKXjSahgcIZs4olBIQ7DGQ9vWQB01wtSwl2Tzv9D0l"
consumer_key = "oVzcEkVrHve3cEfgqAV8VnO1B"
consumer_secret = "mAlyrLi01MUHCG1v3OekClQCnqdSr3PXhPK7fWTXCUYd0oVnl3"

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],api_version=(0,1,0))

t = TwitterListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

stream = Stream(auth, t)
stream.filter(track="#COVID")
