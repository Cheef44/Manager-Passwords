import webview
from src.api import API

def main():
    api = API()
    windows = webview.create_window("Manager passwords", "web_intarface/registration.html", js_api=api)
    webview.start()