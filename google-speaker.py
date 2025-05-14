# -*- coding: utf-8 -*-
import os
from pathlib import Path
from bottle import Bottle, request, template, static_file
from gtts import gTTS
import pychromecast

BASE_DIR = Path(__file__).parent
SPEAK_DIR = BASE_DIR / 'var'
app = Bottle()

@app.route('/speaks/<file_path:path>')
def post_speak(file_path):
    return static_file(file_path, root=SPEAK_DIR)

@app.route("/")
def hello():
    return "Hello World"

@app.route('/form', method='GET')
def get_speak_form():
    content = BASE_DIR / 'template.html'
    text = request.forms.text or ''
    lang = request.forms.lang or 'ja'
    return template(content.open().read(), lang=lang, text=text)


@app.route('/form', method='POST')
def post_speak_form():
    text = request.forms.text
    lang = 'ja'
    text_token = generate_speak(text, lang)
    url = f"http://{app.host}:{app.port}/speaks/{text_token}"
    # 名前が"リビング"のデバイスを探す
    chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=["リビング"])
    cast = chromecasts[0]
    mc = cast.media_controller
    print(url)
    cast.wait()
    mc.play_media(url, 'audio/mp3')
    return get_speak_form()

def generate_speak(text_form, lang='ja'):
    text_token = 'test.mp3'
    speak_path = SPEAK_DIR / text_token
    print(text_form + ',' + lang)
    tts = gTTS(text=str(text_form), lang=lang)
    tts.save(speak_path)
    return text_token

if __name__ == '__main__':
    if not SPEAK_DIR.exists():
        SPEAK_DIR.mkdir()
    app.host = os.environ.get('SERVER_HOST', '192.168.xxx.xxx')
    app.port = os.environ.get('SERVER_PORT', '8080')
    app.run(host=app.host, port=app.port, reloader=True)
