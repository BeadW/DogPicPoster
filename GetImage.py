import requests
import os
import webbrowser
import urllib.request

class FetchImage:
    def __init__(self, address):
        self.address = address
        self.response = ''
        self.link = ''
        self.image = None
        self.filename = "photo.jpg"

    def request(self):
        setattr(self, 'response', requests.get(url=self.address).json())

    def store_link(self):
        setattr(self, 'link', self.response["message"])

    def respond(self):
        print(self.response)
        print(self.link)
        #webbrowser.open_new_tab(self.response["message"])

    def store_image(self):
        setattr(self, 'image', urllib.request.urlretrieve(self.link, self.filename))
