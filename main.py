from flask import Flask
import sys
import pusherclient
import logging

root = logging.getLogger()
root.setLevel(logging.INFO)
ch = logging.StreamHandler(sys.stdout)
root.addHandler(ch)

app = Flask(__name__)

global pusher


@app.route("/")
def hello():
    return "Hello, world!"


def new_listing_handler(listing):
    print(listing)


def connect_handler(data):
    global pusher
    channel = pusher.subscribe('askreddit')
    channel.bind('new-listing', new_listing_handler)


def subscribe_to_channels():
    global pusher
    pusher = pusherclient.Pusher('50ed18dd967b455393ed')
    pusher.connection.bind('pusher:connection_established', connect_handler)
    pusher.connect()


if __name__ == "__main__":
    subscribe_to_channels()
    app.run()
